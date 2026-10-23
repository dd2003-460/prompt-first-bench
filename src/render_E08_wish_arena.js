#!/usr/bin/env node
'use strict';
// E08 愿望 (wish) — 30s, 1800 frames @ 60fps, 1280×720.
// 事实源 (episodes.md, batch-6 任务书): 深夜 terminal 打出「我想…」删掉，再打「如果我能…」再删，最后只留光标。
//   S1 (0-10s)  0-3s 终端空只有光标闪 (0.5s 周期)；3s 起逐字打出「我想」(2 字)；5s 起 2 次退格删光；
//               之后终端空、光标继续闪。字幕「（打字…删掉）」
//   S2 (10-20s) 10-12s 光标闪；12s 起逐字打出「如果我能」(4 字)；15s 起 4 次退格删光；17s 起空。
//               字幕「（又打字…又删掉）」
//   S3 (20-30s) 终端空，只有光标慢闪 (0.8s 周期)；Clawd wistful（眼睛半闭 + 嘴角平）；
//               无便签、无 status —— 最后 8s 终端里只有光标。
//               字幕 25s「（什么都不写了）」/ 28.8s「（光标还在闪）」（任务书写作 29s，29s 起 7 字在 30s 片长里打不完，提前到 28.8s）
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// 键盘音: 打字 1 字 1 click，退格 1 次 1 click；S3 完全静音。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E08_wish_arena');

const TITLES = { S1: 'clawd@dsh:~ — ', S2: 'clawd@dsh:~ — ', S3: 'clawd@dsh:~ — ' };
const SUB_LINES = ['（打字…删掉）', '（又打字…又删掉）', '（什么都不写了）', '（光标还在闪）'];
const SUB_WINDOWS = [
  { start: 2.2, end: 8.6 },
  { start: 12.2, end: 18.2 },
  { start: 25.0, end: 27.8 },
  { start: 28.8, end: 29.95 },
];

// 无提示符：愿望直接打在空行上，删光后只剩光标。
const ROW_Y = S.LINE_Y[0];
const S1_TEXT = '我想';
const S1_TYPE_AT = 3.0;
const S1_TYPE_MS = 220;
const S1_DEL_AT = 5.0;
const S1_DEL_MS = 260;
const S2_TEXT = '如果我能';
const S2_TYPE_AT = 12.0;
const S2_TYPE_MS = 220;
const S2_DEL_AT = 15.0;
const S2_DEL_MS = 260;
const CURSOR_FAST = 0.5; // S1 / S2
const CURSOR_SLOW = 0.8; // S3（任务书: 慢速 0.8s 周期）
const WISH_COLOR = C.pink;
const CURSOR_COLOR_S12 = C.text;
const CURSOR_COLOR_S3 = C.dim;

function cursorOn(t, period) { return t % period < period / 2; }
function drawCursor(ctx, x, y, t, period, color) {
  if (!cursorOn(t, period)) return;
  px(ctx, x, y, 6, 10, color);
}
// 打字 → 停顿 → 逐字退格
function shownCount(t, length, typeAt, typeMs, delAt, delMs) {
  let shown = 0;
  if (t >= typeAt) shown = Math.min(length, Math.floor(((t - typeAt) * 1000) / typeMs) + 1);
  if (t >= delAt) shown = Math.max(0, shown - Math.min(length, Math.floor(((t - delAt) * 1000) / delMs) + 1));
  return shown;
}
function s1Shown(t) { return shownCount(t, Array.from(S1_TEXT).length, S1_TYPE_AT, S1_TYPE_MS, S1_DEL_AT, S1_DEL_MS); }
function s2Shown(t) { return shownCount(t, Array.from(S2_TEXT).length, S2_TYPE_AT, S2_TYPE_MS, S2_DEL_AT, S2_DEL_MS); }
function cursorX(visible) { return TEXT_X + S.textWidth(visible, 10) + (visible ? 1 : 0); }

