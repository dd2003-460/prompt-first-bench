#!/usr/bin/env node
'use strict';
// E05 «惊讶 · surprise» — df -h 突然 100%，陌生进程 PID 9999。
// 30s / 1800 frames / 640×360 (SCALE=2 → 1280×720 @ 60fps)
//   S1 (0-10s)  : `df -h` 显示 25%，一切正常，Clawd calm，字幕「一切正常。」
//   S2 (10-15s) : 0.5s 白屏 → 终端 100%，Clawd 惊愕，字幕「100%。」
//   S3 (15-30s) : `ps aux` 出现陌生进程 PID 9999，Clawd 后仰，字幕「谁放进来的？」
// 复用 src/pixel_story_arena.js 的 440×200 终端 / Clawd 40×17 / 房间 / 字幕条。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, LINE_Y, TEXT_X } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E05_surprise_arena');

const S1_START = 0;
const S2_START = 10;
const S3_START = 15;
const WHITE_START = 10.0; // 白屏 0.5s（规格）
const WHITE_END = 10.5;

const TITLES = ['clawd@dsh:~$ — df -h', 'clawd@dsh:~$ — 100%', 'clawd@dsh:~$ — ps aux'];
const ACCENTS = [C.green, C.red, C.amber];
const DAWN = [0.06, 0.1, 0.14];

const HEADER = 'Filesystem      Size  Used Avail Use%  Mounted on';
const ROW_OK = '/dev/sda1       100G   25G   75G  25%  /';
const ROW_FULL = '/dev/sda1       100G  100G    0G 100%  /';

/* ---------------- S1 · 一切正常 ---------------- */
const S1_LINES = [
  { y: LINE_Y[0], start: 0.70, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], start: 1.90, typed: false, parts: [{ text: HEADER, color: C.dim }] },
  { y: LINE_Y[2], start: 2.20, typed: false, parts: [{ text: ROW_OK, color: C.text }] },
  { y: LINE_Y[3], start: 3.30, typed: false, parts: [{ text: '[clawd] 一切正常。', color: C.green }] },
  { y: LINE_Y[4], start: 4.60, typed: false, parts: [{ text: '[dsd] 还剩 75G，够用。', color: C.dim }] },
];

/* ---------------- S2 · 白屏之后 100% ---------------- */
const S2_LINES = [
  { y: LINE_Y[0], start: 10.95, charMs: 110, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], start: 12.05, typed: false, parts: [{ text: HEADER, color: C.dim }] },
  { y: LINE_Y[2], start: 12.25, typed: false, parts: [{ text: ROW_FULL, color: C.red }] },
  { y: LINE_Y[3], start: 12.95, typed: false, parts: [{ text: '[DSH] ALERT: no space left on device', color: C.red }] },
  { y: LINE_Y[4], start: 13.70, typed: false, parts: [{ text: '[clawd] 等等……', color: C.amber }] },
];

/* ---------------- S3 · 陌生进程 ---------------- */
function serial(lines, start, gap = 0.15) {
  let at = start;
  return lines.map((line) => {
    const out = { ...line, start: at };
    const charMs = out.charMs || S.TYPE_CHAR_MS;
    const count = Array.from(S.lineText(out)).length;
    at += ((Math.max(0, count - 1) * charMs) / 1000) + gap;
    return out;
  });
}

const S3_HEAD = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'ps aux | grep 9999', color: C.text }] },
], 15.70);
const S3_LINES = [
  ...S3_HEAD,
  { y: LINE_Y[1], start: 17.60, typed: false, parts: [{ text: 'nobody   9999  99.9  8.8  ?  ??   ??', color: C.red }] },
  { y: LINE_Y[2], start: 18.40, typed: false, parts: [{ text: '[DSH] uid 9999 not in /etc/passwd', color: C.amber }] },
  { y: LINE_Y[3], start: 20.40, parts: [{ text: '$ ', color: C.green }, { text: 'who let this in', color: C.text }] },
  { y: LINE_Y[4], start: 23.10, typed: false, parts: [{ text: '[clawd] 不是我。', color: C.dim }] },
];

const SCENE_LINES = [S1_LINES, S2_LINES, S3_LINES];
const SCENE_STARTS = [S1_START, S2_START, S3_START];

const STATUS = [
  '[DSH] heartbeat: stable · 02:41',
  '[DSH] disk_usage: 100% · CRITICAL',
  '[DSH] unknown process · pid 9999',
];
const STATUS_AT = [4.40, 13.40, 26.00];
const STATUS_COLOR = [C.green, C.red, C.amber];

const DISK_AT = 0.5;
const SUB_LINES = ['一切正常。', '100%。', '谁放进来的？'];
const SUB_WINDOWS = [{ start: 2.0, end: 8.0 }, { start: 11.4, end: 14.2 }, { start: 23.6, end: 28.6 }];

