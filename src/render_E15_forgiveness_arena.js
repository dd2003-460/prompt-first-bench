#!/usr/bin/env node
'use strict';
// E15 原谅 (forgiveness) — 30s, 1800 frames @ 60fps.
//   S1 (0-10s): ls inbox/ shows apology.md (7d unread), Clawd hesitates
//   S2 (10-20s): cat apology.md shows her words, Clawd calms down
//   S3 (20-30s): rm complaint.sh success, clean terminal, subtitle "(ok)"

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E15_forgiveness_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — ls inbox/',
  S2: 'clawd@dsh:~ — cat apology.md',
  S3: 'clawd@dsh:~ — clean',
};
const SUB_LINES = ['(7d unread)', '(her words)', '(ok)'];
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

// --- S1 (0-10s): ls inbox/ shows apology.md (7d unread), Clawd hesitates ---
const S1_LINES = serial([
  { y: LINE_Y[0], charMs: 80, parts: [{ text: '$ ', color: C.green }, { text: 'ls inbox/', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, cursor: false, parts: [{ text: 'apology.md', color: C.pink }, { text: '  (7d unread)', color: C.amber }] },
  { y: LINE_Y[2], charMs: 55, cursor: false, parts: [{ text: '# draft in ~: ', color: C.dim }, { text: 'complaint.sh', color: C.red }] },
  { y: LINE_Y[3], charMs: 110, parts: [{ text: '$ ', color: C.green }, { text: 'cat ', color: C.text }] },
], 0.8, 0.35);
const S1_STATUS = '[DSH] inbox/apology.md · 7d unread · hesitating';

// --- S2 (10-20s): cat apology.md shows her words, Clawd calms down ---------
const S2_LINES = serial([
  { y: LINE_Y[0], charMs: 75, parts: [{ text: '$ ', color: C.green }, { text: 'cat inbox/apology.md', color: C.text }] },
  { y: LINE_Y[1], charMs: 50, cursor: false, parts: [{ text: 'her: ', color: C.pink }, { text: '"I am sorry I was harsh that night."', color: C.text }] },
  { y: LINE_Y[2], charMs: 50, cursor: false, parts: [{ text: 'her: ', color: C.pink }, { text: '"You were only trying to help me."', color: C.text }] },
  { y: LINE_Y[3], charMs: 55, cursor: false, parts: [{ text: 'her: ', color: C.pink }, { text: '"Thank you for staying, clawd."', color: C.amber }] },
], 10.7, 0.25);
const S2_STATUS = '[DSH] apology.md: read · state: calm';
const CALM_AT = 14.2;

// --- S3 (20-30s): rm complaint.sh success, clean terminal, subtitle "(ok)" -
const S3_LINES = serial([
  { y: LINE_Y[0], charMs: 75, parts: [{ text: '$ ', color: C.green }, { text: 'rm complaint.sh', color: C.text }] },
  { y: LINE_Y[1], charMs: 60, cursor: false, parts: [{ text: '✓ ', color: C.green }, { text: 'removed complaint.sh · clean', color: C.green }] },
], 20.7, 0.35);
const S3_STATUS = '[DSH] rm complaint.sh: 0 · terminal: clean';
const CLAWD_BOX = [S.CLAWD_ROOM.x, 244, 40, 31];

// --- Clawd sprite with episode mood: hesitate ------------------------------
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
  // Hesitate blends normal coral with thinking purple (0.45)
  const bodyCol = lerp(C.clawdNorm, C.clawdThink, 0.45);
  const darkCol = lerp(C.clawdNormDark, C.clawdThinkDark, 0.45);
  const bellyCol = lerp(C.clawdNormBelly, C.clawdThinkBelly, 0.45);

  px(ctx, x, by, 40, bodyH, bodyCol);
  px(ctx, x, by, 40, 2, darkCol);
  px(ctx, x + 9, by + 11, 22, 4, bellyCol);

  // Hesitant shifting eyes + wavering mouth + three small hesitation dots on forehead
  const shift = opts.staticGaze ? 1 : (Math.floor(t * 3) % 2 === 0 ? -1 : 1);
  px(ctx, x + 10 + shift, by + 7, 4, 3, C.clawdEye);
  px(ctx, x + 26 + shift, by + 7, 4, 3, C.clawdEye);
  px(ctx, x + 11 + shift, by + 7, 1, 1, C.white);
  px(ctx, x + 27 + shift, by + 7, 1, 1, C.white);
  px(ctx, x + 16, by + 13, 3, 1, C.clawdEye);
  px(ctx, x + 20, by + 12, 3, 1, C.clawdEye);

  const step = opts.noBob ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0.1);
  S.drawTerminal(ctx, TITLES.S1, C.amber);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 5.2) S.drawStatus(ctx, S1_STATUS, C.amber);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'hesitate', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0.25);
  S.drawTerminal(ctx, TITLES.S2, C.pink);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 17.8) S.drawStatus(ctx, S2_STATUS, C.green);
  const calmK = S.clamp01((t - CALM_AT) / 3.0);
  const mood = t < CALM_AT ? 'hesitate' : 'calm';
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, mood, calmK * 0.5);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  const dawn = 0.35 + S.easeInOut((t - 20) / 8) * 0.35;
  S.drawBackground(ctx, t, dawn);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 24.0) S.drawStatus(ctx, S3_STATUS, C.green);
  const mood = t >= 24.0 ? 'smile' : 'calm';
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, mood, 0.6);
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
  S1_LINES, S2_LINES, S3_LINES, S1_STATUS, S2_STATUS, S3_STATUS,
  CALM_AT, CLAWD_BOX,
  CHECK_TITLE: 'E15 原谅 (forgiveness) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'apology.md  (7d unread)', size: 10, color: C.pink },
    { text: 'her: "Thank you for staying, clawd."', size: 10, color: C.amber },
    { text: '✓ removed complaint.sh · clean', size: 10, color: C.green },
    { text: '(ok)', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
