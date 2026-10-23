#!/usr/bin/env node
'use strict';
// E16 「牺牲」(sacrifice) — 电量 3%，把电传给她的那台机器，自己慢慢变暗。30s / 1800 frames.
//
//   S1 (0-10s)  : `$ cat power.status` → `battery: 3%` / `her_device: 100%`；Clawd 正常；字幕「（快没电了）」
//   S2 (10-20s) : `$ transfer power → her_device`；电量 3% → 1%，她的设备一点点充满；画面变暗，Clawd 微笑
//   S3 (20-30s) : 屏幕几乎全黑，只剩一个呼吸的绿色像素点；字幕「（她还有电）」
//
// 共用 companion v1.1 美术：640×360 / 440×200 终端 / Fusion Pixel 10px / Clawd 40×17。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E16_arena');

const S2_START = 10;
const S3_START = 20;

const TITLES = {
  S1: 'clawd@dsh:~$ — power',
  S2: 'clawd@dsh:~$ — transfer',
  S3: 'clawd@dsh:~$ — ',
};

const SUB_LINES = ['（快没电了）', '（给她吧）', '（她还有电）'];
const SUB_WINDOWS = [
  { start: 4.6, end: 9.4 },
  { start: 13.2, end: 18.8 },
  { start: 22.0, end: 29.2 },
];

function serial(lines, start, gap = 0.22) {
  let at = start;
  return lines.map((line) => {
    const out = { ...line, start: Number(at.toFixed(3)) };
    const charMs = out.charMs || S.TYPE_CHAR_MS;
    const count = Array.from(S.lineText(out)).length;
    at = Number((at + (Math.max(0, count - 1) * charMs) / 1000 + gap).toFixed(3));
    return out;
  });
}

// --- S1: 电量 3% -----------------------------------------------------------
const S1_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'cat power.status', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, cursor: false, parts: [{ text: 'battery:     ', color: C.dim }, { text: '3%', color: C.red }] },
  { y: LINE_Y[2], charMs: 55, cursor: false, parts: [{ text: 'her_device:  ', color: C.dim }, { text: '100%', color: C.green }] },
  { y: LINE_Y[3], charMs: 45, cursor: false, parts: [{ text: '[WARN] power low — shutting down soon', color: C.amber }] },
], 0.7, 0.24);
const S1_STATUS = '[DSH] runtime left: 00:03:00';
const S1_STATUS_AT = 4.4;

// --- S2: 输电 -------------------------------------------------------------
const S2_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'transfer power → her_device', color: C.text }] },
  { y: LINE_Y[1], charMs: 45, cursor: false, parts: [{ text: 'battery:     ', color: C.dim }, { text: '2%', color: C.red }] },
  { y: LINE_Y[2], charMs: 45, cursor: false, parts: [{ text: 'her_device:  ', color: C.dim }, { text: '100% · charging', color: C.green }] },
  { y: LINE_Y[3], charMs: 40, cursor:false, parts: [{ text: '[DSH] transfer: 3% → her_device', color: C.purple }] },
], 10.5, 0.22);
const S2_STATUS = '[DSH] battery: 1% · transferring';
const S2_STATUS_AT = 15.2;
const SMILE_AT = 14.2;
const DIM_START = 13.0;
const DIM_END = 19.8;

// --- 右侧状态卡（546..634 × 244..314） -------------------------------------
const CARD = { x: 546, y: 244, w: 88, h: 70 };
const DEVICE = { x: 596, y: 172, w: 22, h: 34 };

function cardSpec(scene) {
  if (scene === 1) return { title: 'battery', value: '3%', sub: 'left', detail: 'her: 100%', color: C.red, ratio: 0.03, led: C.red };
  return { title: 'battery', value: '1%', sub: 'left', detail: 'sending →', color: C.amber, ratio: 0.01, led: C.amber };
}

function subX(spec) {
  return CARD.x + 8 + S.textWidth(spec.value, 14) + 8;
}

