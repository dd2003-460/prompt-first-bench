#!/usr/bin/env node
'use strict';
// E07 目标 (determination) — 30s, 1800 frames @ 60fps.
// 事实源 (episodes.md): finish before sunrise —— 23:58 开始，00:00 部署完成。
//   S1 (0-10s)  `$ cat task.txt` → "finish before sunrise"；右上时钟 23:58；Clawd determined（眼神收窄）
//   S2 (10-20s) build / test / deploy 日志 0.32s 一行快速滚动；时钟 23:59
//   S3 (20-30s) `deployed ✓`；时钟跳 00:00；Clawd 释然（闭眼笑）；字幕「赶上了。」
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140)；右上像素时钟卡 72×46 @ (552,58)。
// Clawd 40×17 (4×4 眼睛；determined 收窄为 4×2 + 眉线，relieved 闭眼笑)。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, STATUS_Y, LINE_Y, CONTENT, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E07_determination_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — cat task.txt',
  S2: 'clawd@dsh:~ — ship.sh',
  S3: 'clawd@dsh:~ — ship.sh --prod',
};
const SUB_LINES = ['在天亮之前，做完。', '（跑起来了。）', '赶上了。'];
const SUB_WINDOWS = [{ start: 2.6, end: 8.8 }, { start: 12.4, end: 17.8 }, { start: 26.2, end: 29.2 }];

// --- Pixel clock card (top-right) -----------------------------------------
const CLOCK = { x: 552, y: 58, w: 72, h: 46 };
const CLOCK_FLIP_MS = 0.12;
const CLOCK_TIMES = [
  { at: 0, text: '23:58' },
  { at: 14.0, text: '23:59' },
  { at: 24.0, text: '00:00' },
];

function clockText(t) {
  let out = CLOCK_TIMES[0];
  for (const c of CLOCK_TIMES) if (t >= c.at) out = c;
  return out;
}

function drawClock(ctx, t) {
  const { x, y, w, h } = CLOCK;
  const cur = clockText(t);
  const flip = t >= cur.at && t - cur.at < CLOCK_FLIP_MS;
  px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.14)');
  px(ctx, x, y, w, h, C.termBg);
  px(ctx, x, y, w, 2, C.termBd);
  px(ctx, x, y + h - 2, w, 2, C.termBd);
  px(ctx, x, y, 2, h, C.termBd);
  px(ctx, x + w - 2, y, 2, h, C.termBd);
  px(ctx, x + 2, y + 2, w - 4, 2, C.amber); // amber accent under the top border
  S.txt(ctx, x + w / 2, y + 9, cur.text, flip ? C.white : C.amber, 14, 'center');
  S.txt(ctx, x + w / 2, y + 30, 'JST', C.dim, 10, 'center');
}

// --- S1: the task ----------------------------------------------------------
const S1_LINES = [
  { y: LINE_Y[0], start: 0.9, charMs: 90, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'cat task.txt', color: C.text }] },
  { y: LINE_Y[1], start: 2.2, charMs: 70, cursor: false, parts: [{ text: 'finish before sunrise', color: C.amber }] },
  { y: LINE_Y[2], start: 3.8, charMs: 70, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'date', color: C.text }] },
  { y: LINE_Y[3], start: 4.3, charMs: 55, cursor: false, parts: [{ text: 'Fri Oct 23 23:58:07 JST 2026', color: C.dim }] },
];
const S1_STATUS = '[DSH] deadline 06:12 · left 379 min';
const DETERMINED_AT = 2.2;