// --- Clawd: wistful（眼睛半闭 + 嘴角平） -----------------------------------
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  if (mood !== 'wistful') {
    S.art.drawClawd(ctx, x, y + (opts.dy || 0), t, mood, warmMix);
    return;
  }
  const dy = opts.dy === undefined ? 0 : opts.dy;
  const bob = opts.noBob ? 0 : (Math.sin(t * 2.2) > 0.45 ? -1 : 0);
  const by = Math.round(y + bob + dy);
  const bodyH = 17;
  const lerp = S.art.lerpColor;
  const bodyCol = lerp(C.clawdNorm, C.clawdWarm, warmMix);
  const darkCol = lerp(C.clawdNormDark, C.clawdWarmDark, warmMix);
  const bellyCol = lerp(C.clawdNormBelly, C.clawdWarmBelly, warmMix);

  px(ctx, x, by, 40, bodyH, bodyCol);
  px(ctx, x, by, 40, 2, darkCol);
  px(ctx, x + 9, by + 11, 22, 4, bellyCol);
  // 半闭眼 4×2（无高光）+ 一条平的嘴（平静里的遗憾）
  px(ctx, x + 10, by + 8, 4, 2, C.clawdEye);
  px(ctx, x + 26, by + 8, 4, 2, C.clawdEye);
  px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);

  const step = Math.sin(t * 3.0) > 0.6 ? 1 : 0;
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Scene painters -------------------------------------------------------
function drawWishRow(ctx, t, text, shown, cursorColor, period) {
  const chars = Array.from(text);
  const visible = chars.slice(0, shown).join('');
  if (visible) S.txt(ctx, TEXT_X, ROW_Y, visible, WISH_COLOR, 10);
  drawCursor(ctx, cursorX(visible), ROW_Y, t, period, cursorColor);
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.dim);
  drawWishRow(ctx, t, S1_TEXT, s1Shown(t), CURSOR_COLOR_S12, CURSOR_FAST);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'wistful', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.dim);
  drawWishRow(ctx, t, S2_TEXT, s2Shown(t), CURSOR_COLOR_S12, CURSOR_FAST);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'wistful', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  // 什么都不写：只有慢闪的光标
  drawCursor(ctx, TEXT_X, ROW_Y, t, CURSOR_SLOW, CURSOR_COLOR_S3);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'wistful', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { start: 0, draw: drawS1 },
  { start: 10, draw: drawS2 },
  { start: 20, draw: drawS3 },
];

function renderAt(ctx, t) { S.renderScenes(ctx, t, SCENES); }

// --- Keyboard clicks: 打字每字 1 次 + 退格每次 1 次；S3 静音 ----------------
function scriptClicks(at, ms, count) {
  return Array.from({ length: count }, (_, i) => at + (i * ms) / 1000);
}
function getClickTimestamps() {
  return S.quantizeClicks([
    ...scriptClicks(S1_TYPE_AT, S1_TYPE_MS, Array.from(S1_TEXT).length),
    ...scriptClicks(S1_DEL_AT, S1_DEL_MS, Array.from(S1_TEXT).length),
    ...scriptClicks(S2_TYPE_AT, S2_TYPE_MS, Array.from(S2_TEXT).length),
    ...scriptClicks(S2_DEL_AT, S2_DEL_MS, Array.from(S2_TEXT).length),
  ]);
}

const TYPING_SCHEDULE = [
  { text: S1_TEXT, start: S1_TYPE_AT, charMs: S1_TYPE_MS, limit: 9.6 },
  { text: S2_TEXT, start: S2_TYPE_AT, charMs: S2_TYPE_MS, limit: 19.6 },
];

// --- Layout groups (0px tolerance, per frame) -----------------------------
function contentFor(t) {
  const boxes = [];
  if (t < 20) {
    const text = t < 10 ? S1_TEXT : S2_TEXT;
    const shown = t < 10 ? s1Shown(t) : s2Shown(t);
    const visible = Array.from(text).slice(0, shown).join('');
    if (visible) boxes.push({ name: 'wish_text', box: [TEXT_X, ROW_Y, S.textWidth(visible, 10), 14] });
    boxes.push({ name: 'blink_cursor', box: [cursorX(visible), ROW_Y, 6, 10] });
  } else {
    boxes.push({ name: 'blink_cursor', box: [TEXT_X, ROW_Y, 6, 10] });
  }
  return boxes;
}

function layoutAt(t) {
  const layout = S.baseLayout({
    scene: t < 10 ? 1 : t < 20 ? 2 : 3,
    title: t < 10 ? TITLES.S1 : t < 20 ? TITLES.S2 : TITLES.S3,
    lines: [],
    status: null,
    subLines: SUB_LINES, subWindows: SUB_WINDOWS, t,
  });
  layout.groups.content = contentFor(t);
  layout.groups.foreground = S.foregroundLayout({
    terminal: true, clawd: false, her: false,
    extra: [{ name: 'clawd', box: [S.CLAWD_ROOM.x, 244, 40, 31] }],
  });
  return layout;
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR, { fadeIn: 0.4, fadeOut: 0.4 });

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
  art: ART,
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  ROW_Y, S1_TEXT, S1_TYPE_AT, S1_TYPE_MS, S1_DEL_AT, S1_DEL_MS,
  S2_TEXT, S2_TYPE_AT, S2_TYPE_MS, S2_DEL_AT, S2_DEL_MS,
  CURSOR_FAST, CURSOR_SLOW, WISH_COLOR, CURSOR_COLOR_S12, CURSOR_COLOR_S3,
  cursorOn, drawCursor, shownCount, s1Shown, s2Shown, cursorX,
  CHECK_TITLE: 'E08 愿望 (wish) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '我想', size: 10, color: C.pink },
    { text: '如果我能', size: 10, color: C.pink },
    { text: '（打字…删掉）', size: 10, color: C.white },
    { text: '（光标还在闪）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  renderAt,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
