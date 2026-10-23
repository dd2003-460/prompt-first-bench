#!/usr/bin/env node
'use strict';
// E08 「愿望」— 深夜打字又删掉，只剩光标, 30s, 1800 frames.
//
//   S1 (0-10s)  : 打出「我想」→ 逐字退格删掉
//   S2 (10-20s) : 打出「如果我能」→ 逐字退格删掉
//   S3 (20-30s) : 只剩闪烁光标, 字幕「（什么都不写了）」
//
// 每个字符（含退格）都对应一次 sfx_click，时间点由同一份 timeline 推导。
// 起草区固定在终端内 x=114..522 / y=236..280，文字基线 y=252，
// 与标签行 (176)、幽灵行 (196/214)、状态行 (320) 均无重叠。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E08_arena');
const S2_START = 10;
const S3_START = 20;

const TITLE = {
  S1: 'draft.txt — 03:12',
  S2: 'draft.txt — 03:13',
  S3: 'draft.txt — 03:14',
};

const FIELD = { x: TEXT_X, y: 236, w: 408, h: 44 };
const FIELD_TEXT_X = FIELD.x + 12;
const FIELD_TEXT_Y = 252;
const LABEL_Y = 176;
const HINT_Y = 298;
const GHOST_Y = [196, 214];

const SUB_LINES = ['（什么都不写了）'];
const SUB_WINDOWS = [{ start: 22, end: 29 }];

// --- Draft timelines -------------------------------------------------------
// del = 退格时刻；同一个 key 一个 click（打字一下、删字一下）。
function makeTyping(str, start, charMs, delStart, delMs) {
  const chars = Array.from(str);
  return chars.map((ch, i) => ({
    ch,
    at: start + (i * charMs) / 1000,
    del: delStart === null ? null : delStart + ((chars.length - 1 - i) * delMs) / 1000,
  }));
}

const S1_CHARS = makeTyping('我想', 2.6, 140, 6.8, 140);
const S2_CHARS = makeTyping('如果我能', 12.4, 140, 16.8, 140);
const ALL_CHARS = [...S1_CHARS, ...S2_CHARS];

function visibleAt(chars, t) {
  return chars.filter((c) => t >= c.at && (c.del === null || t < c.del)).map((c) => c.ch).join('');
}

// The last deleted character flashes for 0.12s so the backspace reads on screen.
function deletionFlashAt(chars, t) {
  for (const c of chars) {
    if (c.del !== null && t >= c.del && t < c.del + 0.12) return true;
  }
  return false;
}

function typingAt(chars, t) {
  return chars.some((c) => t >= c.at && t < c.at + 0.1);
}

const S1_STATUS = '[DSH] autosave: off';
const S2_STATUS = '[DSH] autosave: off';
const S3_STATUS = '[DSH] draft: 0 bytes · nothing sent';
const S1_STATUS_AT = 1.4;
const S2_STATUS_AT = 11.6;
const S3_STATUS_AT = 21.0;

const CLAWD_BOX = { name: 'clawd', box: [34, 240, 56, 40] };

// --- Drawing ---------------------------------------------------------------
function drawField(ctx, t, caretColor) {
  const { x, y, w, h } = FIELD;
  S.px(ctx, x, y, w, h, '#0F1116');
  S.px(ctx, x, y, w, 2, C.termBd);
  S.px(ctx, x, y + h - 2, w, 2, C.termBd);
  S.px(ctx, x, y, 2, h, C.termBd);
  S.px(ctx, x + w - 2, y, 2, h, C.termBd);
  // A soft accent edge marks the active line without adding another box.
  S.px(ctx, x + 2, y + 2, 3, h - 4, caretColor);
  // Caret: solid while typing, blinking when idle, red flash right after a delete.
  void t;
}

// Rejected drafts stay visible as greyed, struck-out log rows: written, then taken back.
function drawGhost(ctx, text, y) {
  const ghost = '#5B6472';
  S.txt(ctx, TEXT_X, y, '-', ghost, 10);
  const w = S.textWidth(text, 10);
  S.txt(ctx, TEXT_X + 16, y, text, ghost, 10);
  S.px(ctx, TEXT_X + 16, y + 6, w, 1, '#414A57');
}

