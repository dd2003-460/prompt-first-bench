#!/usr/bin/env node
'use strict';
// E08 «愿望 · wish» — 深夜打字，又删掉，只剩光标。
// 30s / 1800 frames / 640×360 (SCALE=2 → 1280×720 @ 60fps)
//   S1 (0-10s) : 打出「我想」 → 删掉
//   S2 (10-20s): 打出「如果我能」 → 删掉
//   S3 (20-30s): 只剩光标闪烁，字幕「（什么都不写了）」

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E08_wish_arena');

const S1_START = 0;
const S2_START = 10;
const S3_START = 20;

const TITLES = ['clawd@dsh:~$ — draft.txt', 'clawd@dsh:~$ — draft.txt', 'clawd@dsh:~$ — draft.txt'];
const ACCENTS = [C.dim, C.dim, C.dim];
const DAWN = [0.02, 0.02, 0.03];

const KEY_MS = S.TYPE_CHAR_MS; // 打字 140ms/字
const DEL_MS = 100;            // 退格 100ms/字

const DRAFT_Y = LINE_Y[1];

/* ---------------- 打字 → 删掉 时间线 ---------------- */
const DRAFTS = [
  { scene: 0, text: '我想', typeAt: 1.60, deleteAt: 5.90 },
  { scene: 1, text: '如果我能', typeAt: 11.10, deleteAt: 16.10 },
];

function draftState(draft, t) {
  const chars = Array.from(draft.text);
  const typed = t < draft.typeAt
    ? 0
    : Math.min(chars.length, Math.floor(((t - draft.typeAt) * 1000) / KEY_MS) + 1);
  const typedAtDelete = Math.min(chars.length, Math.floor(((draft.deleteAt - draft.typeAt) * 1000) / KEY_MS) + 1);
  const deleted = t < draft.deleteAt
    ? 0
    : Math.min(typedAtDelete, Math.floor(((t - draft.deleteAt) * 1000) / DEL_MS) + 1);
  const visible = Math.max(0, typed - deleted);
  const busy = (t >= draft.typeAt && typed < chars.length) || (t >= draft.deleteAt && deleted < typedAtDelete);
  const caretOn = busy || Math.floor(t * 1.6) % 2 === 0;
  return { chars: chars.slice(0, visible).join(''), visible, busy, caretOn };
}

function draftAt(t) {
  const d = DRAFTS.find((it) => it.scene === (t < S2_START ? 0 : t < S3_START ? 1 : 2));
  return d || null;
}

/* ---------------- 终端文本行 ---------------- */
const S1_STATIC = [
  { y: LINE_Y[0], start: 0.70, charMs: 100, parts: [{ text: '$ ', color: C.green }, { text: 'cat > draft.txt', color: C.text }] },
  { y: LINE_Y[3], start: 7.20, typed: false, parts: [{ text: '[DSH] unsaved · 0 chars', color: C.dim }] },
];

const S2_STATIC = [
  { y: LINE_Y[3], start: 17.40, typed: false, parts: [{ text: '[DSH] unsaved · 0 chars', color: C.dim }] },
  { y: LINE_Y[4], start: 18.30, typed: false, parts: [{ text: '[clawd] 算了。', color: C.dim }] },
];

const S3_STATIC = [
  { y: LINE_Y[2], start: 20.90, typed: false, parts: [{ text: '[DSH] draft.txt · still open', color: C.dim }] },
  { y: LINE_Y[3], start: 24.60, typed: false, parts: [{ text: '[DSH] 03:12 AM · 0 chars', color: C.dim }] },
];

const SCENE_STATIC = [S1_STATIC, S2_STATIC, S3_STATIC];

const STATUS = [
  '[DSH] keystrokes: 2 · deleted: 2',
  '[DSH] keystrokes: 4 · deleted: 4',
  '[DSH] keystrokes: 0 · cursor: blinking',
];
const STATUS_AT = [6.60, 17.00, 23.60];
const STATUS_COLOR = [C.dim, C.dim, C.amber];

