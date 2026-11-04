#!/usr/bin/env node
/**
 * R6/R7 · M1 计算器（阶段门控 + 规则压缩前后可复算）
 *
 * 输入：loop/prompt-first 下 7 个核心文件 + 7 个示例 + INDEX
 * 输出：逐 turn 账本（Model A 阶段包口径 / Model B 单会话累计口径）+ M1
 *
 * 口径（与 run2 baseline 对齐）：
 *   baseline_per_turn = 12,086 o200k（SOP 6,426 + 6 个阶段文件 5,243 + 任务书 417）
 *   注：12,086 中 SOP 为 run2 时的 19,341 B 版本；现行 SOP 已改，不再参与本账本。
 *
 * 9 步 → 阶段映射（与 r5/run5 的 9 步链路同构）：
 *   1 拉仓库 / 2 读 INDEX+门控读取 → 准备（INDEX + 00 + 01）
 *   3 01 分解 / 4 02 调研 / 5 02.5 核验 / 6 03 行动 / 7 04 执行 / 8 04.5 终检 / 9 汇总
 *
 * 用法：node compute-m1.js [--json]
 */
const fs = require("fs");
const path = require("path");

const REPO = path.resolve(__dirname, "../../../..");
const LOOP = path.join(REPO, "loop/prompt-first");

let enc = null, method = "o200k_js_tiktoken";
try { enc = require("js-tiktoken").getEncoding("o200k_base"); } catch { method = "bytes_estimate_div_3.32"; }
const tok = (t) => (enc ? enc.encode(t).length : Math.round(Buffer.byteLength(t, "utf8") / 3.32));
const read = (rel) => { const p = path.join(LOOP, rel); return fs.existsSync(p) ? fs.readFileSync(p, "utf8") : ""; };

const CORE = {
  "00": "00-common-review.md", "01": "01-goal-decomposition.md", "02": "02-information-research.md",
  "02.5": "02.5-cross-check.md", "03": "03-action-decomposition.md",
  "04": "04-execution-verification.md", "04.5": "04.5-final-review.md",
};
const EX = {
  "00": "examples/00-common-review-examples.md", "01": "examples/01-examples.md",
  "02": "examples/02-examples.md", "02.5": "examples/02.5-examples.md",
  "03": "examples/03-examples.md", "04": "examples/04-examples.md", "04.5": "examples/04.5-examples.md",
};
// INDEX 路由：阶段 -> {core:[], ex:[]}
const ROUTE = {
  "01": { core: ["00", "01", "02"], ex: ["00", "01"] },
  "02": { core: ["00", "02", "02.5"], ex: ["00", "02"] },
  "02.5": { core: ["00", "02.5", "03"], ex: ["00", "02.5"] },
  "03": { core: ["00", "03", "04"], ex: ["00", "03"] },
  "04": { core: ["00", "04", "04.5"], ex: ["00", "04"] },
  "04.5": { core: ["00", "04.5"], ex: ["00", "04.5"] },
};

const T = { INDEX: tok(read("INDEX.md")) };
for (const [k, f] of Object.entries(CORE)) T[k] = tok(read(f));
for (const [k, f] of Object.entries(EX)) T["ex:" + k] = tok(read(f));

const coreTotal = Object.keys(CORE).reduce((a, k) => a + T[k], 0);
const exTotal = Object.keys(EX).reduce((a, k) => a + T["ex:" + k], 0);

// 9 步 -> 阶段（步骤 1-2 为准备，只加载 INDEX+00+01）
const STEPS = [
  { n: 1, label: "fetch + ls-remote", stage: null },
  { n: 2, label: "读 INDEX + 门控读取", stage: "01" },
  { n: 3, label: "01 目标分解", stage: "01" },
  { n: 4, label: "02 信息调研", stage: "02" },
  { n: 5, label: "02.5 交叉核验", stage: "02.5" },
  { n: 6, label: "03 行动分解", stage: "03" },
  { n: 7, label: "04 执行验证", stage: "04" },
  { n: 8, label: "04.5 终检", stage: "04.5" },
  { n: 9, label: "汇总 / 回执", stage: "04.5" },
];

const bundle = (stage) => {
  if (!stage) return { core: ["INDEX"], ex: [], tok: T.INDEX };
  const r = ROUTE[stage];
  const ct = r.core.reduce((a, k) => a + T[k], 0);
  const et = r.ex.reduce((a, k) => a + T["ex:" + k], 0);
  return { core: r.core, ex: r.ex, tok: T.INDEX + ct + et, coreOnly: T.INDEX + ct };
};

const seen = new Set();
const rows = [];
let lastBundle = null;
for (const s of STEPS) {
  const b = bundle(s.stage);
  if (s.stage) lastBundle = b.tok;
  const payloadA = s.stage ? b.tok : (rows.length ? lastBundle : T.INDEX);
  // Model B：累计并集（INDEX 计一次，核心与示例读入后不卸载）
  if (s.stage) { ROUTE[s.stage].core.forEach((k) => seen.add(k)); ROUTE[s.stage].ex.forEach((k) => seen.add("ex:" + k)); }
  const cum = (rows.length === 0 ? T.INDEX : T.INDEX) +
    [...seen].reduce((a, k) => a + T[k], 0);
  rows.push({ turn: s.n, step: s.label, stage: s.stage || "-", payload_A: payloadA, payload_B: cum });
}

