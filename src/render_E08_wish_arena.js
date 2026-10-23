#!/usr/bin/env node
'use strict';
// E08 · 愿望 (wish) — 「深夜打字又删掉，只剩光标」
// 画布 640×360 (SCALE=2 → 1280×720) @60fps, 1800 帧 = 30.00s
//   S1 0-10s  : prompt 打出「我想」→ 逐字删掉
//   S2 10-20s : 打出「如果我能」→ 逐字删掉
//   S3 20-30s : 只剩光标闪烁 · 字幕「（什么都不写了）」
// 键盘音: 每个打字字符 / 每次 backspace 删除各 1 次 click

const path = require('path');
const S = require('./pixel_story_arena');

const { C, LINE_Y, TERM, SUB, CLAWD_ROOM } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E08_wish_arena');
const T_TITLE = 'clawd@dsh:~$ — new_message.txt';

// --- 字幕 ---
const SUB_LINES = ['深夜，想写点什么。', '写了，又删了。', '（什么都不写了）'];
const SUB_WINDOWS = [{ start: 2.0, end: 8.5 }, { start: 12.0, end: 18.5 }, { start: 21.0, end: 29.0 }];

// ---- 起草 / 删除时间轴 (140ms/char, 删除同样 140ms/char) ----
const PROMPT = '$ ';
const TYPE_Y = LINE_Y[2];
const TYPE_SIZE = 14;
const CURSOR = { w: 8, h: 14 };
const HEAD_Y = LINE_Y[0];
const META_Y = LINE_Y[1];
const HINT_Y = LINE_Y[4];
const FOOT_Y = LINE_Y[5];

const DRAFT_1 = '我想';
const DRAFT_2 = '如果我能';
const TYPE_1_AT = 2.8;
const DEL_1_AT = 6.4;
const TYPE_2_AT = 12.4;
const DEL_2_AT = 17.4;
const CHAR_S = S.TYPE_CHAR_MS / 1000;

// 命令行现存的字符 (三场共用同一时间轴)
function draftState(t) {
  let text = '';
  let typing = false;
  let note = '';
  if (t >= TYPE_1_AT) {
    const d1 = Array.from(DRAFT_1);
    const n = Math.min(d1.length, Math.floor((t - TYPE_1_AT) / CHAR_S) + 1);
    text = d1.slice(0, n).join('');
    typing = t < TYPE_1_AT + d1.length * CHAR_S;
  }
  if (t >= DEL_1_AT) {
    const d1 = Array.from(DRAFT_1);
    const n = Math.min(d1.length, Math.floor((t - DEL_1_AT) / CHAR_S) + 1);
    text = d1.slice(0, Math.max(0, d1.length - n)).join('');
    typing = true;
    note = 'del';
  }
  if (t >= TYPE_2_AT) {
    const d2 = Array.from(DRAFT_2);
    const n = Math.min(d2.length, Math.floor((t - TYPE_2_AT) / CHAR_S) + 1);
    text = d2.slice(0, n).join('');
    typing = t < TYPE_2_AT + d2.length * CHAR_S;
    note = '';
  }
  if (t >= DEL_2_AT) {
    const d2 = Array.from(DRAFT_2);
    const n = Math.min(d2.length, Math.floor((t - DEL_2_AT) / CHAR_S) + 1);
    text = d2.slice(0, Math.max(0, d2.length - n)).join('');
    typing = true;
    note = 'del';
  }
  return { text, typing, note };
}

const blinkOn = (t) => Math.floor(t * 2.5) % 2 === 0;

function draftWidth(text) {
  return S.textWidth(PROMPT + text, TYPE_SIZE);
}

function drawCommandLine(ctx, t) {
  const st = draftState(t);
  S.txt(ctx, S.TEXT_X, TYPE_Y, PROMPT, C.green, TYPE_SIZE);
  if (st.text) S.txt(ctx, S.TEXT_X + S.textWidth(PROMPT, TYPE_SIZE), TYPE_Y, st.text, C.white, TYPE_SIZE);
  const cx = S.TEXT_X + draftWidth(st.text) + 3;
  const show = st.typing ? true : blinkOn(t);
  if (show) S.px(ctx, cx, TYPE_Y + 1, CURSOR.w, CURSOR.h, C.white);
  if (st.note === 'del') S.txt(ctx, S.TEXT_X, HINT_Y, '⌫ deleted', C.dim, 10);
}

