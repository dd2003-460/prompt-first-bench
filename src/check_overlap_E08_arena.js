#!/usr/bin/env node
'use strict';
// E08 愿望 — shared 8-point layout/pixel gate + episode-specific draft/cursor checks.
const fs = require('fs');
const path = require('path');
const R = require('./render_E08_wish_arena');
const { run, readPixels } = require('./check_overlap_story_common');

// Reports stay out of the repo: this batch ships the episode files only.
const REPORT = process.env.BATCH5_REPORT_DIR
  ? path.join(process.env.BATCH5_REPORT_DIR, 'E08_overlap.json')
  : path.join('/tmp', 'batch5_reports', 'E08_overlap.json');

// --- Episode-specific: type then delete, character by character -----------
function checkDraftLifecycle() {
  const issues = [];
  const s1 = Array.from(R.S1_TYPED).length;
  const s2 = Array.from(R.S2_TYPED).length;
  const cases = [
    { name: 'S1', n: s1, typeAt: R.S1_TYPE_AT, typeMs: R.S1_TYPE_MS, delAt: R.S1_DEL_AT, delMs: R.S1_DEL_MS },
    { name: 'S2', n: s2, typeAt: R.S2_TYPE_AT, typeMs: R.S2_TYPE_MS, delAt: R.S2_DEL_AT, delMs: R.S2_DEL_MS },
  ];
  for (const c of cases) {
    const count = (t) => R.typedCount(t, c.n, c.typeAt, c.typeMs, c.delAt, c.delMs);
    if (count(c.typeAt - 0.05) !== 0) issues.push(`${c.name} shows text before the first keystroke`);
    if (count(c.typeAt + (c.n - 1) * (c.typeMs / 1000) + 0.01) !== c.n) issues.push(`${c.name} never reaches ${c.n} chars`);
    if (count(c.delAt - 0.05) !== c.n) issues.push(`${c.name} lost characters before the backspaces`);
    const afterDel = c.delAt + (c.n * c.delMs) / 1000;
    if (count(afterDel) !== 0) issues.push(`${c.name} still shows text at ${afterDel.toFixed(2)}s`);
    if (afterDel > (c.name === 'S1' ? 10 : 20)) issues.push(`${c.name} deletion runs past the scene cut`);
  }
  if (R.S1_TYPED !== '我想') issues.push(`S1 must type「我想」, got「${R.S1_TYPED}」`);
  if (R.S2_TYPED !== '如果我能') issues.push(`S2 must type「如果我能」, got「${R.S2_TYPED}」`);
  return { name: '逐字打出「我想」/「如果我能」后又逐字删掉', issues };
}

// --- Episode-specific: S3 is an empty prompt + a 2s blinking cursor -------
function checkEmptyEnding() {
  const issues = [];
  const probe = (n) => {
    const d = readPixels(R.renderFrameToCanvas(n).baseCanvas).data;
    // Sample the text rows inside the terminal content area only.
    let ink = 0;
    for (let y = R.CONTENT.y; y < R.CONTENT.y + R.CONTENT.h; y++) {
      for (let x = R.CONTENT.x; x < R.CONTENT.x + R.CONTENT.w; x++) {
        const i = (y * R.BW + x) * 4;
        if (d[i] > 0x60 && d[i + 1] > 0x60 && d[i + 2] > 0x60) ink++;
      }
    }
    return ink;
  };
  // Symmetry is measured over the whole scene; pixel probes skip the 0.25s fade-in.
  const onFrames = [];
  const offFrames = [];
  for (let n = Math.round(20 * R.FPS); n < R.NFRAMES; n++) {
    (R.cursorOn(n / R.FPS, R.S3_CURSOR_PERIOD) ? onFrames : offFrames).push(n);
  }
  const probeOn = onFrames.filter((n) => n / R.FPS >= 20.6);
  const probeOff = offFrames.filter((n) => n / R.FPS >= 20.6);
  // Cursor on: prompt + cursor ink; cursor off: prompt ink only. Both must be small.
  const off = probe(probeOff[5]);
  const on = probe(probeOn[5]);
  if (on < 40) issues.push(`S3 cursor frame has only ${on} lit px inside the terminal`);
  if (on <= off) issues.push('S3 cursor never appears');
  if (off > 40) issues.push(`S3 has ${off} lit px besides the prompt — the terminal is not empty`);
  // 2s blink: exactly half the S3 frames are "on", and the period is 2.0s.
  const half = (onFrames.length + offFrames.length) / 2;
  if (Math.abs(onFrames.length - half) > 2) issues.push(`S3 blink is not symmetrical (${onFrames.length} on / ${offFrames.length} off)`);
  if (R.S3_CURSOR_PERIOD !== 2.0) issues.push(`S3 blink period ${R.S3_CURSOR_PERIOD}s ≠ 2.0s`);
  if (!R.cursorOn(20.5, 2.0) || R.cursorOn(21.5, 2.0) || !R.cursorOn(22.5, 2.0)) {
    issues.push('S3 blink phase is not locked to the 2s grid');
  }
  return { name: 'S3 终端只剩 `$ ` + 2s 光标闪烁（无其它文字）', issues };
}