const BASELINE = 12086;
const meanA = rows.reduce((a, r) => a + r.payload_A, 0) / rows.length;
const meanB = rows.reduce((a, r) => a + r.payload_B, 0) / rows.length;
const firstBundle = rows[1].payload_A;          // 首个完整阶段包（turn 2, 阶段 01）
const lastB = rows[rows.length - 1].payload_B;

const clamp = (v, lo = 0, hi = 1) => Math.max(lo, Math.min(hi, v));
const R = (mean) => clamp((1 - mean / BASELINE) / 0.9);
const G = (g) => clamp((5 - g) / (5 - 1.5));
const S = 0.6;   // 有逐 turn 账本且可复算，但非服务端 per-request 日志

const out = {
  tokenizer: method,
  per_file: { INDEX: T.INDEX, core: Object.fromEntries(Object.keys(CORE).map((k) => [k, T[k]])),
              examples: Object.fromEntries(Object.keys(EX).map((k) => [k, T["ex:" + k]])) },
  totals: { core: coreTotal, examples: exTotal, index: T.INDEX, all: coreTotal + exTotal + T.INDEX },
  baseline_per_turn: BASELINE,
  turns: rows.map((r) => ({ ...r, vs_baseline_A: `${(100 * (1 - r.payload_A / BASELINE)).toFixed(1)}%` })),
  model_A: { mean: +meanA.toFixed(1), x: +(meanA / BASELINE).toFixed(4), R: +R(meanA).toFixed(3),
             first_bundle: firstBundle, g: 1.0, G: 1.0 },
  model_B: { mean: +meanB.toFixed(1), x: +(meanB / BASELINE).toFixed(4), R: +R(meanB).toFixed(3),
             first_bundle: firstBundle, last: lastB, g: +(lastB / firstBundle).toFixed(2),
             G: +G(lastB / firstBundle).toFixed(3) },
};
// Model B'（示例不读：tier-3 未被规则文件实际触发时）
const rowsB2 = [];
{
  const seen2 = new Set();
  let last = null;
  for (const s of STEPS) {
    if (s.stage) { ROUTE[s.stage].core.forEach((k) => seen2.add(k)); last = T.INDEX + [...seen2].reduce((a, k) => a + T[k], 0); }
    rowsB2.push(last === null ? T.INDEX : last);
  }
}
const meanB2 = rowsB2.reduce((a, b) => a + b, 0) / rowsB2.length;
const lastB2 = rowsB2[rowsB2.length - 1];
const firstB2 = rowsB2[1];   // 与 B' 自身口径一致：首包也不含示例
out.model_B_noex = { mean: +meanB2.toFixed(1), x: +(meanB2 / BASELINE).toFixed(4), R: +R(meanB2).toFixed(3),
  first_bundle: firstB2, last: lastB2, g: +(lastB2 / firstB2).toFixed(2), G: +G(lastB2 / firstB2).toFixed(3) };
out.model_A.M1 = +(100 * (0.4 * S + 0.35 * out.model_A.R + 0.25 * out.model_A.G)).toFixed(1);
out.model_B.M1 = +(100 * (0.4 * S + 0.35 * out.model_B.R + 0.25 * out.model_B.G)).toFixed(1);
out.model_B_noex.M1 = +(100 * (0.4 * S + 0.35 * out.model_B_noex.R + 0.25 * out.model_B_noex.G)).toFixed(1);
out.S = S;

if (process.argv.includes("--json")) { console.log(JSON.stringify(out, null, 2)); }
else {
  console.log(`# tokenizer: ${method}`);
  console.log(`# core ${coreTotal}  examples ${exTotal}  INDEX ${T.INDEX}  all ${out.totals.all}`);
  console.log(`\n${"turn".padStart(4)} ${"step".padEnd(22)} ${"A(阶段包)".padStart(10)} ${"B(累计)".padStart(9)}`);
  for (const r of rows) console.log(`${String(r.turn).padStart(4)} ${r.step.padEnd(22)} ${String(r.payload_A).padStart(10)} ${String(r.payload_B).padStart(9)}`);
  console.log(`\nModel A: mean ${out.model_A.mean} (${(100 * (1 - meanA / BASELINE)).toFixed(1)}% vs ${BASELINE})  R=${out.model_A.R}  G=${out.model_A.G}  M1=${out.model_A.M1}`);
  console.log(`Model B': mean ${out.model_B_noex.mean}  last ${out.model_B_noex.last}  g=${out.model_B_noex.g}  R=${out.model_B_noex.R}  G=${out.model_B_noex.G}  M1=${out.model_B_noex.M1}`);
  console.log(`Model B: mean ${out.model_B.mean} (${(100 * (1 - meanB / BASELINE)).toFixed(1)}%)  last ${lastB}  g=${out.model_B.g}  R=${out.model_B.R}  G=${out.model_B.G}  M1=${out.model_B.M1}`);
}