function drawComposer(ctx, chars, t) {
  const text = visibleAt(chars, t);
  const deleted = chars.filter((c) => c.del !== null && t >= c.del && t < c.del + 0.35);
  const color = deletionFlashAt(chars, t) ? C.pink : C.text;
  drawField(ctx, t, chars === S1_CHARS ? C.purple : C.blue);
  if (text) {
    S.txt(ctx, FIELD_TEXT_X, FIELD_TEXT_Y, text, color, 10);
  }
  const width = S.textWidth(text, 10);
  // Erased glyphs leave a short pixel trail behind the caret.
  for (const c of deleted) {
    const k = 1 - (t - c.del) / 0.35;
    S.px(ctx, FIELD_TEXT_X + width + 6, FIELD_TEXT_Y + 2, Math.max(2, Math.round(8 * k)), 8, 'rgba(255,154,162,0.45)');
  }
  const cx = FIELD_TEXT_X + width + (text ? 3 : 0);
  const steady = typingAt(chars, t) || deletionFlashAt(chars, t);
  const blinkOn = steady || Math.floor(t * 2) % 2 === 0;
  if (blinkOn) {
    S.px(ctx, cx, FIELD_TEXT_Y, 2, 12, deletionFlashAt(chars, t) ? C.pink : C.purple);
  }
}

function drawCommon(ctx, t, scene) {
  const accent = scene === 3 ? C.purple : C.blue;
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, scene === 1 ? TITLE.S1 : scene === 2 ? TITLE.S2 : TITLE.S3, accent);
  // Label row
  S.txt(ctx, TEXT_X, LABEL_Y, 'clawd · draft', C.dim, 10);
  S.txt(ctx, TEXT_X + FIELD.w - S.textWidth('unsent', 10), LABEL_Y, 'unsent', C.amber, 10);
}

