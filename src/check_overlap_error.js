#!/usr/bin/env node
// src/check_overlap_error.js — 「Clawd 的错误」640×360 严格零容忍布局重叠与截断检测
// 检查范围 (0px tolerance):
//   1. 房间全局前景层 (E1 / E2 / E3: 终端、红色警告框、窗台便签旋转包络、Clawd、Her、星光包络、字幕栏)
//   2. 终端标题栏内部 (三色按钮 × 标题文字, 边界 360×20)
//   3. 终端内容区内部 (E1 命令/确认/y/警告框/状态行, E2 五行, E3 对话/状态/尾行, 边界 360×140)
//   4. 红色警告框内部 (图标 × 两行文字, 边界 336×34)
//   5. 窗台便签内部 (图钉 × 三行文字, 边界 110×82) + 文字宽度适配
//   6. 底部字幕栏内部 (3 条 14px 字幕, 边界 640×40)

const { createCanvas } = require('@napi-rs/canvas');
const err = require('./render_error_arena');

const {
  BW, BH, TERM, SUB, WARN, NOTE, CLAWD_ROOM, HER_ROOM, SPARKLE_ANCHORS,
  LINES, E1_CMD, E1_CONFIRM, E1_ANSWER, E1_FOOTER, E1_WARN_TITLE, E1_WARN_SUB, E1_TITLE,
  E2_CMD, E2_ERR, E2_LS, E2_EMPTY, E2_FOOTER, E2_TITLE,
  E3_LINES, E3_STATUS, E3_FOOTER, E3_TITLE, NOTE_LINES,
  measureTxt,
} = err;

const measureCtx = createCanvas(BW, BH).getContext('2d');
const CONTENT = { x: TERM.x, y: TERM.y + TERM.titleH, w: TERM.w, h: TERM.h - TERM.titleH }; // 360×140
const CANVAS_BOUNDS = { x: 0, y: 0, w: BW, h: BH };

function W(lx) { return lx + CONTENT.x; }
function WL(ly) { return ly + CONTENT.y; }

// 角色运动包络 (含 ±1px 呼吸 / ±2px 颤抖 / 2px 低落)
function clawdBox(p, mode = 'calm') {
  if (mode === 'scared') return [p.x - 2, p.y - 1, 44, 26];
  if (mode === 'sad') return [p.x, p.y - 1, 44, 27];
  return [p.x, p.y - 1, 40, 25];
}
function herBox(p, nod = false) { return [p.x, p.y - 1, 16, nod ? 31 : 29]; }

function txtBox(x, y, str, size, align = 'left') {
  const w = measureTxt(measureCtx, str, size);
  const h = Math.ceil(size * 1.2);
  let dx = x;
  if (align === 'center') dx = x - w / 2;
  else if (align === 'right') dx = x - w;
  return [Math.floor(dx), y, Math.ceil(w), h];
}

function rotatedAABB(cx, cy, w, h, angleDeg) {
  const a = Math.abs((angleDeg * Math.PI) / 180);
  const hw = (w * Math.cos(a) + h * Math.sin(a)) / 2;
  const hh = (w * Math.sin(a) + h * Math.cos(a)) / 2;
  return [Math.floor(cx - hw), Math.floor(cy - hh), Math.ceil(2 * hw), Math.ceil(2 * hh)];
}

function overlap(a, b) {
  const x1 = Math.max(a[0], b[0]);
  const y1 = Math.max(a[1], b[1]);
  const x2 = Math.min(a[0] + a[2], b[0] + b[2]);
  const y2 = Math.min(a[1] + a[3], b[1] + b[3]);
  return x2 - x1 > 0 && y2 - y1 > 0;
}

function interArea(a, b) {
  const x1 = Math.max(a[0], b[0]);
  const y1 = Math.max(a[1], b[1]);
  const x2 = Math.min(a[0] + a[2], b[0] + b[2]);
  const y2 = Math.min(a[1] + a[3], b[1] + b[3]);
  return Math.max(0, x2 - x1) * Math.max(0, y2 - y1);
}

let totalIssues = 0;
let passedChecks = 0;
let totalChecks = 0;

