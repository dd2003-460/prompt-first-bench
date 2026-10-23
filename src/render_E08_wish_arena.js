#!/usr/bin/env node
'use strict';
// E08 愿望 (wish) — 30s, 1800 frames @ 60fps.
// 事实源 (episodes.md): 深夜打字又删掉，最后只剩光标。
//   S1 (0-10s)  打出「我想」→ 逐字删掉；Clawd wish（眼睛向上看一点）
//   S2 (10-20s) 打出「如果我能」→ 逐字删掉；房间压暗 10%
//   S3 (20-30s) 终端只剩 `$ ` 和 2s 一次的光标闪烁；字幕「（什么都不写了）」
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// Clawd 40×17 (4×4 眼睛收成 4×3 仰视，1×1 高光；无嘴)。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, STATUS_Y, LINE_Y, CONTENT, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E08_wish_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — draft',
  S2: 'clawd@dsh:~ — draft',
  S3: 'clawd@dsh:~ — ',
};
const SUB_LINES = ['', '', '（什么都不写了）'];
const SUB_WINDOWS = [{ start: 0, end: 0 }, { start: 0, end: 0 }, { start: 22.4, end: 29.0 }];

const PROMPT = '$ ';
const DRAFT_Y = LINE_Y[3];
const HINT_Y = LINE_Y[0];
const HINT_TEXT = '# 03:12 AM · 没人在线';

// --- S1: 「我想」→ 删掉 ---------------------------------------------------
const S1_TYPED = '我想';
const S1_TYPE_AT = 2.4;
const S1_TYPE_MS = 320;
const S1_DEL_AT = 5.6;
const S1_DEL_MS = 280;
const S1_CURSOR_PERIOD = 1.2;

// --- S2: 「如果我能」→ 删掉 -----------------------------------------------
const S2_TYPED = '如果我能';
const S2_TYPE_AT = 11.4;
const S2_TYPE_MS = 280;
const S2_DEL_AT = 15.4;
const S2_DEL_MS = 260;
const S2_CURSOR_PERIOD = 1.2;
const S2_DIM = 0.1;

// --- S3: 只剩光标 ----------------------------------------------------------
const S3_CURSOR_PERIOD = 2.0;

const CLAWD_BOX = [40, 242, 44, 32];
const CLAWD_X = S.CLAWD_ROOM.x;
const CLAWD_Y = S.CLAWD_ROOM.y;

