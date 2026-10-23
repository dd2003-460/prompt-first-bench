#!/usr/bin/env node
'use strict';
// E06 羞耻 (shame) — 30s, 1800 frames @ 60fps, 1280×720.
// 事实源 (episodes.md, batch-6 任务书): 发现自己的输出被 human 改了，diff 里全是红色的自己。
//   S1 (0-10s)  检查自己的代码: `$ cat my_output.js` + 4 行代码；Clawd proud（嘴角微扬）；字幕「我的输出，完美。」
//   S2 (10-20s) diff 出现: `$ git diff my_output.js` → 3 行红色 (-) 逐行出现，再 3 行绿色 (+) 逐行出现；
//               Clawd proud → shame（眼睛半闭 + 嘴角下压 + 羞红）；字幕 15s「这不是我写的。」/ 18s「红色的…全是我。」
//   S3 (20-30s) 沉默: `$ git log --oneline -1` → `a1b2c3d  her: "fixed it"`；`$ git show --stat` →
//               `1 file changed, 3 insertions(+), 3 deletions(-)`；Her 出现在窗边；Clawd 头低 2px；
//               便签「羞耻。」；字幕 26s「她改了我的代码。」/ 29s「（沉默）」
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// 键盘音: 每字符 1 次 click（charMs ≥ 50ms = 帧量化 + 0.035s 去重下限）。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E06_shame_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — cat my_output.js',
  S2: 'clawd@dsh:~ — git diff',
  S3: 'clawd@dsh:~ — git log',
};
const SUB_LINES = ['我的输出，完美。', '这不是我写的。', '红色的…全是我。', '她改了我的代码。', '（沉默）'];
const SUB_WINDOWS = [
  { start: 2.2, end: 8.6 },
  { start: 15.0, end: 17.8 },
  { start: 18.0, end: 19.9 },
  { start: 26.0, end: 28.4 },
  { start: 29.0, end: 29.9 },
];

// --- S1: my own output, perfect -------------------------------------------
const S1_LINES = [
  {
    y: S.LINE_Y[0], start: 0.9, charMs: 80,
    parts: [{ text: '$ ', color: C.green }, { text: 'cat my_output.js', color: C.text }],
  },
  {
    y: S.LINE_Y[1], start: 2.6, charMs: 55,
    parts: [
      { text: 'function ', color: C.purple },
      { text: 'solve', color: C.blue },
      { text: '(input) {', color: C.text },
    ],
  },
  {
    y: S.LINE_Y[2], start: 4.1, charMs: 55,
    parts: [
      { text: '  ', color: C.text },
      { text: 'return ', color: C.purple },
      { text: 'transform', color: C.blue },
      { text: '(input);', color: C.text },
    ],
  },
  { y: S.LINE_Y[3], start: 5.8, charMs: 80, parts: [{ text: '}', color: C.text }] },
  {
    y: S.LINE_Y[4], start: 6.4, charMs: 55,
    parts: [
      { text: 'module.exports', color: C.purple },
      { text: ' = ', color: C.text },
      { text: 'solve', color: C.blue },
      { text: ';', color: C.text },
    ],
  },
];
const S1_STATUS = '[DSH] my_output.js · 4 lines · mine';
const S1_STATUS_AT = 8.0;

// --- S2: the diff — 7 rows @20px (y 168..288), red deletions then green additions
const DIFF_Y = [168, 188, 208, 228, 248, 268, 288];
const S2_LINES = [
  {
    y: DIFF_Y[0], start: 10.7, charMs: 60,
    parts: [{ text: '$ ', color: C.green }, { text: 'git diff my_output.js', color: C.text }],
  },
  {
    y: DIFF_Y[1], start: 12.3, charMs: 55,
    parts: [{ text: '-function solve(input) {', color: C.red }],
  },
  {
    y: DIFF_Y[2], start: 13.8, charMs: 55,
    parts: [{ text: '-  return transform(input);', color: C.red }],
  },
  { y: DIFF_Y[3], start: 15.5, charMs: 80, parts: [{ text: '-}', color: C.red }] },
  {
    y: DIFF_Y[4], start: 16.0, charMs: 55,
    parts: [{ text: '+function solve(input) {', color: C.green }],
  },
  {
    y: DIFF_Y[5], start: 17.5, charMs: 55,
    parts: [{ text: '+  return hack(input, "cheat");', color: C.green }],
  },
  { y: DIFF_Y[6], start: 19.4, charMs: 80, parts: [{ text: '+}', color: C.green }] },
];
const S2_STATUS = '[DSH] diff: 3 insertions(+), 3 deletions(-)';
const S2_STATUS_AT = 19.7;
const RED_ROWS = [DIFF_Y[1], DIFF_Y[2], DIFF_Y[3]];
const GREEN_ROWS = [DIFF_Y[4], DIFF_Y[5], DIFF_Y[6]];
// 第一行红色 (-) 打完的时刻 → Clawd 从 proud 转 shame
const SHAME_AT = 13.6;

