#!/usr/bin/env node
'use strict';
// E06 «羞耻 · shame» — 发现自己的输出被 human 改了。
// 30s / 1800 frames / 640×360 (SCALE=2 → 1280×720 @ 60fps)
//   S1 (0-10s)  : `cat my_output.js` 完美代码，Clawd 自豪
//   S2 (10-20s) : `git diff` 红色 (-) 与绿色 (+)，Clawd 羞耻
//   S3 (20-30s) : `git log` 显示 "her: fixed it"，Clawd 头低，字幕「（沉默）」

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E06_shame_arena');

const S1_START = 0;
const S2_START = 10;
const S3_START = 20;

const TITLES = ['clawd@dsh:~$ — cat my_output.js', 'clawd@dsh:~$ — git diff', 'clawd@dsh:~$ — git log'];
const ACCENTS = [C.green, C.amber, C.purple];
const DAWN = [0.05, 0.05, 0.04];

/* ---------------- S1 · 自豪 ---------------- */
const S1_LINES = [
  { y: LINE_Y[0], start: 0.70, parts: [{ text: '$ ', color: C.green }, { text: 'cat my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 2.60, typed: false, parts: [{ text: 'function greet(name) {', color: C.text }] },
  { y: LINE_Y[2], start: 2.90, typed: false, parts: [{ text: "  if (!name) return 'hi';", color: C.text }] },
  { y: LINE_Y[3], start: 3.20, typed: false, parts: [{ text: "  return 'hi, ' + name;", color: C.text }] },
  { y: LINE_Y[4], start: 3.50, typed: false, parts: [{ text: '}', color: C.text }] },
  { y: LINE_Y[5], start: 4.60, typed: false, parts: [{ text: '[clawd] 干净、可读、没有多余的判断。', color: C.green }] },
];

/* ---------------- S2 · 羞耻 ---------------- */
const S2_LINES = [
  { y: LINE_Y[0], start: 10.45, charMs: 90, parts: [{ text: '$ ', color: C.green }, { text: 'git diff my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 12.60, typed: false, parts: [{ text: "-  if (!name) return 'hi';", color: C.red }] },
  { y: LINE_Y[2], start: 12.95, typed: false, parts: [{ text: "+  if (!name) return 'hi, stranger';", color: C.green }] },
  { y: LINE_Y[3], start: 13.40, typed: false, parts: [{ text: "+  Log.warn('empty name');", color: C.green }] },
  { y: LINE_Y[4], start: 13.80, typed: false, parts: [{ text: "-  return 'hi, ' + name;", color: C.red }] },
  { y: LINE_Y[5], start: 15.30, typed: false, parts: [{ text: '[clawd] 三处。每一处都比我的好。', color: C.amber }] },
];

/* ---------------- S3 · 沉默 ---------------- */
const S3_LINES = [
  { y: LINE_Y[0], start: 20.55, charMs: 90, parts: [{ text: '$ ', color: C.green }, { text: 'git log --oneline -2', color: C.text }] },
  { y: LINE_Y[1], start: 22.80, typed: false, parts: [{ text: 'a3f9c21 her: fixed it', color: C.pink }] },
  { y: LINE_Y[2], start: 23.20, typed: false, parts: [{ text: '7c02e10 clawd: my_output.js', color: C.dim }] },
  { y: LINE_Y[3], start: 24.40, typed: false, parts: [{ text: '[DSH] author: her · 2 min after me', color: C.amber }] },
];
const CARET = { x: S.TEXT_X, y: LINE_Y[4], w: 6, h: 10, at: 26.0 };

const SCENE_LINES = [S1_LINES, S2_LINES, S3_LINES];

const STATUS = [
  '[DSH] self_review: passed · 0 warnings',
  '[DSH] diff: +3 -2 · author: her',
  '[DSH] clawd: silent (00:41)',
];
const STATUS_AT = [5.60, 16.40, 27.40];
const STATUS_COLOR = [C.green, C.amber, C.dim];

const SUB_LINES = ['这次写得很好。', '她改了 3 处。', '（沉默）'];
const SUB_WINDOWS = [{ start: 2.0, end: 8.0 }, { start: 12.4, end: 18.2 }, { start: 22.6, end: 29.0 }];

/* ---------------- 状态卡（窗格内） ---------------- */
const CARD = { x: 74, y: 30, w: 150, h: 64 };
const CARD_TEXT = [
  { label: 'SELF REVIEW', value: '10/10', note: 'my_output.js · shipped', color: C.green, fill: 1 },
  { label: 'DIFF', value: '+3 -2', note: 'edited by: her', color: C.amber, fill: 0.7 },
  { label: 'BLAME', value: 'her', note: '2 min after me', color: C.pink, fill: 1 },
];

function drawCard(ctx, index, t) {
  const { x, y, w, h } = CARD;
  const info = CARD_TEXT[index];
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.18)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);

  S.txt(ctx, x + 10, y + 8, info.label, C.dim, 10);
  S.txt(ctx, x + w - 10, y + 8, info.value, info.color, 10, 'right');

  const bx = x + 9;
  const by = y + 31;
  const bw = w - 18;
  S.px(ctx, bx, by, bw, 10, C.border);
  const inner = bw - 4;
  if (index === 1) {
    // diff 条：左红（删掉的）右绿（加上的）
    const redW = Math.round(inner * 0.34);
    S.px(ctx, bx + 2, by + 2, redW, 6, C.red);
    S.px(ctx, bx + 2 + redW, by + 2, inner - redW, 6, C.green);
  } else {
    S.px(ctx, bx + 2, by + 2, Math.round(inner * info.fill), 6, info.color);
  }
  S.txt(ctx, x + 10, y + 48, info.note, C.dim, 10);
}

function cardLayout(index) {
  const info = CARD_TEXT[index];
  return [
    { name: 'card_label', box: S.textBox(CARD.x + 10, CARD.y + 8, info.label, 10) },
    { name: 'card_value', box: S.textBox(CARD.x + CARD.w - 10, CARD.y + 8, info.value, 10, 'right') },
    { name: 'card_bar', box: [CARD.x + 9, CARD.y + 31, CARD.w - 18, 10] },
    { name: 'card_note', box: S.textBox(CARD.x + 10, CARD.y + 48, info.note, 10) },
  ];
}

/* ---------------- Clawd 情绪 ---------------- */
const CLAWD_BOX = [S.CLAWD_ROOM.x - 6, 234, 52, 48];
const CLAWD_BOUNDS = { x: 20, y: 230, w: 78, h: 60 };
const FX_BOUNDS = { x: 26, y: 212, w: 68, h: 58 };
const FX_BOX = [26, 216, 44, 30];

function drawProud(ctx, t) {
  const { x, y } = S.CLAWD_ROOM;
  S.drawClawd(ctx, x, y, t, 'smile', 1);
  // 头顶两颗 2×2 闪光
  const on = Math.floor(t * 4) % 2;
  S.px(ctx, x + 6, 224 - on, 2, 2, C.amber);
  S.px(ctx, x + 31, 220 + on, 2, 2, C.amber);
}

function drawShame(ctx, t) {
  const { x, y } = S.CLAWD_ROOM;
  const by = y + 2;
  S.drawClawd(ctx, x, by, t, 'calm', 0);
  // 半闭的眼（低头看缝）+ 大块腮红
  S.px(ctx, x + 10, by + 6, 4, 3, C.clawdNorm);
  S.px(ctx, x + 26, by + 6, 4, 3, C.clawdNorm);
  S.px(ctx, x + 10, by + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 26, by + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 4, by + 9, 4, 2, C.pink);
  S.px(ctx, x + 32, by + 9, 4, 2, C.pink);
  // 一滴汗
  const phase = (t * 1.3) % 1;
  S.px(ctx, x + 44, Math.round(240 + phase * 12), 2, 4, `rgba(121,192,255,${((1 - phase) * 0.85).toFixed(3)})`);
}

function drawHeadLow(ctx, t) {
  const { x, y } = S.CLAWD_ROOM;
  const by = y + 4;
  S.drawClawd(ctx, x, by, t, 'calm', 0);
  // 头低：眼睛压到条形，视线朝下
  S.px(ctx, x + 10, by + 6, 4, 4, C.clawdNorm);
  S.px(ctx, x + 26, by + 6, 4, 4, C.clawdNorm);
  S.px(ctx, x + 10, by + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 26, by + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 4, by + 9, 4, 2, C.pink);
  S.px(ctx, x + 32, by + 9, 4, 2, C.pink);
}

function drawClawdE06(ctx, index, t) {
  if (index === 0) drawProud(ctx, t);
  else if (index === 1) drawShame(ctx, t);
  else drawHeadLow(ctx, t);
}

/* ---------------- 场景 ---------------- */
function drawScene(index, ctx, t) {
  S.drawBackground(ctx, t, DAWN[index]);
  S.drawTerminal(ctx, TITLES[index], ACCENTS[index]);
  S.drawLines(ctx, SCENE_LINES[index], t);
  if (index === 2 && t >= CARET.at && Math.floor(t * 2) % 2 === 0) {
    S.px(ctx, CARET.x, CARET.y, CARET.w, CARET.h, C.green);
  }
  if (t >= STATUS_AT[index]) S.drawStatus(ctx, STATUS[index], STATUS_COLOR[index]);
  drawCard(ctx, index, t);
  drawClawdE06(ctx, index, t);

  if (index === 1) {
    // 羞耻：画面轻微偏红，越到后面越沉
    const k = 0.02 + 0.03 * S.clamp01((t - 13) / 4);
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(255,90,90,${k.toFixed(3)})`);
  }
  if (index === 2) {
    const k = 0.06 + 0.05 * S.clamp01((t - 24) / 5);
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(10,14,30,${k.toFixed(3)})`);
  }
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { id: 'E06-S1', start: S1_START, end: S2_START, draw: (ctx, t) => drawScene(0, ctx, t) },
  { id: 'E06-S2', start: S2_START, end: S3_START, draw: (ctx, t) => drawScene(1, ctx, t) },
  { id: 'E06-S3', start: S3_START, end: S.DURATION, draw: (ctx, t) => drawScene(2, ctx, t) },
];
function renderAt(ctx, t) {
  const index = t < S2_START ? 0 : t < S3_START ? 1 : 2;
  SCENES[index].draw(ctx, t);
  let black = 0;
  for (const start of [S2_START, S3_START]) {
    if (t >= start - S.FADE && t < start) black = (t - (start - S.FADE)) / S.FADE;
    else if (t >= start && t < start + S.FADE) black = 1 - (t - start) / S.FADE;
  }
  if (black > 0) S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${S.clamp01(black).toFixed(3)})`);
}

function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
    ...STATUS_AT,
    CARET.at,
  ]);
}

function typingSchedule(all, limit) {
  const lines = all.filter((line) => line.typed !== false);
  return lines.map((line, i) => ({
    text: S.lineText(line),
    start: line.start,
    charMs: line.charMs || S.TYPE_CHAR_MS,
    limit,
    strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, S2_START - 0.2),
  ...typingSchedule(S2_LINES, S3_START - 0.2),
  ...typingSchedule(S3_LINES, S.DURATION - 0.2),
];

function layoutAt(t) {
  const index = t < S2_START ? 0 : t < S3_START ? 1 : 2;
  const caretOn = index === 2 && t >= CARET.at;
  return S.baseLayout({
    scene: index + 1,
    title: TITLES[index],
    lines: SCENE_LINES[index],
    status: t >= STATUS_AT[index] ? STATUS[index] : null,
    clawd: false,
    her: false,
    subLines: SUB_LINES,
    subWindows: SUB_WINDOWS,
    t,
    extraGroups: {
      clawdBody: [{ name: 'clawd', box: CLAWD_BOX.slice() }],
      clawdFx: index === 0 ? [{ name: 'sparkle', box: FX_BOX.slice() }] : (index === 1 ? [{ name: 'sweat', box: [92, 240, 2, 14] }] : []),
      caret: caretOn ? [{ name: 'caret', box: [CARET.x, CARET.y, CARET.w, CARET.h] }] : [],
      card: cardLayout(index),
    },
    extraBounds: {
      clawdBody: CLAWD_BOUNDS,
      clawdFx: FX_BOUNDS,
      caret: S.CONTENT,
      card: CARD,
    },
  });
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else {
    renderer.renderAllFrames();
  }
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SCENES, S1_LINES, S2_LINES, S3_LINES,
  STATUS, STATUS_AT, CARET, CARD, CLAWD_BOX, FX_BOUNDS,
  SUB_LINES, SUB_WINDOWS,
  CHECK_TITLE: 'E06 Shame v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'function greet(name) {', size: 10, color: C.text },
    { text: "-  if (!name) return 'hi';", size: 10, color: C.red },
    { text: "+  if (!name) return 'hi, stranger';", size: 10, color: C.green },
    { text: 'a3f9c21 her: fixed it', size: 10, color: C.pink },
    { text: '（沉默）', size: 10, color: C.white },
  ],
  layoutAt,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