// ---------------- 右侧时钟 / 草稿面板 (terminal 右缘 540 → 552..628) ----------------
const PANEL = { x: 552, y: 186, w: 76, h: 96 };

function drawPanel(ctx, t, left) {
  const { x, y, w, h } = PANEL;
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.16)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);
  S.txt(ctx, x + 8, y + 8, 'TIME', C.dim, 10);
  S.txt(ctx, x + w / 2, y + 24, '03:41', C.purple, 14, 'center');
  S.txt(ctx, x + 8, y + 48, 'UNSENT', C.dim, 10);
  S.txt(ctx, x + w / 2, y + 62, `${left}`, left ? C.amber : C.dim, 14, 'center');
  S.txt(ctx, x + 8, y + 82, 'she: asleep', C.dim, 10);
}

function panelLayout() {
  return [
    { name: 'panel_time_label', box: S.textBox(PANEL.x + 8, PANEL.y + 8, 'TIME', 10) },
    { name: 'panel_time', box: S.textBox(PANEL.x + PANEL.w / 2, PANEL.y + 24, '03:41', 14, 'center') },
    { name: 'panel_unsent_label', box: S.textBox(PANEL.x + 8, PANEL.y + 48, 'UNSENT', 10) },
    { name: 'panel_unsent', box: S.textBox(PANEL.x + PANEL.w / 2, PANEL.y + 62, '1', 14, 'center') },
    { name: 'panel_note', box: S.textBox(PANEL.x + 8, PANEL.y + 82, 'she: asleep', 10) },
  ];
}

function drawHeader(ctx) {
  S.txt(ctx, S.TEXT_X, HEAD_Y, '$ clawd@dsh:~$', C.green, 10);
  S.txt(ctx, S.TEXT_X, META_Y, 'draft: new_message.txt', C.dim, 10);
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_TITLE, C.purple);
  drawHeader(ctx);
  drawCommandLine(ctx, t);
  S.txt(ctx, S.TEXT_X, FOOT_Y, 'unsent · 0 message', C.dim, 10);
  S.drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, t < TYPE_1_AT ? 'calm' : 'thinking', 0);
  drawPanel(ctx, t, 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_TITLE, C.purple);
  drawHeader(ctx);
  drawCommandLine(ctx, t);
  S.txt(ctx, S.TEXT_X, FOOT_Y, 'unsent · 0 message', C.dim, 10);
  S.drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'thinking', 0);
  drawPanel(ctx, t, 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_TITLE, C.dim);
  drawHeader(ctx);
  // 只剩 prompt + 光标
  S.txt(ctx, S.TEXT_X, TYPE_Y, PROMPT, C.green, TYPE_SIZE);
  if (blinkOn(t)) S.px(ctx, S.TEXT_X + S.textWidth(PROMPT, TYPE_SIZE) + 3, TYPE_Y + 1, CURSOR.w, CURSOR.h, C.white);
  S.txt(ctx, S.TEXT_X, HINT_Y, 'draft cleared', C.dim, 10);
  S.txt(ctx, S.TEXT_X, FOOT_Y, 'unsent · 0 message', C.dim, 10);
  // Clawd 头低 (40×17 body 不变, 表情/眼睑叠加)
  S.drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'calm', 0);
  const by = Math.round(CLAWD_ROOM.y + (Math.sin(t * 2.2) > 0.45 ? -1 : 0));
  for (const ex of [10, 26]) {
    S.px(ctx, CLAWD_ROOM.x + ex, by + 10, 4, 1, C.clawdEye);
    S.px(ctx, CLAWD_ROOM.x + ex, by + 7, 4, 3, 'rgba(0,0,0,0.22)');
  }
  S.px(ctx, CLAWD_ROOM.x, by, 40, 17, 'rgba(0,0,0,0.18)');
  S.px(ctx, CLAWD_ROOM.x + 1, by, 38, 4, 'rgba(0,0,0,0.16)');
  S.px(ctx, CLAWD_ROOM.x + 17, by + 13, 6, 1, C.clawdEye);
  drawPanel(ctx, t, 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < 10) drawS1(ctx, t);
  else if (t < 20) drawS2(ctx, t);
  else drawS3(ctx, t);
}