function drawClawdMood(ctx, t, scene) {
  if (scene === 1) {
    S.drawClawd(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm', 0);
    return;
  }
  if (scene === 2) {
    S.drawClawd(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'thinking', 0);
    return;
  }
  // Scene 3: eyes closed, head lowered, one pixel of breathing.
  const x = S.CLAWD_ROOM.x;
  const y = S.CLAWD_ROOM.y + 2;
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  S.px(ctx, x + 9, y + 4, 28, 6, C.clawdNorm);
  S.px(ctx, x + 12, y + 8, 6, 1, C.clawdEye);
  S.px(ctx, x + 22, y + 8, 6, 1, C.clawdEye);
  S.px(ctx, x + 17, y + 13, 6, 1, C.clawdEye);
}

function drawS1(ctx, t) {
  drawCommon(ctx, t, 1);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.dim);
  drawComposer(ctx, S1_CHARS, t);
  S.txt(ctx, TEXT_X, HINT_Y, 'enter to send · esc to keep it', C.dim, 10);
  drawClawdMood(ctx, t, 1);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  drawCommon(ctx, t, 2);
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.dim);
  drawComposer(ctx, S2_CHARS, t);
  S.txt(ctx, TEXT_X, HINT_Y, 'enter to send · backspace to forget', C.dim, 10);
  drawClawdMood(ctx, t, 2);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  drawCommon(ctx, t, 3);
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawGhost(ctx, '我想', GHOST_Y[0]);
  drawGhost(ctx, '如果我能', GHOST_Y[1]);
  // Empty composer: only the caret is left, and it keeps blinking.
  drawField(ctx, t, C.purple);
  if (Math.floor(t * 2) % 2 === 0) S.px(ctx, FIELD_TEXT_X, FIELD_TEXT_Y, 2, 12, C.purple);
  S.txt(ctx, TEXT_X, HINT_Y, 'enter to send · backspace to forget', '#3F4652', 10);
  drawClawdMood(ctx, t, 3);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function fade(ctx, a) {
  if (a > 0) S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${Math.min(1, a).toFixed(3)})`);
}

function renderAt(ctx, t) {
  if (t < S2_START) {
    drawS1(ctx, t);
    if (t >= S2_START - S.FADE) fade(ctx, (t - (S2_START - S.FADE)) / S.FADE);
    return;
  }
  if (t < S3_START) {
    drawS2(ctx, t);
    if (t < S2_START + S.FADE) fade(ctx, 1 - (t - S2_START) / S.FADE);
    if (t >= S3_START - S.FADE) fade(ctx, (t - (S3_START - S.FADE)) / S.FADE);
    return;
  }
  drawS3(ctx, t);
  if (t < S3_START + S.FADE) fade(ctx, 1 - (t - S3_START) / S.FADE);
  // Closing dusk: the room dims as the wish is dropped.
  fade(ctx, S.clamp01((t - 28.2) / 1.8) * 0.25);
}

function getClickTimestamps() {
  const raw = [S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT];
  for (const c of ALL_CHARS) {
    raw.push(c.at);
    if (c.del !== null) raw.push(c.del);
  }
  return S.quantizeClicks(raw);
}

// Typing-rate assertions for the shared checker: the composer is manually timed,
// so expose the plain-text lines it produces as schedule entries.
function typingSchedule(lines, limit) {
  return lines.map((line, i) => ({
    text: S.lineText(line), start: line.start, charMs: line.charMs || S.TYPE_CHAR_MS,
    limit, strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const SCHEDULE_LINES = [
  { y: FIELD_TEXT_Y, start: S1_CHARS[0].at, parts: [{ text: '我想', color: C.text }] },
  { y: FIELD_TEXT_Y, start: S2_CHARS[0].at, parts: [{ text: '如果我能', color: C.text }] },
];
const TYPING_SCHEDULE = [
  ...typingSchedule([SCHEDULE_LINES[0]], 9.8),
  ...typingSchedule([SCHEDULE_LINES[1]], 19.8),
];

const COMPOSER_LINES_S1 = [];
function composerLayout(chars, t) {
  const text = visibleAt(chars, t);
  const list = [];
  if (text) {
    list.push({ name: 'composer_text', box: S.textBox(FIELD_TEXT_X, FIELD_TEXT_Y, text, 10) });
  }
  const width = S.textWidth(text, 10);
  list.push({
    name: 'caret',
    box: [Math.round(FIELD_TEXT_X + width + (text ? 3 : 0)), FIELD_TEXT_Y, 2, 12],
  });
  return list;
}

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  const base = S.baseLayout({
    ...common, scene: t < S2_START ? 1 : t < S3_START ? 2 : 3,
    title: t < S2_START ? TITLE.S1 : t < S3_START ? TITLE.S2 : TITLE.S3,
    lines: [], status: t < S2_START ? S1_STATUS : t < S3_START ? S2_STATUS : S3_STATUS,
    clawd: false, her: false,
    extra: [CLAWD_BOX],
  });
  const content = [
    { name: 'label', box: S.textBox(TEXT_X, LABEL_Y, 'clawd · draft', 10) },
    { name: 'unsent', box: S.textBox(TEXT_X + FIELD.w - S.textWidth('unsent', 10), LABEL_Y, 'unsent', 10) },
    { name: 'hint', box: S.textBox(TEXT_X, HINT_Y, t < S2_START ? 'enter to send · esc to keep it' : 'enter to send · backspace to forget', 10) },
    { name: 'status', box: S.textBox(TEXT_X, S.STATUS_Y, t < S2_START ? S1_STATUS : t < S3_START ? S2_STATUS : S3_STATUS, 10) },
  ];
  if (t < S3_START) {
    content.push(...composerLayout(t < S2_START ? S1_CHARS : S2_CHARS, t));
  } else {
    content.push({ name: 'ghost_mark_1', box: S.textBox(TEXT_X, GHOST_Y[0], '-', 10) });
    content.push({ name: 'ghost_1', box: S.textBox(TEXT_X + 16, GHOST_Y[0], '我想', 10) });
    content.push({ name: 'ghost_mark_2', box: S.textBox(TEXT_X, GHOST_Y[1], '-', 10) });
    content.push({ name: 'ghost_2', box: S.textBox(TEXT_X + 16, GHOST_Y[1], '如果我能', 10) });
  }
  base.groups.content = content;
  base.groups.field = [{ name: 'composer_field', box: [FIELD.x, FIELD.y, FIELD.w, FIELD.h] }];
  base.bounds.field = FIELD;
  return base;
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) console.log(JSON.stringify({ count: getClickTimestamps().length, clicks: getClickTimestamps() }));
  else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    require('fs').writeFileSync(`/tmp/E08_${n}.png`, out.outCanvas.toBuffer('image/png'));
    console.log(`/tmp/E08_${n}.png`);
  } else renderer.renderAllFrames();
}

module.exports = {
  ...S,
  OUT_DIR, TITLE, SUB_LINES, SUB_WINDOWS,
  S1_CHARS, S2_CHARS, ALL_CHARS,
  S1_STATUS, S2_STATUS, S3_STATUS,
  S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  S2_START, S3_START, FIELD, FIELD_TEXT_X, FIELD_TEXT_Y, LABEL_Y, HINT_Y, GHOST_Y,
  CLAWD_BOX, visibleAt, COMPOSER_LINES_S1,
  CHECK_TITLE: 'E08 Wish Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'clawd · draft', size: 10, color: C.dim },
    { text: '如果我能', size: 10, color: C.text },
    { text: 'enter to send · esc to keep it', size: 10, color: C.dim },
    { text: 'enter to send · backspace to forget', size: 10, color: C.dim },
    { text: '（什么都不写了）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
