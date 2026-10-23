#!/usr/bin/env node
'use strict';
// E05 「惊讶」— df -h 突然 100%，陌生进程出现, 30s, 1800 frames.
//
//   S1 (0-10s)  : `$ df -h` 正常 25% · Clawd calm · 字幕「一切正常。」
//   S2 (10-15s) : 白屏 0.5s → `$ df -h` 变成 100% · Clawd surprised (wide eyes)
//   S3 (15-30s) : `$ ps aux` 出现陌生进程 PID 9999 · Clawd 后仰 · 字幕「谁放进来的？」
//
// 与 companion / reboot 共用 640×360 画布、440×200 终端、Fusion Pixel 10px 字体、
// Clawd 40×17 像素规格；键盘音由同一份 line 对象推导，保证「每字符 1 次 click」。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E05_arena');

// Scene boundaries: two short scenes up to 15s, the aftermath fills the rest.
const S2_START = 10;
const S3_START = 15;
const FLASH_END = 10.4;   // 0.4s full white
const FLASH_FADE = 0.2;   // + 0.2s fade back into the terminal

const TITLES = {
  S1: 'clawd@dsh:~$ — disk check',
  S2: 'clawd@dsh:~$ — disk alert',
  S3: 'clawd@dsh:~$ — ps aux',
};

const SUB_LINES = ['一切正常。', '谁放进来的？'];
const SUB_WINDOWS = [{ start: 2, end: 8 }, { start: 20, end: 28 }];

// Serial scheduling keeps every typed line complete before the next one starts.
function serial(lines, start, gap = 0.2) {
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
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], charMs: 22, cursor: false, parts: [{ text: 'Filesystem      Size  Used Avail Use%', color: C.dim }] },
  { y: LINE_Y[2], charMs: 22, cursor: false, parts: [{ text: '/dev/disk1      256G   64G  192G  25%', color: C.text }] },
], 0.8, 0.22);

const S2_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], charMs: 22, cursor: false, parts: [{ text: 'Filesystem      Size  Used Avail Use%', color: C.dim }] },
  { y: LINE_Y[2], charMs: 22, cursor: false, parts: [{ text: '/dev/disk1      256G  256G     0 100%', color: C.red }] },
  { y: LINE_Y[3], charMs: 14, cursor: false, parts: [{ text: '[write failed] no space left on device', color: C.red }] },
], 10.7, 0.2);

const S3_LINES = serial([
  { y: LINE_Y[0], charMs: 70, parts: [{ text: '$ ', color: C.green }, { text: 'ps aux | grep -v clawd', color: C.text }] },
  { y: LINE_Y[1], charMs: 16, cursor: false, parts: [{ text: 'USER   PID  %CPU  %MEM  COMMAND', color: C.dim }] },
  { y: LINE_Y[2], charMs: 16, cursor: false, parts: [{ text: 'root     1   0.0   0.1  /sbin/init', color: C.dim }] },
  { y: LINE_Y[3], charMs: 16, cursor: false, parts: [{ text: 'root  9999  97.3  12.4  ./unknown', color: C.red }] },
  { y: LINE_Y[4], charMs: 18, cursor: false, parts: [{ text: '[DSH] pid 9999: parent=?, user=root', color: C.amber }] },
], 15.7, 0.22);

const S1_STATUS = '[DSH] disk: 25% · all systems nominal';
const S2_STATUS = '[ALERT] disk: 100% · i did not write this';
const S3_STATUS = '[DSH] trace: no signature · origin unknown';
const S1_STATUS_AT = 3.5;
const S2_STATUS_AT = 13.6;
const S3_STATUS_AT = 20.2;

// Decorative disk gauge lives under the log rows (rows 5-6 are empty in S1/S2).
const GAUGE = { x: TEXT_X, y: LINE_Y[4], w: 408, h: 18 };
const CLAWD_BOX = { name: 'clawd', box: [36, 242, 56, 36] };

function drawGauge(ctx, ratio, color, t) {
  const { x, y } = GAUGE;
  S.txt(ctx, x, y, 'disk', C.dim, 10);
  const bx = x + 40;
  const bw = 300;
  S.px(ctx, bx - 2, y - 2, bw + 4, 14, C.border);
  S.px(ctx, bx, y, bw, 10, '#1F242C');
  const fill = Math.max(0, Math.min(bw, Math.round(bw * ratio)));
  if (fill > 0) S.px(ctx, bx, y, fill, 10, color);
  // 20 block ticks keep the bar readable as pixel art.
  for (let i = 1; i < 20; i++) S.px(ctx, bx + i * 15, y, 1, 10, 'rgba(0,0,0,0.35)');
  const label = `${Math.round(ratio * 100)}%`;
  S.txt(ctx, bx + bw + 8, y, label, color, 10);
}

// --- Clawd expressions: overlays on the shared 40×17 body ---
function overlaySurprised(ctx, x, y) {
  S.px(ctx, x + 9, y + 4, 6, 6, C.clawdEye);
  S.px(ctx, x + 25, y + 4, 6, 6, C.clawdEye);
  S.px(ctx, x + 11, y + 6, 2, 2, C.white);
  S.px(ctx, x + 27, y + 6, 2, 2, C.white);
  S.px(ctx, x + 17, y + 12, 6, 5, C.clawdEye);
  S.px(ctx, x + 19, y + 14, 2, 2, C.red);
}