// --- 键盘音: 每个打字 / 删除字符 1 click ---
function draftClicks() {
  const out = [];
  const d1 = Array.from(DRAFT_1);
  const d2 = Array.from(DRAFT_2);
  for (let i = 0; i < d1.length; i++) out.push(TYPE_1_AT + i * CHAR_S);
  for (let i = 0; i < d1.length; i++) out.push(DEL_1_AT + i * CHAR_S);
  for (let i = 0; i < d2.length; i++) out.push(TYPE_2_AT + i * CHAR_S);
  for (let i = 0; i < d2.length; i++) out.push(DEL_2_AT + i * CHAR_S);
  return out;
}

function getClickTimestamps() {
  return S.quantizeClicks(draftClicks());
}

// 打字 / 删除排期 (供 check_overlap 的串行校验)
const TYPING_SCHEDULE = [
  { text: DRAFT_1, start: TYPE_1_AT, limit: DEL_1_AT },
  { text: DRAFT_1, start: DEL_1_AT, limit: TYPE_2_AT },
  { text: DRAFT_2, start: TYPE_2_AT, limit: DEL_2_AT },
  { text: DRAFT_2, start: DEL_2_AT, limit: 19.8 },
];

function cursorBox(t) {
  const st = draftState(t);
  const cx = S.TEXT_X + draftWidth(st.text) + 3;
  return [cx, TYPE_Y + 1, CURSOR.w, CURSOR.h];
}

function layoutAt(t) {
  const scene = t < 10 ? 1 : t < 20 ? 2 : 3;
  const st = draftState(t);
  const content = [
    { name: 'row_1', box: S.textBox(S.TEXT_X, HEAD_Y, '$ clawd@dsh:~$', 10) },
    { name: 'row_2', box: S.textBox(S.TEXT_X, META_Y, 'draft: new_message.txt', 10) },
    { name: 'row_3', box: S.textBox(S.TEXT_X, TYPE_Y, PROMPT + st.text, TYPE_SIZE) },
    { name: 'cursor_3', box: cursorBox(t) },
  ];
  if (scene === 3) {
    content.push({ name: 'row_5', box: S.textBox(S.TEXT_X, HINT_Y, 'draft cleared', 10) });
    content.push({ name: 'row_6', box: S.textBox(S.TEXT_X, FOOT_Y, 'unsent · 0 message', 10) });
  } else {
    if (st.note === 'del') content.push({ name: 'row_5', box: S.textBox(S.TEXT_X, HINT_Y, '⌫ deleted', 10) });
    content.push({ name: 'row_6', box: S.textBox(S.TEXT_X, FOOT_Y, 'unsent · 0 message', 10) });
  }

  const fx = [];
  if (scene === 1) fx.push({ name: 'wish_glow_1', box: [CLAWD_ROOM.x + 41, CLAWD_ROOM.y - 6, 4, 21] });
  if (scene === 2) fx.push({ name: 'wish_glow_2', box: [CLAWD_ROOM.x + 41, CLAWD_ROOM.y - 6, 4, 21] });
  if (scene === 3) fx.push({ name: 'low_shadow', box: [CLAWD_ROOM.x + 2, CLAWD_ROOM.y + 9, 8, 5] });

  return {
    scene,
    groups: {
      foreground: [
        { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
        { name: 'clawd', box: [CLAWD_ROOM.x, CLAWD_ROOM.y - 1, 40, 25] },
        { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
      ],
      titleBar: S.titleLayout(T_TITLE),
      content,
      subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, t),
      panel: panelLayout(),
      fx,
    },
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      titleBar: S.TITLE_BOUNDS,
      content: S.CONTENT,
      subtitle: S.SUB,
      panel: PANEL,
      fx: S.CANVAS_BOUNDS,
    },
  };
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) console.log(JSON.stringify({ count: getClickTimestamps().length, clicks: getClickTimestamps() }));
  else renderer.renderAllFrames();
}

module.exports = {
  ...S,
  OUT_DIR, T_TITLE,
  SUB_LINES, SUB_WINDOWS,
  PROMPT, DRAFT_1, DRAFT_2, TYPE_SIZE, CURSOR,
  TYPE_1_AT, DEL_1_AT, TYPE_2_AT, DEL_2_AT,
  PANEL, draftState, cursorBox, draftClicks,
  CHECK_TITLE: 'E08 Wish Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ clawd@dsh:~$', size: 10, color: C.green },
    { text: 'draft: new_message.txt', size: 10, color: C.dim },
    { text: '如果我能', size: TYPE_SIZE, color: C.white },
    { text: SUB_LINES[2], size: 10, color: C.white },
  ],
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
