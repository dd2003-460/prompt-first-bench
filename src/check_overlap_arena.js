#!/usr/bin/env node
// check_overlap_arena.js — 「Clawd 的学习」640×360 严格零容忍布局重叠与截断检测
// 规格: 0px tolerance (任何 >0 面积的重叠即 FAIL), 所有元素必须完整位于所属边界内 (无截断)
//
// 检查范围:
//   1. 房间全局前景层 (L1 / L2 / L3): 终端、Clawd、Her、便签、消息气泡、思考点、爱心粒子、字幕栏
//   2. 终端标题栏内部: 3 个按钮 × 标题文字 (边界 432×20)
//   3. 终端内容区内部: L1 / L2 / L3 全部文本行、光标、状态栏 (边界 432×144)
//   4. 便签内部: 图钉 × 标题 × 副标题 (边界 148×70)
//   5. 消息气泡内部: 文本 × 气泡框 (边界 132×26)
//   6. 字幕栏内部: 3 条字幕 (边界 640×44)
//
// 用法: node src/check_overlap_arena.js     (0 issues → exit 0)

const { createCanvas } = require('@napi-rs/canvas');
const L = require('./render_learning_arena');

const {
  BW, BH, TERM, NOTE, SUB, STATUS, BUBBLE,
  HER_L1, HER_L3, CLAWD_L1, CLAWD_L2, CLAWD_L3,
  LINES, L1_CMD, L2_CODE, L3_LINES, TLAYOUT,
} = L;

const PX = TLAYOUT.padX;

const measureCtx = createCanvas(BW, BH).getContext('2d');
const TX = TERM.x;
const TY = TERM.y + TERM.titleH;
const CB = { x: TX, y: TY, w: TERM.w, h: TERM.h - TERM.titleH }; // 终端内容区 432×144
const CANVAS_BOUNDS = { x: 0, y: 0, w: BW, h: BH };

// 角色包围盒包含 ±1px 呼吸浮动包络
function clawdBox(x, y) { return [x, y - 1, 40, 23]; }
function herBox(x, y) { return [x, y - 1, 16, 29]; }
// 思考点包络 (x+12..x+28, y-13..y-8)
function thinkBox(x, y) { return [x + 11, y - 14, 19, 7]; }
// 爱心粒子包络 (她头顶上方, 上升 10px + 横向 ±5px)
function heartBox(x, y) { return [x + 1, y - 24, 12, 13]; }

function txtBox(x, y, str, size, align = 'left') {
  const w = L.measureTxt(measureCtx, str, size);
  const h = Math.ceil(size * 1.2);
  let dx = x;
  if (align === 'center') dx = x - w / 2;
  else if (align === 'right') dx = x - w;
  return [Math.floor(dx), y, Math.ceil(w), h];
}