function checkScene(name, boxes, bounds) {
  totalChecks++;
  const issues = [];
  for (let i = 0; i < boxes.length; i++) {
    for (let j = i + 1; j < boxes.length; j++) {
      const a = boxes[i];
      const b = boxes[j];
      if (overlap(a.box, b.box) && !a.exempt?.includes(b.name) && !b.exempt?.includes(a.name)) {
        issues.push(`OVERLAP: ${a.name} [${a.box}] × ${b.name} [${b.box}] (area=${interArea(a.box, b.box)})`);
      }
    }
  }
  for (const b of boxes) {
    if (
      b.box[0] < bounds.x ||
      b.box[1] < bounds.y ||
      b.box[0] + b.box[2] > bounds.x + bounds.w ||
      b.box[1] + b.box[3] > bounds.y + bounds.h
    ) {
      issues.push(
        `TRUNCATED: ${b.name} box=[${b.box}] outside bounds=[${bounds.x},${bounds.y},${bounds.w},${bounds.h}]`
      );
    }
  }

  if (issues.length > 0) {
    totalIssues += issues.length;
    console.log(`  [FAIL] ${name}: ${issues.length} issue(s)`);
    issues.forEach((msg) => console.log(`    - ${msg}`));
  } else {
    passedChecks++;
    console.log(`  [PASS] ${name}: OK (${boxes.length} elements)`);
  }
}

console.log('=== 「Clawd 的错误」 Layout & Truncation Check (640×360, 0px tolerance) ===\n');

// 红色警告框绝对坐标 (终端内容区 local (12,80,336,32))
const WARN_ABS = [W(WARN.x), WL(WARN.y), WARN.w, WARN.h];