/* ---------------- 磁盘仪表卡（窗格内） ---------------- */
const CARD = { x: 74, y: 30, w: 150, h: 64 };
const CARD_NOTES = ['ok · 75G free', '0 bytes free', '0 bytes free'];

function drawDiskCard(ctx, pct, t, alert) {
  const { x, y, w, h } = CARD;
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.18)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);

  S.txt(ctx, x + 10, y + 8, 'DISK USAGE', C.dim, 10);
  const col = alert ? (Math.floor(t * 6) % 2 ? C.red : '#C9524B') : C.green;
  S.txt(ctx, x + w - 10, y + 8, `${pct}%`, col, 10, 'right');

  const bx = x + 10;
  const by = y + 32;
  const bw = w - 20;
  S.px(ctx, bx, by, bw, 8, C.border);
  const fill = Math.max(0, Math.min(bw, Math.round((bw - 4) * (pct / 100))));
  if (fill > 0) S.px(ctx, bx + 2, by + 2, fill, 4, col);

  S.txt(ctx, x + 10, y + 48, CARD_NOTES[alert ? 1 : 0], alert ? C.red : C.dim, 10);
}

function diskCardLayout(pct, alert) {
  return [
    { name: 'card_label', box: S.textBox(CARD.x + 10, CARD.y + 8, 'DISK USAGE', 10) },
    { name: 'card_pct', box: S.textBox(CARD.x + CARD.w - 10, CARD.y + 8, `${pct}%`, 10, 'right') },
    { name: 'card_bar', box: [CARD.x + 9, CARD.y + 31, CARD.w - 18, 10] },
    { name: 'card_note', box: S.textBox(CARD.x + 10, CARD.y + 48, CARD_NOTES[alert ? 1 : 0], 10) },
  ];
}

/* ---------------- Clawd 情绪位 ---------------- */
const CLAWD_BOX = [S.CLAWD_ROOM.x - 6, 234, 52, 48];
const FX_BOUNDS = { x: 26, y: 212, w: 68, h: 58 };

function drawExclaim(ctx, t, color = C.red) {
  const pulse = Math.floor(t * 5) % 2;
  const x = S.CLAWD_ROOM.x + 26;
  const y = 220 + pulse;
  S.px(ctx, x, y, 4, 9, color);
  S.px(ctx, x, y + 12, 4, 4, color);
}

function drawSweat(ctx, t) {
  const phase = (t * 1.6) % 1;
  const x = 90;
  const y = Math.round(248 + phase * 14);
  const alpha = (1 - phase) * 0.9;
  S.px(ctx, x, y, 2, 4, `rgba(121,192,255,${alpha.toFixed(3)})`);
  S.px(ctx, x, y + 4, 2, 2, `rgba(121,192,255,${(alpha * 0.7).toFixed(3)})`);
}

function drawMotionLines(ctx, t) {
  const shift = Math.floor(t * 12) % 3;
  for (let i = 0; i < 3; i++) {
    const y = 250 + i * 6;
    S.px(ctx, S.CLAWD_ROOM.x - 12 - shift, y, 8, 1, 'rgba(139,148,158,0.55)');
  }
}

function drawClawdE05(ctx, index, t) {
  const { x, y } = S.CLAWD_ROOM;
  if (index === 0) {
    S.drawClawd(ctx, x, y, t, 'calm', 0);
    return;
  }
  if (index === 1) {
    // 惊愕：身体轻微抖动 + 头顶感叹号 + 冒汗
    const jitter = Math.round(Math.sin(t * 26));
    S.drawClawd(ctx, x, y + jitter, t, 'calm', 0);
    drawExclaim(ctx, t);
    drawSweat(ctx, t);
    return;
  }
  // 后仰：整个人往后退 2px、抬起 2px，速度线在身后
  const recoil = Math.round(Math.sin(t * 3.2) > 0.3 ? 1 : 0);
  S.px(ctx, x + 2, y + 24, 36, 2, 'rgba(0,0,0,0.18)'); // 退后留下的影子
  S.drawClawd(ctx, x - 2, y - 2 - recoil, t, 'calm', 0);
  drawExclaim(ctx, t);
  drawSweat(ctx, t);
  drawMotionLines(ctx, t);
}

