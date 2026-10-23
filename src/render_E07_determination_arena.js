#!/usr/bin/env node
'use strict';
// E07 «目标 · determination» — finish before sunrise，时钟 23:58 → 00:00。
// 30s / 1800 frames / 640×360 (SCALE=2 → 1280×720 @ 60fps)
//   S1 (0-10s)  : `cat task.txt` = "finish before sunrise"，时钟 23:58，Clawd determined
//   S2 (10-20s) : 终端快速滚动 (build / test / deploy)，时钟 23:59
//   S3 (20-30s) : "deployed ✓"，时钟 00:00，Clawd 释然，字幕「赶上了。」

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E07_determination_arena');

const S1_START = 0;
const S2_START = 10;
const S3_START = 20;

const TITLES = ['clawd@dsh:~$ — cat task.txt', 'clawd@dsh:~$ — make all', 'clawd@dsh:~$ — deploy'];
const ACCENTS = [C.amber, C.amber, C.green];
const DAWN = [0.04, 0.06, 0.1];

/* ---------------- S1 · 任务 ---------------- */
const S1_LINES = [
  { y: LINE_Y[0], start: 0.70, parts: [{ text: '$ ', color: C.green }, { text: 'cat task.txt', color: C.text }] },
  { y: LINE_Y[1], start: 2.40, typed: false, parts: [{ text: 'finish before sunrise', color: C.amber }] },
  { y: LINE_Y[2], start: 3.10, typed: false, parts: [{ text: '[DSH] deadline: 05:12', color: C.dim }] },
  { y: LINE_Y[3], start: 3.80, typed: false, parts: [{ text: '[DSH] remaining: 5h 14m', color: C.dim }] },
  { y: LINE_Y[4], start: 5.10, typed: false, parts: [{ text: '[clawd] 开始。', color: C.green }] },
];

/* ---------------- S2 · 快速滚动 ---------------- */
const S2_ITEMS = [
  { t: 10.60, text: '$ make all', color: C.text, typed: true, charMs: 70 },
  { t: 11.60, text: '[1/6] install .............. ok', color: C.dim },
  { t: 11.95, text: '[2/6] lint ................. ok', color: C.dim },
  { t: 12.30, text: '[3/6] unit tests .......... 128 ok', color: C.dim },
  { t: 12.65, text: '[4/6] tsc -p . ............. ok', color: C.dim },
  { t: 13.00, text: '[5/6] bundle ............... ok', color: C.dim },
  { t: 13.35, text: '[6/6] smoke test ........... ok', color: C.green },
  { t: 14.10, text: '$ git push origin main', color: C.text, typed: true, charMs: 70 },
  { t: 15.30, text: '[git] remote: 41 objects written', color: C.dim },
  { t: 15.70, text: '[git] main -> main  (1.2s)', color: C.dim },
  { t: 16.40, text: '$ deploy --prod', color: C.text, typed: true, charMs: 70 },
  { t: 17.40, text: '[deploy] uploading 41 files', color: C.dim },
  { t: 17.70, text: '[deploy] health check ....... ok', color: C.green },
  { t: 18.10, text: '[deploy] 00:00:41 remaining', color: C.amber },
];
const S2_ROWS = 6;
const S2_SCROLL_MS = 160;

/* ---------------- S3 · 赶上了 ---------------- */
const S3_LINES = [
  { y: LINE_Y[0], start: 20.45, charMs: 78, parts: [{ text: '$ ', color: C.green }, { text: 'deploy --prod --wait', color: C.text }] },
  { y: LINE_Y[1], start: 22.30, charMs: 120, parts: [{ text: 'deployed ', color: C.green }, { text: '✓', color: C.green }] },
  { y: LINE_Y[2], start: 23.90, typed: false, parts: [{ text: '[DSH] handoff complete · 0 errors', color: C.dim }] },
  { y: LINE_Y[3], start: 25.10, typed: false, parts: [{ text: '[DSH] 00:00 · sunrise in 5h12m', color: C.amber }] },
  { y: LINE_Y[4], start: 26.60, typed: false, parts: [{ text: '[clawd] 赶上了。', color: C.green }] },
];

const SCENE_LINES = [S1_LINES, S3_LINES];

const STATUS = [
  '[DSH] deadline: sunrise 05:12',
  '[DSH] build: 6/6 · tests: 128 · 23:59',
  '[DSH] task: completed · 5h12m early',
];
const STATUS_AT = [4.60, 18.40, 27.20];
const STATUS_COLOR = [C.amber, C.amber, C.green];

const SUB_LINES = ['天亮之前，必须完成。', '还有时间。还有一点。', '赶上了。'];
const SUB_WINDOWS = [{ start: 3.0, end: 8.4 }, { start: 12.6, end: 18.4 }, { start: 24.0, end: 29.2 }];

