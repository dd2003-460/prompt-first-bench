#!/usr/bin/env node
'use strict';
// E05 · 惊讶 (surprise) — 「df -h 突然 100%，陌生进程出现」
// 画布 640×360 (SCALE=2 → 1280×720) @60fps, 1800 帧 = 30.00s
//   S1 0-10s  : `df -h` 一切正常 25% · Clawd calm · 字幕「一切正常。」
//   S2 10-15s : 0.5s 白屏 → `df -h` 100% · Clawd surprised · 字幕「全满了。」
//   S3 15-30s : `ps aux` 陌生进程 PID 9999 · Clawd 后仰 · 字幕「谁放进来的？」
// 像素标准 SOP 05: 4-6px 像素块 / Fusion Pixel 10px / Clawd 40×17 / 终端 440×200

const path = require('path');
const S = require('./pixel_story_arena');

const { C, TEXT_X, STATUS_Y, LINE_Y, TERM, SUB, BW, BH, CLAWD_ROOM } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E05_surprise_arena');

const T_DF = 'clawd@dsh:~$ — E05 · surprise';
const T_PS = 'clawd@dsh:~$ — ps aux';

// --- Subtitles (10px Fusion Pixel, 160ms/char) ---
const SUB_LINES = ['一切正常。', '全满了。', '谁放进来的？'];
const SUB_WINDOWS = [{ start: 2.0, end: 8.0 }, { start: 11.2, end: 14.6 }, { start: 21.5, end: 29.0 }];

// --- df / ps column alignment (monospace 5px/ASCII char) ---
const padR = (s, n) => s + ' '.repeat(Math.max(0, n - s.length));
const padL = (s, n) => ' '.repeat(Math.max(0, n - s.length)) + s;
const dfRow = (name, size, used, avail, pct, mount) =>
  padR(name, 16) + padL(size, 6) + padL(used, 6) + padL(avail, 6) + padL(pct, 6) + ' ' + mount;
const DF_HEADER = padR('Filesystem', 16) + padL('Size', 6) + padL('Used', 6) + padL('Avail', 6) + padL('Use%', 6) + ' Mounted on';
const psRow = (user, pid, cpu, cmd) => padR(user, 9) + padL(pid, 6) + padL(cpu, 6) + '  ' + cmd;
const PS_HEADER = padR('USER', 9) + padL('PID', 6) + padL('%CPU', 6) + '  COMMAND';

// --- S1: 一切正常 (0-10s) ---
const S1_STATUS = '[DSH] disk 25% · all clean';
const S1_LINES = [
  { y: LINE_Y[0], start: 0.6, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], start: 2.2, typed: false, parts: [{ text: DF_HEADER, color: C.dim }] },
  { y: LINE_Y[2], start: 2.5, typed: false, parts: [{ text: dfRow('/dev/vda1', '40G', '10G', '30G', '25%', '/'), color: C.text }] },
  { y: LINE_Y[3], start: 2.8, typed: false, parts: [{ text: dfRow('/dev/vdb1', '200G', '50G', '150G', '25%', '/memory'), color: C.green }] },
  { y: LINE_Y[4], start: 3.1, typed: false, parts: [{ text: dfRow('tmpfs', '2.0G', '12M', '2.0G', '1%', '/tmp'), color: C.dim }] },
];

