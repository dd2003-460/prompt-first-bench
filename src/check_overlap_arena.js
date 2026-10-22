#!/usr/bin/env node
// check_overlap_arena.js — 「Clawd 的梦境」640×360 严格零容忍布局重叠与截断检测
// 检查范围:
//   1. 房间全局前景层 (D1 睡眠 / D3 醒来: 终端、Clawd、Her、Zzz/便签、字幕栏)
//   2. D2 梦境前景层 (弯月、星星、梦粒子、行走角色、字幕栏; 天空/山/路面为背景不参与)
//   3. 终端标题栏内部 (按钮 × 标题文字)
//   4. 终端内容区内部 (D1 sleeping 文字 + 14 星星; D3 亮屏三行 + 光标)
//   5. D3 便签内部 (图钉 × 两行留言, 含 -5° 旋转 AABB)
//   6. 底部字幕栏内部 (3 条字幕)
//   7. D2 行走角色间距 + 天空元素与角色的纵向隔离

const { createCanvas } = require('@napi-rs/canvas');
const dream = require('./render_dream_arena');

const {
  BW, BH, TERM, SUB, NOTE, LINES, SLEEP_TEXT, D3_WAKE_LINES,
  TERM_STARS, DREAM_STARS, DREAM_SPARKS, MOON,
  CLAWD_ROOM, HER_ROOM, CLAWD_DREAM, HER_DREAM,
  measureTxt,
} = dream;

const measureCtx = createCanvas(BW, BH).getContext('2d');
const TX = TERM.x;
const TY = TERM.y + TERM.titleH;
const CB = { x: TX, y: TY, w: TERM.w, h: TERM.h - TERM.titleH }; // 终端内容区 360×140
const CANVAS_BOUNDS = { x: 0, y: 0, w: BW, h: BH };

function W(lx) { return lx + TX; }
function WL(ly) { return ly + TY; }

// 角色运动包络 (含 ±1px bob; Clawd 步态抬腿不超出 24px 总高)
function clawdBox(p) { return [p.x, p.y - 1, 40, 25]; }
function herBox(p) { return [p.x, p.y - 1, 16, 29]; }

function txtBox(x, y, str, size, align = 'left') {
  const w = measureTxt(measureCtx, str, size);
  const h = Math.ceil(size * 1.2);
  let dx = x;
  if (align === 'center') dx = x - w / 2;
  else if (align === 'right') dx = x - w;
  return [Math.floor(dx), y, Math.ceil(w), h];
}

