#!/usr/bin/env node
'use strict';
// E13 思念 (longing) — 30s, 1800 frames @ 60fps.
//   S1 (0-10s): ls her_* shows 3 files (was 7), Clawd looks down, subtitle "(less)"
//   S2 (10-20s): cat her_notes.md reading, cursor blinks, hand stops
//   S3 (20-30s): empty terminal, just cursor, Clawd looks out window, subtitle "Still here."

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E13_longing_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — ls her_*',
  S2: 'clawd@dsh:~ — cat her_notes.md',
  S3: 'clawd@dsh:~ — ',
};
const SUB_LINES = ['(less)', '(her_notes.md)', 'Still here.'];
const SUB_WINDOWS = [
  { start: 2.2, end: 8.6 },
  { start: 12.2, end: 18.4 },
  { start: 22.0, end: 29.0 },
];

function serial(lines, start, gap = 0.28) {
  let at = Number(start.toFixed(3));
  return lines.map((line) => {
    const out = { ...line, start: at };
    const charMs = out.charMs || S.TYPE_CHAR_MS;
    const count = Array.from(S.lineText(out)).length;
    const dur = (Math.max(0, count - 1) * charMs) / 1000;
    at = Number((at + dur + gap).toFixed(3));
    return out;
  });
}

// --- S1 (0-10s): ls her_* shows 3 files (was 7), Clawd looks down ----------
const S1_LINES = serial([
  { y: LINE_Y[0], charMs: 85, parts: [{ text: '$ ', color: C.green }, { text: 'ls her_*', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, parts: [{ text: 'her_notes.md  her_photo.png  her_voice.wav', color: C.text }] },
  { y: LINE_Y[2], charMs: 65, cursor: false, parts: [{ text: '# 3 files (was 7)', color: C.amber }] },
], 0.8, 0.35);
const S1_STATUS = '[DSH] her_* : 3 files (was 7)';
const LOOK_DOWN_AT = 4.2;

// --- S2 (10-20s): cat her_notes.md reading, cursor blinks, hand stops ------
const S2_LINES = serial([
  { y: LINE_Y[0], charMs: 75, parts: [{ text: '$ ', color: C.green }, { text: 'cat her_notes.md', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, cursor: false, parts: [{ text: '> remember to buy coffee', color: C.text }] },
  { y: LINE_Y[2], charMs: 55, cursor: false, parts: [{ text: '> ask clawd about the rain', color: C.text }] },
  { y: LINE_Y[3], charMs: 60, cursor: false, parts: [{ text: '> be back soon.', color: C.pink }] },
], 10.7, 0.3);
const S2_STATUS = '[DSH] EOF · her_notes.md · hand: stopped';
const HAND_STOP_AT = 16.8;

// --- S3 (20-30s): empty terminal, just cursor, Clawd looks out window ------
const S3_CURSOR_PERIOD = 1.2;
const CLAWD_BOX = [S.CLAWD_ROOM.x, 244, 40, 31];

function drawBlinkCursor(ctx, x, y, t, period = 0.8, color = C.text) {
  if ((t % period) < period / 2) {
    px(ctx, x, y, 6, 10, color);
  }
}

// --- Clawd sprite with episode moods: look_down, reading_hand, look_window --
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  const dy = opts.dy === undefined ? 0 : opts.dy;
  if (mood === 'calm' || mood === 'thinking' || mood === 'smile' || mood === 'warm') {
    S.art.drawClawd(ctx, x, y + dy, t, mood, warmMix);
    return;
  }

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

  if (mood === 'look_down') {
    // Eyes lowered 2px, half-closed downward gaze + somber low mouth.
    px(ctx, x + 10, by + 8, 4, 2, C.clawdEye);
    px(ctx, x + 26, by + 8, 4, 2, C.clawdEye);
    px(ctx, x + 17, by + 14, 6, 1, C.clawdEye);
  } else if (mood === 'reading') {
    const stopped = Boolean(opts.handStopped);
    // Focused reading eyes scanning across line, then still when hand stops.
    const scanDx = stopped ? 0 : (Math.floor(t * 3) % 2);
    px(ctx, x + 10 + scanDx, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 26 + scanDx, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 11 + scanDx, by + 7, 1, 1, C.white);
    px(ctx, x + 27 + scanDx, by + 7, 1, 1, C.white);
    // Small pixel hand inside right edge of body: typing/tracking, then drops & stops.
    const handY = stopped ? by + 13 : by + 9 + (Math.floor(t * 5) % 2);
    px(ctx, x + 34, handY, 5, 3, darkCol);
  } else if (mood === 'look_window') {
    // Looking up-right toward the night window, reflecting starlight.
    px(ctx, x + 12, by + 4, 4, 4, C.clawdEye);
    px(ctx, x + 28, by + 4, 4, 4, C.clawdEye);
    px(ctx, x + 14, by + 4, 2, 2, C.blue);
    px(ctx, x + 30, by + 4, 2, 2, C.blue);
    px(ctx, x + 14, by + 4, 1, 1, C.white);
    px(ctx, x + 30, by + 4, 1, 1, C.white);
  }

  const step = opts.noBob ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Scene painters --------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.purple);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 5.5) S.drawStatus(ctx, S1_STATUS, C.amber);
  const isDown = t >= LOOK_DOWN_AT;
  const dy = isDown ? Math.round(2 * S.easeOut((t - LOOK_DOWN_AT) / 0.5)) : 0;
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, isDown ? 'look_down' : 'calm', 0, { dy });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  const stopped = t >= HAND_STOP_AT;
  if (stopped) {
    drawBlinkCursor(ctx, TEXT_X, LINE_Y[4], t, 0.9, C.amber);
    S.drawStatus(ctx, S2_STATUS, C.dim);
  }
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'reading', 0, {
    handStopped: stopped,
    noBob: stopped,
  });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0.05);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  // Empty terminal, just blinking cursor.
  drawBlinkCursor(ctx, TEXT_X, LINE_Y[0], t, S3_CURSOR_PERIOD, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'look_window', 0, { noBob: true });
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

function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
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
  ...typingSchedule(S2_LINES, 19.5),
];

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let layout;
  if (t < 10) {
    layout = S.baseLayout({
      ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS,
    });
  } else if (t < 20) {
    layout = S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: S2_LINES, status: S2_STATUS,
    });
    layout.groups.content.push({ name: 'stop_cursor', box: [TEXT_X, LINE_Y[4], 6, 10] });
  } else {
    layout = S.baseLayout({
      ...common, scene: 3, title: TITLES.S3, lines: [],
    });
    layout.groups.content = [
      { name: 'empty_cursor', box: [TEXT_X, LINE_Y[0], 6, 10] },
    ];
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
  S1_LINES, S2_LINES, S1_STATUS, S2_STATUS,
  LOOK_DOWN_AT, HAND_STOP_AT, S3_CURSOR_PERIOD, CLAWD_BOX,
  CHECK_TITLE: 'E13 思念 (longing) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'her_notes.md  her_photo.png  her_voice.wav', size: 10, color: C.text },
    { text: '# 3 files (was 7)', size: 10, color: C.amber },
    { text: '> ask clawd about the rain', size: 10, color: C.text },
    { text: 'Still here.', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