// --- S2: 100% (10-15s) ---
const S2_STATUS = '[DSH] disk 100% · QUOTA EXCEEDED';
const S2_LINES = [
  { y: LINE_Y[0], start: 10.0, charMs: 60, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  {
    y: LINE_Y[1], start: 10.5, typed: false,
    parts: [{ text: dfRow('/dev/vda1', '40G', '40G', '0', '100%', '/'), color: C.red }],
  },
  {
    y: LINE_Y[2], start: 10.8, typed: false,
    parts: [{ text: dfRow('/dev/vdb1', '200G', '199G', '1.0G', '100%', '/memory'), color: C.red }],
  },
  { y: LINE_Y[3], start: 11.1, typed: false, parts: [{ text: '!! free space: 0 bytes', color: C.red }] },
  { y: LINE_Y[4], start: 11.4, typed: false, parts: [{ text: '==> all writes blocked', color: C.amber }] },
];

// --- S3: 陌生进程 (15-30s) ---
const S3_STATUS = '[DSH] 1 unknown process · origin: ???';
const S3_LINES = [
  { y: LINE_Y[0], start: 15.6, charMs: 110, parts: [{ text: '$ ', color: C.green }, { text: 'ps aux', color: C.text }] },
  { y: LINE_Y[1], start: 17.0, typed: false, parts: [{ text: PS_HEADER, color: C.dim }] },
  { y: LINE_Y[2], start: 17.5, typed: false, parts: [{ text: psRow('???', '9999', '99.9', '/usr/bin/.hidden'), color: C.red }] },
  { y: LINE_Y[3], start: 18.0, typed: false, parts: [{ text: psRow('???', '9991', '0.1', '/usr/bin/.hidden --child'), color: C.amber }] },
  { y: LINE_Y[4], start: 18.5, typed: false, parts: [{ text: psRow('root', '1', '0.0', '/sbin/init'), color: C.dim }] },
];

// 右侧磁盘水位卡片 (terminal 右缘 540 → 552..628, subtitle y=340 之上)
const GAUGE = { x: 552, y: 186, w: 76, h: 96 };
const GAUGE_LABEL = 'DISK';
const GAUGE_FOOT = 'used';

function drawGauge(ctx, ratio, text, color) {
  const { x, y, w, h } = GAUGE;
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.16)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);
  S.txt(ctx, x + 8, y + 8, GAUGE_LABEL, C.dim, 10);
  S.txt(ctx, x + w / 2, y + 26, text, color, 14, 'center');
  const bx = x + 8;
  const by = y + 54;
  const bw = w - 16;
  const bh = 10;
  S.px(ctx, bx, by, bw, bh, C.termBg);
  S.px(ctx, bx, by, bw, 1, C.border);
  S.px(ctx, bx, by + bh - 1, bw, 1, C.border);
  S.px(ctx, bx, by, 1, bh, C.border);
  S.px(ctx, bx + bw - 1, by, 1, bh, C.border);
  const fill = Math.round((bw - 4) * ratio);
  if (fill > 0) S.px(ctx, bx + 2, by + 2, fill, bh - 4, color);
  S.txt(ctx, x + 8, y + 74, GAUGE_FOOT, C.dim, 10);
}

function gaugeLayout(text) {
  return [
    { name: 'gauge_label', box: S.textBox(GAUGE.x + 8, GAUGE.y + 8, GAUGE_LABEL, 10) },
    { name: 'gauge_pct', box: S.textBox(GAUGE.x + GAUGE.w / 2, GAUGE.y + 26, text, 14, 'center') },
    { name: 'gauge_bar', box: [GAUGE.x + 8, GAUGE.y + 54, GAUGE.w - 16, 10] },
    { name: 'gauge_foot', box: S.textBox(GAUGE.x + 8, GAUGE.y + 74, GAUGE_FOOT, 10) },
  ];
}

// --- Clawd 表情 (base 40×17 保持 SOP 标准, 表情为像素叠加) ---
const clawdBob = (t) => (Math.sin(t * 2.2) > 0.45 ? -1 : 0);

function drawClawdSurprised(ctx, x, y, t) {
  S.drawClawd(ctx, x, y, t, 'calm', 0);
  const by = Math.round(y + clawdBob(t));
  // 6×6 睁大的眼睛 + 2×2 瞳孔 (取代 calm 的 4×4)
  for (const ex of [9, 25]) {
    S.px(ctx, x + ex, by + 5, 6, 6, C.white);
    S.px(ctx, x + ex + 2, by + 7, 2, 2, C.clawdEye);
  }
  // 惊讶的小圆嘴
  S.px(ctx, x + 19, by + 12, 3, 3, C.clawdEye);
  // 冷汗
  S.px(ctx, x + 35, by + 1, 2, 4, C.blue);
  S.px(ctx, x + 35, by + 5, 2, 1, C.blue);
}

function drawClawdRecoil(ctx, x, y, t) {
  drawClawdSurprised(ctx, x, y, t);
  const by = Math.round(y + clawdBob(t));
  // 惊呼感叹号
  S.txt(ctx, x + 42, y - 6, '!', C.red, 10);
  // 后仰运动线
  S.px(ctx, x - 18, by + 4, 10, 2, C.dim);
  S.px(ctx, x - 14, by + 9, 8, 2, C.dim);
  S.px(ctx, x - 10, by + 14, 6, 2, C.dim);
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_DF, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 0.4) S.drawStatus(ctx, S1_STATUS, C.dim);
  S.drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'calm', 0);
  drawGauge(ctx, 0.25, '25%', C.green);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_DF, C.red);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 10.2) S.drawStatus(ctx, S2_STATUS, C.red);
  drawClawdSurprised(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y - 1, t);
  drawGauge(ctx, 1, '100%', C.red);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
  // 0.5s 白屏: t=10.0 全白 → t=10.5 完全显现
  if (t < 10.5) {
    const a = 1 - S.clamp01((t - 10) / 0.5);
    S.px(ctx, 0, 0, BW, BH, `rgba(255,255,255,${a.toFixed(3)})`);
  }
}

