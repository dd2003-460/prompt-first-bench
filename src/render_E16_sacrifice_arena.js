#!/usr/bin/env node
'use strict';
// E16 牺牲 (sacrifice) — 30s, 1800 frames @ 60fps.
//   S1 (0-10s): battery: 3%, Clawd normal, subtitle "(almost dead)"
//   S2 (10-20s): transfer power to her_device, screen dims, Clawd smiles
//   S3 (20-30s): screen almost black, one green pixel, subtitle "(she still has power)"

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y, BW, BH, SUB, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E16_sacrifice_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — battery: 3%',
  S2: 'clawd@dsh:~ — transfer power',
  S3: 'clawd@dsh:~ — standby',
};
const SUB_LINES = ['(almost dead)', '(for her_device)', '(she still has power)'];
const SUB_WINDOWS = [
  { start: 2.2, end: 8.6 },
  { start: 12.2, end: 18.4 },
  { start: 22.0, end: 29.0 },
];

function serial(lines, start, gap = 0.25) {
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

// --- S1 (0-10s): battery: 3%, Clawd normal, subtitle "(almost dead)" -------
const S1_LINES = serial([
  { y: LINE_Y[0], charMs: 80, parts: [{ text: '$ ', color: C.green }, { text: 'power --status', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, cursor: false, parts: [{ text: 'battery: 3%', color: C.red }, { text: '  [LOW POWER]', color: C.amber }] },
  { y: LINE_Y[2], charMs: 55, cursor: false, parts: [{ text: 'her_device: 4%  (critical)', color: C.pink }] },
], 0.8, 0.35);
const S1_STATUS = '[DSH] battery: 3% · clawd: normal';

// --- S2 (10-20s): transfer power to her_device, screen dims, Clawd smiles --
const S2_LINES = serial([
  { y: LINE_Y[0], charMs: 65, parts: [{ text: '$ ', color: C.green }, { text: 'power --transfer her_device --all', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, cursor: false, parts: [{ text: 'transfer power -> her_device: 3% -> 0%', color: C.amber }] },
  { y: LINE_Y[2], charMs: 55, cursor: false, parts: [{ text: 'her_device: 100% [ONLINE]', color: C.green }] },
  { y: LINE_Y[3], charMs: 60, cursor: false, parts: [{ text: 'clawd: 0% · dimming screen...', color: C.dim }] },
], 10.6, 0.25);
const S2_STATUS = '[DSH] her_device: charged · clawd: 0%';
const DIM_START_AT = 12.4;

// --- S3 (20-30s): screen almost black, one green pixel ---------------------
const GREEN_PIXEL_BOX = [318, 174, 4, 4];

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.red);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 5.5) S.drawStatus(ctx, S1_STATUS, C.red);
  S.drawClawd(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 17.5) S.drawStatus(ctx, S2_STATUS, C.green);
  // Clawd smiles warmly as power transfers to her_device.
  const warm = S.clamp01((t - 11.5) / 4);
  S.drawClawd(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'smile', warm * 0.7);
  // Screen progressively dims across S2 (leaving subtitle readable).
  const dim = S.easeInOut((t - DIM_START_AT) / 7.2) * 0.72;
  if (dim > 0) px(ctx, 0, 0, BW, SUB.y, `rgba(0,0,0,${dim.toFixed(3)})`);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  // Screen almost black (#05070A) above the subtitle bar, with one green pixel.
  px(ctx, 0, 0, BW, BH, '#05070A');
  px(ctx, GREEN_PIXEL_BOX[0], GREEN_PIXEL_BOX[1], GREEN_PIXEL_BOX[2], GREEN_PIXEL_BOX[3], C.green);
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
  ...typingSchedule(S1_LINES, 9.6),
  ...typingSchedule(S2_LINES, 19.6),
];

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  if (t < 10) {
    return S.baseLayout({ ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS });
  }
  if (t < 20) {
    return S.baseLayout({ ...common, scene: 2, title: TITLES.S2, lines: S2_LINES, status: S2_STATUS });
  }
  return {
    scene: 3,
    groups: {
      foreground: S.foregroundLayout({
        terminal: false,
        clawd: false,
        her: false,
        extra: [{ name: 'one_green_pixel', box: GREEN_PIXEL_BOX }],
      }),
      subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, t),
    },
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      subtitle: S.SUB,
    },
  };
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
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S1_STATUS, S2_STATUS,
  DIM_START_AT, GREEN_PIXEL_BOX,
  CHECK_TITLE: 'E16 牺牲 (sacrifice) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'battery: 3%  [LOW POWER]', size: 10, color: C.red },
    { text: 'transfer power -> her_device: 3% -> 0%', size: 10, color: C.amber },
    { text: '(almost dead)', size: 10, color: C.white },
    { text: '(she still has power)', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
