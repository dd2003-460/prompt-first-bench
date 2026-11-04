#!/usr/bin/env node
/**
 * R6 · 规则负载计量器（阶段门控加载对照组）
 *
 * 口径：o200k_base tokenizer（与 run2 token-counts.txt 同口径）。
 *   优先 js-tiktoken（npm i js-tiktoken，ranks 内置，可离线）；
 *   缺依赖时降级为字节估算 bytes/3.32（该常数由 run2 实测 39858B→12086tok 与
 *   本脚本 o200k 实测 42331B→12768tok 双向校准，见 run6-token-analysis.md §2）。
 *
 * 用法：
 *   node count-rule-tokens.js                 # 打印单文件 + 全量 + 6 个阶段包
 *   node count-rule-tokens.js --json          # 机器可读
 *   node count-rule-tokens.js --stage 02.5    # 只算某阶段包（含 INDEX）
 */
const fs = require("fs");
const path = require("path");

const REPO = path.resolve(__dirname, "../../../..");
const LOOP = path.join(REPO, "loop/prompt-first");

const FILES = {
  "00": "00-common-review.md",
  "01": "01-goal-decomposition.md",
  "02": "02-information-research.md",
  "02.5": "02.5-cross-check.md",
  "03": "03-action-decomposition.md",
  "04": "04-execution-verification.md",
  "04.5": "04.5-final-review.md",
  INDEX: "INDEX.md",
};

// INDEX.md 路由表（与 loop/prompt-first/INDEX.md 逐行对应；改表必须同步改这里）
const ROUTES = {
  "01": ["00", "01", "02"],
  "02": ["00", "02", "02.5"],
  "02.5": ["00", "02.5", "03"],
  "03": ["00", "03", "04"],
  "04": ["00", "04", "04.5"],
  "04.5": ["00", "04.5"],
};

// 示例（tier-3，真正按需）：R8 起不在路由表中，不默认读取。
// 保留 EX_ROUTES 为空对象以兼容 --stage 输出；实际加载由 agent 遇到卡点时触发。
const EXAMPLES = {
  "00": "examples/00-common-review-examples.md",
  "01": "examples/01-examples.md",
  "02": "examples/02-examples.md",
  "02.5": "examples/02.5-examples.md",
  "03": "examples/03-examples.md",
  "04": "examples/04-examples.md",
  "04.5": "examples/04.5-examples.md",
};
const EX_ROUTES = {};

let enc = null;
let method = "o200k_js_tiktoken";
try {
  enc = require("js-tiktoken").getEncoding("o200k_base");
} catch (e) {
  method = "bytes_estimate_div_3.32";
}

function count(text) {
  if (enc) return enc.encode(text).length;
  return Math.round(Buffer.byteLength(text, "utf8") / 3.32);
}

const out = { tokenizer: method, files: {}, examples: {}, bundles: {}, all_loop_files: 0, all_examples: 0 };

for (const [k, f] of Object.entries(FILES)) {
  const p = path.join(LOOP, f);
  const text = fs.readFileSync(p, "utf8");
  out.files[k] = { name: f, tokens: count(text), bytes: Buffer.byteLength(text, "utf8") };
}

for (const [k, f] of Object.entries(EXAMPLES)) {
  const p = path.join(LOOP, f);
  if (!fs.existsSync(p)) continue;
  const text = fs.readFileSync(p, "utf8");
  out.examples[k] = { name: f, tokens: count(text), bytes: Buffer.byteLength(text, "utf8") };
}
out.all_examples = Object.values(out.examples).reduce((a, v) => a + v.tokens, 0);

out.all_loop_files = ["00", "01", "02", "02.5", "03", "04", "04.5"].reduce((a, k) => a + out.files[k].tokens, 0);

for (const [stage, members] of Object.entries(ROUTES)) {
  const body = members.reduce((a, k) => a + out.files[k].tokens, 0);
  const ex = (EX_ROUTES[stage] || []).reduce((a, k) => a + (out.examples[k] ? out.examples[k].tokens : 0), 0);
  out.bundles[stage] = {
    files: members,
    body_tokens: body,
    body_with_index: body + out.files.INDEX.tokens,
    example_tokens: ex,
    with_index_and_examples: body + ex + out.files.INDEX.tokens,
  };
}

const argv = process.argv.slice(2);
if (argv.includes("--json")) {
  console.log(JSON.stringify(out, null, 2));
  process.exit(0);
}
const si = argv.indexOf("--stage");
if (si >= 0) {
  const s = argv[si + 1];
  if (!out.bundles[s]) {
    console.error(`unknown stage: ${s}; known: ${Object.keys(ROUTES).join(",")}`);
    process.exit(1);
  }
  console.log(JSON.stringify({ stage: s, ...out.bundles[s], tokenizer: method }, null, 2));
  process.exit(0);
}

console.log(`# tokenizer: ${method}`);
if (!enc) console.log("# WARN: 降级字节估算，对单文件误差约 ±18%（core 实测 3.63 B/tok，examples 2.85 B/tok；3.32 仅对两者合计成立）");
console.log("## single files");
for (const [k, v] of Object.entries(out.files)) {
  console.log(`${String(v.tokens).padStart(6)} tok  ${String(v.bytes).padStart(6)} B  ${k.padEnd(6)} ${v.name}`);
}
console.log(`\n## all 7 loop files: ${out.all_loop_files} tok`);
if (out.all_examples) console.log(`## all 7 examples:   ${out.all_examples} tok (tier-3)`);
console.log("## stage bundles");
for (const [s, v] of Object.entries(out.bundles)) {
  console.log(`  ${s.padEnd(5)} core ${String(v.body_tokens).padStart(5)} +INDEX ${String(v.body_with_index).padStart(5)} ` +
              `+ex ${String(v.example_tokens).padStart(4)} => ${String(v.with_index_and_examples).padStart(5)}`);
}
const vals = Object.values(out.bundles);
const m1 = vals.reduce((a, v) => a + v.body_with_index, 0) / vals.length;
const m2 = vals.reduce((a, v) => a + v.with_index_and_examples, 0) / vals.length;
console.log(`  mean  core+INDEX ${Math.round(m1)} tok  |  core+INDEX+ex ${Math.round(m2)} tok  (n=${vals.length})`);
