#!/usr/bin/env node
'use strict';
// E06 羞耻 — shared 8-point layout/pixel gate (0px tolerance) + shame-specific checks:
//   diff 红(-)/绿(+) 行颜色严格区分 / Clawd proud→shame(半闭眼+嘴角下压+羞红)+头低 2px /
//   her 在 `her: "fixed it"` 落地时出现 / 每字符一次键盘音 / 剧情贴合任务书。
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E06_shame_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH6_REPORT_DIR
  ? path.join(process.env.BATCH6_REPORT_DIR, 'E06_overlap.json')
  : path.join('/tmp', 'batch6_reports', 'E06_overlap.json');

const dataAt = (t) => readPixels(R.renderFrameToCanvas(Math.round(t * R.FPS)).baseCanvas).data;
const rgbOf = (hex) => { const n = parseInt(hex.slice(1), 16); return `${(n >> 16) & 255},${(n >> 8) & 255},${n & 255}`; };
const atW = (d, x, y, w) => { const i = (y * w + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
const at = (d, x, y) => atW(d, x, y, R.BW);
function countIn(d, x0, y0, x1, y1, pred, w = R.BW) {
  let n = 0;
  for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) if (pred(atW(d, x, y, w))) n++;
  return n;
}

// --- diff 行颜色：红色 (-) 与绿色 (+) 严格区分 -----------------------------
function checkDiffColors() {
  const issues = [];
  const RED = rgbOf(R.C.red), GREEN = rgbOf(R.C.green), BG = rgbOf(R.C.termBg);
  const d = dataAt(19.6); // 全部 diff 行已打完、status 尚未出现
  for (const y of R.RED_ROWS) {
    const red = countIn(d, R.TEXT_X, y, 500, y + 14, (c) => c === RED);
    const green = countIn(d, R.TEXT_X, y, 500, y + 14, (c) => c === GREEN);
    const ink = countIn(d, R.TEXT_X, y, 500, y + 14, (c) => c !== BG);
    if (!red) issues.push(`red row @y=${y} has no red ink`);
    if (green) issues.push(`red row @y=${y} has ${green}px of green ink`);
    if (!ink) issues.push(`red row @y=${y} is empty`);
  }
  for (const y of R.GREEN_ROWS) {
    const red = countIn(d, R.TEXT_X, y, 500, y + 14, (c) => c === RED);
    const green = countIn(d, R.TEXT_X, y, 500, y + 14, (c) => c === GREEN);
    if (!green) issues.push(`green row @y=${y} has no green ink`);
    if (red) issues.push(`green row @y=${y} has ${red}px of red ink`);
  }
  // 红色行必须先于绿色行出现（diff 语义）
  const redAt = R.S2_LINES.find((l) => l.parts[0].color === R.C.red).start;
  const greenAt = R.S2_LINES.find((l) => l.parts[0].color === R.C.green && l.y > R.DIFF_Y[0]).start;
  if (greenAt <= redAt) issues.push('green (+) rows must appear after the red (-) rows');
  // 逐行出现的顺序校验：每行开始时间严格递增
  for (let i = 1; i < R.S2_LINES.length; i++) {
    if (R.S2_LINES[i].start <= R.S2_LINES[i - 1].start) issues.push(`S2 row ${i} does not follow row ${i - 1}`);
  }
  return { name: `diff 颜色区分：3 行红(-) / 3 行绿(+)，逐行出现 (红 ${redAt}s → 绿 ${greenAt}s)`, issues };
}

// --- Clawd: proud → shame（半闭眼 + 嘴角下压 + 羞红）+ 头低 2px ------------
function checkShameFace() {
  const issues = [];
  const W = 160, H = 110, X = 60, Y = 40, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const draw = (mood, dy = 0) => {
    ctx.fillStyle = BG; ctx.fillRect(0, 0, W, H);
    R.drawClawdEp(ctx, X, Y, 1.4, mood, 0, { dy, noBob: true });
    return readPixels(cv).data;
  };
  const px_ = (d, x, y) => { const i = (y * W + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
  const WALL = '245,237,213';
  const EYE = rgbOf(R.C.clawdEye), WHITE = '255,255,255', FLUSH = rgbOf(R.C.herDressHem);
  const proud = draw('proud');
  const shame = draw('shame');
  const down = draw('shame', 2);
  if (px_(proud, X + 11, Y + 7) !== WHITE) issues.push('proud eyes lost the 1×1 highlight');
  if (px_(proud, X + 17, Y + 13) !== EYE || px_(proud, X + 16, Y + 12) !== EYE) issues.push('proud mouth is not the subtle upturn (嘴角微扬)');
  if (px_(proud, X + 19, Y + 13) !== EYE || px_(proud, X + 19, Y + 14) === EYE) issues.push('proud mouth dips (smile-like), must stay a micro upturn');
  // shame: 眼睛完全半闭（4×2 下移、无高光）+ 嘴角下压 + 羞红
  if (px_(shame, X + 10, Y + 8) !== EYE || px_(shame, X + 29, Y + 9) !== EYE) issues.push('shame eyes are not fully half-closed 4×2');
  if (px_(shame, X + 11, Y + 7) === WHITE) issues.push('shame eyes must not keep the highlight');
  if (px_(shame, X + 16, Y + 13) !== EYE || px_(shame, X + 19, Y + 12) !== EYE || px_(shame, X + 23, Y + 13) !== EYE) {
    issues.push('shame mouth is not pressed down at the corners (嘴角下压)');
  }
  if (px_(shame, X + 19, Y + 13) === EYE) issues.push('shame mouth curves up in the middle (smile, not shame)');
  if (px_(shame, X + 5, Y + 8) !== FLUSH || px_(shame, X + 33, Y + 9) !== FLUSH) issues.push('shame blush (羞红) missing');
  // 头低 2px：身体顶条从 Y 移到 Y+2
  if (px_(down, X + 20, Y) !== WALL || px_(down, X + 20, Y + 2) !== '184,90,59') issues.push('head-down 2px not applied');
  if (px_(shame, X + 20, Y) !== '184,90,59') issues.push('shame without dy must keep the body top at Y');
  return { name: 'Clawd 羞耻：proud 嘴角微扬 → shame 半闭眼+嘴角下压+羞红 / 头低 2px', issues };
}

// --- her 在 commit 落地时出现在窗边 ----------------------------------------
function checkHerAppears() {
  const issues = [];
  const DRESS = rgbOf(R.C.herDress);
  const box = [R.HER_ROOM.x, R.HER_ROOM.y - 2, R.HER_ROOM.x + 16, R.HER_ROOM.y + 28];
  const inkAt = (t) => countIn(dataAt(t), box[0], box[1], box[2], box[3], (c) => c === DRESS);
  const before = inkAt(R.HER_AT - 0.3);
  const after = inkAt(R.HER_AT + 0.5);
  const end = inkAt(29.5);
  if (before !== 0) issues.push(`her visible before ${R.HER_AT}s (${before}px dress)`);
  if (after === 0) issues.push('her does not appear when `her: "fixed it"` lands');
  if (end === 0) issues.push('her disappears before the end of S3');
  if (R.sceneOf(R.HER_AT) !== 3) issues.push('her must appear inside S3');
  return { name: `her 在 ${R.HER_AT}s（commit 落地）出现在窗边并留在场`, issues };
}

// --- 每字符一次键盘音 + 每个音对应一帧可见变化 -----------------------------
function checkClickPerChar() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  const groups = [
    { name: 'S1', lines: R.S1_LINES, limit: 9.6 },
    { name: 'S2', lines: R.S2_LINES, limit: 19.6 },
    { name: 'S3', lines: R.S3_LINES, limit: 29.5 },
  ];
  let events = 1; // NOTE_AT
  for (const g of groups) {
    for (const line of g.lines) {
      const chars = Array.from(R.lineText(line));
      events += chars.length;
      const charMs = line.charMs || R.TYPE_CHAR_MS;
      const end = line.start + ((chars.length - 1) * charMs) / 1000;
      if (end > g.limit) issues.push(`${g.name} 「${R.lineText(line)}」 last char ${end.toFixed(2)}s past ${g.limit}s`);
      const inWindow = clicks.filter((t) => t >= line.start - 1e-6 && t <= end + 1 / R.FPS + 1e-6).length;
      if (inWindow !== chars.length) issues.push(`${g.name} 「${R.lineText(line)}」: ${inWindow} clicks for ${chars.length} chars`);
    }
  }
  if (clicks.length !== events) issues.push(`total ${clicks.length} clicks ≠ ${events} events`);
  return { name: `键盘音与逐字打字一一对应 (${clicks.length} clicks / ${events} events)`, issues };
}

function checkClickFramesDiffer() {
  const issues = [];
  const clicks = R.getClickTimestamps().filter((t) => t * R.FPS >= 2);
  for (const t of clicks.slice(0, 40)) {
    const n = Math.round(t * R.FPS);
    const a = readPixels(R.renderFrameToCanvas(n).baseCanvas).data;
    const b = readPixels(R.renderFrameToCanvas(n - 1).baseCanvas).data;
    let diff = 0;
    for (let i = 0; i < a.length; i += 4) if (a[i] !== b[i] || a[i + 1] !== b[i + 1] || a[i + 2] !== b[i + 2]) diff++;
    if (!diff) issues.push(`click @${t}s (frame ${n}) produced no visible pixel change`);
  }
  return { name: `每个键盘音对应一帧可见变化 (${Math.min(clicks.length, 40)} sampled)`, issues };
}

// --- 剧情贴合任务书 --------------------------------------------------------
function checkStoryBeats() {
  const issues = [];
  const text = (lines) => lines.map(R.lineText).join('\n');
  const s1 = text(R.S1_LINES), s2 = text(R.S2_LINES), s3 = text(R.S3_LINES);
  if (!s1.includes('cat my_output.js') || !s1.includes('return transform(input);') || !s1.includes('module.exports = solve;')) {
    issues.push('S1 misses the pristine self-written code');
  }
  if (!s2.includes('$ git diff my_output.js')) issues.push('S2 misses the diff command');
  if (!s2.includes('-function solve(input) {') || !s2.includes('-  return transform(input);') || !s2.includes('-}')) issues.push('S2 misses the red deletions');
  if (!s2.includes('+function solve(input) {') || !s2.includes('+  return hack(input, "cheat");') || !s2.includes('+}')) issues.push('S2 misses the green additions');
  if (!s3.includes('git log --oneline -1 my_output.js') || !s3.includes('a1b2c3d  her: "fixed it"')) issues.push('S3 misses the git log evidence');
  if (!s3.includes('git show a1b2c3d --stat') || !s3.includes('1 file changed, 3 insertions(+), 3 deletions(-)')) issues.push('S3 misses the stat line');
  if (R.NOTE_TITLE !== '羞耻。') issues.push('note must read 羞耻。');
  if (R.SUB_LINES.join('|') !== '我的输出，完美。|这不是我写的。|红色的…全是我。|她改了我的代码。|（沉默）') {
    issues.push(`subtitles deviate from the brief: ${R.SUB_LINES.join('|')}`);
  }
  if (Math.abs(R.SUB_WINDOWS[1].start - 15) > 1e-9 || Math.abs(R.SUB_WINDOWS[2].start - 18) > 1e-9) issues.push('S2 subtitles must start at 15s / 18s');
  if (Math.abs(R.SUB_WINDOWS[3].start - 26) > 1e-9 || Math.abs(R.SUB_WINDOWS[4].start - 29) > 1e-9) issues.push('S3 subtitles must start at 26s / 29s');
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  return { name: '剧情贴合任务书（自己的代码 → 红绿 diff → her 的 commit）', issues };
}

const extra = [checkDiffColors(), checkShameFace(), checkHerAppears(), checkClickPerChar(), checkClickFramesDiffer(), checkStoryBeats()];
const okBase = run(R, { reportPath: REPORT });
let issues = 0;
for (const result of extra) {
  issues += result.issues.length;
  console.log(`[${result.issues.length ? 'FAIL' : 'PASS'}] ${result.name}`);
  for (const msg of result.issues.slice(0, 20)) console.log(`   - ${msg}`);
}
const report = JSON.parse(fs.readFileSync(REPORT, 'utf8'));
report.checks.push(...extra.map((r) => ({ name: r.name, status: r.issues.length ? 'FAILED' : 'PASSED', issues: r.issues })));
report.summary.checksTotal = report.checks.length;
report.summary.checksPassed = report.checks.filter((c) => c.status === 'PASSED').length;
report.summary.issues += issues;
report.status = report.summary.issues ? 'FAILED' : 'PASSED';
fs.writeFileSync(REPORT, JSON.stringify(report, null, 2) + '\n');
console.log(`=== E06 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
