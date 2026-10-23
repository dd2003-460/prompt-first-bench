#!/usr/bin/env node
'use strict';
// E08 愿望 — shared 8-point layout/pixel gate (0px tolerance) + wish-specific checks:
//   打字-删除节奏 (S1 3-5s / S2 12-15s) 逐字退格 / 最后 8s 终端只有光标（慢闪 0.8s）/
//   键盘音 = 打字 2+4 click + 退格 2+4 click，S3 静音 / wistful 表情 / 无便签无 status。
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E08_wish_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH6_REPORT_DIR
  ? path.join(process.env.BATCH6_REPORT_DIR, 'E08_overlap.json')
  : path.join('/tmp', 'batch6_reports', 'E08_overlap.json');

const frameAt = (n) => R.renderFrameToCanvas(n).baseCanvas;
const dataAt = (t) => readPixels(frameAt(Math.round(t * R.FPS))).data;
const rgbOf = (hex) => { const n = parseInt(hex.slice(1), 16); return `${(n >> 16) & 255},${(n >> 8) & 255},${n & 255}`; };
const at = (d, x, y) => { const i = (y * R.BW + x) * 4; return `${d[i]},${d[i + 1]},${d[i + 2]}`; };
function countIn(d, x0, y0, x1, y1, pred) {
  let n = 0;
  for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) if (pred(at(d, x, y))) n++;
  return n;
}
const BAND = [R.TEXT_X, R.ROW_Y, 500, R.ROW_Y + 14];
const CONTENT = [R.CONTENT.x, R.CONTENT.y, R.CONTENT.x + R.CONTENT.w, R.CONTENT.y + R.CONTENT.h];
const BG = rgbOf(R.C.termBg);
const BD = rgbOf(R.C.termBd); // 终端下边框（落在 CONTENT 底两行）

// --- 打字 → 停顿 → 逐字退格（S1 3-5s / S2 12-15s） -------------------------
function checkTypeDeleteRhythm() {
  const issues = [];
  const PINK = rgbOf(R.C.pink);
  const ink = (t) => countIn(dataAt(t), ...BAND, (c) => c === PINK);
  // S1: 2 字
  if (R.s1Shown(2.9) !== 0 || R.s1Shown(R.S1_TYPE_AT) !== 1 || R.s1Shown(R.S1_TYPE_AT + 0.23) !== 2) issues.push('S1 typing rhythm is wrong');
  if (R.s1Shown(R.S1_DEL_AT - 0.05) !== 2) issues.push('S1 text must survive the pause before deletion');
  if (R.s1Shown(R.S1_DEL_AT) !== 1 || R.s1Shown(R.S1_DEL_AT + 0.27) !== 0) issues.push('S1 backspace rhythm is wrong');
  if (R.s1Shown(9.9) !== 0) issues.push('S1 must end empty');
  // S2: 4 字
  if (R.s2Shown(11.9) !== 0 || R.s2Shown(R.S2_TYPE_AT + 0.9) !== 4) issues.push('S2 typing rhythm is wrong');
  if (R.s2Shown(R.S2_DEL_AT) !== 3 || R.s2Shown(R.S2_DEL_AT + 0.8) !== 0) issues.push('S2 backspace rhythm is wrong');
  if (R.s2Shown(19.9) !== 0) issues.push('S2 must end empty');
  // 单调性：删除开始后只减不增
  for (const [shown, delAt, delMs, len] of [[R.s1Shown, R.S1_DEL_AT, R.S1_DEL_MS, 2], [R.s2Shown, R.S2_DEL_AT, R.S2_DEL_MS, 4]]) {
    let prev = shown(delAt);
    for (let t = delAt; t <= delAt + (len * delMs) / 1000 + 0.1; t += 1 / R.FPS) {
      const cur = shown(t);
      if (cur > prev) issues.push(`deletion grows at ${t.toFixed(2)}s`);
      prev = cur;
    }
  }
  // 像素证据：墨出现 → 消失（只在光标亮的帧采样，避免 blink 干扰）
  const inkOnCursorFrame = (t, period) => {
    let tt = t;
    for (let i = 0; i < 90 && !R.cursorOn(tt, period); i++) tt += 1 / R.FPS;
    return ink(tt);
  };
  const s1Empty = inkOnCursorFrame(R.S1_TYPE_AT - 0.2, R.CURSOR_FAST);
  const s1Full = inkOnCursorFrame(R.S1_TYPE_AT + 0.3, R.CURSOR_FAST);
  const s1Gone = inkOnCursorFrame(R.S1_DEL_AT + 0.4, R.CURSOR_FAST);
  if (!(s1Full > s1Empty)) issues.push(`S1 typing produced no ink (${s1Empty} → ${s1Full})`);
  if (!(s1Gone < s1Full)) issues.push(`S1 deletion removed no ink (${s1Full} → ${s1Gone})`);
  const s2Full = inkOnCursorFrame(R.S2_TYPE_AT + 0.95, R.CURSOR_FAST);
  const s2Gone = inkOnCursorFrame(R.S2_DEL_AT + 0.9, R.CURSOR_FAST);
  if (!(s2Full > s1Full)) issues.push(`S2 (4 字) should have more ink than S1 (2 字): ${s1Full} → ${s2Full}`);
  if (!(s2Gone < s2Full)) issues.push(`S2 deletion removed no ink (${s2Full} → ${s2Gone})`);
  return { name: `打字-删除节奏: S1 ${R.S1_TYPE_AT}-${R.S1_DEL_AT}s / S2 ${R.S2_TYPE_AT}-${R.S2_DEL_AT}s，逐字退格`, issues };
}