function overlayLeaning(ctx, x, y) {
  // Wide eyes with the pupils pushed away from the terminal, plus a sweat pixel.
  S.px(ctx, x + 9, y + 5, 6, 5, C.clawdEye);
  S.px(ctx, x + 25, y + 5, 6, 5, C.clawdEye);
  S.px(ctx, x + 12, y + 6, 2, 2, C.white);
  S.px(ctx, x + 28, y + 6, 2, 2, C.white);
  S.px(ctx, x + 17, y + 13, 2, 1, C.clawdEye);
  S.px(ctx, x + 20, y + 14, 2, 1, C.clawdEye);
  S.px(ctx, x + 23, y + 13, 2, 1, C.clawdEye);
  S.px(ctx, x + 35, y + 3, 2, 3, C.blue);
  S.px(ctx, x + 35, y + 6, 2, 1, C.blue);
}

function drawClawdSurprise(ctx, t, stage) {
  const baseX = S.CLAWD_ROOM.x;
  const baseY = S.CLAWD_ROOM.y;
  if (stage === 1) {
    S.drawClawd(ctx, baseX, baseY, t, 'calm', 0);
    return;
  }
  if (stage === 2) {
    // Jolt: 2px hop plus a 1px nervous shake.
    const shake = Math.floor(t * 14) % 2 === 0 ? 0 : 1;
    S.drawClawd(ctx, baseX + shake, baseY - 2, t, 'calm', 0);
    overlaySurprised(ctx, baseX + shake, baseY - 2);
    return;
  }
  // Leaning back, away from the terminal.
  S.drawClawd(ctx, baseX - 5, baseY + 1, t, 'calm', 0);
  overlayLeaning(ctx, baseX - 5, baseY + 1);
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  drawGauge(ctx, 0.25, C.green, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.green);
  drawClawdSurprise(ctx, t, 1);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.red);
  S.drawLines(ctx, S2_LINES, t);
  drawGauge(ctx, 1, C.red, t);
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.red);
  drawClawdSurprise(ctx, t, 2);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
  // Alert wash over the room keeps the jump readable at a glance.
  const pulse = 0.05 + 0.03 * Math.sin(t * 12);
  S.px(ctx, 0, 0, S.BW, 140, `rgba(255,60,50,${pulse.toFixed(3)})`);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.amber);
  S.drawLines(ctx, S3_LINES, t);
  // Highlight the intruder row.
  if (t >= S3_LINES[3].start) S.px(ctx, TEXT_X - 6, LINE_Y[3] - 2, 430, 17, 'rgba(255,123,114,0.14)');
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.red);
  drawClawdSurprise(ctx, t, 3);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < S2_START) {
    drawS1(ctx, t);
    return;
  }
  if (t < S3_START) {
    drawS2(ctx, t);
    // 0.5s white-out: the screen simply loses it for a moment.
    if (t < FLASH_END + FLASH_FADE) {
      const a = t < FLASH_END ? 1 : 1 - (t - FLASH_END) / FLASH_FADE;
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(255,255,255,${Math.max(0, a).toFixed(3)})`);
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
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
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
  ...typingSchedule(S2_LINES, 14.7),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let scene; let title; let lines; let status;
  if (t < S2_START) { scene = 1; title = TITLES.S1; lines = S1_LINES; status = S1_STATUS; }
  else if (t < S3_START) { scene = 2; title = TITLES.S2; lines = S2_LINES; status = S2_STATUS; }
  else { scene = 3; title = TITLES.S3; lines = S3_LINES; status = S3_STATUS; }
  const opts = {
    ...common, scene, title, lines, status,
    clawd: false, her: false,
    extra: [CLAWD_BOX],
  };
  if (scene !== 3) {
    opts.extraGroups = { gauge: [{ name: 'disk_gauge', box: [GAUGE.x, GAUGE.y, GAUGE.w, GAUGE.h] }] };
    opts.extraBounds = { gauge: GAUGE };
  }
  return S.baseLayout(opts);
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) console.log(JSON.stringify({ count: getClickTimestamps().length, clicks: getClickTimestamps() }));
  else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    require('fs').writeFileSync(`/tmp/E05_${n}.png`, out.outCanvas.toBuffer('image/png'));
    console.log(`/tmp/E05_${n}.png`);
  } else renderer.renderAllFrames();
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  S2_START, S3_START, FLASH_END, FLASH_FADE,
  GAUGE, CLAWD_BOX,
  CHECK_TITLE: 'E05 Surprise Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ df -h', size: 10, color: C.text },
    { text: 'Filesystem      Size  Used Avail Use%', size: 10, color: C.dim },
    { text: '/dev/disk1      256G  256G     0 100%', size: 10, color: C.red },
    { text: 'root  9999  97.3  12.4  ./unknown', size: 10, color: C.red },
    { text: '谁放进来的？', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps, drawGauge,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