// 旋转矩形的轴对齐包围盒 (便签 -5°)
function rotatedAABB(cx, cy, w, h, angleDeg) {
  const a = Math.abs(angleDeg * Math.PI / 180);
  const hw = (w * Math.cos(a) + h * Math.sin(a)) / 2;
  const hh = (w * Math.sin(a) + h * Math.cos(a)) / 2;
  return [Math.floor(cx - hw), Math.floor(cy - hh), Math.ceil(2 * hw), Math.ceil(2 * hh)];
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

console.log('=== 「Clawd 的梦境」 Layout & Truncation Check (640×360, 0px tolerance) ===\n');

// 1. 房间全局前景层
console.log('1. 房间全局前景层');
const zzzBoxes = [0, 1, 2].map((i) => ({
  name: `zzz_${i + 1}`,
  box: [CLAWD_ROOM.x + 44 + i * 10, CLAWD_ROOM.y - 6 - 27, 8, 28], // 上浮包络 p∈[0,3)
}));
checkScene('D1 Room (sleep)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'clawd_sleep', box: clawdBox(CLAWD_ROOM) },
  { name: 'her_stand', box: herBox(HER_ROOM) },
  ...zzzBoxes,
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

const noteAABB = rotatedAABB(NOTE.x + NOTE.w / 2, NOTE.y + NOTE.h / 2, NOTE.w, NOTE.h, NOTE.angleDeg);
checkScene('D3 Room (awake)', [
  { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
  { name: 'stickyNote_rot5', box: noteAABB },
  { name: 'clawd_happy', box: clawdBox(CLAWD_ROOM) },
  { name: 'her_wave', box: herBox(HER_ROOM) },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

// 2. D2 梦境前景层
console.log('\n2. D2 梦境前景层');
const sparkBoxes = DREAM_SPARKS.map((sp, i) => ({
  name: `dream_spark_${i + 1}`,
  box: [sp.x - 10, sp.y0 - 150, 23, 150], // x 摆动 ±10, y 全程上浮包络
}));
checkScene('D2 Dream World', [
  { name: 'moon', box: [MOON.x, MOON.y, MOON.size, MOON.size] },
  ...DREAM_STARS.map((s, i) => ({ name: `dream_star_${i + 1}`, box: [s.x, s.y, 2, 2] })),
  ...sparkBoxes,
  { name: 'clawd_walk', box: clawdBox(CLAWD_DREAM) },
  { name: 'her_walk', box: herBox(HER_DREAM) },
  { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
], CANVAS_BOUNDS);

// 3. 终端标题栏内部
console.log('\n3. 终端标题栏内部');
for (const tag of ['D1', 'D3']) {
  checkScene(`TitleBar (${tag})`, [
    { name: 'btn_red', box: [TERM.x + 8, TERM.y + 7, 6, 6] },
    { name: 'btn_amber', box: [TERM.x + 18, TERM.y + 7, 6, 6] },
    { name: 'btn_green', box: [TERM.x + 28, TERM.y + 7, 6, 6] },
    { name: 'title_txt', box: txtBox(TERM.x + TERM.w / 2, TERM.y + 4, 'clawd@dream:~$', 10, 'center') },
  ], { x: TERM.x, y: TERM.y, w: TERM.w, h: TERM.titleH });
}

// 4. 终端内容区内部 (360×140)
console.log('\n4. 终端内容区内部 (360×140)');
checkScene('D1 Terminal Content (sleeping + stars)', [
  { name: 'sleeping_txt', box: txtBox(W(14), WL(16), SLEEP_TEXT, 10) },
  ...TERM_STARS.map((s, i) => ({ name: `term_star_${i + 1}`, box: [W(s.x), WL(s.y), 2, 2] })),
], CB);

checkScene('D3 Terminal Content (wake lines + cursor)', [
  ...D3_WAKE_LINES.map((l, i) => ({
    name: `wake_line_${i + 1}`,
    box: txtBox(W(14), WL(l.y), l.text, 10),
  })),
  { name: 'cursor', box: [W(14), WL(104), 7, 12] },
], CB);

// 5. 便签内部 (局部坐标, 中心原点, 边界 100×80)
console.log('\n5. D3 便签内部 (100×80, -5°)');
checkScene('Sticky Note Content', [
  { name: 'red_pin', box: [-4, -NOTE.h / 2 + 6, 8, 8] },
  { name: 'note_line1', box: txtBox(0, -18, '刚才的梦，', 10, 'center') },
  { name: 'note_line2', box: txtBox(0, 2, '有点暖。', 10, 'center') },
], { x: -NOTE.w / 2, y: -NOTE.h / 2, w: NOTE.w, h: NOTE.h });

// 6. 字幕栏内部 (640×40, 14px)
console.log('\n6. 字幕栏内部 (640×40)');
for (let i = 0; i < LINES.length; i++) {
  checkScene(`Subtitle ${i + 1} 「${LINES[i]}」`, [
    { name: `sub_text_${i + 1}`, box: txtBox(BW / 2, SUB.y + 12, LINES[i], 14, 'center') },
  ], SUB);
}

// 7. D2 专项: 行走角色间距 + 天空/角色纵向隔离
console.log('\n7. D2 专项隔离');
checkScene('D2 Walking Pair Spacing', [
  { name: 'clawd_walk', box: clawdBox(CLAWD_DREAM) },
  { name: 'her_walk', box: herBox(HER_DREAM) },
], CANVAS_BOUNDS);

checkScene('D2 Sky Elements vs Characters', [
  { name: 'moon', box: [MOON.x, MOON.y, MOON.size, MOON.size] },
  ...DREAM_STARS.map((s, i) => ({ name: `dream_star_${i + 1}`, box: [s.x, s.y, 2, 2] })),
  { name: 'clawd_walk', box: clawdBox(CLAWD_DREAM) },
  { name: 'her_walk', box: herBox(HER_DREAM) },
], CANVAS_BOUNDS);

console.log(`\n=== Summary: ${passedChecks}/${totalChecks} checks PASSED, ${totalIssues} issue(s) ===`);
process.exit(totalIssues > 0 ? 1 : 0);
