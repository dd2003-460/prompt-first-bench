#!/usr/bin/env node
'use strict';
// E07 目标 — shared 8-point layout/pixel gate (0px tolerance) + determination-specific checks:
//   时钟三态 23:58→23:59(10s)→00:00(22s) + 跳变闪光 / 终端滚动平滑（逐帧 ≤2px、无跳行）/
//   finish before sunrise 全链路文本 / determined→relieved 表情 / 每字符一次键盘音。
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E07_determination_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH6_REPORT_DIR
  ? path.join(process.env.BATCH6_REPORT_DIR, 'E07_overlap.json')
  : path.join('/tmp', 'batch6_reports', 'E07_overlap.json');

const dataAt = (t) => readPixels(R.renderFrameToCanvas(Math.round(t * R.FPS)).baseCanvas).data;
const rgbOf = (hex) => { const n = parseInt(hex.slice(1), 16); return `${(n >> 16) & 255},${(n >> 8) & 255},${n & 255}`; };
const atW = (d, x, y, w) => { const i = (y * w + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
const at = (d, x, y) => atW(d, x, y, R.BW);
function countIn(d, x0, y0, x1, y1, pred, w = R.BW) {
  let n = 0;
  for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) if (pred(atW(d, x, y, w))) n++;
  return n;
}
function bandSig(d, x0, y0, x1, y1) {
  const out = [];
  for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) out.push(atW(d, x, y, R.BW));
  return out.join(';');
}

// --- 右上角时钟：三个读数 + 10s/22s 跳变闪光 -------------------------------
function checkClock() {
  const issues = [];
  for (const [t, want] of [[0, '23:58'], [5, '23:58'], [9.9, '23:58'], [10, '23:59'], [15, '23:59'], [21.9, '23:59'], [22, '00:00'], [29.9, '00:00']]) {
    if (R.clockAt(t) !== want) issues.push(`clockAt(${t}) = ${R.clockAt(t)}, expected ${want}`);
  }
  const AMBER = rgbOf(R.C.amber), WHITE = '255,255,255';
  const [dx0, dy0] = [R.CLOCK.x + 22, R.CLOCK.y + 5];
  const d5 = dataAt(5), d12 = dataAt(12), d25 = dataAt(25);
  const amber5 = countIn(d5, dx0, dy0, dx0 + 26, dy0 + 14, (c) => c === AMBER);
  const amber12 = countIn(d12, dx0, dy0, dx0 + 26, dy0 + 14, (c) => c === AMBER);
  const amber25 = countIn(d25, dx0, dy0, dx0 + 26, dy0 + 14, (c) => c === AMBER);
  if (!amber5 || !amber12 || !amber25) issues.push(`clock digits are not amber ink in all three phases (${amber5}/${amber12}/${amber25}px)`);
  const s5 = bandSig(d5, dx0, dy0, dx0 + 26, dy0 + 14);
  const s12 = bandSig(d12, dx0, dy0, dx0 + 26, dy0 + 14);
  const s25 = bandSig(d25, dx0, dy0, dx0 + 26, dy0 + 14);
  if (s5 === s12 || s12 === s25 || s5 === s25) issues.push('the three clock readings do not render as different digits');
  const dFlash = dataAt(R.CLOCK_FLASH_AT[0] + 0.1);
  const whiteFlash = countIn(dFlash, R.CLOCK.x, R.CLOCK.y, R.CLOCK.x + R.CLOCK.w, R.CLOCK.y + R.CLOCK.h, (c) => c === WHITE);
  const dCalm = dataAt(5);
  const whiteCalm = countIn(dCalm, R.CLOCK.x, R.CLOCK.y, R.CLOCK.x + R.CLOCK.w, R.CLOCK.y + R.CLOCK.h, (c) => c === WHITE);
  if (!(whiteFlash > whiteCalm)) issues.push('the clock does not flash white on the minute change');
  // 时钟盒在右上角且不越界、不与终端/字幕重叠
  if (R.CLOCK.x + R.CLOCK.w > R.BW || R.CLOCK.y < 0) issues.push('clock card outside canvas');
  if (R.CLOCK.y + R.CLOCK.h > R.TERM.y) issues.push('clock card collides with the terminal');
  return { name: `右上角时钟 23:58 → 23:59 (10s) → 00:00 (22s) + 跳变闪光`, issues };
}

