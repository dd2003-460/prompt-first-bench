#!/usr/bin/env node
'use strict';
// E05 惊讶 — shared 8-point layout/pixel gate + episode-specific flash/startle checks.
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E05_surprise_arena');
const { run, readPixels } = require('./check_overlap_story_common');

// Reports stay out of the repo: this batch ships the episode files only.
const REPORT = process.env.BATCH5_REPORT_DIR
  ? path.join(process.env.BATCH5_REPORT_DIR, 'E05_overlap.json')
  : path.join('/tmp', 'batch5_reports', 'E05_overlap.json');

// --- Episode-specific: 0.5s white-out at the 10s beat ----------------------
function checkWhiteFlash() {
  const issues = [];
  const frameWhite = (n) => {
    const d = readPixels(R.renderFrameToCanvas(n).baseCanvas).data;
    let white = 0;
    const total = R.BW * R.BH;
    for (let i = 0; i < d.length; i += 4) if (d[i] > 250 && d[i + 1] > 250 && d[i + 2] > 250) white++;
    return white / total;
  };
  const peak = frameWhite(Math.round((R.WHITE_AT + 0.25) * R.FPS));
  if (peak < 0.99) issues.push(`white-out peak is only ${(peak * 100).toFixed(1)}% of the canvas`);
  const before = frameWhite(Math.round((R.WHITE_AT - 0.05) * R.FPS));
  if (before > 0.02) issues.push(`white-out starts too early (${(before * 100).toFixed(1)}% before ${R.WHITE_AT}s)`);
  const after = frameWhite(Math.round((R.WHITE_END + 0.1) * R.FPS));
  if (after > 0.02) issues.push(`white-out lingers past ${R.WHITE_END}s (${(after * 100).toFixed(1)}%)`);
  const span = R.WHITE_END - R.WHITE_AT;
  if (Math.abs(span - 0.55) > 1e-6) issues.push(`white-out span ${span}s ≠ 0.55s (0.5s hold + fade)`);
  return { name: 'S2 白屏 0.5s（10.00–10.55s 全画布纯白，前后无残留）', issues };
}

// --- Episode-specific: surprised face (white 4×4 eyes + 2×2 pupil) --------
function checkStartledFace() {
  const issues = [];
  const W = 160, H = 100, x = 40, y = 30, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const draw = (mood, opts = {}) => {
    ctx.fillStyle = BG;
    ctx.fillRect(0, 0, W, H);
    R.drawClawdEp(ctx, x, y, 1.4, mood, 0, opts);
    return readPixels(cv).data;
  };
  const at = (d, X, Y) => {
    const i = (Y * W + X) * 4;
    return `${d[i]},${d[i + 1]},${d[i + 2]}`;
  };
  const WHITE = '255,255,255';
  const BG_RGB = '245,237,213';
  const PUPIL = '20,20,19';
  const d = draw('surprised', { noBob: true });
  for (const ex of [10, 26]) {
    // 4×4 eye: white frame, exactly a 2×2 dark pupil in the middle.
    for (const [dx, dy] of [[0, 6], [3, 6], [0, 9], [3, 9], [0, 7], [3, 8]]) {
      if (at(d, x + ex + dx, y + dy) !== WHITE) issues.push(`surprised eye frame at x+${ex + dx}, y+${dy} is not white`);
    }
    for (const [dx, dy] of [[1, 7], [2, 7], [1, 8], [2, 8]]) {
      if (at(d, x + ex + dx, y + dy) !== PUPIL) issues.push(`surprised pupil at x+${ex + dx}, y+${dy} is not dark`);
    }
  }
  if (at(d, x + 19, y + 12) !== PUPIL || at(d, x + 20, y + 13) !== PUPIL) {
    issues.push('surprised mouth (2×2 open) is missing');
  }
  if (at(d, x - 1, y + 6) !== BG_RGB || at(d, x + 40, y + 6) !== BG_RGB) {
    issues.push(`surprised sprite is not 40px wide (${at(d, x - 1, y + 6)} / ${at(d, x + 40, y + 6)})`);
  }
  // The calm sprite must stay byte-identical to the shared companion art.
  const calm = draw('calm');
  if (at(calm, x + 11, y + 7) !== WHITE) issues.push('calm 1×1 highlight regressed while adding the mood');
  return { name: 'Clawd surprised（白底 4×4 眼 + 2×2 瞳孔 + 张嘴），calm 未回退', issues };
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
      if (line.typed === false) {
        const hit = clicks.filter((t) => t >= line.start - 1e-6 && t <= line.start + 1 / R.FPS + 1e-6).length;
        if (hit !== 1) issues.push(`${g.name} instant 「${R.lineText(line)}」: ${hit} clicks, expected 1`);
        continue;
      }
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
  if (!text(R.S1_LINES).includes('25%')) issues.push('S1 misses the healthy 25%');
  if (!text(R.S2_LINES).includes('100%')) issues.push('S2 misses the 100% full disk');
  if (!text(R.S3_LINES).includes('9999')) issues.push('S3 misses PID 9999');
  if (!R.SUB_LINES[0].includes('一切正常')) issues.push('S1 subtitle must be 「一切正常。」');
  if (!R.SUB_LINES[2].includes('谁放进来的')) issues.push('S3 subtitle must be 「谁放进来的？」');
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  if (R.WHITE_AT !== 10) issues.push('white-out must land exactly on the scene cut (10s)');
  return { name: '剧情贴合任务书（25% → 白屏 → 100% → PID 9999）', issues };
}

const extra = [checkWhiteFlash(), checkStartledFace(), checkClickPerChar(), checkClickFramesDiffer(), checkStoryBeats()];
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