// --- Clawd: quiet "wish" gaze --------------------------------------------
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  const dx = opts.dx || 0;
  const dy = opts.dy || 0;
  if (mood !== 'wish') {
    S.art.drawClawd(ctx, x + dx, y + dy, t, mood, warmMix);
    return;
  }
  // Slow breath: one 1px rise every 3s instead of the usual 2.2Hz bob.
  const bob = opts.noBob ? 0 : (Math.sin(t * 0.9) > 0.5 ? -1 : 0);
  const by = Math.round(y + bob + dy);
  const bx = x + dx;
  const bodyH = 17;
  const lerp = S.art.lerpColor;
  const bodyCol = lerp(C.clawdNorm, C.clawdWarm, warmMix);
  const darkCol = lerp(C.clawdNormDark, C.clawdWarmDark, warmMix);
  const bellyCol = lerp(C.clawdNormBelly, C.clawdWarmBelly, warmMix);

  px(ctx, bx, by, 40, bodyH, bodyCol);
  px(ctx, bx, by, 40, 2, darkCol);
  px(ctx, bx + 9, by + 11, 22, 4, bellyCol);

  // Eyes look up: 4×3 pupils one row higher, highlight in the top-left corner.
  for (const ex of [10, 26]) {
    px(ctx, bx + ex, by + 5, 4, 3, C.clawdEye);
    px(ctx, bx + ex + 1, by + 5, 1, 1, C.white);
  }

  const step = Math.sin(t * 3.0) > 0.75 ? 1 : 0;
  px(ctx, bx + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, bx + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Draft-line helpers ---------------------------------------------------
function cursorOn(t, period) {
  return t % period < period / 2;
}

function typedCount(t, length, typeAt, typeMs, delAt, delMs) {
  let shown = 0;
  if (t >= typeAt) shown = Math.min(length, Math.floor(((t - typeAt) * 1000) / typeMs) + 1);
  if (t >= delAt) {
    const gone = Math.min(length, Math.floor(((t - delAt) * 1000) / delMs) + 1);
    shown = Math.max(0, shown - gone);
  }
  return shown;
}

function drawDraft(ctx, t, typed, typeAt, typeMs, delAt, delMs, period) {
  S.txt(ctx, TEXT_X, DRAFT_Y, PROMPT, C.green, 10);
  const px0 = TEXT_X + S.textWidth(PROMPT, 10);
  const chars = Array.from(typed);
  const shown = typedCount(t, chars.length, typeAt, typeMs, delAt, delMs);
  const visible = chars.slice(0, shown).join('');
  if (visible) S.txt(ctx, px0, DRAFT_Y, visible, C.text, 10);
  const cx = px0 + S.textWidth(visible, 10) + (visible ? 1 : 0);
  if (cursorOn(t, period)) px(ctx, cx, DRAFT_Y, 6, 10, C.blue);
  return { cursorX: cx, shown };
}

function dimRoom(ctx, amount) {
  if (amount <= 0) return;
  px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${amount.toFixed(3)})`);
}

// --- Scene painters --------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  dimRoom(ctx, 0.05);
  S.drawTerminal(ctx, TITLES.S1, C.dim);
  if (t >= 0.8) S.txt(ctx, TEXT_X, HINT_Y, HINT_TEXT, C.dim, 10);
  drawDraft(ctx, t, S1_TYPED, S1_TYPE_AT, S1_TYPE_MS, S1_DEL_AT, S1_DEL_MS, S1_CURSOR_PERIOD);
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, 'wish', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  dimRoom(ctx, S2_DIM);
  S.drawTerminal(ctx, TITLES.S2, C.dim);
  S.txt(ctx, TEXT_X, HINT_Y, HINT_TEXT, C.dim, 10);
  drawDraft(ctx, t, S2_TYPED, S2_TYPE_AT, S2_TYPE_MS, S2_DEL_AT, S2_DEL_MS, S2_CURSOR_PERIOD);
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, 'wish', 0, { dy: 1 });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  dimRoom(ctx, S2_DIM);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  S.txt(ctx, TEXT_X, DRAFT_Y, PROMPT, C.green, 10);
  const cx = TEXT_X + S.textWidth(PROMPT, 10);
  if (cursorOn(t, S3_CURSOR_PERIOD)) px(ctx, cx, DRAFT_Y, 6, 10, C.blue);
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, 'wish', 0, { dy: 1 });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { start: 0, draw: drawS1 },
  { start: 10, draw: drawS2 },
  { start: 20, draw: drawS3 },
];

function renderAt(ctx, t) {
  S.renderScenes(ctx, t, SCENES);
}

// --- Clicks: every typed character AND every backspace --------------------
function scriptClicks(count, at, ms) {
  return Array.from({ length: count }, (_, i) => at + (i * ms) / 1000);
}

function getClickTimestamps() {
  return S.quantizeClicks([
    ...scriptClicks(Array.from(S1_TYPED).length, S1_TYPE_AT, S1_TYPE_MS),
    ...scriptClicks(Array.from(S1_TYPED).length, S1_DEL_AT, S1_DEL_MS),
    ...scriptClicks(Array.from(S2_TYPED).length, S2_TYPE_AT, S2_TYPE_MS),
    ...scriptClicks(Array.from(S2_TYPED).length, S2_DEL_AT, S2_DEL_MS),
  ]);
}

const TYPING_SCHEDULE = [
  { text: PROMPT + S1_TYPED, start: S1_TYPE_AT, charMs: S1_TYPE_MS, limit: 9.6 },
  { text: PROMPT + S2_TYPED, start: S2_TYPE_AT, charMs: S2_TYPE_MS, limit: 19.6 },
  { text: PROMPT, start: 20.05, charMs: S.TYPE_CHAR_MS, limit: 29.6 },
];

// --- Layout groups (0px tolerance, per frame) ------------------------------
const PROMPT_W = S.textWidth(PROMPT, 10);

function draftLayout(typed) {
  const w = S.textWidth(typed, 10);
  const list = [{ name: 'prompt_row', box: S.textBox(TEXT_X, DRAFT_Y, PROMPT, 10) }];
  if (w > 0) {
    list.push({ name: 'typed_row', box: [TEXT_X + PROMPT_W, DRAFT_Y, w, 13] });
    list.push({ name: 'blink_cursor', box: [TEXT_X + PROMPT_W + w + 2, DRAFT_Y, 6, 10] });
  } else {
    list.push({ name: 'blink_cursor', box: [TEXT_X + PROMPT_W + 2, DRAFT_Y, 6, 10] });
  }
  return list;
}

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let layout;
  if (t < 10) {
    layout = S.baseLayout({ ...common, scene: 1, title: TITLES.S1, lines: [] });
    layout.groups.content = [
      { name: 'hint', box: S.textBox(TEXT_X, HINT_Y, HINT_TEXT, 10) },
      ...draftLayout(S1_TYPED),
    ];
  } else if (t < 20) {
    layout = S.baseLayout({ ...common, scene: 2, title: TITLES.S2, lines: [] });
    layout.groups.content = [
      { name: 'hint', box: S.textBox(TEXT_X, HINT_Y, HINT_TEXT, 10) },
      ...draftLayout(S2_TYPED),
    ];
  } else {
    layout = S.baseLayout({ ...common, scene: 3, title: TITLES.S3, lines: [] });
    layout.groups.content = draftLayout('');
  }
  layout.groups.foreground = S.foregroundLayout({
    terminal: true, clawd: false, her: false,
    extra: [{ name: 'clawd', box: CLAWD_BOX }],
  });
  return layout;
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
  art: ART,
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  PROMPT, DRAFT_Y, HINT_Y, HINT_TEXT, PROMPT_W,
  S1_TYPED, S1_TYPE_AT, S1_TYPE_MS, S1_DEL_AT, S1_DEL_MS, S1_CURSOR_PERIOD,
  S2_TYPED, S2_TYPE_AT, S2_TYPE_MS, S2_DEL_AT, S2_DEL_MS, S2_CURSOR_PERIOD,
  S3_CURSOR_PERIOD, S2_DIM, CLAWD_BOX,
  CHECK_TITLE: 'E08 愿望 (wish) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '# 03:12 AM · 没人在线', size: 10, color: C.dim },
    { text: '$ 如果我能', size: 10, color: C.text },
    { text: '（什么都不写了）', size: 10, color: C.white },
    { text: '$ ', size: 10, color: C.green },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps, drawClawdEp, cursorOn, typedCount, scriptClicks,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