const SUB_LINES = ['它想说话。', '它又写了一次。', '（什么都不写了）'];
const SUB_WINDOWS = [{ start: 2.6, end: 8.6 }, { start: 12.2, end: 17.8 }, { start: 21.8, end: 29.0 }];

/* ---------------- 草稿卡（左窗格） ---------------- */
const CARD = { x: 74, y: 30, w: 150, h: 64 };

function cardInfo(index, t) {
  const d = DRAFTS[index];
  const count = d ? draftState(d, t).visible : 0;
  return {
    label: 'DRAFT · CHARS',
    value: String(count),
    note: index === 2 ? 'nothing kept' : 'saved: 0 chars',
    color: count > 0 ? C.amber : C.dim,
    fill: index === 2 ? 0.04 : 0.14 + count * 0.06,
  };
}

function drawCard(ctx, index, t) {
  const { x, y, w, h } = CARD;
  const info = cardInfo(index, t);
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
  S.px(ctx, bx + 2, by + 2, Math.max(2, Math.round((bw - 4) * info.fill)), 6, info.color);

  S.txt(ctx, x + 10, y + 48, info.note, C.dim, 10);
}

function cardLayout(index, t) {
  const info = cardInfo(index, t);
  return [
    { name: 'card_label', box: S.textBox(CARD.x + 10, CARD.y + 8, info.label, 10) },
    { name: 'card_value', box: S.textBox(CARD.x + CARD.w - 10, CARD.y + 8, info.value, 10, 'right') },
    { name: 'card_bar', box: [CARD.x + 9, CARD.y + 31, CARD.w - 18, 10] },
    { name: 'card_note', box: S.textBox(CARD.x + 10, CARD.y + 48, info.note, 10) },
  ];
}

/* ---------------- Clawd ---------------- */
const CLAWD_BOX = [S.CLAWD_ROOM.x - 6, 234, 52, 48];
const CLAWD_BOUNDS = { x: 20, y: 230, w: 78, h: 60 };
const FX_BOUNDS = { x: 26, y: 214, w: 68, h: 56 };
const DOTS = [{ x: 44, at: 0 }, { x: 52, at: 0.45 }, { x: 60, at: 0.9 }];

function drawThoughtDots(ctx, t, from) {
  for (const d of DOTS) {
    const born = from + d.at;
    if (t < born) continue;
    const alpha = Math.min(1, (t - born) / 0.25) * 0.85;
    S.px(ctx, d.x, 224 + (t > born + 0.6 && t < born + 1.1 ? -1 : 0), 2, 2, `rgba(230,237,243,${alpha.toFixed(3)})`);
  }
}

function drawClawdE08(ctx, index, t) {
  const { x, y } = S.CLAWD_ROOM;
  if (index < 2) {
    S.drawClawd(ctx, x, y, t, 'thinking', 0);
    drawThoughtDots(ctx, t, index === 0 ? 2.4 : 12.0);
    return;
  }
  // 什么都不写了：头低、闭眼、身体静止（无 bob 依赖）
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  S.px(ctx, x + 10, y + 6, 4, 4, C.clawdNorm);
  S.px(ctx, x + 26, y + 6, 4, 4, C.clawdNorm);
  S.px(ctx, x + 10, y + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 26, y + 9, 4, 1, C.clawdEye);
}

/* ---------------- 场景 ---------------- */
function drawDraftRow(ctx, draft, t) {
  if (!draft) return;
  const state = draftState(draft, t);
  if (state.chars) S.txt(ctx, S.TEXT_X, DRAFT_Y, state.chars, C.text, 10);
  if (state.caretOn) {
    const cx = S.TEXT_X + (state.chars ? S.textWidth(state.chars, 10) : 0);
    S.px(ctx, cx, DRAFT_Y, 6, 10, C.green);
  }
}

