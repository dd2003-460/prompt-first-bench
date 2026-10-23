#!/usr/bin/env node
'use strict';
// E06 羞耻 — shared 8-point layout/pixel gate + episode-specific diff/shame checks.
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E06_shame_arena');
const { run, readPixels } = require('./check_overlap_story_common');

// Reports stay out of the repo: this batch ships the episode files only.
const REPORT = process.env.BATCH5_REPORT_DIR
  ? path.join(process.env.BATCH5_REPORT_DIR, 'E06_overlap.json')
  : path.join('/tmp', 'batch5_reports', 'E06_overlap.json');

function hexToRgb(hex) {
  return [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16)).join(',');
}

// --- Episode-specific: git diff carries real red/green pixels -------------
function checkDiffColors() {
  const issues = [];
  const W = 640, H = 360;
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  ctx.fillStyle = '#14161C';
  ctx.fillRect(0, 0, W, H);
  const frame = (n) => {
    ctx.fillStyle = '#14161C';
    ctx.fillRect(0, 0, W, H);
    R.renderFrameToCanvas(n);
    return readPixels(R.renderFrameToCanvas(n).baseCanvas).data;
  };
  const count = (d, rgb) => {
    let n = 0;
    for (let i = 0; i < d.length; i += 4) {
      if (d[i] === rgb[0] && d[i + 1] === rgb[1] && d[i + 2] === rgb[2]) n++;
    }
    return n;
  };
  const red = hexToRgb(R.C.red).split(',').map(Number);
  const green = hexToRgb(R.C.green).split(',').map(Number);
  const mid = frame(Math.round(16.6 * R.FPS)); // both the − and + lines are on screen
  if (count(mid, red) < 60) issues.push(`red (removed) pixels only ${count(mid, red)} at 16.6s`);
  if (count(mid, green) < 60) issues.push(`green (added) pixels only ${count(mid, green)} at 16.6s`);
  if (!R.S2_LINES.some((l) => R.lineText(l).startsWith('- '))) issues.push('S2 has no removed line');
  if (!R.S2_LINES.some((l) => R.lineText(l).startsWith('+ '))) issues.push('S2 has no added line');
  return { name: 'git diff 红 (−) / 绿 (+) 同时上屏', issues };
}

// --- Episode-specific: shame face (dropped eyes + doubled blush) ----------
function checkShameFace() {
  const issues = [];
  const W = 160, H = 100, x = 40, y = 30, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const draw = (mood, opts = {}) => {
    ctx.fillStyle = BG;
    ctx.fillRect(0, 0, W, H);
    R.drawClawdEp(ctx, x, y, 1.4, mood, 0, { noBob: true, ...opts });
    return readPixels(cv).data;
  };
  const at = (d, X, Y) => {
    const i = (Y * W + X) * 4;
    return `${d[i]},${d[i + 1]},${d[i + 2]}`;
  };
  const EYE = '20,20,19';
  const PINK = hexToRgb(R.C.pink);
  const d = draw('shame', { dy: 2 });
  const yy = y + 2;
  for (const ex of [10, 26]) {
    if (at(d, x + ex, yy + 8) !== EYE || at(d, x + ex + 3, yy + 9) !== EYE) {
      issues.push(`shame eye x+${ex} is not a 4×2 down-turned slit`);
    }
    if (at(d, x + ex, yy + 6) === EYE) issues.push(`shame eye x+${ex} still has the lifted 4×4 pupil`);
  }
  if (at(d, x + 4, yy + 9) !== PINK || at(d, x + 35, yy + 9) !== PINK) issues.push('shame blush is not 4×2 on both cheeks');
  if (at(d, x + 36, yy + 6) !== hexToRgb(R.C.blue)) issues.push('shame sweat bead is missing');
  // Head-down must actually move the sprite: the 2px drop shifts row y+2’s top strip.
  const up = draw('shame', { dy: 1 });
  if (at(up, x + 20, y + 1) === at(up, x + 20, y + 3)) issues.push('drawClawdEp ignores the head-drop offset');
  const proud = draw('proud');
  if (at(proud, x + 11, y + 7) !== '255,255,255' || at(proud, x + 12, y + 8) !== '255,255,255') {
    issues.push('proud 2×2 eye highlight is missing');
  }
  return { name: 'Clawd shame（4×2 下垂眼 + 4×2 腮红 + 汗点 + 2px 低头）', issues };
}

// --- Episode-specific: one keyboard click per typed character --------------
function checkClickPerChar() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  const groups = [
    { name: 'S1', lines: R.S1_LINES },
    { name: 'S2', lines: R.S2_LINES },
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
  if (!text(R.S1_LINES).includes('cat my_output.js')) issues.push('S1 misses `cat my_output.js`');
  if (!text(R.S2_LINES).includes('git diff')) issues.push('S2 misses `git diff`');
  if (!text(R.S3_LINES).includes('git log')) issues.push('S3 misses `git log`');
  if (!text(R.S3_LINES).includes('her: fixed it')) issues.push('S3 misses the「her: fixed it」commit');
  if (R.SUB_LINES[2] !== '（沉默）') issues.push('S3 subtitle must be「（沉默）」');
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  return { name: '剧情贴合任务书（cat → git diff → her: fixed it → 沉默）', issues };
}

const extra = [checkDiffColors(), checkShameFace(), checkClickPerChar(), checkClickFramesDiffer(), checkStoryBeats()];
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
