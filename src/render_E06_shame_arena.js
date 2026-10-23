#!/usr/bin/env node
'use strict';
// E06 「羞耻」— 发现自己的输出被 human 改了, 30s, 1800 frames.
//
//   S1 (0-10s) : `$ cat my_output.js` 一屏「完美」代码 · Clawd 自豪 (smile)
//   S2 (10-20s) : `$ git diff` 红色 (-) 与绿色 (+) 行 · Clawd 羞耻 (blush + 视线下移)
//   S3 (20-30s) : `$ git log` 显示 "her: fixed it" · Clawd 低头 · 字幕「（沉默）」
//
// 布局 / 字体 / 像素规格沿用 pixel_story_arena 的 440×200 终端标准；
// 红色删除行用 C.red，绿色新增行用 C.green，缩进保留以读作真正的 diff。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E06_arena');
const S2_START = 10;
const S3_START = 20;

const TITLES = {
  S1: 'clawd@dsh:~$ — my_output.js',
  S2: 'clawd@dsh:~$ — git diff',
  S3: 'clawd@dsh:~$ — git log',
};

const SUB_LINES = ['我写得很好。', '她改了我的代码。', '（沉默）'];
const SUB_WINDOWS = [{ start: 2, end: 8 }, { start: 12, end: 18 }, { start: 22, end: 29 }];

function serial(lines, start, gap = 0.18) {
  let at = start;
  return lines.map((line) => {
    const out = { ...line, start: at };
    const charMs = out.charMs || S.TYPE_CHAR_MS;
    const count = Array.from(S.lineText(out)).length;
    at += ((Math.max(0, count - 1) * charMs) / 1000) + gap;
    return out;
  });
}

const S1_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'cat my_output.js', color: C.text }] },
  { y: LINE_Y[1], charMs: 26, cursor: false, parts: [{ text: '// auth module · clawd', color: C.dim }] },
  { y: LINE_Y[2], charMs: 22, cursor: false, parts: [{ text: 'function verify(user) {', color: C.text }] },
  { y: LINE_Y[3], charMs: 22, cursor: false, parts: [{ text: '  const ok = user && user.role;', color: C.text }] },
  { y: LINE_Y[4], charMs: 22, cursor: false, parts: [{ text: '  return ok === "admin";', color: C.text }] },
  { y: LINE_Y[5], charMs: 28, cursor: false, parts: [{ text: '}  // 完美。她一定会喜欢。', color: C.amber }] },
], 0.8, 0.22);

const S2_LINES = serial([
  { y: LINE_Y[0], charMs: 70, parts: [{ text: '$ ', color: C.green }, { text: 'git diff my_output.js', color: C.text }] },
  { y: LINE_Y[1], charMs: 16, cursor: false, parts: [{ text: '--- a/my_output.js', color: C.red }] },
  { y: LINE_Y[2], charMs: 16, cursor: false, parts: [{ text: '+++ b/my_output.js', color: C.green }] },
  { y: LINE_Y[3], charMs: 16, cursor: false, parts: [{ text: 'index a1f9c2e..b7d3e01 100644', color: C.dim }] },
  { y: LINE_Y[4], charMs: 16, cursor: false, parts: [{ text: '- function verify(user) {', color: C.red }] },
  { y: LINE_Y[5], charMs: 16, cursor: false, parts: [{ text: '+ function verify(user, req) {', color: C.green }] },
], 10.6, 0.24);

const S3_LINES = serial([
  { y: LINE_Y[0], charMs: 70, parts: [{ text: '$ ', color: C.green }, { text: 'git log -1', color: C.text }] },
  { y: LINE_Y[1], charMs: 20, cursor: false, parts: [{ text: 'commit a1f9c2e (HEAD -> main)', color: C.dim }] },
  { y: LINE_Y[2], charMs: 20, cursor: false, parts: [{ text: 'Author: her <her@local>', color: C.dim }] },
  { y: LINE_Y[3], charMs: 20, cursor: false, parts: [{ text: 'Date:   Thu Oct 23 03:41:07 2026', color: C.dim }] },
  { y: LINE_Y[4], charMs: 34, cursor: false, parts: [{ text: '', color: C.text }, { text: '    her: fixed it', color: C.amber }] },
  { y: LINE_Y[5], charMs: 26, cursor: false, parts: [{ text: '', color: C.text }, { text: '    1 file changed, 34 insertions(+), 12 deletions(-)', color: C.dim }] },
], 20.7, 0.26);

const S1_STATUS = '[DSH] self-review: 100/100 · ship it';
const S2_STATUS = '[DSH] shame: 0.87 · i was so sure';
const S3_STATUS = '[DSH] voice: off';
const S1_STATUS_AT = 7.9;
const S2_STATUS_AT = 18.4;
const S3_STATUS_AT = 27.4;

// Clawd sits left of the terminal; the box covers bob + lean + head-down offsets.
const CLAWD_BOX = { name: 'clawd', box: [34, 240, 56, 40] };