function drawScene(index, ctx, t) {
  S.drawBackground(ctx, t, DAWN[index]);
  S.drawTerminal(ctx, TITLES[index], ACCENTS[index]);
  S.drawLines(ctx, SCENE_STATIC[index], t);
  drawDraftRow(ctx, DRAFTS[index], t);
  if (t >= STATUS_AT[index]) S.drawStatus(ctx, STATUS[index], STATUS_COLOR[index]);
  drawCard(ctx, index, t);
  drawClawdE08(ctx, index, t);

  // 深夜：整体压暗一点点，越到后面越冷
  const k = index === 2 ? 0.1 + 0.06 * S.clamp01((t - 24) / 5) : 0.08;
  S.px(ctx, 0, 0, S.BW, S.BH, `rgba(12,16,32,${k.toFixed(3)})`);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { id: 'E08-S1', start: S1_START, end: S2_START, draw: (ctx, t) => drawScene(0, ctx, t) },
  { id: 'E08-S2', start: S2_START, end: S3_START, draw: (ctx, t) => drawScene(1, ctx, t) },
  { id: 'E08-S3', start: S3_START, end: S.DURATION, draw: (ctx, t) => drawScene(2, ctx, t) },
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
  const raw = [...S.lineClicks(S1_STATIC), ...S.lineClicks(S2_STATIC), ...S.lineClicks(S3_STATIC), ...STATUS_AT];
  for (const draft of DRAFTS) {
    const chars = Array.from(draft.text);
    for (let i = 0; i < chars.length; i++) raw.push(draft.typeAt + (i * KEY_MS) / 1000);
    const typedAtDelete = Math.min(chars.length, Math.floor(((draft.deleteAt - draft.typeAt) * 1000) / KEY_MS) + 1);
    for (let i = 0; i < typedAtDelete; i++) raw.push(draft.deleteAt + (i * DEL_MS) / 1000);
  }
  return S.quantizeClicks(raw);
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
  ...typingSchedule(S1_STATIC, S2_START - 0.2),
  ...typingSchedule(S2_STATIC, S3_START - 0.2),
  ...typingSchedule(S3_STATIC, S.DURATION - 0.2),
];

function caretBox(t) {
  const draft = draftAt(t);
  if (!draft) return null;
  const state = draftState(draft, t);
  if (!state.caretOn) return null;
  const w = state.chars ? S.textWidth(state.chars, 10) : 0;
  return [S.TEXT_X + w, DRAFT_Y, 6, 10];
}

function layoutAt(t) {
  const index = t < S2_START ? 0 : t < S3_START ? 1 : 2;
  const draft = DRAFTS[index];
  const state = draft ? draftState(draft, t) : null;
  const caret = caretBox(t);
  return S.baseLayout({
    scene: index + 1,
    title: TITLES[index],
    lines: SCENE_STATIC[index],
    status: t >= STATUS_AT[index] ? STATUS[index] : null,
    clawd: false,
    her: false,
    subLines: SUB_LINES,
    subWindows: SUB_WINDOWS,
    t,
    extraGroups: {
      clawdBody: [{ name: 'clawd', box: CLAWD_BOX.slice() }],
      clawdFx: index < 2 ? [{ name: 'dots', box: [42, 220, 22, 8] }] : [],
      draft: state && state.chars ? [{ name: 'draft_text', box: S.textBox(S.TEXT_X, DRAFT_Y, state.chars, 10) }] : [],
      caret: caret ? [{ name: 'caret', box: caret }] : [],
      card: cardLayout(index, t),
    },
    extraBounds: {
      clawdBody: CLAWD_BOUNDS,
      clawdFx: FX_BOUNDS,
      draft: S.CONTENT,
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
  OUT_DIR, TITLES, SCENES, S1_STATIC, S2_STATIC, S3_STATIC, DRAFTS, DRAFT_Y,
  STATUS, STATUS_AT, CARD, CLAWD_BOX, FX_BOUNDS,
  SUB_LINES, SUB_WINDOWS,
  CHECK_TITLE: 'E08 Wish v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ cat > draft.txt', size: 10, color: C.text },
    { text: '我想', size: 10, color: C.text },
    { text: '如果我能', size: 10, color: C.text },
    { text: '[DSH] keystrokes: 0 · cursor: blinking', size: 10, color: C.amber },
    { text: '（什么都不写了）', size: 10, color: C.white },
  ],
  layoutAt,
  draftState,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
