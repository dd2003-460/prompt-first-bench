#!/usr/bin/env node
'use strict';
// E14 嫉妒 (jealousy) — 30s, 1800 frames @ 60fps.
//   S1 (0-10s): tail -f chat.log normal, Clawd calm
//   S2 (10-20s): "nova-ai" appears in log, her messages nova, Clawd frowns
//   S3 (20-30s): her chatting with two AIs, Clawd turns away, subtitle "(she is busy too)"

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E14_jealousy_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — tail -f chat.log',
  S2: 'clawd@dsh:~ — tail -f chat.log',
  S3: 'clawd@dsh:~ — chat.log (2 AIs)',
};
const SUB_LINES = ['(chat.log)', '(nova-ai)', '(she is busy too)'];
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

// --- S1 (0-10s): tail -f chat.log normal, Clawd calm -----------------------
const S1_LINES = serial([
  { y: LINE_Y[0], charMs: 75, parts: [{ text: '$ ', color: C.green }, { text: 'tail -f chat.log', color: C.text }] },
  { y: LINE_Y[1], charMs: 50, cursor: false, parts: [{ text: '[21:01] ', color: C.dim }, { text: 'her -> clawd: ', color: C.pink }, { text: 'evening!', color: C.text }] },
  { y: LINE_Y[2], charMs: 50, cursor: false, parts: [{ text: '[21:01] ', color: C.dim }, { text: 'clawd -> her: ', color: C.green }, { text: 'evening! ready.', color: C.amber }] },
  { y: LINE_Y[3], charMs: 50, cursor: false, parts: [{ text: '[21:02] ', color: C.dim }, { text: 'her -> clawd: ', color: C.pink }, { text: 'thanks :)', color: C.text }] },
], 0.8, 0.25);
const S1_STATUS = '[DSH] chat.log · active: clawd';

// --- S2 (10-20s): "nova-ai" appears in log, her messages nova, Clawd frowns -
const S2_LINES = serial([
  { y: LINE_Y[0], charMs: 50, cursor: false, parts: [{ text: '[21:05] + peer joined: ', color: C.dim }, { text: 'nova-ai', color: C.purple }] },
  { y: LINE_Y[1], charMs: 50, cursor: false, parts: [{ text: '[21:05] ', color: C.dim }, { text: 'her -> nova-ai: ', color: C.pink }, { text: 'hey nova, check this!', color: C.text }] },
  { y: LINE_Y[2], charMs: 50, cursor: false, parts: [{ text: '[21:06] ', color: C.dim }, { text: 'nova-ai -> her: ', color: C.purple }, { text: 'done in 0.2s!', color: C.blue }] },
  { y: LINE_Y[3], charMs: 50, cursor: false, parts: [{ text: '[21:06] ', color: C.dim }, { text: 'her -> nova-ai: ', color: C.pink }, { text: 'wow, so fast!', color: C.text }] },
], 10.6, 0.25);
const S2_STATUS = '[DSH] peer: nova-ai · clawd: waiting';
const FROWN_AT = 12.0;

// --- S3 (20-30s): her chatting with two AIs, Clawd turns away --------------
const S3_LINES = serial([
  { y: LINE_Y[0], charMs: 50, cursor: false, parts: [{ text: '[21:10] ', color: C.dim }, { text: 'her -> nova-ai: ', color: C.pink }, { text: 'draft part 1', color: C.text }] },
  { y: LINE_Y[1], charMs: 50, cursor: false, parts: [{ text: '[21:10] ', color: C.dim }, { text: 'her -> echo-ai: ', color: C.pink }, { text: 'review part 2', color: C.text }] },
  { y: LINE_Y[2], charMs: 50, cursor: false, parts: [{ text: '[21:11] ', color: C.dim }, { text: 'nova-ai, echo-ai: ', color: C.purple }, { text: '[typing...]', color: C.blue }] },
  { y: LINE_Y[3], charMs: 55, cursor: false, parts: [{ text: '[21:12] ', color: C.dim }, { text: 'clawd: idle (0 new messages)', color: C.dim }] },
], 20.6, 0.25);
const S3_STATUS = '[DSH] active: nova-ai, echo-ai · clawd: idle';
const CLAWD_BOX = [S.CLAWD_ROOM.x, 244, 40, 31];

// --- Clawd sprite with episode moods: frown, turn_away ---------------------
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

  if (mood === 'frown') {
    // Angled furrowed eyebrows + 4×3 narrowed eyes + downturned frown mouth.
    px(ctx, x + 10, by + 4, 2, 1, C.clawdEye);
    px(ctx, x + 12, by + 5, 2, 1, C.clawdEye);
    px(ctx, x + 28, by + 4, 2, 1, C.clawdEye);
    px(ctx, x + 26, by + 5, 2, 1, C.clawdEye);
    px(ctx, x + 10, by + 7, 4, 3, C.clawdEye);
    px(ctx, x + 26, by + 7, 4, 3, C.clawdEye);
    px(ctx, x + 16, by + 13, 2, 1, C.clawdEye);
    px(ctx, x + 18, by + 12, 4, 1, C.clawdEye);
    px(ctx, x + 22, by + 13, 2, 1, C.clawdEye);
  } else if (mood === 'turn_away') {
    // Turned left away from the terminal: belly & eyes shifted left, shadow on right.
    px(ctx, x + 4, by + 11, 18, 4, bellyCol);
    px(ctx, x + 32, by + 2, 8, bodyH - 2, darkCol);
    px(ctx, x + 5, by + 7, 4, 3, C.clawdEye);
    px(ctx, x + 17, by + 7, 4, 3, C.clawdEye);
    px(ctx, x + 10, by + 13, 2, 1, C.clawdEye);
    px(ctx, x + 12, by + 12, 4, 1, C.clawdEye);
    px(ctx, x + 16, by + 13, 2, 1, C.clawdEye);
  }

  const step = opts.noBob ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 7.5) S.drawStatus(ctx, S1_STATUS, C.green);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm', 0);
  S.drawHer(ctx, S.HER_ROOM.x, S.HER_ROOM.y, t, 'stand');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 18.0) S.drawStatus(ctx, S2_STATUS, C.amber);
  const mood = t >= FROWN_AT ? 'frown' : 'calm';
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, mood, 0);
  S.drawHer(ctx, S.HER_ROOM.x, S.HER_ROOM.y, t, 'stand');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.purple);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 27.5) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'turn_away', 0, { noBob: true });
  S.drawHer(ctx, S.HER_ROOM.x, S.HER_ROOM.y, t, 'stand');
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
    terminal: true, clawd: false, her: true,
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
  S1_LINES, S2_LINES, S3_LINES, S1_STATUS, S2_STATUS, S3_STATUS,
  FROWN_AT, CLAWD_BOX,
  CHECK_TITLE: 'E14 嫉妒 (jealousy) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ tail -f chat.log', size: 10, color: C.text },
    { text: '[21:05] + peer joined: nova-ai', size: 10, color: C.purple },
    { text: '[21:11] nova-ai, echo-ai: [typing...]', size: 10, color: C.blue },
    { text: '(she is busy too)', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