/* ---------------- 时钟卡（左窗格） ---------------- */
const CARD = { x: 74, y: 30, w: 150, h: 64 };
const CARD_INFO = [
  { clock: '23:58', noteLabel: 'TO SUNRISE', fill: 0.18, color: C.amber },
  { clock: '23:59', noteLabel: 'TO SUNRISE', fill: 0.06, color: C.red },
  { clock: '00:00', noteLabel: 'SUNRISE 05:12', fill: 1, color: C.green },
];

function drawClockCard(ctx, index, t) {
  const { x, y, w, h } = CARD;
  const info = CARD_INFO[index];
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.18)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);

  S.txt(ctx, x + 10, y + 6, 'LOCAL TIME', C.dim, 10);
  S.txt(ctx, x + w - 10, y + 6, info.noteLabel, C.dim, 10, 'right');

  // 大号时钟：秒级的「滴」闪烁，越靠近 00:00 越紧张
  const tick = index === 2 ? false : Math.floor(t * 2) % 2 === 0;
  S.txt(ctx, x + w / 2, y + 24, info.clock, tick ? info.color : C.white, 14, 'center');

  const bx = x + 9;
  const by = y + 50;
  const bw = w - 18;
  S.px(ctx, bx, by, bw, 8, C.border);
  const inner = bw - 4;
  S.px(ctx, bx + 2, by + 2, Math.max(2, Math.round(inner * info.fill)), 4, info.color);
}

function clockCardLayout(index) {
  const info = CARD_INFO[index];
  return [
    { name: 'card_label', box: S.textBox(CARD.x + 10, CARD.y + 6, 'LOCAL TIME', 10) },
    { name: 'card_note', box: S.textBox(CARD.x + CARD.w - 10, CARD.y + 6, info.noteLabel, 10, 'right') },
    { name: 'card_clock', box: S.textBox(CARD.x + CARD.w / 2, CARD.y + 24, info.clock, 14, 'center') },
    { name: 'card_bar', box: [CARD.x + 9, CARD.y + 49, CARD.w - 18, 10] },
  ];
}

/* ---------------- S2 滚动终端 ---------------- */
function visibleS2Items(t) {
  const items = S2_ITEMS.filter((it) => t >= it.t);
  return items.slice(-S2_ROWS);
}

function scrollProgress(t) {
  const last = S2_ITEMS.filter((it) => t >= it.t).pop();
  if (!last) return 1;
  return S.clamp01((t - last.t) / (S2_SCROLL_MS / 1000));
}

function drawScrolledLines(ctx, t) {
  const rows = visibleS2Items(t);
  const p = scrollProgress(t);
  const shift = Math.round((1 - p) * 11);
  for (let r = 0; r < rows.length; r++) {
    const it = rows[r];
    const y = LINE_Y[r] + shift;
    if (it.typed) {
      const chars = Array.from(it.text);
      const n = Math.min(chars.length, Math.floor(((t - it.t) * 1000) / (it.charMs || S.TYPE_CHAR_MS)) + 1);
      const shown = chars.slice(0, n).join('');
      if (shown) S.txt(ctx, S.TEXT_X, y, shown, it.color, 10);
    } else {
      S.txt(ctx, S.TEXT_X, y, it.text, it.color, 10);
    }
  }
}

/* ---------------- Clawd 情绪 ---------------- */
const CLAWD_BOX = [S.CLAWD_ROOM.x - 6, 234, 52, 48];
const CLAWD_BOUNDS = { x: 20, y: 230, w: 78, h: 60 };
const FX_BOUNDS = { x: 26, y: 214, w: 68, h: 56 };

function drawClawdE07(ctx, index, t) {
  const { x, y } = S.CLAWD_ROOM;
  if (index === 0) {
    S.drawClawd(ctx, x, y, t, 'thinking', 0);
    // 专注：头上一盏小小的琥珀色灯
    const glow = 0.45 + 0.25 * Math.sin(t * 3.6);
    S.px(ctx, x + 18, 226, 4, 4, C.amber);
    S.px(ctx, x + 16, 224, 8, 2, `rgba(227,179,65,${glow.toFixed(3)})`);
    return;
  }
  if (index === 1) {
    S.drawClawd(ctx, x, y, t, 'thinking', 0);
    // 高速工作：身后速度线
    const shift = Math.floor(t * 14) % 4;
    for (let i = 0; i < 3; i++) {
      S.px(ctx, x - 10 - shift, 246 + i * 6, 9, 1, 'rgba(139,148,158,0.5)');
    }
    return;
  }
  S.drawClawd(ctx, x, y, t, 'smile', 1);
  // 释然：闭眼 + 一口气（透明的呼气团）
  S.px(ctx, x + 10, y + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 26, y + 9, 4, 1, C.clawdEye);
  S.px(ctx, x + 4, y + 9, 4, 2, C.pink);
  S.px(ctx, x + 32, y + 9, 4, 2, C.pink);
  const phase = (t * 0.7) % 1;
  S.px(ctx, x + 44 + Math.round(phase * 8), Math.round(252 - phase * 6), 3, 3, `rgba(230,237,243,${((1 - phase) * 0.35).toFixed(3)})`);
}