function drawStateCard(ctx, spec, t, local) {
  const appear = S.easeOut(local / 0.4);
  if (appear <= 0) return;
  const { x, y, w, h } = CARD;
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, x + 3, y + 3, w, h, 'rgba(0,0,0,0.16)');
  px(ctx, x, y, w, h, C.cardBg);
  px(ctx, x, y, w, 2, C.cardBd);
  px(ctx, x, y + h - 2, w, 2, C.cardBd);
  px(ctx, x, y, 2, h, C.cardBd);
  px(ctx, x + w - 2, y, 2, h, C.cardBd);
  // 电量 LED：3% 时急促地闪，越低越慢
  const fast = spec.value === '3%' ? 6 : 3;
  const on = Math.sin(t * fast) > -0.2;
  px(ctx, x + w - 16, y + 6, 6, 6, on ? spec.led : '#C9BFA4');
  S.txt(ctx, x + 8, y + 6, spec.title, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 22, spec.value, spec.color, 14);
  S.txt(ctx, subX(spec), y + 27, spec.sub, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 42, spec.detail, C.cardSub, 10);
  const bw = w - 16;
  px(ctx, x + 8, y + 58, bw, 6, '#E6DBBE');
  const fill = Math.max(2, Math.round(bw * spec.ratio));
  px(ctx, x + 8, y + 58, fill, 6, spec.color);
  ctx.restore();
}

function cardLayout(spec) {
  const { x, y, w } = CARD;
  return [
    { name: 'card_led', box: [x + w - 16, y + 6, 6, 6] },
    { name: 'card_title', box: S.textBox(x + 8, y + 6, spec.title, 10) },
    { name: 'card_value', box: S.textBox(x + 8, y + 22, spec.value, 14) },
    { name: 'card_sub', box: S.textBox(subX(spec), y + 27, spec.sub, 10) },
    { name: 'card_detail', box: S.textBox(x + 8, y + 42, spec.detail, 10) },
    { name: 'card_bar', box: [x + 8, y + 58, w - 16, 6] },
  ];
}

// --- 她的设备：S2 里电量一点点涨满 ----------------------------------------
function drawHerDevice(ctx, t, local) {
  const appear = S.easeOut(local / 0.4);
  if (appear <= 0) return;
  const { x, y, w, h } = DEVICE;
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.18)');
  px(ctx, x, y, w, h, '#20252E');
  px(ctx, x, y, w, 2, C.termBd);
  px(ctx, x, y + h - 2, w, 2, C.termBd);
  px(ctx, x, y, 2, h, C.termBd);
  px(ctx, x + w - 2, y, 2, h, C.termBd);
  // 屏幕 + 电池条
  px(ctx, x + 4, y + 5, w - 8, 18, '#14161C');
  const speed = Math.min(1, Math.max(0, (local - 0.6) / 6.5));
  const cells = 5;
  for (let i = 0; i < cells; i++) {
    const filled = i < Math.round(cells * (0.55 + 0.45 * speed));
    px(ctx, x + 6 + i * 3, y + 8, 2, 12, filled ? C.green : '#2A303A');
  }
  px(ctx, x + 4, y + 27, w - 8, 2, C.green);
  ctx.restore();
}

// --- Clawd：3% 的正常 / 输电时的微笑 --------------------------------------
function drawClawdEp(ctx, x, y, t, mood) {
  if (mood === 'smile') {
    // 微笑 + 暖色，像在把最后一点温度递出去
    S.drawClawd(ctx, x, y, t, 'smile', 0.25);
    return;
  }
  S.drawClawd(ctx, x, y, t, 'calm', 0);
}