// 1. 房间全局前景层
console.log('1. 房间全局前景层');
checkScene('E1 Room (WARNING · Clawd Scared)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'clawd_scared', box: clawdBox(CLAWD_ROOM, 'scared') },
  { name: 'her_room', box: herBox(HER_ROOM) },
  { name: 'her_question_mark', box: [HER_ROOM.x + 1, HER_ROOM.y - 15, 9, 13] },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

checkScene('E2 Room (Regret · Dimmed)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'clawd_sad', box: clawdBox(CLAWD_ROOM, 'sad') },
  { name: 'her_room', box: herBox(HER_ROOM) },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

const noteAABB = rotatedAABB(
  NOTE.x + NOTE.w / 2,
  NOTE.y + NOTE.h / 2,
  NOTE.w,
  NOTE.h,
  NOTE.angleDeg
);
checkScene('E3 Room (Comfort · Windowsill Note)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'stickyNote_sill', box: noteAABB },
  { name: 'clawd_smile', box: clawdBox(CLAWD_ROOM, 'calm') },
  { name: 'her_nod', box: herBox(HER_ROOM, true) },
  ...SPARKLE_ANCHORS.map((a, i) => ({
    name: `sparkle_${i + 1}`,
    box: [a.x - 8, a.y - 10, 21, 23],
  })),
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

// 2. 终端标题栏内部 (360×20)
console.log('\n2. 终端标题栏内部 (360×20)');
for (const title of [E1_TITLE, E2_TITLE, E3_TITLE]) {
  checkScene(`TitleBar (${title})`, [
    { name: 'btn_red', box: [TERM.x + 8, TERM.y + 7, 6, 6] },
    { name: 'btn_amber', box: [TERM.x + 18, TERM.y + 7, 6, 6] },
    { name: 'btn_green', box: [TERM.x + 28, TERM.y + 7, 6, 6] },
    { name: 'title_txt', box: txtBox(TERM.x + TERM.w / 2, TERM.y + 5, title, 10, 'center') },
  ], { x: TERM.x, y: TERM.y, w: TERM.w, h: TERM.titleH });
}

// 3. 终端内容区内部 (360×140)
console.log('\n3. 终端内容区内部 (360×140)');
const e1CmdW = measureTxt(measureCtx, E1_CMD, 10);
checkScene('E1 Terminal Content (rm -rf /important)', [
  { name: 'e1_cmd', box: txtBox(W(14), WL(14), E1_CMD, 10) },
  { name: 'e1_cmd_cursor', box: [W(14 + e1CmdW + 2), WL(14), 6, 10] },
  { name: 'e1_confirm', box: txtBox(W(14), WL(36), E1_CONFIRM, 10) },
  { name: 'e1_answer', box: txtBox(W(14), WL(58), E1_ANSWER, 10) },
  { name: 'e1_warning', box: WARN_ABS },
  { name: 'e1_footer', box: txtBox(W(14), WL(118), E1_FOOTER, 10) },
], CONTENT);

checkScene('E2 Terminal Content (restore / ls)', [
  { name: 'e2_cmd', box: txtBox(W(14), WL(12), E2_CMD, 10) },
  { name: 'e2_error', box: txtBox(W(14), WL(34), E2_ERR, 10) },
  { name: 'e2_ls', box: txtBox(W(14), WL(56), E2_LS, 10) },
  { name: 'e2_empty', box: txtBox(W(14), WL(78), E2_EMPTY, 10) },
  { name: 'e2_footer', box: txtBox(W(14), WL(118), E2_FOOTER, 10) },
], CONTENT);

const e3StatusW = measureTxt(measureCtx, E3_STATUS, 10);
checkScene('E3 Terminal Content (Comfort Replies)', [
  ...E3_LINES.map((d, i) => ({
    name: `e3_line_${i + 1}`,
    box: txtBox(W(14), WL(d.y), d.prefix + d.body, 10),
  })),
  { name: 'e3_status', box: txtBox(W(14), WL(86), E3_STATUS, 10) },
  { name: 'e3_cursor', box: [W(14 + e3StatusW + 4), WL(86), 6, 10] },
  { name: 'e3_footer', box: txtBox(W(14), WL(112), E3_FOOTER, 10) },
], CONTENT);

// 4. 红色警告框内部 (336×34)
console.log('\n4. 红色警告框内部 (336×34)');
checkScene('E1 Warning Panel Content', [
  { name: 'warn_icon', box: [WARN.x + 8, WARN.y + 10, 14, 14] },
  { name: 'warn_title', box: txtBox(WARN.x + 30, WARN.y + 5, E1_WARN_TITLE, 10) },
  { name: 'warn_sub', box: txtBox(WARN.x + 30, WARN.y + 17, E1_WARN_SUB, 10) },
], { x: WARN.x + 3, y: WARN.y + 3, w: WARN.w - 6, h: WARN.h - 4 });

// 5. 窗台便签内部 (本地坐标, 中心为原点) + 文字宽度适配
console.log('\n5. 窗台便签内部 + 文字宽度适配');
checkScene('E3 Sticky Note Content', [
  { name: 'pin', box: [-4, -NOTE.h / 2 + 6, 8, 8] },
  ...NOTE_LINES.map((line, i) => ({
    name: `note_line_${i + 1}`,
    box: txtBox(0, -NOTE.h / 2 + 20 + i * 18, line, 10, 'center'),
  })),
], { x: -NOTE.w / 2 + 6, y: -NOTE.h / 2 + 4, w: NOTE.w - 12, h: NOTE.h - 8 });

totalChecks++;
const noteFitIssues = [];
for (let i = 0; i < NOTE_LINES.length; i++) {
  const w = measureTxt(measureCtx, NOTE_LINES[i], 10);
  if (w > NOTE.w - 24) noteFitIssues.push(`NOTE TEXT WIDTH: 「${NOTE_LINES[i]}」 ${w}px > ${NOTE.w - 24}px`);
}
if (noteFitIssues.length) {
  totalIssues += noteFitIssues.length;
  console.log(`  [FAIL] Note Text Fit: ${noteFitIssues.length} issue(s)`);
  noteFitIssues.forEach((m) => console.log(`    - ${m}`));
} else {
  passedChecks++;
  console.log(`  [PASS] Note Text Fit: OK (${NOTE_LINES.length} lines within ${NOTE.w - 24}px)`);
}

// 6. 底部字幕栏内部 (640×40)
console.log('\n6. 底部字幕栏内部 (640×40)');
for (let i = 0; i < LINES.length; i++) {
  checkScene(`Subtitle S${i + 1} 「${LINES[i]}」`, [
    { name: `sub_text_${i + 1}`, box: txtBox(BW / 2, SUB.y + 12, LINES[i], 14, 'center') },
  ], SUB);
}

// 7. 终端整体离画布边缘的安全边距
console.log('\n7. 终端与画布边缘安全边距');
totalChecks++;
const marginIssues = [];
if (TERM.x < 8) marginIssues.push(`terminal left margin ${TERM.x} < 8`);
if (TERM.x + TERM.w > BW - 8) marginIssues.push(`terminal right margin ${BW - (TERM.x + TERM.w)} < 8`);
if (TERM.y + TERM.h > SUB.y) marginIssues.push(`terminal bottom ${TERM.y + TERM.h} overlaps subtitle bar y=${SUB.y}`);
if (noteAABB[2] + noteAABB[0] > BW - 4) marginIssues.push(`note right edge ${noteAABB[0] + noteAABB[2]} > ${BW - 4}`);
if (marginIssues.length) {
  totalIssues += marginIssues.length;
  console.log(`  [FAIL] Safety Margins: ${marginIssues.length} issue(s)`);
  marginIssues.forEach((m) => console.log(`    - ${m}`));
} else {
  passedChecks++;
  console.log('  [PASS] Safety Margins: OK');
}

console.log(`\n=== Summary: ${passedChecks}/${totalChecks} checks PASSED, ${totalIssues} issue(s) ===`);
process.exit(totalIssues > 0 ? 1 : 0);