// --- S2: the long scroll ---------------------------------------------------
// 34 log lines, one new line every 0.32s: the terminal reads as a fast scroll.
const SCROLL_START = 10.0;
const SCROLL_STEP = 0.32;
const SCROLL_ROWS = 6;
const LOG_LINES = [
  { text: '$ ./ship.sh --prod --no-prompt', color: C.text },
  { text: '[build] bundling 214 modules', color: C.dim },
  { text: '[build] tree-shake -38% · 519 ms', color: C.dim },
  { text: '[build] dist/ 1.2 MB · gzip 214 kB', color: C.dim },
  { text: '[build] source maps off (prod)', color: C.dim },
  { text: '[test] running 42 specs ...', color: C.dim },
  { text: '[test] 42 passing (0 failing)', color: C.green },
  { text: '[test] coverage 94% · +3 vs main', color: C.green },
  { text: '[test] slowest: render.test.js 212 ms', color: C.dim },
  { text: '[deploy] target prod-sfo-1', color: C.blue },
  { text: '[deploy] uploading 18 files ...', color: C.blue },
  { text: '[deploy] health check 200 OK', color: C.green },
  { text: '[deploy] cache warm 96%', color: C.dim },
  { text: '[deploy] rolling 3 pods ... 1/3', color: C.blue },
  { text: '[deploy] rolling 3 pods ... 2/3', color: C.blue },
  { text: '[deploy] rolling 3 pods ... 3/3', color: C.blue },
  { text: '[smoke] GET / 200 · 41 ms', color: C.green },
  { text: '[smoke] POST /api/sum 201 · 63 ms', color: C.green },
  { text: '[smoke] 12/12 checks green', color: C.green },
  { text: '[deploy] traffic 100% -> v1.4.2', color: C.blue },
  { text: '[deploy] done in 58.4s', color: C.green },
  { text: '$ git log --oneline -1', color: C.text },
  { text: 'b7d1e02  clawd: ship it before sun', color: C.dim },
  { text: '[lint] 0 errors · 0 warnings', color: C.green },
  { text: '[doc] changelog updated', color: C.dim },
  { text: '[ci] artifact archived', color: C.dim },
  { text: '[ops] dashboard refreshed', color: C.dim },
  { text: '[ops] alerts silenced until 07:00', color: C.dim },
  { text: '$ date', color: C.text },
  { text: 'Fri Oct 23 23:59:41 JST 2026', color: C.dim },
  { text: '[clock] ticking · 19 min left', color: C.amber },
  { text: '[deploy] verify prod ...', color: C.blue },
  { text: '[deploy] verify prod ... ok', color: C.green },
  { text: '[clawd] one more check', color: C.purple },
];
const S2_STATUS = '[DSH] build → test → deploy · t-3:56';
const S2_LOG_WIDTH = 0; // filled below (longest line) for layout boxes

// --- S3: done at 00:00 -----------------------------------------------------
const S3_LINES = [
  { y: LINE_Y[0], start: 20.8, charMs: 70, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: './ship.sh --prod', color: C.text }] },
  { y: LINE_Y[1], start: 22.2, charMs: 55, cursor: false, parts: [{ text: 'deployed ', color: C.green }, { text: '✓', color: C.green }] },
  { y: LINE_Y[2], start: 23.0, charMs: 55, cursor: false, parts: [{ text: 'Done in 58.4s · v1.4.2 live', color: C.dim }] },
  { y: LINE_Y[3], start: 24.8, charMs: 70, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'date', color: C.text }] },
  { y: LINE_Y[4], start: 25.3, charMs: 55, cursor: false, parts: [{ text: 'Sat Oct 24 00:00:03 JST 2026', color: C.amber }] },
];
const S3_STATUS = '[DSH] sunrise in 5h 41m · shipped';
const RELIEVED_AT = 24.0;

const CLAWD_BOX = [40, 242, 44, 32];
const CLAWD_X = S.CLAWD_ROOM.x;
const CLAWD_Y = S.CLAWD_ROOM.y;

// --- Clawd: determined / relieved on the shared 40×17 sprite --------------
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  const dx = opts.dx || 0;
  const dy = opts.dy || 0;
  if (mood !== 'determined' && mood !== 'relieved') {
    S.art.drawClawd(ctx, x + dx, y + dy, t, mood, warmMix);
    return;
  }
  const bob = opts.noBob ? 0 : (Math.sin(t * 2.2) > 0.45 ? -1 : 0);
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

  if (mood === 'determined') {
    for (const ex of [10, 26]) {
      px(ctx, bx + ex, by + 4, 4, 1, C.clawdEye);  // brow
      px(ctx, bx + ex, by + 7, 4, 2, C.clawdEye);  // narrowed 4×2 eye
    }
    px(ctx, bx + 18, by + 13, 4, 1, C.clawdEye);   // straight mouth
  } else {
    // Relieved: closed happy eyes (^ ^) and a small smile.
    for (const ex of [10, 26]) {
      px(ctx, bx + ex, by + 8, 4, 1, C.clawdEye);
      px(ctx, bx + ex + 1, by + 7, 2, 1, C.clawdEye);
    }
    px(ctx, bx + 16, by + 12, 2, 1, C.clawdEye);
    px(ctx, bx + 18, by + 13, 4, 1, C.clawdEye);
    px(ctx, bx + 22, by + 12, 2, 1, C.clawdEye);
    px(ctx, bx + 5, by + 8, 3, 2, C.pink);
    px(ctx, bx + 32, by + 8, 3, 2, C.pink);
  }

  const step = mood === 'relieved' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, bx + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, bx + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Scroll model (shared by the painter and the layout) -------------------
