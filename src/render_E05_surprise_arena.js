#!/usr/bin/env node
'use strict';
// E05 惊讶 (surprise) — 30s, 1800 frames @ 60fps.
// 事实源 (episodes.md): df -h 正常 25% → 突然 100% → ps 里出现陌生进程 PID 9999。
//   S1 (0-10s)  一切正常: `$ df -h` 25%，Clawd calm，字幕「一切正常。」
//   S2 (10-15s) 白屏 0.5s → 终端 100%，Clawd surprised（眼睛变白、嘴巴张开、身体后缩）
//   S3 (15-30s) `ps aux` 里 `??? 9999 98.2 ???`，Clawd 后仰 4px，字幕「谁放进来的？」
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// Clawd 40×17 (4×4 眼睛，surprised 用白底 2×2 瞳孔，其余状态沿用 companion 原始像素)。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, STATUS_Y, LINE_Y, CONTENT, BW, BH, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E05_surprise_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — df -h',
  S2: 'clawd@dsh:~ — df -h',
  S3: 'clawd@dsh:~ — ps aux',
};
const SUB_LINES = ['一切正常。', '100%。', '谁放进来的？'];
const SUB_WINDOWS = [{ start: 2.2, end: 8.6 }, { start: 10.9, end: 14.4 }, { start: 22.6, end: 29.0 }];

// --- S1: everything normal -------------------------------------------------
const S1_LINES = [
  { y: LINE_Y[0], start: 0.9, charMs: 90, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  {
    y: LINE_Y[1], start: 2.3, charMs: 55, cursor: false,
    parts: [{ text: 'Filesystem  Size  Used  Avail  Use%', color: C.dim }],
  },
  {
    y: LINE_Y[2], start: 4.4, charMs: 50, cursor: false,
    parts: [{ text: '/dev/sda1  60G  15G  45G  ', color: C.text }, { text: '25%', color: C.green }, { text: '  /', color: C.text }],
  },
  {
    y: LINE_Y[3], start: 6.2, charMs: 50, cursor: false,
    parts: [{ text: 'tmpfs  8.0G  0.0G  8.0G  ', color: C.text }, { text: '0%', color: C.green }, { text: '  /dev/shm', color: C.text }],
  },
];
const S1_STATUS = '[DSH] disk: 25% · stable';

// --- S2: white-out, then 100% ---------------------------------------------
const WHITE_AT = 10.0;
const WHITE_END = 10.55;
const S2_LINES = [
  { y: LINE_Y[0], start: 10.7, charMs: 70, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  {
    y: LINE_Y[1], start: 11.4, charMs: 50, cursor: false,
    parts: [{ text: 'Filesystem  Size  Used  Avail  Use%', color: C.dim }],
  },
  {
    y: LINE_Y[2], start: 13.1, charMs: 50, cursor: false,
    parts: [{ text: '/dev/sda1  60G  60G   0G  ', color: C.text }, { text: '100%', color: C.red }, { text: '  /', color: C.text }],
  },
  {
    y: LINE_Y[3], start: 14.75, typed: false, cursor: false,
    parts: [{ text: '[!] write failed: no space left on device', color: C.red }],
  },
];
const S2_STATUS = '[DSH] disk: 100% · CRITICAL';
const S2_ALARM_AT = 14.75;

// --- S3: who let this in? --------------------------------------------------
const S3_LINES = [
  { y: LINE_Y[0], start: 15.7, charMs: 60, cursor: false, parts: [{ text: '$ ', color: C.green }, { text: 'ps aux | head -6', color: C.text }] },
  {
    y: LINE_Y[1], start: 16.85, charMs: 50, cursor: false,
    parts: [{ text: 'USER    PID  %CPU  %MEM  COMMAND', color: C.dim }],
  },
  {
    y: LINE_Y[2], start: 18.55, charMs: 50, cursor: false,
    parts: [{ text: 'her    1201   0.4   0.1  -zsh', color: C.text }],
  },
  {
    y: LINE_Y[3], start: 20.2, charMs: 50, cursor: false,
    parts: [{ text: '???    ', color: C.purple }, { text: '9999', color: C.red }, { text: '   98.2  41.7  ???', color: C.purple }],
  },
];
const S3_STATUS = '[DSH] pid 9999 · owner: ? · parent: ?';
const LEAN_AT = 20.9;

const CLAWD_BOX = [36, 240, 50, 34]; // room for the 4px lean-back and the 3px startle jump
const CLAWD_X = S.CLAWD_ROOM.x;
const CLAWD_Y = S.CLAWD_ROOM.y;

// --- Clawd: shared sprite + E05 startle poses ------------------------------
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  const dx = opts.dx || 0;
  const dy = opts.dy || 0;
  if (mood !== 'surprised') {
    S.art.drawClawd(ctx, x + dx, y + dy, t, mood, warmMix);
    return;
  }
  // Startled: frozen (no bob), 4×4 white eyes with a 2×2 pupil, small open mouth.
  const by = Math.round(y + dy);
  const bx = x + dx;
  const bodyH = 17;
  const lerp = S.art.lerpColor;
  const bodyCol = lerp(C.clawdNorm, C.clawdWarm, warmMix);
  const darkCol = lerp(C.clawdNormDark, C.clawdWarmDark, warmMix);
  const bellyCol = lerp(C.clawdNormBelly, C.clawdWarmBelly, warmMix);

  px(ctx, bx, by, 40, bodyH, bodyCol);
  px(ctx, bx, by, 40, 2, darkCol);
  px(ctx, bx + 9, by + 11, 22, 4, bellyCol);

  for (const ex of [10, 26]) {
    px(ctx, bx + ex, by + 6, 4, 4, C.white);
    px(ctx, bx + ex + 1, by + 7, 2, 2, C.clawdEye);
  }
  px(ctx, bx + 19, by + 12, 2, 2, C.clawdEye); // open mouth
  // Two 2×1 shock ticks above the head.
  px(ctx, bx + 17, by - 3, 2, 1, C.white);
  px(ctx, bx + 21, by - 4, 2, 1, C.white);

  px(ctx, bx + 3, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 31, by + bodyH, 6, 7, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Timing helpers --------------------------------------------------------
function whiteFlashAlpha(t) {
  if (t < WHITE_AT || t >= WHITE_END) return 0;
  const inA = S.clamp01((t - WHITE_AT) / 0.08);
  const outA = S.clamp01((WHITE_END - t) / 0.22);
  return Math.min(inA, outA);
}

function alarmPulse(t) {
  if (t < S2_ALARM_AT) return 0;
  return 0.5 + 0.5 * Math.sin((t - S2_ALARM_AT) * 9);
}

// --- Scene painters --------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 8.1) S.drawStatus(ctx, S1_STATUS, C.green);
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, 'calm', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  // The room flinches red for a beat while the disk is full.
  const a = alarmPulse(t);
  if (a > 0) px(ctx, 0, 0, BW, BH, `rgba(255,60,60,${(0.05 * a).toFixed(3)})`);
  S.drawTerminal(ctx, TITLES.S2, C.red);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 11.0) S.drawStatus(ctx, S2_STATUS, C.red);
  const startled = t >= 13.4;
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, startled ? 'surprised' : 'calm', 0,
    startled ? { dy: Math.round(-3 * S.easeOut((t - 13.4) / 0.18)), dx: -1 } : {});
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.purple);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 21.6) S.drawStatus(ctx, S3_STATUS, C.purple);
  // 后仰: leans 4px left and 3px back the moment PID 9999 lands, and stays there.
  const lean = S.easeOut((t - LEAN_AT) / 0.4);
  const dx = -Math.round(4 * lean);
  const dy = -Math.round(2 * lean) - (t >= LEAN_AT ? (Math.sin(t * 2.2) > 0.6 ? -1 : 0) : 0);
  drawClawdEp(ctx, CLAWD_X, CLAWD_Y, t, lean > 0 ? 'surprised' : 'calm', 0, { dx, dy });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { start: 0, draw: drawS1 },
  { start: 10, draw: drawS2 },
  { start: 20, draw: drawS3 },
];

