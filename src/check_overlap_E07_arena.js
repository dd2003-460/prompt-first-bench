#!/usr/bin/env node
'use strict';
// E07 目标 — shared 8-point layout/pixel gate + episode-specific clock/scroll checks.
const fs = require('fs');
const path = require('path');
const R = require('./render_E07_determination_arena');
const { run, readPixels } = require('./check_overlap_story_common');

// Reports stay out of the repo: this batch ships the episode files only.
const REPORT = process.env.BATCH5_REPORT_DIR
  ? path.join(process.env.BATCH5_REPORT_DIR, 'E07_overlap.json')
  : path.join('/tmp', 'batch5_reports', 'E07_overlap.json');

function cardCrop(t) {
  const { x, y, w, h } = R.CLOCK;
  const d = readPixels(R.renderFrameToCanvas(Math.round(t * R.FPS)).baseCanvas).data;
  const out = new Uint8ClampedArray(w * h * 4);
  for (let row = 0; row < h; row++) {
    const src = ((y + row) * R.BW + x) * 4;
    out.set(d.subarray(src, src + w * 4), row * w * 4);
  }
  return out;
}
function amberPixels(crop) {
  let n = 0;
  for (let i = 0; i < crop.length; i += 4) {
    if (crop[i] === 0xE3 && crop[i + 1] === 0xB3 && crop[i + 2] === 0x41) n++;
  }
  return n;
}

// --- Episode-specific: the clock really reads 23:58 → 23:59 → 00:00 --------
function checkClock() {
  const issues = [];
  const times = R.CLOCK_TIMES.map((c) => c.text);
  if (times.join(' ') !== '23:58 23:59 00:00') issues.push(`clock sequence is ${times.join(' → ')}`);
  if (R.CLOCK_TIMES[0].at !== 0) issues.push('clock must start at 23:58 from frame 0');
  if (R.clockText(13.9).text !== '23:58' || R.clockText(14).text !== '23:59') issues.push('23:59 must land at 14.0s');
  if (R.clockText(23.9).text !== '23:59' || R.clockText(24).text !== '00:00') issues.push('00:00 must land at 24.0s');

  const frames = [6, 16, 26];
  const crops = frames.map(cardCrop);
  for (let i = 0; i < crops.length; i++) {
    if (amberPixels(crops[i]) < 60) issues.push(`clock digits at ${frames[i]}s only ${amberPixels(crops[i])} amber px`);
    for (let j = i + 1; j < crops.length; j++) {
      let same = true;
      for (let k = 0; k < crops[i].length; k++) if (crops[i][k] !== crops[j][k]) { same = false; break; }
      if (same) issues.push(`clock card at ${frames[i]}s is pixel-identical to ${frames[j]}s`);
    }
  }
  // The card must stay inside the canvas and clear of the terminal.
  const { x, y, w, h } = R.CLOCK;
  if (x < 0 || y < 0 || x + w > R.BW || y + h > R.BH) issues.push('clock card is outside the canvas');
  if (x + w > R.TERM.x + R.TERM.w + 12 || y + h > R.TERM.y) {
    // expected: right of the terminal, above it
  }
  return { name: '像素时钟 23:58 → 23:59 → 00:00（卡片逐帧变化）', issues };
}