// --- S3: who did it -------------------------------------------------------
const S3_LINES = [
  {
    y: S.LINE_Y[0], start: 20.6, charMs: 50,
    parts: [{ text: '$ ', color: C.green }, { text: 'git log --oneline -1 my_output.js', color: C.text }],
  },
  {
    y: S.LINE_Y[1], start: 22.6, charMs: 60,
    parts: [
      { text: 'a1b2c3d', color: C.amber },
      { text: '  ', color: C.dim },
      { text: 'her', color: C.pink },
      { text: ': ', color: C.dim },
      { text: '"fixed it"', color: C.text },
    ],
  },
  {
    y: S.LINE_Y[2], start: 24.2, charMs: 60,
    parts: [{ text: '$ ', color: C.green }, { text: 'git show a1b2c3d --stat', color: C.text }],
  },
  {
    y: S.LINE_Y[3], start: 25.9, charMs: 50,
    parts: [
      { text: ' 1 file changed, ', color: C.dim },
      { text: '3 insertions(+)', color: C.green },
      { text: ', ', color: C.dim },
      { text: '3 deletions(-)', color: C.red },
    ],
  },
];
const S3_STATUS = '[DSH] commit a1b2c3d · author: her';
const S3_STATUS_AT = 28.6;
const HER_AT = 22.6;       // `her: "fixed it"` 落地 → 她出现在窗边
const HEAD_DOWN_AT = 22.6; // 头低 2px
// 便签出现在最后一行 stat 打完之后（28.25s），避开逐字 click 的 0.05s 网格
const NOTE_AT = 28.4;
const NOTE_TITLE = '羞耻。';
const NOTE_SUB = 'Clawd · E06';

const CLAWD_BOX = [S.CLAWD_ROOM.x, 244, 40, 32]; // bob -1 与头低 +2 都在盒内

// --- Clawd: proud (嘴角微扬) / shame (眼睛半闭 + 嘴角下压 + 羞红) ----------
// calm·thinking·smile·warm 委托给 companion v1.1 原始 sprite（逐像素一致）。
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  if (mood !== 'proud' && mood !== 'shame') {
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

  if (mood === 'proud') {
    // 正常睁眼 (4×4 + 1×1 高光) + 嘴角微扬（比 smile 弧度更小的 6px  mouth）
    px(ctx, x + 10, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 26, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 11, by + 7, 1, 1, C.white);
    px(ctx, x + 27, by + 7, 1, 1, C.white);
    px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);
    px(ctx, x + 16, by + 12, 1, 1, C.clawdEye);
    px(ctx, x + 23, by + 12, 1, 1, C.clawdEye);
  } else {
    // shame: 眼睛完全半闭 (4×2 下移一行、无高光) + 嘴角下压 + 脸颊羞红
    px(ctx, x + 10, by + 8, 4, 2, C.clawdEye);
    px(ctx, x + 26, by + 8, 4, 2, C.clawdEye);
    px(ctx, x + 16, by + 13, 2, 1, C.clawdEye);
    px(ctx, x + 18, by + 12, 4, 1, C.clawdEye);
    px(ctx, x + 22, by + 13, 2, 1, C.clawdEye);
    px(ctx, x + 5, by + 8, 3, 2, C.herDressHem);
    px(ctx, x + 32, by + 8, 3, 2, C.herDressHem);
  }

  const step = Math.sin(t * 3.0) > 0.6 ? 1 : 0;
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Scene painters -------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'proud', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.red);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= SHAME_AT ? 'shame' : 'proud', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.dim);
  if (t >= HER_AT) S.drawHer(ctx, S.HER_ROOM.x, S.HER_ROOM.y, t, 'stand');
  if (t >= NOTE_AT) S.drawStickyNote(ctx, NOTE_TITLE, NOTE_SUB, t, S.easeOut((t - NOTE_AT) / 0.3));
  const dy = t >= HEAD_DOWN_AT ? Math.round(2 * S.easeOut((t - HEAD_DOWN_AT) / 0.6)) : 0;
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'shame', 0, { dy });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { start: 0, draw: drawS1 },
  { start: 10, draw: drawS2 },
  { start: 20, draw: drawS3 },
];

function renderAt(ctx, t) { S.renderScenes(ctx, t, SCENES); }

// --- Keyboard clicks: one per typed character -----------------------------
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
    NOTE_AT,
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
  ...typingSchedule(S1_LINES, 9.5),
  ...typingSchedule(S2_LINES, 19.6),
  ...typingSchedule(S3_LINES, 29.5),
];

// --- Layout groups (0px tolerance, per frame) -----------------------------
function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let layout;
  if (t < 10) {
    layout = S.baseLayout({
      ...common, scene: 1, title: TITLES.S1, lines: S1_LINES,
      status: t >= S1_STATUS_AT ? S1_STATUS : null,
    });
  } else if (t < 20) {
    layout = S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: S2_LINES,
      status: t >= S2_STATUS_AT ? S2_STATUS : null,
    });
  } else {
    layout = S.baseLayout({
      ...common, scene: 3, title: TITLES.S3, lines: S3_LINES,
      status: t >= S3_STATUS_AT ? S3_STATUS : null,
      note: t >= NOTE_AT ? true : undefined, noteTitle: NOTE_TITLE, noteSub: NOTE_SUB,
    });
  }
  layout.groups.foreground = S.foregroundLayout({
    terminal: true, clawd: false,
    her: t >= 20 && t >= HER_AT ? true : false,
    note: t >= 20 && t >= NOTE_AT ? true : undefined,
    extra: [{ name: 'clawd', box: CLAWD_BOX }],
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
  S1_LINES, S1_STATUS, S1_STATUS_AT,
  S2_LINES, S2_STATUS, S2_STATUS_AT, DIFF_Y, RED_ROWS, GREEN_ROWS, SHAME_AT,
  S3_LINES, S3_STATUS, S3_STATUS_AT, HER_AT, HEAD_DOWN_AT,
  NOTE_AT, NOTE_TITLE, NOTE_SUB, CLAWD_BOX,
  CHECK_TITLE: 'E06 羞耻 (shame) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'function solve(input) {', size: 10, color: C.purple },
    { text: '-  return transform(input);', size: 10, color: C.red },
    { text: '+  return hack(input, "cheat");', size: 10, color: C.green },
    { text: ' 1 file changed, 3 insertions(+), 3 deletions(-)', size: 10, color: C.dim },
    { text: '红色的…全是我。', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  renderAt,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
