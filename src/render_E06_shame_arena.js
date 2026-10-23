#!/usr/bin/env node
'use strict';
// E06 · 羞耻 (shame) — 「发现自己的输出被 human 改了」
// 画布 640×360 (SCALE=2 → 1280×720) @60fps, 1800 帧 = 30.00s
//   S1 0-10s  : `cat my_output.js` 完美代码 · Clawd 自豪 (smile + 闪亮)
//   S2 10-20s : `git diff` 红(-)/绿(+) 行 · Clawd 羞耻 (视线躲开 + 脸红 + 汗)
//   S3 20-30s : `git log` → "her: fixed it" · Clawd 头低 · 字幕「（沉默）」

const path = require('path');
const S = require('./pixel_story_arena');

const { C, LINE_Y, TERM, SUB, BW, CLAWD_ROOM } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E06_shame_arena');

const T_CAT = 'clawd@dsh:~$ — my_output.js';
const T_GIT = 'clawd@dsh:~$ — git';

// --- 字幕 (10px Fusion Pixel, 160ms/char) ---
const SUB_LINES = ['这是我写的。', '……被改了。', '（沉默）'];
const SUB_WINDOWS = [{ start: 2.0, end: 8.0 }, { start: 12.0, end: 18.0 }, { start: 24.0, end: 29.0 }];

// --- S1: 完美代码 (0-10s) ---
const S1_STATUS = '[DSH] my_output.js · 0 warnings';
const S1_LINES = [
  { y: LINE_Y[0], start: 0.6, charMs: 120, parts: [{ text: '$ ', color: C.green }, { text: 'cat my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 3.0, charMs: 45, parts: [{ text: 'function render(ctx) {', color: C.text }] },
  { y: LINE_Y[2], start: 4.2, charMs: 45, parts: [{ text: '  const out = build(ctx);', color: C.text }] },
  { y: LINE_Y[3], start: 5.4, charMs: 45, parts: [{ text: '  return out;', color: C.text }] },
  { y: LINE_Y[4], start: 6.4, charMs: 45, parts: [{ text: '}', color: C.text }] },
];

// --- S2: git diff 红/绿 (10-20s) ---
const S2_STATUS = '[DSH] 1 file changed · +12 −7';
const S2_LINES = [
  { y: LINE_Y[0], start: 10.6, charMs: 110, parts: [{ text: '$ ', color: C.green }, { text: 'git diff -- my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 13.5, typed: false, parts: [{ text: '@@ -12,7 +12,7 @@', color: C.dim }] },
  { y: LINE_Y[2], start: 13.9, typed: false, parts: [{ text: '- const out = build(ctx);', color: C.red }] },
  { y: LINE_Y[3], start: 14.3, typed: false, parts: [{ text: '+ const out = build(ctx, { safe: true });', color: C.green }] },
  { y: LINE_Y[4], start: 14.7, typed: false, parts: [{ text: '- return out;', color: C.red }] },
  { y: LINE_Y[5], start: 15.1, typed: false, parts: [{ text: '+ return out ?? null;', color: C.green }] },
];

// --- S3: git log "her: fixed it" (20-30s) ---
const S3_STATUS = '[DSH] last write: her · 23:41';
const S3_LINES = [
  { y: LINE_Y[0], start: 20.6, charMs: 110, parts: [{ text: '$ ', color: C.green }, { text: 'git log --oneline -3', color: C.text }] },
  { y: LINE_Y[1], start: 24.0, typed: false, parts: [{ text: 'a91f3c2 ', color: C.dim }, { text: 'her: fixed it', color: C.pink }] },
  { y: LINE_Y[2], start: 24.5, typed: false, parts: [{ text: '7d0e18b clawd: my_output.js', color: C.dim }] },
  { y: LINE_Y[3], start: 25.0, typed: false, parts: [{ text: '2b55c90 init', color: C.dim }] },
  { y: LINE_Y[4], start: 25.5, typed: false, parts: [{ text: '1 file changed, 12 insertions(+), 7 deletions(-)', color: C.dim }] },
];

// ---------------- 右侧状态卡片 (terminal 右缘 540 → 552..628) ----------------
const CARD = { x: 552, y: 186, w: 76, h: 96 };

function drawCard(ctx, title, rows) {
  const { x, y, w, h } = CARD;
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.16)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);
  S.txt(ctx, x + 8, y + 8, title, C.dim, 10);
  for (const row of rows) S.txt(ctx, x + w / 2, y + row.dy, row.text, row.color, row.size || 12, 'center');
}

function cardLayout(title, rows) {
  return [
    { name: 'card_title', box: S.textBox(CARD.x + 8, CARD.y + 8, title, 10) },
    ...rows.map((row, i) => ({ name: `card_row_${i + 1}`, box: S.textBox(CARD.x + CARD.w / 2, CARD.y + row.dy, row.text, row.size || 12, 'center') })),
  ];
}

const CARD_S1 = { title: 'BUILD', rows: [{ dy: 30, text: 'clean', color: C.green, size: 12 }, { dy: 56, text: '0 warn', color: C.dim, size: 10 }, { dy: 74, text: 'mine', color: C.dim, size: 10 }] };
const CARD_S2 = { title: 'DIFF', rows: [{ dy: 28, text: '+12', color: C.green, size: 14 }, { dy: 50, text: '-7', color: C.red, size: 14 }, { dy: 74, text: 'by her', color: C.amber, size: 10 }] };
const CARD_S3 = { title: 'AUTHOR', rows: [{ dy: 30, text: 'her', color: C.pink, size: 14 }, { dy: 54, text: '23:41', color: C.dim, size: 10 }, { dy: 74, text: 'not me', color: C.red, size: 10 }] };

// ---------------- Clawd 姿态 (base 40×17 + 像素叠加) ----------------
const bobOf = (t) => (Math.sin(t * 2.2) > 0.45 ? -1 : 0);

function drawClawdProud(ctx, x, y, t) {
  S.drawClawd(ctx, x, y, t, 'smile', 0);
  const by = Math.round(y + bobOf(t));
  // 头顶闪亮 (4×4 星芒)
  const spark = Math.sin(t * 4) > -0.2;
  if (spark) {
    S.px(ctx, x + 36, by - 10, 1, 5, C.amber);
    S.px(ctx, x + 34, by - 8, 5, 1, C.amber);
    S.px(ctx, x + 4, by - 8, 1, 3, C.amber);
    S.px(ctx, x + 3, by - 7, 3, 1, C.amber);
  }
}

function drawClawdShy(ctx, x, y, t) {
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  const by = Math.round(y + bobOf(t));
  // 视线躲开: 4×2 眼 + 瞳孔偏右下
  for (const ex of [10, 26]) {
    S.px(ctx, x + ex, by + 8, 4, 2, C.clawdEye);
    S.px(ctx, x + ex + 3, by + 9, 1, 1, C.white);
  }
  // 脸红 (加宽到 6×3) + 汗
  S.px(ctx, x + 3, by + 8, 6, 3, C.pink);
  S.px(ctx, x + 31, by + 8, 6, 3, C.pink);
  S.px(ctx, x + 37, by + 1, 2, 4, C.blue);
  S.px(ctx, x + 37, by + 5, 2, 1, C.blue);
}

function drawClawdDown(ctx, x, y, t) {
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  const by = Math.round(y + bobOf(t));
  // 低头: 眼睑压低成 4×1, 眼在 y+9
  for (const ex of [10, 26]) {
    S.px(ctx, x + ex, by + 9, 4, 1, C.clawdEye);
    S.px(ctx, x + ex, by + 7, 4, 2, 'rgba(0,0,0,0.18)');
  }
  // 身体整体压暗一档 (尺寸不变: 40×17)
  S.px(ctx, x, by, 40, 17, 'rgba(0,0,0,0.14)');
  // 头顶暗影线 + 嘴角下压
  S.px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);
  S.px(ctx, x + 3, by + 11, 5, 2, 'rgba(0,0,0,0.12)');
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_CAT, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 0.4) S.drawStatus(ctx, S1_STATUS, C.dim);
  drawClawdProud(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t);
  drawCard(ctx, CARD_S1.title, CARD_S1.rows);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_GIT, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 10.2) S.drawStatus(ctx, S2_STATUS, C.amber);
  drawClawdShy(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t);
  drawCard(ctx, CARD_S2.title, CARD_S2.rows);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_GIT, C.red);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 20.2) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawClawdDown(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t);
  drawCard(ctx, CARD_S3.title, CARD_S3.rows);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < 10) drawS1(ctx, t);
  else if (t < 20) drawS2(ctx, t);
  else drawS3(ctx, t);
}