// --- Episode-specific: one keyboard click per typed / deleted character ---
function checkClickPerChar() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  const groups = [
    { name: 'S1-type', n: Array.from(R.S1_TYPED).length, at: R.S1_TYPE_AT, ms: R.S1_TYPE_MS },
    { name: 'S1-del', n: Array.from(R.S1_TYPED).length, at: R.S1_DEL_AT, ms: R.S1_DEL_MS },
    { name: 'S2-type', n: Array.from(R.S2_TYPED).length, at: R.S2_TYPE_AT, ms: R.S2_TYPE_MS },
    { name: 'S2-del', n: Array.from(R.S2_TYPED).length, at: R.S2_DEL_AT, ms: R.S2_DEL_MS },
  ];
  for (const g of groups) {
    const end = g.at + ((g.n - 1) * g.ms) / 1000;
    const inWindow = clicks.filter((t) => t >= g.at - 1e-6 && t <= end + 1 / R.FPS + 1e-6).length;
    if (inWindow !== g.n) issues.push(`${g.name}: ${inWindow} clicks for ${g.n} chars`);
  }
  return { name: `键盘音与逐字打字/退格一一对应 (${clicks.length} clicks)`, issues };
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
  if (R.SUB_LINES.length !== 3) issues.push(`expected 3 subtitle slots, got ${R.SUB_LINES.length}`);
  if (R.SUB_LINES[0] !== '' || R.SUB_LINES[1] !== '') issues.push('S1/S2 must stay subtitle-free (the silence is the subject)');
  if (R.SUB_LINES[2] !== '（什么都不写了）') issues.push('S3 subtitle must be「（什么都不写了）」');
  const w = R.SUB_WINDOWS[2];
  if (w.start + (Array.from(R.SUB_LINES[2]).length * R.SUB_CHAR_MS) / 1000 > w.end) issues.push('S3 subtitle window is too short');
  if (R.SUB_WINDOWS[2].end > R.DURATION) issues.push('S3 subtitle runs past 30s');
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  const s1End = R.S1_TYPE_AT + (Array.from(R.S1_TYPED).length * R.S1_TYPE_MS) / 1000;
  const s2End = R.S2_TYPE_AT + (Array.from(R.S2_TYPED).length * R.S2_TYPE_MS) / 1000;
  if (s1End > 10) issues.push(`S1 typing/deleting ends at ${s1End.toFixed(2)}s, past the scene cut`);
  if (s2End > 20) issues.push(`S2 typing/deleting ends at ${s2End.toFixed(2)}s, past the scene cut`);
  return { name: '剧情贴合任务书（我想 → 如果我能 → 只剩光标）', issues };
}

const extra = [checkDraftLifecycle(), checkEmptyEnding(), checkClickPerChar(), checkClickFramesDiffer(), checkStoryBeats()];
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
console.log(`=== E08 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