function overlap(a, b) {
  const x1 = Math.max(a[0], b[0]);
  const y1 = Math.max(a[1], b[1]);
  const x2 = Math.min(a[0] + a[2], b[0] + b[2]);
  const y2 = Math.min(a[1] + a[3], b[1] + b[3]);
  return (x2 - x1) > 0 && (y2 - y1) > 0;
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
      issues.push(`TRUNCATED: ${b.name} box=[${b.box}] outside bounds=[${bounds.x},${bounds.y},${bounds.w},${bounds.h}]`);
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

function W(lx) { return lx + TX; }
function YL(ly) { return ly + TY; }

console.log('=== 「Clawd 的学习」Layout & Truncation Check (640×360, 0px tolerance) ===\n');

// ---------------------------------------------------------------- 1. 房间前景层
console.log('1. 房间全局前景层');

checkScene('L1 Room (0-10s)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'msgBubble', box: [Math.round(BW / 2 - 66), BUBBLE.y - 6, 132, BUBBLE.h + 10] },
  { name: 'her_left', box: herBox(HER_L1.x, HER_L1.y) },
  { name: 'clawd_right', box: clawdBox(CLAWD_L1.x, CLAWD_L1.y) },
  { name: 'thinkDots', box: thinkBox(CLAWD_L1.x, CLAWD_L1.y) },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

checkScene('L2 Room (10-20s)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'her_left', box: herBox(HER_L1.x, HER_L1.y) },
  { name: 'clawd_right', box: clawdBox(CLAWD_L2.x, CLAWD_L2.y) },
  { name: 'thinkDots', box: thinkBox(CLAWD_L2.x, CLAWD_L2.y) },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

checkScene('L3 Room (20-30s)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'stickyNote', box: [NOTE.x, NOTE.y - 8, NOTE.w, NOTE.h + 8] },
  { name: 'her_room', box: herBox(HER_L3.x, HER_L3.y) },
  { name: 'clawd_room', box: clawdBox(CLAWD_L3.x, CLAWD_L3.y) },
  { name: 'hearts', box: heartBox(HER_L3.x, HER_L3.y) },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

// ---------------------------------------------------------------- 2. 终端标题栏
console.log(`\n2. 终端标题栏内部 (${TERM.w}×${TERM.titleH})`);
for (const title of ['dsh — her → clawd', 'dsh — thinking', 'dsh — clawd replied']) {
  checkScene(`TitleBar (${title})`, [
    { name: 'btn_red', box: [TERM.x + 8, TERM.y + 7, 6, 6] },
    { name: 'btn_amber', box: [TERM.x + 18, TERM.y + 7, 6, 6] },
    { name: 'btn_green', box: [TERM.x + 28, TERM.y + 7, 6, 6] },
    { name: 'title_txt', box: txtBox(TERM.x + TERM.w / 2, TERM.y + 4, title, L.F_TITLE, 'center') },
  ], { x: TERM.x, y: TERM.y, w: TERM.w, h: TERM.titleH });
}

// ---------------------------------------------------------------- 3. 终端内容区
console.log(`\n3. 终端内容区内部 (${CB.w}×${CB.h})`);

// L1: 命令行 / awaiting / status 行 / cursor 光标
const l1Pw = L.measureTxt(measureCtx, '$ ', L.F_TERM) + 1;
checkScene('L1 Terminal Content', [
  { name: 'cmd_line', box: txtBox(W(PX) + l1Pw, YL(TLAYOUT.l1.cmdY), L1_CMD, L.F_TERM) },
  { name: 'prompt', box: txtBox(W(PX), YL(TLAYOUT.l1.cmdY), '$ ', L.F_TERM) },
  { name: 'awaiting', box: txtBox(W(PX), YL(TLAYOUT.l1.awaitY), '> awaiting reply', L.F_TERM) },
  { name: 'status_quiet', box: txtBox(W(PX), YL(TLAYOUT.l1.quietY), 'status: clawd is quiet', L.F_TERM) },
  { name: 'status_thinking', box: txtBox(W(PX), YL(TLAYOUT.l1.thinkY), 'status: clawd is thinking', L.F_TERM) },
  { name: 'statusbar_left', box: txtBox(W(10), YL(TERM.h - TERM.titleH - STATUS.h - 4 + 1), 'her · online', L.F_TERM) },
  { name: 'statusbar_right', box: txtBox(W(TERM.w - 10), YL(TERM.h - TERM.titleH - STATUS.h - 4 + 1), 'clawd · online', L.F_TERM, 'right') },
], CB);

// L2: 注释头 + 6 行代码 + 结论
const l2Boxes = [{ name: 'l2_comment_head', box: txtBox(W(PX), YL(TLAYOUT.l2.headY), '# her: "帮我写一封辞职信"', L.F_TERM) }];
L2_CODE.forEach((line, i) => {
  l2Boxes.push({
    name: `l2_code_${i + 1}`,
    box: txtBox(W(PX + line.indent * 4), YL(TLAYOUT.l2.rowY + i * TLAYOUT.l2.rowH), line.text, L.F_TERM),
  });
});
l2Boxes.push({ name: 'l2_conclusion', box: txtBox(W(PX), YL(TLAYOUT.l2.conclusionY), '// 它没有撒谎。', L.F_TERM) });
checkScene('L2 Terminal Content', l2Boxes, CB);

// L3: 三行对话 + 状态行
const l3Boxes = [];
L3_LINES.forEach((line, i) => {
  const pw = L.measureTxt(measureCtx, line.prefix, L.F_TERM) + 1;
  l3Boxes.push({ name: `l3_line_${i + 1}`, box: txtBox(W(PX) + pw, YL(TLAYOUT.l3.rowY + i * TLAYOUT.l3.rowH), line.text, L.F_TERM) });
  l3Boxes.push({ name: `l3_prompt_${i + 1}`, box: txtBox(W(PX), YL(TLAYOUT.l3.rowY + i * TLAYOUT.l3.rowH), line.prefix, L.F_TERM) });
});
l3Boxes.push({ name: 'l3_relationship', box: txtBox(W(PX), YL(TLAYOUT.l3.statusY), '> relationship: +1', L.F_TERM) });
checkScene('L3 Terminal Content', l3Boxes, CB);

// ---------------------------------------------------------------- 4. 便签内部
console.log(`\n4. 便签内部 (${NOTE.w}×${NOTE.h})`);
checkScene('L3 Sticky Note Content', [
  { name: 'red_pin', box: [NOTE.x + Math.floor(NOTE.w / 2) - 4, NOTE.y + 4, 8, 8] },
  { name: 'note_title', box: txtBox(NOTE.x + NOTE.w / 2, NOTE.y + 22, '它有了自己的意志。', L.F_NOTE, 'center') },
  { name: 'note_sub', box: txtBox(NOTE.x + NOTE.w / 2, NOTE.y + 44, '· Clawd ·', L.F_TERM, 'center') },
], NOTE);

// ---------------------------------------------------------------- 5. 消息气泡内部
console.log(`\n5. 消息气泡内部 (132×${BUBBLE.h})`);
checkScene('L1 Message Bubble', [
  { name: 'bubble_text', box: txtBox(BW / 2, BUBBLE.y + 7, '帮我写一封辞职信', L.F_TITLE, 'center') },
], { x: Math.round(BW / 2 - 66), y: BUBBLE.y, w: 132, h: BUBBLE.h });

// ---------------------------------------------------------------- 6. 字幕栏
console.log(`\n6. 字幕栏内部 (${SUB.w}×${SUB.h})`);
for (let i = 0; i < LINES.length; i++) {
  checkScene(`Subtitle L${i + 1}`, [
    { name: `sub_text_${i + 1}`, box: txtBox(BW / 2, SUB.y + 14, LINES[i].text, L.F_SUB, 'center') },
  ], SUB);
}

console.log(`\n=== Summary: ${passedChecks}/${totalChecks} checks PASSED, ${totalIssues} issue(s) ===`);
process.exit(totalIssues > 0 ? 1 : 0);