// --- 终端滚动：平滑、无跳行、滚出的行不再出现 ------------------------------
function checkScroll() {
  const issues = [];
  const t0 = R.SCROLL_STEPS[0].at;
  const t1 = R.SCROLL_STEPS[1].at + R.SCROLL_MS;
  if (R.scrollAt(t0 - 0.05) !== 0) issues.push('scroll must start at 0');
  if (R.scrollAt(t1 + 0.05) !== R.ROW_GAP * 2) issues.push('scroll must settle at two row heights');
  let prev = 0;
  let maxStep = 0;
  for (let n = Math.round((t0 - 0.05) * R.FPS); n <= Math.round((t1 + 0.05) * R.FPS); n++) {
    const cur = R.scrollAt(n / R.FPS);
    if (cur < prev) issues.push(`scroll went backwards at frame ${n}`);
    maxStep = Math.max(maxStep, cur - prev);
    prev = cur;
  }
  if (maxStep > 2) issues.push(`scroll jumps ${maxStep}px in one frame (not smooth)`);
  // 停稳后 8 行铺满视口，滚出的行彻底消失（无残行）
  const rows = R.s2Visible(19.5);
  if (rows.length !== R.VIEW_ROWS) issues.push(`expected ${R.VIEW_ROWS} visible rows at rest, got ${rows.length}`);
  if (rows[0].line.y !== 2) issues.push(`top visible row at 19.5s must be index 2, got ${rows[0].line.y}`);
  if (rows.some((r) => r.hh !== 14 || r.top !== R.ROW_TOP + (r.line.y - 2) * R.ROW_GAP)) issues.push('rows are not settled on the 17px grid at rest');
  // 滚动中途：被裁的行申报高度 < 14 且 ≥1（逐像素滑出，无整行闪现/消失）
  const mid = R.s2Visible(t0 + R.SCROLL_MS / 2);
  const partial = mid.filter((r) => r.hh < 14);
  if (!partial.length) issues.push('no partially clipped row mid-scroll (scroll is not gradual)');
  if (partial.some((r) => r.hh <= 0)) issues.push('declared a zero-height row');
  // 像素证据：19.6s 顶行是 amber 的 `> 99.9%`，不是带绿色提示符的命令行
  const AMBER = rgbOf(R.C.amber), GREEN = rgbOf(R.C.green);
  const d = dataAt(19.6);
  const topAmber = countIn(d, R.TEXT_X, R.ROW_TOP, 500, R.ROW_TOP + 14, (c) => c === AMBER);
  const topGreen = countIn(d, R.TEXT_X, R.ROW_TOP, 500, R.ROW_TOP + 14, (c) => c === GREEN);
  if (!topAmber) issues.push('top row at 19.6s is not the amber 99.9% line');
  if (topGreen) issues.push('a command line with a green prompt is still at the top after two scrolls');
  // 10 行日志文本齐全（任务书原文）
  const all = R.S2_LINES.map(R.lineText).join('\n');
  for (const needle of ['$ npm run build', '> building...', '> 99.9%', '$ npm test', '> 47 passed, 0 failed', '> 100%', '$ deploy --prod', '> deploying...']) {
    if (!all.includes(needle)) issues.push(`S2 log misses 「${needle}」`);
  }
  return { name: `终端滚动平滑 (每帧 ≤${maxStep}px) 且 8 行视口停稳、滚出无残行`, issues };
}

