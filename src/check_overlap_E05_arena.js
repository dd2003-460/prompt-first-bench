#!/usr/bin/env node
'use strict';
// E05 惊讶 — shared 8-point layout/pixel gate (0px tolerance) + surprise-specific checks:
//   白屏恰好 30 帧且硬边 / 25% → 100% 原地翻转 / PID 9999 持续可见 / 惊讶脸 + 后仰 2px /
//   每字符一次键盘音（白屏期间静音）/ 场景硬切无黑场过渡。
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E05_surprise_arena');
const { run, readPixels } = require('./check_overlap_story_common');

// Reports stay out of the repo: this batch ships only the episode deliverables.
const REPORT = process.env.BATCH6_REPORT_DIR
  ? path.join(process.env.BATCH6_REPORT_DIR, 'E05_overlap.json')
  : path.join('/tmp', 'batch6_reports', 'E05_overlap.json');

const frameAt = (t) => R.renderFrameToCanvas(Math.round(t * R.FPS)).baseCanvas;
const dataAt = (t) => readPixels(frameAt(t)).data;
const rgbOf = (hex) => {
  const n = parseInt(hex.slice(1), 16);
  return `${(n >> 16) & 255},${(n >> 8) & 255},${n & 255}`;
};
const atW = (d, x, y, w) => { const i = (y * w + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
const at = (d, x, y) => atW(d, x, y, R.BW);
function countIn(d, x0, y0, x1, y1, pred, w = R.BW) {
  let n = 0;
  for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) if (pred(atW(d, x, y, w))) n++;
  return n;
}
const TERM_IN = [R.TERM.x + 2, R.TERM.y + 2, R.TERM.x + R.TERM.w - 2, R.TERM.y + R.TERM.h - 2];

// --- 白屏 0.5s = 恰好 30 帧，前后硬边，期间静音 ---------------------------
function checkWhiteFlash() {
  const issues = [];
  const WHITE = '255,255,255';
  const [x0, y0, x1, y1] = TERM_IN;
  const area = (x1 - x0) * (y1 - y0);
  const frac = (n) => countIn(readPixels(R.renderFrameToCanvas(n).baseCanvas).data, x0, y0, x1, y1, (c) => c === WHITE) / area;
  const first = Math.round(R.FLASH_START * R.FPS);   // 600
  const last = Math.round(R.FLASH_END * R.FPS) - 1;  // 629
  if (last - first + 1 !== 30 || R.FLASH_FRAMES !== 30) issues.push(`white flash is ${last - first + 1} frames, expected exactly 30 (0.5s @60fps)`);
  for (let n = first; n <= last; n++) {
    const f = frac(n);
    if (f !== 1) issues.push(`frame ${n} (t=${(n / R.FPS).toFixed(4)}s) is ${(f * 100).toFixed(1)}% white, expected 100%`);
  }
  // 前后帧无过渡：相邻帧要么全白要么几乎无白，不允许中间态。
  for (let n = first - 30; n <= last + 30; n++) {
    const f = frac(n);
    const inFlash = n >= first && n <= last;
    if (inFlash && f < 1) issues.push(`frame ${n} inside the flash is not pure white (${(f * 100).toFixed(1)}%)`);
    if (!inFlash && f > 0.02) issues.push(`frame ${n} outside the flash has ${(f * 100).toFixed(1)}% white (fade/transition leak)`);
  }
  if (frac(first - 1) >= frac(first)) issues.push('the flash does not start on a hard edge');
  if (frac(last + 1) >= frac(last)) issues.push('the flash does not end on a hard edge');
  const during = R.getClickTimestamps().filter((t) => t >= R.FLASH_START && t < R.FLASH_END);
  if (during.length) issues.push(`${during.length} keyboard click(s) during the white flash (must be silent)`);
  return { name: `白屏恰好 ${R.FLASH_FRAMES} 帧 (10.000-10.483s) 硬边 + 期间静音`, issues };
}

// --- 同一行 df 输出从 25% 原地翻转成 100% ---------------------------------
function checkDiskFlip() {
  const issues = [];
  const rowY = R.LINE_DF_25.y;
  const textAt = (t) => R.activeLines(t).map(R.lineText).join('\n');
  if (!textAt(R.FLASH_START - 0.1).includes('380G    25%')) issues.push('before the flash the row must read 380G / 25%');
  if (!textAt(R.FLASH_END).includes('500G  500G     0   100%')) issues.push('after the flash the row must read 500G / 0 / 100%');
  if (textAt(R.FLASH_END).includes('25%')) issues.push('the 25% row is still on screen after the flash');
  const GREEN = rgbOf(R.C.green), RED = rgbOf(R.C.red);
  const band = [R.TEXT_X, rowY, 420, rowY + 14];
  const before = dataAt(R.FLASH_START - 1 / R.FPS);
  const after = dataAt(R.FLASH_END + 1 / R.FPS);
  const gB = countIn(before, ...band, (c) => c === GREEN);
  const rB = countIn(before, ...band, (c) => c === RED);
  const gA = countIn(after, ...band, (c) => c === GREEN);
  const rA = countIn(after, ...band, (c) => c === RED);
  if (!(gB > 0)) issues.push('no green 25% ink before the flash');
  if (!(rB === 0)) issues.push(`red ink (${rB}px) in the df row before the flash`);
  if (!(rA > 0)) issues.push('no red 100% ink after the flash');
  if (!(gA === 0)) issues.push(`green ink (${gA}px) left in the df row after the flash`);
  // 100% 行必须停在原位（同一 y），不是新增一行
  if (R.LINE_DF_100.y !== R.LINE_DF_25.y) issues.push('the 100% row must replace the 25% row in place');
  return { name: `df 行原地翻转：25% (绿 ${gB}px) → 100% (红 ${rA}px) @ y=${rowY}`, issues };
}

// --- 陌生进程 PID 9999 从落地到 30s 持续可见 ------------------------------
function checkUnknownProcess() {
  const issues = [];
  const textAt = (t) => R.activeLines(t).map(R.lineText).join('\n');
  const from = R.PID_LANDED_AT;
  let sampled = 0;
  for (let t = from; t <= R.DURATION - 0.05; t += 0.25) {
    sampled++;
    const txt = textAt(t);
    if (!txt.includes('9999')) issues.push(`t=${t.toFixed(2)}s: PID 9999 not on screen`);
    if (!txt.includes('unknown_process')) issues.push(`t=${t.toFixed(2)}s: unknown_process not on screen`);
  }
  if (!textAt(R.DURATION - 0.05).includes('00:00:10')) issues.push('etime 00:00:10 missing at the end');
  if (!textAt(29.9).includes('ps -o etime= -p 9999')) issues.push('the etime command is missing at the end');
  // 像素证据：ps 行与 etime 行在 S3 全程有墨
  const bands = [[R.TEXT_X, R.LINE_PS_ROW.y, 420, R.LINE_PS_ROW.y + 14], [R.TEXT_X, R.LINE_ETIME_ROW.y, 200, R.LINE_ETIME_ROW.y + 14]];
  const BG = rgbOf(R.C.termBg);
  for (const t of [20.2, 24.5, 27.0, 29.5]) {
    const d = dataAt(t);
    bands.forEach((b, i) => {
      const ink = countIn(d, ...b, (c) => c !== BG);
      if (!ink) issues.push(`t=${t}s band ${i}: no terminal ink where the process lines must be`);
    });
  }
  return { name: `陌生进程 PID 9999 持续可见 (${from.toFixed(2)}s → 30.00s, ${sampled} samples)`, issues };
}

// --- 惊讶脸：半闭 → 圆眼 → 圆眼 + 后仰 2px --------------------------------
function checkSurpriseFace() {
  const issues = [];
  const W = 160, H = 100, X = 60, Y = 40, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const drawPose = (t) => {
    ctx.fillStyle = BG; ctx.fillRect(0, 0, W, H);
    const p = R.clawdPose(t);
    R.drawClawdEp(ctx, X, Y, t, p.mood, 0, { dx: p.dx, dy: p.dy, noBob: true });
    return readPixels(cv).data;
  };
  const px_ = (d, x, y) => { const i = (y * W + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
  const EYE = rgbOf(R.C.clawdEye), BODY = '217,119,87', DARK = '184,90,59', BGC = rgbOf(BG), WHITE = '255,255,255';
  const idle = drawPose(5);        // S1 calm / 眼睛半闭
  const surp = drawPose(12);       // 白屏后：眼睛突然变圆
  const start = drawPose(20);      // S3：身体后仰 2px
  if (px_(idle, X + 10, Y + 8) !== EYE) issues.push('idle eyes are not half-closed 4×2 slits');
  if (px_(idle, X + 10, Y + 6) === EYE || px_(idle, X + 11, Y + 7) === WHITE) issues.push('idle eyes must not be wide open / highlighted');
  if (px_(surp, X + 10, Y + 5) !== EYE || px_(surp, X + 9, Y + 6) !== EYE || px_(surp, X + 14, Y + 9) !== EYE) {
    issues.push('surprised eyes are not the 6×6 round shape');
  }
  if (px_(surp, X + 10, Y + 6) !== WHITE) issues.push('surprised eyes lost the 2×2 highlight');
  const eyeInk = (d) => countIn(d, X + 8, Y + 4, X + 16, Y + 11, (c) => c === EYE || c === WHITE, W);
  if (eyeInk(surp) <= eyeInk(idle)) issues.push(`surprised eye is not bigger than idle (${eyeInk(idle)} → ${eyeInk(surp)} px)`);
  // 后仰 2px：身体左上角移到 (X-2, Y-2)，右边缘离开 (X+38, Y-2)
  if (px_(start, X - 2, Y - 2) !== DARK) issues.push('startled body did not lean back 2px (top strip not at X-2,Y-2)');
  if (px_(surp, X - 2, Y - 2) !== BGC) issues.push('surprised pose must not already be shifted');
  if (px_(start, X + 38, Y - 2) !== BGC) issues.push('startled body is still 40px wide at the un-shifted origin');
  if (px_(start, X - 2 + 9, Y - 2 + 3) !== EYE) issues.push('startled pose lost the raised eyebrows');
  if (R.clawdPose(9.9).mood !== 'idle' || R.clawdPose(10).mood !== 'surprised' || R.clawdPose(15).mood !== 'startled') {
    issues.push('pose timeline is not idle → surprised(10s) → startled(15s)');
  }
  return { name: 'Clawd 惊讶：半闭眼 → 6×6 圆眼 → 圆眼+抬眉+后仰 2px', issues };
}

// --- 每字符一次键盘音 ------------------------------------------------------
function checkClickPerChar() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  for (const line of R.ALL_LINES) {
    const chars = Array.from(R.lineText(line));
    if (line.typed === false) {
      const q = Math.ceil(line.start * R.FPS - 1e-9) / R.FPS;
      const hit = clicks.filter((t) => Math.abs(t - q) < 1e-6).length;
      if (hit !== 1) issues.push(`instant row 「${R.lineText(line)}」 has ${hit} clicks, expected exactly 1 @${q}s`);
      continue;
    }
    const charMs = line.charMs || R.TYPE_CHAR_MS;
    const end = line.start + ((chars.length - 1) * charMs) / 1000;
    const inWindow = clicks.filter((t) => t >= line.start - 1e-6 && t <= end + 1 / R.FPS + 1e-6).length;
    if (inWindow !== chars.length) {
      issues.push(`「${R.lineText(line)}」: ${inWindow} clicks for ${chars.length} chars (charMs=${charMs})`);
    }
  }
  const typedChars = R.ALL_LINES.reduce((n, l) => n + (l.typed === false ? 1 : Array.from(R.lineText(l)).length), 0);
  if (clicks.length !== typedChars) issues.push(`total ${clicks.length} clicks ≠ ${typedChars} character events`);
  return { name: `键盘音与文字同步：${clicks.length} clicks / ${typedChars} 字符事件`, issues };
}

// --- 每个键盘音对应一帧可见变化 -------------------------------------------
function checkClickFramesDiffer() {
  const issues = [];
  const clicks = R.getClickTimestamps().filter((t) => t * R.FPS >= 2 && !(t >= R.FLASH_START && t < R.FLASH_END));
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

// --- 场景硬切（无黑场过渡）+ 剧情贴合 -------------------------------------
function checkHardCutsAndStory() {
  const issues = [];
  const BLACK = (c) => { const [r, g, b] = c.split(',').map(Number); return r + g + b < 40; };
  for (const n of [...Array.from({ length: 60 }, (_, i) => 570 + i), ...Array.from({ length: 60 }, (_, i) => 1170 + i)]) {
    const d = readPixels(R.renderFrameToCanvas(n).baseCanvas).data;
    const dark = countIn(d, 0, 0, R.BW, R.BH, BLACK) / (R.BW * R.BH);
    if (dark > 0.35) issues.push(`frame ${n} (t=${(n / R.FPS).toFixed(2)}s) is ${(dark * 100).toFixed(0)}% black — scene cut must be a hard cut`);
  }
  const text = (lines) => lines.map(R.lineText).join('\n');
  const all = text(R.ALL_LINES);
  for (const needle of ['$ df -h', 'Filesystem   Size  Used Avail Capacity', '/dev/disk3   500G  120G  380G    25%',
    '/dev/disk3   500G  500G     0   100%', '$ ps aux | grep -v grep', 'user  9999  99.9  45.2  unknown_process',
    '$ lsof -p 9999', 'unknown_process  /dev/null  ???', '$ ps -o etime= -p 9999', '00:00:10']) {
    if (!all.includes(needle)) issues.push(`terminal never shows 「${needle}」`);
  }
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(19.9) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  if (R.SUB_LINES.join('|') !== '一切正常。|它出现了 10 秒。|谁放进来的？') issues.push(`subtitles deviate from the brief: ${R.SUB_LINES.join('|')}`);
  if (Math.abs(R.SUB_WINDOWS[1].start - 25.0) > 1e-9 || Math.abs(R.SUB_WINDOWS[2].start - 28.0) > 1e-9) issues.push('S3 subtitles must start at 25s and 28s');
  return { name: '场景硬切（10s 由白屏承担 / 20s 内容连续）+ 终端文本贴合任务书', issues };
}

const extra = [
  checkWhiteFlash(), checkDiskFlip(), checkUnknownProcess(),
  checkSurpriseFace(), checkClickPerChar(), checkClickFramesDiffer(), checkHardCutsAndStory(),
];
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
console.log(`=== E05 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