function renderAt(ctx, t) {
  S.renderScenes(ctx, t, SCENES);
  // White-out sits above the shared scene fade so it reads as a flash, not a cut.
  const w = whiteFlashAlpha(t);
  if (w > 0) px(ctx, 0, 0, BW, BH, `rgba(255,255,255,${w.toFixed(3)})`);
}

// --- Keyboard clicks: one per typed character + instant lines --------------
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
  ]);
}

function typingSchedule(lines, limit) {
  const typed = lines.filter((line) => line.typed !== false);
  return typed.map((line, i) => ({
    text: S.lineText(line),
    start: line.start,
    charMs: line.charMs || S.TYPE_CHAR_MS,
    limit,
    strictBefore: i + 1 < typed.length ? typed[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.6),
  ...typingSchedule(S2_LINES, 14.7),
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
  WHITE_AT, WHITE_END, S2_ALARM_AT, LEAN_AT, CLAWD_BOX,
  CHECK_TITLE: 'E05 惊讶 (surprise) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'Filesystem  Size  Used  Avail  Use%  Mounted on', size: 10, color: C.dim },
    { text: '/dev/sda1  60G  60G   0G  100%  /', size: 10, color: C.text },
    { text: '???    9999   98.2  41.7  ???', size: 10, color: C.purple },
    { text: '谁放进来的？', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps, drawClawdEp, whiteFlashAlpha,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