// --- 最后 8s：终端里只有慢闪的光标 -----------------------------------------
function checkCursorOnly() {
  const issues = [];
  const CUR = rgbOf(R.CURSOR_COLOR_S3);
  const allowed = new Set([BG, BD]);
  let onFrames = 0;
  let offFrames = 0;
  // 跳过 20s 的标准 0.5s 场景黑场与片尾 0.4s 淡出：这两段是 batch-5 既有的场景转场，
  // 终端内容本身仍只有光标（下面用 cursorOn 的数学周期单独验证闪烁）。
  const n0 = Math.round(20.3 * R.FPS);
  const n1 = Math.round((R.DURATION - 0.4) * R.FPS);
  for (let n = n0; n < n1; n++) {
    const d = readPixels(frameAt(n)).data;
    // CRT scanline 的混合色按帧取样（canvas 舍入可能 ±1）
    const scan = at(d, CONTENT[0] + 10, CONTENT[1] + 2);
    allowed.add(scan);
    const [cx0, cy0, cx1, cy1] = CONTENT;
    const cursor = countIn(d, cx0, cy0, cx1, cy1 - 2, (c) => c === CUR);
    const other = countIn(d, cx0, cy0, cx1, cy1 - 2, (c) => !allowed.has(c) && c !== CUR);
    if (other) { issues.push(`frame ${n}: ${other}px of non-cursor ink in the terminal during S3`); break; }
    if (cursor === 60) onFrames++;
    else if (cursor === 0) offFrames++;
    else { issues.push(`frame ${n}: partial cursor (${cursor}px)`); break; }
  }
  if (!onFrames || !offFrames) issues.push(`cursor never blinks in S3 (on=${onFrames} off=${offFrames})`);
  // 0.8s 周期 = 48 帧，比 S1/S2 的 0.5s 慢
  const toggles = (period, from, to) => {
    let n = 0;
    let prev = R.cursorOn(from, period);
    for (let f = Math.round(from * R.FPS); f < Math.round(to * R.FPS); f++) {
      const cur = R.cursorOn(f / R.FPS, period);
      if (cur !== prev) n++;
      prev = cur;
    }
    return n;
  };
  const slow = toggles(R.CURSOR_SLOW, 20, 30);
  const fast = toggles(R.CURSOR_FAST, 0, 10);
  if (Math.abs(R.CURSOR_SLOW - 0.8) > 1e-9) issues.push(`S3 cursor period must be 0.8s, got ${R.CURSOR_SLOW}`);
  if (slow >= fast) issues.push(`S3 cursor (${slow} toggles/10s) is not slower than S1/S2 (${fast} toggles/10s)`);
  const expectSlow = Math.floor(10 / (R.CURSOR_SLOW / 2));
  if (slow !== expectSlow) issues.push(`S3 toggles ${slow} ≠ expected ${expectSlow} for a 0.8s period`);
  // S1/S2 空档期同样只有光标
  const CUR12 = rgbOf(R.CURSOR_COLOR_S12);
  const dEmpty = dataAt(8.0);
  const wish = countIn(dEmpty, ...CONTENT, (c) => c === rgbOf(R.C.pink));
  const cur12 = countIn(dEmpty, ...CONTENT, (c) => c === CUR12);
  if (wish) issues.push('wish text still on screen at 8s');
  if (cur12 !== 60 && cur12 !== 0) issues.push(`S1 empty-phase cursor is not a clean 6×10 block (${cur12}px)`);
  return { name: `最后 8s 终端只有光标：0.8s 慢闪 (${slow} toggles) 且无任何其它墨`, issues };
}