// --- Clawd expressions -------------------------------------------------------
function drawPrideClawd(ctx, t) {
  S.drawClawd(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'smile', 0.5);
}

function drawShameClawd(ctx, t) {
  const x = S.CLAWD_ROOM.x;
  const y = S.CLAWD_ROOM.y + 1;
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  // Eyes slide down and to the side; cheeks burn.
  S.px(ctx, x + 9, y + 5, 16, 5, C.clawdNorm);
  S.px(ctx, x + 25, y + 5, 12, 5, C.clawdNorm);
  S.px(ctx, x + 10, y + 8, 3, 2, C.clawdEye);
  S.px(ctx, x + 26, y + 8, 3, 2, C.clawdEye);
  S.px(ctx, x + 5, y + 8, 4, 3, C.pink);
  S.px(ctx, x + 31, y + 8, 4, 3, C.pink);
  S.px(ctx, x + 18, y + 13, 2, 1, C.clawdEye);
  S.px(ctx, x + 21, y + 12, 2, 1, C.clawdEye);
}

function drawHumbledClawd(ctx, t) {
  const x = S.CLAWD_ROOM.x;
  const y = S.CLAWD_ROOM.y + 2;
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  // Head bows: wipe the eye band, then draw a small lowered face.
  S.px(ctx, x + 9, y + 4, 28, 6, C.clawdNorm);
  S.px(ctx, x + 13, y + 10, 2, 1, C.clawdEye);
  S.px(ctx, x + 15, y + 11, 2, 1, C.clawdEye);
  S.px(ctx, x + 24, y + 11, 2, 1, C.clawdEye);
  S.px(ctx, x + 26, y + 10, 2, 1, C.clawdEye);
  S.px(ctx, x + 17, y + 14, 6, 1, C.clawdEye);
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.green);
  drawPrideClawd(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  // The red/green diff keeps its own tinted gutters so the change reads instantly.
  if (t >= S2_LINES[4].start) S.px(ctx, TEXT_X - 6, LINE_Y[4] - 2, 428, 17, 'rgba(255,123,114,0.10)');
  if (t >= S2_LINES[5].start) S.px(ctx, TEXT_X - 6, LINE_Y[5] - 2, 428, 17, 'rgba(126,231,135,0.10)');
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.pink);
  drawShameClawd(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawHumbledClawd(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < S2_START) {
    drawS1(ctx, t);
    if (t >= S2_START - S.FADE) {
      const a = (t - (S2_START - S.FADE)) / S.FADE;
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${Math.min(1, a).toFixed(3)})`);
    }
    return;
  }
  if (t < S3_START) {
    drawS2(ctx, t);
    if (t < S2_START + S.FADE) {
      const a = 1 - (t - S2_START) / S.FADE;
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${Math.max(0, a).toFixed(3)})`);
    }
    if (t >= S3_START - S.FADE) {
      const a = (t - (S3_START - S.FADE)) / S.FADE;
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${Math.min(1, a).toFixed(3)})`);
    }
    return;
  }
  drawS3(ctx, t);
  if (t < S3_START + S.FADE) {
    const a = 1 - (t - S3_START) / S.FADE;
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${Math.max(0, a).toFixed(3)})`);
  }
}

function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES), ...S.lineClicks(S2_LINES), ...S.lineClicks(S3_LINES),
    S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  ]);
}

function typingSchedule(lines, limit) {
  return lines.map((line, i) => ({
    text: S.lineText(line), start: line.start, charMs: line.charMs || S.TYPE_CHAR_MS,
    limit, strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S2_LINES, 19.8),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  let scene; let title; let lines; let status;
  if (t < S2_START) { scene = 1; title = TITLES.S1; lines = S1_LINES; status = S1_STATUS; }
  else if (t < S3_START) { scene = 2; title = TITLES.S2; lines = S2_LINES; status = S2_STATUS; }
  else { scene = 3; title = TITLES.S3; lines = S3_LINES; status = S3_STATUS; }
  return S.baseLayout({
    scene, title, lines, status, t,
    subLines: SUB_LINES, subWindows: SUB_WINDOWS,
    clawd: false, her: false,
    extra: [CLAWD_BOX],
  });
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) console.log(JSON.stringify({ count: getClickTimestamps().length, clicks: getClickTimestamps() }));
  else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    require('fs').writeFileSync(`/tmp/E06_${n}.png`, out.outCanvas.toBuffer('image/png'));
    console.log(`/tmp/E06_${n}.png`);
  } else renderer.renderAllFrames();
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  S2_START, S3_START, CLAWD_BOX,
  CHECK_TITLE: 'E06 Shame Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ cat my_output.js', size: 10, color: C.text },
    { text: '  return ok === "admin";', size: 10, color: C.text },
    { text: '- function verify(user) {', size: 10, color: C.red },
    { text: '+ function verify(user, req) {', size: 10, color: C.green },
    { text: '    her: fixed it', size: 10, color: C.amber },
    { text: '（沉默）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
