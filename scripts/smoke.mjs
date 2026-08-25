#!/usr/bin/env node
// MCP stdio smoke test: spawn a server command, run initialize -> tools/list,
// require at least one tool, print the result, exit non-zero on failure.
import { spawn } from "node:child_process";

const argv = process.argv.slice(2);
const cmd = argv.length ? argv : ["docker", "run", "-i", "--rm", "vascue-public-knowledge-search"];
const timeoutMs = Number(process.env.SMOKE_TIMEOUT_MS ?? 90_000);

const child = spawn(cmd[0], cmd.slice(1), { stdio: ["pipe", "pipe", "inherit"] });
const send = (msg) => child.stdin.write(JSON.stringify(msg) + "\n");
const pending = new Map();
let buf = "";
child.stdout.on("data", (chunk) => {
  buf += chunk.toString();
  let i;
  while ((i = buf.indexOf("\n")) >= 0) {
    const line = buf.slice(0, i).trim();
    buf = buf.slice(i + 1);
    if (!line) continue;
    let msg;
    try { msg = JSON.parse(line); } catch { continue; }
    if (msg.id !== undefined && pending.has(msg.id)) pending.get(msg.id)(msg);
  }
});
const request = (id, method, params = {}) =>
  new Promise((resolve, reject) => {
    pending.set(id, (m) => (m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result)));
    send({ jsonrpc: "2.0", id, method, params });
  });

const timer = setTimeout(() => { console.error(`smoke: timed out after ${timeoutMs} ms`); child.kill(); process.exit(1); }, timeoutMs);
child.on("exit", (code) => { if (pending.size) { console.error(`smoke: server exited early (code ${code})`); process.exit(1); } });

try {
  const init = await request(1, "initialize", {
    protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "vascue-smoke", version: "1.0.0" },
  });
  send({ jsonrpc: "2.0", method: "notifications/initialized" });
  const tools = await request(2, "tools/list");
  const names = (tools.tools ?? []).map((t) => t.name);
  if (!names.length) throw new Error("tools/list returned no tools");
  const callQuery = process.env.SMOKE_CALL_QUERY;
  if (callQuery) {
    const call = await request(3, "tools/call", { name: "search", arguments: { query: callQuery } });
    const payload = JSON.parse(call.content?.[0]?.text ?? "{}");
    const chunks = payload.chunks ?? payload.result?.chunks ?? [];
    if (!chunks.length) throw new Error(`search("${callQuery}") returned no chunks`);
    const first = chunks[0];
    const url = first.url ?? first.item?.metadata?.url ?? "";
    if (!url.startsWith("https://www.vascue.io")) throw new Error(`chunk url missing/foreign: ${url}`);
    console.log(`smoke: search("${callQuery}") -> ${chunks.length} chunks, top ${url}`);
  }
  console.log(JSON.stringify({ serverInfo: init.serverInfo, protocolVersion: init.protocolVersion, tools: tools.tools }, null, 2));
  console.log(`smoke: ok (${names.join(", ")})`);
  clearTimeout(timer);
  pending.clear();
  child.kill();
  process.exit(0);
} catch (err) {
  console.error(`smoke: ${err.message}`);
  child.kill();
  process.exit(1);
}