/* ---------------- 场景 ---------------- */
function drawScene(index, ctx, t) {
  S.drawBackground(ctx, t, DAWN[index]);
  S.drawTerminal(ctx, TITLES[index], ACCENTS[index]);
  if (index === 1) {
    drawScrolledLines(ctx, t);
  } else {
    S.drawLines(ctx, index === 0 ? S1_LINES : S3_LINES, t);
  }
  if (t >= STATUS_AT[index]) S.drawStatus(ctx, STATUS[index], STATUS_COLOR[index]);
  drawClockCard(ctx, index, t);
  drawClawdE07(ctx, index, t);

  if (index === 2) {
    // 00:00 之后：窗户开始透出一点晨光
    const k = S.clamp01((t - 24) / 5);
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(255,205,110,${(k * 0.05).toFixed(3)})`);
  }
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { id: 'E07-S1', start: S1_START, end: S2_START, draw: (ctx, t) => drawScene(0, ctx, t) },
  { id: 'E07-S2', start: S2_START, end: S3_START, draw: (ctx, t) => drawScene(1, ctx, t) },
  { id: 'E07-S3', start: S3_START, end: S.DURATION, draw: (ctx, t) => drawScene(2, ctx, t) },
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
  const raw = [
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S3_LINES),
    ...STATUS_AT,
  ];
  // S2：整屏快速滚动，每行每个字符都是一次真实敲击
  for (const it of S2_ITEMS) {
    if (!it.typed) raw.push(it.t);
    else {
      const chars = Array.from(it.text);
      for (let i = 0; i < chars.length; i++) raw.push(it.t + (i * (it.charMs || S.TYPE_CHAR_MS)) / 1000);
    }
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
const S2_TYPED_ITEMS = S2_ITEMS.filter((it) => it.typed).map((it) => ({
  y: LINE_Y[0], start: it.t, charMs: it.charMs, parts: [{ text: it.text, color: it.color }],
}));
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, S2_START - 0.2),
  ...typingSchedule(S2_TYPED_ITEMS, S3_START - 0.2),
  ...typingSchedule(S3_LINES, S.DURATION - 0.2),
];

function layoutAt(t) {
  const index = t < S2_START ? 0 : t < S3_START ? 1 : 2;
  const lines = index === 0 ? S1_LINES
    : index === 1 ? visibleS2Items(t).map((it, r) => ({ y: LINE_Y[r], typed: false, parts: [{ text: it.text, color: it.color }] }))
      : S3_LINES;
  const fx = index === 1
    ? [{ name: 'speed', box: [26, 244, 12, 14] }]
    : index === 2 ? [{ name: 'breath', box: [80, 236, 14, 16] }] : [{ name: 'focus', box: [32, 222, 12, 8] }];
  return S.baseLayout({
    scene: index + 1,
    title: TITLES[index],
    lines,
    status: t >= STATUS_AT[index] ? STATUS[index] : null,
    clawd: false,
    her: false,
    subLines: SUB_LINES,
    subWindows: SUB_WINDOWS,
    t,
    extraGroups: {
      clawdBody: [{ name: 'clawd', box: CLAWD_BOX.slice() }],
      clawdFx: fx,
      clockCard: clockCardLayout(index),
    },
    extraBounds: {
      clawdBody: CLAWD_BOUNDS,
      clawdFx: FX_BOUNDS,
      clockCard: CARD,
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
  OUT_DIR, TITLES, SCENES, S1_LINES, S2_ITEMS, S3_LINES,
  STATUS, STATUS_AT, CARD, CLAWD_BOX, FX_BOUNDS,
  SUB_LINES, SUB_WINDOWS,
  CHECK_TITLE: 'E07 Determination v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'finish before sunrise', size: 10, color: C.amber },
    { text: '[4/6] tsc -p . ............. ok', size: 10, color: C.dim },
    { text: 'deployed ✓', size: 10, color: C.green },
    { text: '23:58', size: 14, color: C.amber },
    { text: '赶上了。', size: 10, color: C.white },
  ],
  layoutAt,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