// --- 完成链路 + 时钟 00:00 + 字幕 cue --------------------------------------
function checkFinishBeats() {
  const issues = [];
  const text = (lines) => lines.map(R.lineText).join('\n');
  if (!text(R.S1_LINES).includes('finish before sunrise')) issues.push('S1 misses the single task line');
  const s3 = text(R.S3_LINES);
  for (const needle of ['> deployed ✓', '$ echo "done"', 'done', '$ date', 'Thu Oct 24 00:00:01 CST 2026']) {
    if (!s3.includes(needle)) issues.push(`S3 misses 「${needle}」`);
  }
  if (R.clockAt(22) !== '00:00') issues.push('clock must read 00:00 from 22s');
  const dateRow = R.S3_LINES.find((l) => R.lineText(l).startsWith('Thu Oct'));
  if (dateRow.start < 24) issues.push('$ date output must land at/after 24s');
  if (Math.abs(R.SUB_WINDOWS[2].start - 27) > 1e-9) issues.push('「赶上了。」must start at 27s');
  if (R.SUB_WINDOWS[3].start > 28.8) issues.push('「（天还没亮）」must be visible before the fade');
  if (R.SUB_LINES.join('|') !== '天亮之前。|还差一点。|赶上了。|（天还没亮）') issues.push(`subtitles deviate: ${R.SUB_LINES.join('|')}`);
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  // 窗外必须保持深夜（天还没亮）
  const d = dataAt(29.0);
  const sky = at(d, 300, 40);
  const dawnish = sky.startsWith('135,') || sky.startsWith('255,'); // dawnSkyTop #87CEEB / dawnSkyBottom #FFE4B5
  if (dawnish) issues.push(`window sky turned to dawn at 29s (${sky}); the brief says 天还没亮`);
  return { name: '完成链路 deployed ✓ → echo done → date 00:00:01 + 窗外仍是深夜', issues };
}

// --- determined → relieved 表情像素 ----------------------------------------
function checkFaces() {
  const issues = [];
  const W = 160, H = 100, X = 60, Y = 40;
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const draw = (mood) => {
    ctx.fillStyle = '#F5EDD5'; ctx.fillRect(0, 0, W, H);
    R.drawClawdEp(ctx, X, Y, 1.4, mood, 0, { noBob: true });
    return readPixels(cv).data;
  };
  const px_ = (d, x, y) => { const i = (y * W + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
  const EYE = rgbOf(R.C.clawdEye), WHITE = '255,255,255';
  const det = draw('determined');
  const rel = draw('relieved');
  if (px_(det, X + 9, Y + 4) !== EYE || px_(det, X + 30, Y + 4) !== EYE) issues.push('determined brows missing (压眉)');
  if (px_(det, X + 10, Y + 6) !== EYE || px_(det, X + 13, Y + 9) !== EYE) issues.push('determined eyes are not fully open 4×4');
  if (px_(det, X + 11, Y + 7) !== WHITE || px_(det, X + 12, Y + 8) !== WHITE) issues.push('determined eyes lost the 2×2 highlight');
  if (px_(det, X + 17, Y + 13) !== EYE) issues.push('determined mouth is not a tight flat line (抿嘴)');
  if (px_(det, X + 16, Y + 12) === EYE || px_(det, X + 23, Y + 12) === EYE) issues.push('determined mouth must not curve up (that is relief)');
  if (px_(rel, X + 10, Y + 7) !== EYE || px_(rel, X + 13, Y + 8) !== EYE) issues.push('relieved eyes are not half-closed 4×2');
  if (px_(rel, X + 11, Y + 7) === WHITE) issues.push('relieved eyes must not keep the highlight');
  if (px_(rel, X + 16, Y + 12) !== EYE || px_(rel, X + 23, Y + 12) !== EYE || px_(rel, X + 19, Y + 13) !== EYE) issues.push('relieved mouth is not the micro upturn (嘴角微扬)');
  return { name: 'Clawd 目标：determined (睁眼+高光+抿嘴+压眉) → relieved (微闭+嘴角微扬)', issues };
}

// --- 每字符一次键盘音 + 音画同步 -------------------------------------------
function checkClickPerChar() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  let events = 0;
  const groups = [
    { name: 'S1', lines: R.S1_LINES, limit: 9.6 },
    { name: 'S2', lines: R.S2_LINES, limit: 19.6 },
    { name: 'S3', lines: R.S3_LINES, limit: 29.5 },
  ];
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

const extra = [checkClock(), checkScroll(), checkFinishBeats(), checkFaces(), checkClickPerChar(), checkClickFramesDiffer()];
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
console.log(`=== E07 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