function scrollIndex(t) {
  if (t < SCROLL_START) return 0;
  return Math.min(LOG_LINES.length - SCROLL_ROWS, Math.floor((t - SCROLL_START) / SCROLL_STEP));
}

function scrollClicks() {
  const out = [];
  const maxIdx = LOG_LINES.length - SCROLL_ROWS;
  for (let i = 0; i <= maxIdx; i++) out.push(SCROLL_START + i * SCROLL_STEP);
  return out;
}

// --- Scene painters --------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.amber);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 6.2) S.drawStatus(ctx, S1_STATUS, C.amber);
  const det = t >= DETERMINED_AT;
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, det ? 'determined' : 'calm', 0, det ? { dy: -1 } : {});
  drawClock(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.blue);
  const idx = scrollIndex(t);
  for (let i = 0; i < SCROLL_ROWS; i++) {
    const line = LOG_LINES[idx + i];
    S.txt(ctx, TEXT_X, LINE_Y[i], line.text, line.color, 10);
  }
  S.drawStatus(ctx, S2_STATUS, C.blue);
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, 'determined', 0, { dy: -1, noBob: true });
  drawClock(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 26.9) S.drawStatus(ctx, S3_STATUS, C.green);
  const rel = t >= RELIEVED_AT;
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, rel ? 'relieved' : 'determined', 0, rel ? { dy: -1 } : {});
  drawClock(ctx, t);
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

// --- Keyboard clicks: per typed char in S1/S3, one per scrolled log line --
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...scrollClicks(),
    ...S.lineClicks(S3_LINES),
  ]);
}

function typingSchedule(lines, limit) {
  return lines.map((line, i) => ({
    text: S.lineText(line),
    start: line.start,
    charMs: line.charMs || S.TYPE_CHAR_MS,
    limit,
    strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.6),
  ...typingSchedule(S3_LINES, 29.5),
];

// --- Layout groups (0px tolerance, per frame) ------------------------------
const LOG_BOX_W = Math.ceil(Math.max(...LOG_LINES.map((l) => S.textWidth(l.text, 10))));

function clockLayout(t) {
  const cur = clockText(t);
  return [
    { name: 'clock_digits', box: S.textBox(CLOCK.x + CLOCK.w / 2, CLOCK.y + 9, cur.text, 14, 'center') },
    { name: 'clock_label', box: S.textBox(CLOCK.x + CLOCK.w / 2, CLOCK.y + 30, 'JST', 10, 'center') },
  ];
}

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let layout;
  if (t < 10) {
    layout = S.baseLayout({ ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS });
  } else if (t < 20) {
    layout = S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: [], status: S2_STATUS,
      extraGroups: {
        content: [
          ...LINE_Y.map((y, i) => ({ name: `log_${i + 1}`, box: [TEXT_X, y, LOG_BOX_W, 13] })),
          { name: 'status', box: S.textBox(TEXT_X, STATUS_Y, S2_STATUS, 10) },
        ],
        clock: clockLayout(t),
      },
      extraBounds: { clock: CLOCK },
    });
  } else {
    layout = S.baseLayout({ ...common, scene: 3, title: TITLES.S3, lines: S3_LINES, status: S3_STATUS });
  }
  if (t < 10 || t >= 20) {
    layout.groups.clock = clockLayout(t);
    layout.bounds.clock = CLOCK;
  }
  layout.groups.foreground = S.foregroundLayout({
    terminal: true, clawd: false, her: false,
    extra: [
      { name: 'clawd', box: CLAWD_BOX },
      { name: 'clock_card', box: [CLOCK.x, CLOCK.y, CLOCK.w, CLOCK.h] },
    ],
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
  S1_LINES, S1_STATUS, S2_STATUS, S3_LINES, S3_STATUS,
  CLOCK, CLOCK_TIMES, LOG_LINES, SCROLL_START, SCROLL_STEP, SCROLL_ROWS,
  DETERMINED_AT, RELIEVED_AT, CLAWD_BOX, clockText, scrollIndex, scrollClicks, drawClock,
  CHECK_TITLE: 'E07 目标 (determination) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'finish before sunrise', size: 10, color: C.amber },
    { text: '[deploy] rolling 3 pods ... 3/3', size: 10, color: C.blue },
    { text: 'Sat Oct 24 00:00:03 JST 2026', size: 10, color: C.amber },
    { text: '赶上了。', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps, drawClawdEp,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