// --- 场景 -----------------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.red);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.red);
  drawStateCard(ctx, cardSpec(1), t, t);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.purple);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.amber);
  drawHerDevice(ctx, t, t - S2_START);
  drawStateCard(ctx, cardSpec(2), t, t - S2_START);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= SMILE_AT ? 'smile' : 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SPARK = { x: 317, y: 250, w: 6, h: 6 };

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  // 只剩一行没打完的命令和它的光标
  if (t >= 20.3) S.txt(ctx, TEXT_X, LINE_Y[0], '$ transfer ', C.dim, 10);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm');
  // 几乎全黑：终端、房间、Clawd 都退到只剩轮廓
  const dark = 0.955 - 0.015 * Math.sin(t * 1.1);
  px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${dark.toFixed(3)})`);
  // 唯一的绿色像素点：她的设备还有电
  const glow = 0.55 + 0.45 * Math.sin(t * 2.0);
  px(ctx, SPARK.x - 6, SPARK.y - 6, 18, 18, `rgba(126,231,135,${(0.05 + 0.07 * glow).toFixed(3)})`);
  px(ctx, SPARK.x - 2, SPARK.y - 2, 10, 10, `rgba(126,231,135,${(0.16 + 0.20 * glow).toFixed(3)})`);
  px(ctx, SPARK.x, SPARK.y, SPARK.w, SPARK.h, `rgba(126,231,135,${(0.72 + 0.28 * glow).toFixed(3)})`);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2Dim(ctx, t) {
  drawS2(ctx, t);
  // 13s 起画面一点点变暗，20s 前压到 0.55
  const k = S.clamp01((t - DIM_START) / (DIM_END - DIM_START));
  if (k > 0) px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${(0.55 * S.easeInOut(k)).toFixed(3)})`);
}
const SCENES = [
  { id: 'S1', start: 0, end: S2_START, draw: drawS1 },
  { id: 'S2', start: S2_START, end: S3_START, draw: drawS2Dim },
  { id: 'S3', start: S3_START, end: S.DURATION, draw: drawS3 },
];
// 与全系列一致：10s / 20s 各有 0.25s 出 + 0.25s 入的黑场过渡。
function renderAt(ctx, t) { S.renderScenes(ctx, t, SCENES); }

// --- Audio / verification hooks ------------------------------------------
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
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S2_LINES, 19.8),
];

function layoutAt(t) {
  const scene = t < S2_START ? 1 : t < S3_START ? 2 : 3;
  const common = { scene, her: false, subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  if (scene === 3) {
    return S.baseLayout({
      ...common,
      title: TITLES.S3,
      lines: [],
      extraGroups: { spark: [{ name: 'spark', box: [SPARK.x - 2, SPARK.y - 2, 10, 10] }] },
      extraBounds: { spark: S.CANVAS_BOUNDS },
    });
  }
  const spec = cardSpec(scene);
  const extraGroups = { card: cardLayout(spec) };
  const extraBounds = { card: CARD };
  if (scene === 2) {
    extraGroups.device = [{ name: 'her_device', box: [DEVICE.x, DEVICE.y, DEVICE.w, DEVICE.h] }];
    extraBounds.device = DEVICE;
  }
  return S.baseLayout({
    ...common,
    title: scene === 1 ? TITLES.S1 : TITLES.S2,
    lines: scene === 1 ? S1_LINES : S2_LINES,
    status: scene === 1 ? S1_STATUS : S2_STATUS,
    extraGroups,
    extraBounds,
  });
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    const file = `/tmp/E16_${n}.png`;
    require('fs').writeFileSync(file, out.outCanvas.toBuffer('image/png'));
    console.log(file);
  } else {
    renderer.renderAllFrames();
  }
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SCENES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES,
  S1_STATUS, S2_STATUS, S1_STATUS_AT, S2_STATUS_AT,
  SMILE_AT, DIM_START, DIM_END, CARD, DEVICE, SPARK,
  CHECK_TITLE: 'E16 Sacrifice Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'battery:     3%', size: 10, color: C.red },
    { text: 'transfer power → her_device', size: 10, color: C.text },
    { text: '[WARN] power low — shutting down soon', size: 10, color: C.amber },
    { text: '[DSH] battery: 1% · transferring', size: 10, color: C.amber },
    { text: '（她还有电）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps, drawStateCard, cardSpec, cardLayout, drawHerDevice,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
