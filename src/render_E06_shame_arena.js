#!/usr/bin/env node
'use strict';
// E06 羞耻 (shame) — 30s, 1800 frames @ 60fps.
// 事实源 (episodes.md): 自己的输出被 human 改了 —— 先自豪，再看见 diff，最后沉默。
//   S1 (0-10s)  `$ cat my_output.js` 完美代码，Clawd proud（挺胸 + 高光 2×2 + 腮红）
//   S2 (10-20s) `git diff` 红 − / 绿 +，Clawd shame（眼睛下垂、腮红加重、汗点）
//   S3 (20-30s) `git log` 第一行 `her: fixed it`，Clawd 头低 2px，字幕「（沉默）」
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// Clawd 40×17 (4×4 眼睛；proud 用 2×2 高光，shame 用 4×2 下垂眼 + 4×2 腮红)。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, STATUS_Y, LINE_Y, CONTENT, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E06_shame_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — cat my_output.js',
  S2: 'clawd@dsh:~ — git diff',
  S3: 'clawd@dsh:~ — git log',
};
const SUB_LINES = ['这代码写得真好。', '……她改过了。', '（沉默）'];
const SUB_WINDOWS = [{ start: 2.6, end: 8.8 }, { start: 13.6, end: 18.6 }, { start: 24.0, end: 29.0 }];

// --- S1: my perfect little file -------------------------------------------
const S1_LINES = [
  { y: LINE_Y[0], start: 0.9, charMs: 90, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'cat my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 2.6, charMs: 55, cursor: false, parts: [{ text: '// sum two numbers', color: C.dim }] },
  { y: LINE_Y[2], start: 3.7, charMs: 55, cursor: false, parts: [{ text: 'const sum = (a, b) => a + b;', color: C.blue }] },
  { y: LINE_Y[3], start: 5.3, charMs: 55, cursor: false, parts: [{ text: 'export default sum;', color: C.purple }] },
  { y: LINE_Y[4], start: 6.4, charMs: 60, cursor: false, parts: [{ text: '// 12 lines · clean.', color: C.dim }] },
];
const S1_STATUS = '[DSH] lint: 0 errors · tests: 12/12';
const PROUD_AT = 6.4;

// --- S2: she rewrote it ----------------------------------------------------
const S2_LINES = [
  { y: LINE_Y[0], start: 10.8, charMs: 70, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'git diff my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 12.6, charMs: 55, cursor: false, parts: [{ text: '@@ -1,4 +1,9 @@', color: C.blue }] },
  { y: LINE_Y[2], start: 13.5, charMs: 55, cursor: false, parts: [{ text: '- const sum = (a, b) => a + b;', color: C.red }] },
  { y: LINE_Y[3], start: 15.2, charMs: 50, cursor: false, parts: [{ text: '+ const sum = (a = 0, b = 0) => a + b;', color: C.green }] },
  { y: LINE_Y[4], start: 17.3, charMs: 55, cursor: false, parts: [{ text: '+ // her: edge cases matter', color: C.green }] },
];
const S2_STATUS = '[DSH] diff: +5 -2 · author: her';
const SHAME_AT = 13.5;

// --- S3: her commit --------------------------------------------------------
const S3_LINES = [
  { y: LINE_Y[0], start: 20.8, charMs: 70, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'git log --oneline -3', color: C.text }] },
  {
    y: LINE_Y[1], start: 22.4, charMs: 55, cursor: false,
    parts: [{ text: 'c3f9a01  ', color: C.dim }, { text: 'her: fixed it', color: C.amber }],
  },
  { y: LINE_Y[2], start: 23.7, charMs: 50, cursor: false, parts: [{ text: 'b21e7c4  clawd: my_output', color: C.dim }] },
  { y: LINE_Y[3], start: 25.0, charMs: 50, cursor: false, parts: [{ text: 'a90d3f2  clawd: init', color: C.dim }] },
];
const S3_STATUS = '[DSH] last commit: her · 21:07';
const HEAD_DOWN_AT = 24.0;

const CLAWD_BOX = [40, 242, 44, 32]; // room for 1px lift (proud) and the 2px head drop (shame)
const CLAWD_X = S.CLAWD_ROOM.x;
const CLAWD_Y = S.CLAWD_ROOM.y;