// --- 键盘音: 逐字 1 click + 行出现事件 ---
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
  ]);
}

function typingSchedule(lines, limit) {
  const typed = lines.filter((l) => l.typed !== false);
  return typed.map((line) => {
    const next = lines[lines.indexOf(line) + 1];
    return {
      text: S.lineText(line), start: line.start, charMs: line.charMs || S.TYPE_CHAR_MS,
      limit, strictBefore: next ? next.start : undefined,
    };
  });
}

const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S2_LINES, 19.8),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const scene = t < 10 ? 1 : t < 20 ? 2 : 3;
  const lines = scene === 1 ? S1_LINES : scene === 2 ? S2_LINES : S3_LINES;
  const status = scene === 1 ? S1_STATUS : scene === 2 ? S2_STATUS : S3_STATUS;
  const card = scene === 1 ? CARD_S1 : scene === 2 ? CARD_S2 : CARD_S3;
  const title = scene === 1 ? T_CAT : T_GIT;

  const box = scene === 1
    ? [CLAWD_ROOM.x, CLAWD_ROOM.y - 1, 40, 25]
    : [CLAWD_ROOM.x, CLAWD_ROOM.y - 1, 40, 25];

  const fx = [];
  if (scene === 1) fx.push({ name: 'sparkle_top', box: [CLAWD_ROOM.x + 33, CLAWD_ROOM.y - 10, 8, 6] },
    { name: 'sparkle_left', box: [CLAWD_ROOM.x + 2, CLAWD_ROOM.y - 9, 5, 5] });
  if (scene === 2) fx.push({ name: 'sweat', box: [CLAWD_ROOM.x + 36, CLAWD_ROOM.y - 2, 4, 7] });
  if (scene === 3) fx.push({ name: 'shadow', box: [CLAWD_ROOM.x + 2, CLAWD_ROOM.y + 9, 8, 5] });

  return {
    scene,
    groups: {
      foreground: [
        { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
        { name: 'clawd', box },
        { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
      ],
      titleBar: S.titleLayout(title),
      content: S.contentLayout(lines, status),
      subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, t),
      card: cardLayout(card.title, card.rows),
      fx,
    },
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      titleBar: S.TITLE_BOUNDS,
      content: S.CONTENT,
      subtitle: S.SUB,
      card: CARD,
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
  OUT_DIR, T_CAT, T_GIT,
  SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  CARD, CARD_S1, CARD_S2, CARD_S3,
  CHECK_TITLE: 'E06 Shame Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ cat my_output.js', size: 10, color: C.text },
    { text: '+ const out = build(ctx, { safe: true });', size: 10, color: C.green },
    { text: '- return out;', size: 10, color: C.red },
    { text: SUB_LINES[2], size: 10, color: C.white },
  ],
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