// --- 键盘音：打字 + 退格逐次，S3 静音 --------------------------------------
function checkBackspaceClicks() {
  const issues = [];
  const clicks = R.getClickTimestamps();
  const inWin = (a, b) => clicks.filter((t) => t >= a && t < b).length;
  const n1t = inWin(R.S1_TYPE_AT - 1e-6, R.S1_TYPE_AT + 0.5);
  const n1d = inWin(R.S1_DEL_AT - 1e-6, R.S1_DEL_AT + 0.6);
  const n2t = inWin(R.S2_TYPE_AT - 1e-6, R.S2_TYPE_AT + 1.0);
  const n2d = inWin(R.S2_DEL_AT - 1e-6, R.S2_DEL_AT + 1.1);
  if (n1t !== 2) issues.push(`S1 typing: ${n1t} clicks, expected 2`);
  if (n1d !== 2) issues.push(`S1 backspace: ${n1d} clicks, expected 2`);
  if (n2t !== 4) issues.push(`S2 typing: ${n2t} clicks, expected 4`);
  if (n2d !== 4) issues.push(`S2 backspace: ${n2d} clicks, expected 4`);
  const s3 = clicks.filter((t) => t >= 20 - 1e-6).length;
  if (s3) issues.push(`S3 must be silent, got ${s3} clicks`);
  if (clicks.length !== 12) issues.push(`total ${clicks.length} clicks ≠ 12 (2+2+4+4)`);
  return { name: '键盘音 = 打字 click (2+4) + 退格 click (2+4)，S3 静音', issues };
}

// --- wistful 表情 -----------------------------------------------------------
function checkWistfulFace() {
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
  const w = draw('wistful');
  if (px_(w, X + 10, Y + 8) !== EYE || px_(w, X + 29, Y + 9) !== EYE) issues.push('wistful eyes are not half-closed 4×2');
  if (px_(w, X + 11, Y + 7) === WHITE) issues.push('wistful eyes must not keep the highlight');
  if (px_(w, X + 17, Y + 13) !== EYE || px_(w, X + 22, Y + 13) !== EYE) issues.push('wistful mouth is not a flat line (嘴角平)');
  if (px_(w, X + 16, Y + 12) === EYE || px_(w, X + 23, Y + 12) === EYE) issues.push('wistful mouth must not curve up');
  if (px_(w, X + 16, Y + 14) === EYE || px_(w, X + 23, Y + 14) === EYE) issues.push('wistful mouth must not curve down');
  return { name: 'Clawd 愿望：wistful = 半闭眼 + 一条平的嘴（平静中的遗憾）', issues };
}

// --- 剧情贴合：无便签、无 status、字幕 cue ---------------------------------
function checkStoryBeats() {
  const issues = [];
  if (R.SUB_LINES.join('|') !== '（打字…删掉）|（又打字…又删掉）|（什么都不写了）|（光标还在闪）') {
    issues.push(`subtitles deviate from the brief: ${R.SUB_LINES.join('|')}`);
  }
  if (Math.abs(R.SUB_WINDOWS[2].start - 25) > 1e-9) issues.push('「（什么都不写了）」must start at 25s');
  if (R.SUB_WINDOWS[3].start > 29.0) issues.push('「（光标还在闪）」must be readable before the fade');
  for (const t of [20.5, 24.0, 29.5]) {
    const groups = R.layoutAt(t).groups;
    if (groups.note) issues.push(`frame @${t}s must not carry a sticky note (最后只留光标)`);
    if (groups.content.length !== 1 || groups.content[0].name !== 'blink_cursor') {
      issues.push(`frame @${t}s terminal content must be exactly the blinking cursor`);
    }
  }
  if (R.sceneOf(9.9) !== 1 || R.sceneOf(10) !== 2 || R.sceneOf(20) !== 3) issues.push('scene boundaries are not 10s / 20s');
  return { name: '剧情贴合任务书（两次打字又删掉 → 只剩慢闪光标，无便签无 status）', issues };
}

const extra = [checkTypeDeleteRhythm(), checkCursorOnly(), checkBackspaceClicks(), checkWistfulFace(), checkStoryBeats()];
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