// --- Clawd: proud / shame poses on the shared 40×17 sprite ----------------
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  const dx = opts.dx || 0;
  const dy = opts.dy || 0;
  if (mood !== 'proud' && mood !== 'shame') {
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

  if (mood === 'proud') {
    // Chest up: 4×4 eyes with a 2×2 highlight, wide smile, blush, one amber sparkle.
    for (const ex of [10, 26]) {
      px(ctx, bx + ex, by + 6, 4, 4, C.clawdEye);
      px(ctx, bx + ex + 1, by + 7, 2, 2, C.white);
    }
    px(ctx, bx + 16, by + 12, 2, 1, C.clawdEye);
    px(ctx, bx + 18, by + 13, 4, 1, C.clawdEye);
    px(ctx, bx + 22, by + 12, 2, 1, C.clawdEye);
    px(ctx, bx + 5, by + 8, 3, 2, C.pink);
    px(ctx, bx + 32, by + 8, 3, 2, C.pink);
    px(ctx, bx + 37, by + 1, 2, 2, C.amber);
    px(ctx, bx + 39, by + 3, 1, 1, C.amber);
  } else {
    // Eyes slide down 1px and narrow to 4×2; blush doubles; a sweat bead appears.
    for (const ex of [10, 26]) {
      px(ctx, bx + ex, by + 8, 4, 2, C.clawdEye);
      px(ctx, bx + ex + 1, by + 9, 2, 1, C.clawdEye);
    }
    // Downturned mouth: corners sit one row below the middle (mirror of the smile).
    px(ctx, bx + 16, by + 13, 2, 1, C.clawdEye);
    px(ctx, bx + 18, by + 12, 4, 1, C.clawdEye);
    px(ctx, bx + 22, by + 13, 2, 1, C.clawdEye);
    px(ctx, bx + 4, by + 8, 4, 2, C.pink);
    px(ctx, bx + 32, by + 8, 4, 2, C.pink);
    px(ctx, bx + 36, by + 6, 2, 3, C.blue); // sweat
  }

  const step = mood === 'shame' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, bx + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, bx + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Scene painters --------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.blue);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 7.4) S.drawStatus(ctx, S1_STATUS, C.green);
  const proud = t >= PROUD_AT;
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, proud ? 'proud' : 'calm', 0, proud ? { dy: -1 } : {});
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 18.8) S.drawStatus(ctx, S2_STATUS, C.dim);
  const shame = t >= SHAME_AT;
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, shame ? 'shame' : 'calm', 0, shame ? { dy: 1 } : {});
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 26.1) S.drawStatus(ctx, S3_STATUS, C.dim);
  const down = t >= HEAD_DOWN_AT;
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, 'shame', 0, { dy: down ? 2 : 1 });
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

// --- Keyboard clicks: one per typed character ------------------------------
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
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
  ...typingSchedule(S2_LINES, 19.6),
  ...typingSchedule(S3_LINES, 29.5),
];

// --- Layout groups (0px tolerance, per frame) ------------------------------
function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let layout;
  if (t < 10) {
    layout = S.baseLayout({ ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS });
  } else if (t < 20) {
    layout = S.baseLayout({ ...common, scene: 2, title: TITLES.S2, lines: S2_LINES, status: S2_STATUS });
  } else {
    layout = S.baseLayout({ ...common, scene: 3, title: TITLES.S3, lines: S3_LINES, status: S3_STATUS });
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
  S1_LINES, S1_STATUS, S2_LINES, S2_STATUS, S3_LINES, S3_STATUS,
  PROUD_AT, SHAME_AT, HEAD_DOWN_AT, CLAWD_BOX,
  CHECK_TITLE: 'E06 羞耻 (shame) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'const sum = (a, b) => a + b;', size: 10, color: C.blue },
    { text: '- const sum = (a, b) => a + b;', size: 10, color: C.red },
    { text: '+ const sum = (a = 0, b = 0) => a + b;', size: 10, color: C.green },
    { text: '（沉默）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps, drawClawdEp,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