const RECOIL = { dx: -4, dy: -2 };

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_PS, C.red);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 19.0) S.drawStatus(ctx, S3_STATUS, C.red);
  drawClawdRecoil(ctx, CLAWD_ROOM.x + RECOIL.dx, CLAWD_ROOM.y + RECOIL.dy, t);
  drawGauge(ctx, 1, '100%', C.red);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < 10) {
    drawS1(ctx, t);
  } else if (t < 15) {
    drawS2(ctx, t);
  } else {
    drawS3(ctx, t);
  }
  // S2 → S3 的 0.2s 黑场 (scenes 内唯一非白屏转场)
  const fadeStart = 15 - 0.2;
  if (t >= fadeStart && t < 15) {
    S.px(ctx, 0, 0, BW, BH, `rgba(0,0,0,${S.clamp01((t - fadeStart) / 0.2).toFixed(3)})`);
  } else if (t >= 15 && t < 15.2) {
    S.px(ctx, 0, 0, BW, BH, `rgba(0,0,0,${(1 - S.clamp01((t - 15) / 0.2)).toFixed(3)})`);
  }
}

// --- 键盘音: 每个打字字符 1 次 click + 面板事件 ---
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
    2.2, 2.5, 2.8, 3.1,
    10.5, 10.8, 11.1, 11.4,
    17.0, 17.5, 18.0, 18.5,
  ]);
}

function typingSchedule(lines, limit) {
  const typed = lines.filter((l) => l.typed !== false);
  return typed.map((line) => {
    const idx = lines.indexOf(line);
    const next = lines[idx + 1];
    return {
      text: S.lineText(line),
      start: line.start,
      charMs: line.charMs || S.TYPE_CHAR_MS,
      limit,
      strictBefore: next ? next.start : undefined,
    };
  });
}

const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S2_LINES, 14.8),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const scene = t < 10 ? 1 : t < 15 ? 2 : 3;
  const lines = scene === 1 ? S1_LINES : scene === 2 ? S2_LINES : S3_LINES;
  const status = scene === 1 ? S1_STATUS : scene === 2 ? S2_STATUS : S3_STATUS;
  const title = scene === 3 ? T_PS : T_DF;
  const pct = scene === 1 ? '25%' : '100%';

  const lean = scene === 3 ? RECOIL.dx : 0;
  const lift = scene === 3 ? RECOIL.dy : scene === 2 ? -1 : 0;
  const cx = CLAWD_ROOM.x + lean;
  const cy = CLAWD_ROOM.y + lift;

  const foreground = [
    { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
    { name: 'clawd', box: [cx, cy - 1, 40, 25] },
    { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
  ];

  const fx = [{ name: 'sweat', box: [cx + 34, cy - 3, 5, 9] }];
  if (scene === 3) {
    fx.push(
      { name: 'alert_bang', box: [cx + 42, cy - 6, 5, 14] },
      { name: 'motion_line_1', box: [cx - 18, cy + 2, 10, 2] },
      { name: 'motion_line_2', box: [cx - 14, cy + 7, 8, 2] },
      { name: 'motion_line_3', box: [cx - 10, cy + 12, 6, 2] },
    );
  }

  return {
    scene,
    groups: {
      foreground,
      titleBar: S.titleLayout(title),
      content: S.contentLayout(lines, status),
      subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, t),
      gauge: gaugeLayout(pct),
      fx,
    },
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      titleBar: S.TITLE_BOUNDS,
      content: S.CONTENT,
      subtitle: S.SUB,
      gauge: GAUGE,
      fx: S.CANVAS_BOUNDS,
    },
  };
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) console.log(JSON.stringify({ count: getClickTimestamps().length, clicks: getClickTimestamps() }));
  else renderer.renderAllFrames();
}

module.exports = {
  ...S,
  OUT_DIR,
  T_DF, T_PS,
  SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  GAUGE, RECOIL,
  CHECK_TITLE: 'E05 Surprise Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ df -h', size: 10, color: C.text },
    { text: DF_HEADER, size: 10, color: C.dim },
    { text: '[DSH] disk 100% · QUOTA EXCEEDED', size: 10, color: C.red },
    { text: SUB_LINES[2], size: 10, color: C.white },
  ],
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