/* ---------------- 场景绘制 ---------------- */
function drawScene(index, ctx, t) {
  S.drawBackground(ctx, t, DAWN[index]);
  S.drawTerminal(ctx, TITLES[index], ACCENTS[index]);
  S.drawLines(ctx, SCENE_LINES[index], t);
  if (t >= STATUS_AT[index]) S.drawStatus(ctx, STATUS[index], STATUS_COLOR[index]);

  const pct = index === 0 ? 25 : 100;
  if (t >= DISK_AT) drawDiskCard(ctx, pct, t, index !== 0);
  drawClawdE05(ctx, index, t);

  if (index >= 1) {
    // 冷色焦虑氛围：轻微红色呼吸
    const k = 0.035 + 0.025 * (0.5 + 0.5 * Math.sin(t * 3.4));
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(255,70,70,${k.toFixed(3)})`);
  }
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { id: 'E05-S1', start: S1_START, end: S2_START, draw: (ctx, t) => drawScene(0, ctx, t) },
  { id: 'E05-S2', start: S2_START, end: S3_START, draw: (ctx, t) => drawScene(1, ctx, t) },
  { id: 'E05-S3', start: S3_START, end: S.DURATION, draw: (ctx, t) => drawScene(2, ctx, t) },
];

// S1→S2 是规格要求的一次真·白屏（0.5s），S2→S3 仍是 0.25s+0.25s 黑场。
function renderAt(ctx, t) {
  const index = t < S2_START ? 0 : t < S3_START ? 1 : 2;
  SCENES[index].draw(ctx, t);

  let black = 0;
  if (t >= S3_START - S.FADE && t < S3_START) black = (t - (S3_START - S.FADE)) / S.FADE;
  else if (t >= S3_START && t < S3_START + S.FADE) black = 1 - (t - S3_START) / S.FADE;
  if (black > 0) S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${S.clamp01(black).toFixed(3)})`);

  let white = 0;
  if (t >= WHITE_START - 0.08 && t < WHITE_START) white = (t - (WHITE_START - 0.08)) / 0.08;
  else if (t >= WHITE_START && t <= WHITE_END) white = 1;
  else if (t > WHITE_END && t < WHITE_END + 0.15) white = 1 - (t - WHITE_END) / 0.15;
  if (white > 0) S.px(ctx, 0, 0, S.BW, S.BH, `rgba(255,255,255,${S.clamp01(white).toFixed(3)})`);
}

/* ---------------- 音效 / 检查用时间表 ---------------- */
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
    ...STATUS_AT,
    DISK_AT,
  ]);
}

function typingSchedule(all, limit) {
  const lines = all.filter((line) => line.typed !== false);
  return lines.map((line, i) => ({
    text: S.lineText(line),
    start: line.start,
    charMs: line.charMs || S.TYPE_CHAR_MS,
    limit,
    strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, S2_START - 0.2),
  ...typingSchedule(S2_LINES, S3_START - 0.2),
  ...typingSchedule(S3_LINES, S.DURATION - 0.2),
];

/* ---------------- 逐帧布局（check_overlap 用） ---------------- */
function sceneIndexAt(t) {
  return t < S2_START ? 0 : t < S3_START ? 1 : 2;
}

function fxLayout(index, t) {
  if (index === 0) return [];
  const list = [{ name: 'exclaim', box: [S.CLAWD_ROOM.x + 26, 220, 4, 16] }];
  const phase = (t * 1.6) % 1;
  list.push({ name: 'sweat', box: [90, Math.round(248 + phase * 14), 2, 6] });
  if (index === 2) list.push({ name: 'motion', box: [S.CLAWD_ROOM.x - 14, 250, 9, 13] });
  return list;
}

function layoutAt(t) {
  const index = sceneIndexAt(t);
  const pct = index === 0 ? 25 : 100;
  return S.baseLayout({
    scene: index + 1,
    title: TITLES[index],
    lines: SCENE_LINES[index],
    status: t >= STATUS_AT[index] ? STATUS[index] : null,
    clawd: false,
    her: false,
    subLines: SUB_LINES,
    subWindows: SUB_WINDOWS,
    t,
    extraGroups: {
      clawdBody: [{ name: 'clawd', box: CLAWD_BOX.slice() }],
      clawdFx: fxLayout(index, t),
      diskCard: t >= DISK_AT ? diskCardLayout(pct, index !== 0) : [],
    },
    extraBounds: {
      clawdBody: S.CANVAS_BOUNDS,
      clawdFx: FX_BOUNDS,
      diskCard: CARD,
    },
  });
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
  OUT_DIR, TITLES, SCENES, S1_LINES, S2_LINES, S3_LINES,
  STATUS, STATUS_AT, SCENE_STARTS, WHITE_START, WHITE_END,
  SUB_LINES, SUB_WINDOWS, CARD, CLAWD_BOX, FX_BOUNDS,
  CHECK_TITLE: 'E05 Surprise v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: HEADER, size: 10, color: C.dim },
    { text: ROW_FULL, size: 10, color: C.red },
    { text: '[DSH] ALERT: no space left on device', size: 10, color: C.red },
    { text: '谁放进来的？', size: 10, color: C.white },
    { text: '100%', size: 10, color: C.amber },
  ],
  layoutAt,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