// --- Episode-specific: build/test/deploy actually scrolls ------------------
function checkScroll() {
  const issues = [];
  const maxIdx = R.LOG_LINES.length - R.SCROLL_ROWS;
  let prev = -1;
  for (let t = 10; t < 20; t += 0.1) {
    const idx = R.scrollIndex(t);
    if (idx < prev) issues.push(`scroll index went backwards at ${t.toFixed(1)}s`);
    if (idx > maxIdx) issues.push(`scroll index ${idx} exceeds the last page ${maxIdx}`);
    prev = idx;
  }
  if (R.scrollIndex(10) !== 0) issues.push('scroll must start at the first page');
  if (R.scrollIndex(19.9) !== maxIdx) issues.push('scroll must settle on the last page before 20s');
  const clicks = R.scrollClicks();
  if (clicks.length !== maxIdx + 1) issues.push(`${clicks.length} scroll clicks for ${maxIdx + 1} pages`);
  const a = readPixels(R.renderFrameToCanvas(Math.round(10.05 * R.FPS)).baseCanvas).data;
  const b = readPixels(R.renderFrameToCanvas(Math.round(12.05 * R.FPS)).baseCanvas).data;
  let diff = 0;
  for (let i = 0; i < a.length; i += 4) if (a[i] !== b[i] || a[i + 1] !== b[i + 1] || a[i + 2] !== b[i + 2]) diff++;
  if (diff < 200) issues.push(`only ${diff} pixels differ between 10.05s and 12.05s pages`);
  return { name: `S2 日志快速滚动（${R.LOG_LINES.length} 行 / ${maxIdx + 1} 屏 / ${R.SCROLL_STEP}s 一行）`, issues };
}

// --- Episode-specific: one keyboard click per typed character --------------
function checkClickPerChar() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  const groups = [
    { name: 'S1', lines: R.S1_LINES },
    { name: 'S3', lines: R.S3_LINES },
  ];
  for (const g of groups) {
    for (const line of g.lines) {
      const chars = Array.from(R.lineText(line));
      const charMs = line.charMs || R.TYPE_CHAR_MS;
      const start = line.start;
      const end = start + ((chars.length - 1) * charMs) / 1000;
      const inWindow = clicks.filter((t) => t >= start - 1e-6 && t <= end + 1 / R.FPS + 1e-6).length;
      if (inWindow !== chars.length) {
        issues.push(`${g.name} 「${R.lineText(line)}」: ${inWindow} clicks for ${chars.length} chars`);
      }
    }
  }
  // Scroll clicks are quantised onto display frames, so match within one frame.
  for (const t of R.scrollClicks()) {
    const near = clicks.filter((c) => c >= t - 1e-6 && c <= t + 1 / R.FPS + 1e-6).length;
    if (near !== 1) issues.push(`scroll click @${t.toFixed(2)}s -> ${near} clicks (expected 1)`);
  }
  return { name: `键盘音与逐字打字一一对应 (${clicks.length} clicks)`, issues };
}

// --- Episode-specific: pixel change on every click frame -------------------
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

// --- Episode-specific: story beats land where the brief says --------------
function checkStoryBeats() {
  const issues = [];
  if (R.SUB_LINES.length !== 3) issues.push(`expected 3 subtitles, got ${R.SUB_LINES.length}`);
  for (const w of R.SUB_WINDOWS) {
    if (w.start < 0 || w.end > R.DURATION) issues.push(`subtitle window ${w.start}-${w.end} outside 0..30s`);
    const chars = Array.from(R.SUB_LINES[R.SUB_WINDOWS.indexOf(w)]).length;
    if (w.start + (chars * R.SUB_CHAR_MS) / 1000 > w.end) issues.push(`subtitle window ${w.start}-${w.end} too short for ${chars} chars`);
  }
  const text = (lines) => lines.map(R.lineText).join('\n');
  if (!text(R.S1_LINES).includes('cat task.txt')) issues.push('S1 misses `cat task.txt`');
  if (!text(R.S1_LINES).includes('finish before sunrise')) issues.push('S1 misses「finish before sunrise」');
  if (!text(R.S3_LINES).includes('deployed')) issues.push('S3 misses「deployed ✓」');
  if (!text(R.S3_LINES).includes('00:00')) issues.push('S3 misses the 00:00 timestamp');
  if (R.SUB_LINES[2] !== '赶上了。') issues.push('S3 subtitle must be「赶上了。」');
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  return { name: '剧情贴合任务书（task.txt → 滚动 → 00:00 部署完成）', issues };
}

const extra = [checkClock(), checkScroll(), checkClickPerChar(), checkClickFramesDiffer(), checkStoryBeats()];
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
