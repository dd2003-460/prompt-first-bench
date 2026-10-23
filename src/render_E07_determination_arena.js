#!/usr/bin/env node
'use strict';
// E07 · 目标 (determination) — 「finish before sunrise，时钟 23:58 → 00:00」
// 画布 640×360 (SCALE=2 → 1280×720) @60fps, 1800 帧 = 30.00s
//   S1 0-10s  : `cat task.txt` = "finish before sunrise" · 时钟 23:58 · Clawd determined (thinking)
//   S2 10-20s : build / test / lint / deploy 快速滚动 · 时钟 23:59
//   S3 20-30s : "deployed ✓" · 时钟 00:00 · Clawd 释然 (smile) · 字幕「赶上了。」

const path = require('path');
const S = require('./pixel_story_arena');

const { C, LINE_Y, TERM, SUB, CLAWD_ROOM } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E07_determination_arena');

const T_TASK = 'clawd@dsh:~$ — task.txt';
const T_DEPLOY = 'clawd@dsh:~$ — deploy';

// --- 字幕 ---
const SUB_LINES = ['日出之前。', '还有两分钟。', '赶上了。'];
const SUB_WINDOWS = [{ start: 2.0, end: 8.0 }, { start: 11.5, end: 18.5 }, { start: 23.0, end: 29.0 }];

// --- S1: 任务 + 23:58 ---
const S1_STATUS = '[DSH] deadline: sunrise · t-2min';
const S1_LINES = [
  { y: LINE_Y[0], start: 0.6, charMs: 120, parts: [{ text: '$ ', color: C.green }, { text: 'cat task.txt', color: C.text }] },
  { y: LINE_Y[1], start: 3.0, charMs: 90, parts: [{ text: 'finish before sunrise', color: C.amber }] },
  { y: LINE_Y[2], start: 4.9, typed: false, parts: [{ text: 'deadline: 00:00', color: C.dim }] },
  { y: LINE_Y[3], start: 5.3, typed: false, parts: [{ text: 'owner: clawd', color: C.dim }] },
  { y: LINE_Y[4], start: 5.7, typed: false, parts: [{ text: 'status: ', color: C.dim }, { text: 'not yet', color: C.red }] },
];

// --- S2: 快速滚动 build/test/lint/deploy, 时钟 23:59 ---
const S2_STATUS = '[DSH] build 3/3 · deploy running';
const S2_LINES = [
  { y: LINE_Y[0], start: 10.3, charMs: 50, parts: [{ text: '$ ', color: C.green }, { text: './ship.sh --now', color: C.text }] },
  { y: LINE_Y[1], start: 11.2, typed: false, parts: [{ text: '[1/4] build   ', color: C.text }, { text: '✓', color: C.green }] },
  { y: LINE_Y[2], start: 11.8, typed: false, parts: [{ text: '[2/4] test 214', color: C.text }, { text: '✓', color: C.green }] },
  { y: LINE_Y[3], start: 12.4, typed: false, parts: [{ text: '[3/4] lint    ', color: C.text }, { text: '✓', color: C.green }] },
  { y: LINE_Y[4], start: 13.0, typed: false, parts: [{ text: '[4/4] deploy  ', color: C.text }, { text: '···', color: C.amber }] },
];

// S2 滚动日志行 (y=LINE_Y[5]=294, 每 0.2s 换一行, 固定 24 字符宽)
const ROLL_START = 13.6;
const ROLL_EVERY = 0.2;
const ROLL_LOGS = [
  'push image → registry   ',
  'health check 200 OK     ',
  'dns switch → prod       ',
  'warming 4 regions       ',
  'cutover 10% → 50%       ',
  'cutover 50% → 100%      ',
];
const rollIndex = (t) => Math.max(0, Math.floor((t - ROLL_START) / ROLL_EVERY));
const S2_ROLL_LINE = {
  y: LINE_Y[5], start: ROLL_START, typed: false, parts: [{ text: ROLL_LOGS[0], color: C.dim }],
};

// --- S3: deployed ✓ · 00:00 ---
const S3_STATUS = '[DSH] deployed · 00:00 · sunrise in 5h';
const S3_LINES = [
  { y: LINE_Y[0], start: 20.5, charMs: 90, parts: [{ text: '$ ', color: C.green }, { text: 'tail -f deploy.log', color: C.text }] },
  { y: LINE_Y[1], start: 22.4, typed: false, parts: [{ text: '✓ ', color: C.green }, { text: 'build passed', color: C.dim }] },
  { y: LINE_Y[2], start: 22.8, typed: false, parts: [{ text: '✓ ', color: C.green }, { text: 'tests passed', color: C.dim }] },
  { y: LINE_Y[3], start: 23.4, typed: false, parts: [{ text: '✓ ', color: C.green }, { text: 'deployed', color: C.green }, { text: '   00:00', color: C.white }] },
  { y: LINE_Y[4], start: 24.4, typed: false, parts: [{ text: '完成时间 00:00 · 距离日出 5h', color: C.amber }] },
];

// ---------------- 右侧时钟 / 进度面板 (terminal 右缘 540 → 552..628) ----------------
const CLOCK = { x: 552, y: 186, w: 76, h: 76 };
const PROG = { x: 552, y: 270, w: 76, h: 58 };

function clockDigits(t) {
  if (t < 20) return t < 12 ? '23:58' : '23:59';
  return '00:00';
}

function clockShown(t) {
  const time = clockDigits(t);
  const blink = Math.floor(t * 2) % 2 === 0;
  return t >= 12 && t < 20 && !blink ? time.replace(':', ' ') : time;
}

function clockAccent(t) {
  if (t >= 20) return C.green;
  return t < 12 ? C.amber : C.red;
}

function panelBg(ctx, box) {
  const { x, y, w, h } = box;
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.16)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);
}

function drawClock(ctx, t) {
  const { x, y, w, h } = CLOCK;
  panelBg(ctx, CLOCK);
  S.txt(ctx, x + 8, y + 8, 'DEADLINE', C.dim, 10);
  S.txt(ctx, x + w / 2, y + 26, clockShown(t), clockAccent(t), 14, 'center');
  S.txt(ctx, x + 8, y + 52, t >= 20 ? 'done' : 'to 00:00', C.dim, 10);
}

function deployPct(t) {
  if (t < ROLL_START) return 34;
  return Math.min(100, 34 + Math.round((t - ROLL_START) / 6 * 66));
}

function drawProgress(ctx, t) {
  const { x, y, w, h } = PROG;
  const pct = deployPct(t);
  const done = pct >= 100;
  panelBg(ctx, PROG);
  S.txt(ctx, x + 8, y + 6, 'DEPLOY', C.dim, 10);
  S.txt(ctx, x + w / 2, y + 22, `${pct}%`, done ? C.green : C.amber, 14, 'center');
  const bx = x + 8;
  const by = y + 44;
  const bw = w - 16;
  S.px(ctx, bx, by, bw, 6, C.termBg);
  S.px(ctx, bx, by, bw, 1, C.border);
  S.px(ctx, bx, by + 5, bw, 1, C.border);
  const fill = Math.round((bw - 2) * (pct / 100));
  if (fill > 0) S.px(ctx, bx + 1, by + 1, fill, 4, done ? C.green : C.amber);
}

// ---------------- Clawd 姿态 ----------------
const bobOf = (t) => (Math.sin(t * 2.2) > 0.45 ? -1 : 0);

function drawClawdDetermined(ctx, x, y, t) {
  S.drawClawd(ctx, x, y, t, 'thinking', 0);
  const by = Math.round(y + bobOf(t));
  // 专注的眉线
  S.px(ctx, x + 9, by + 5, 5, 1, C.clawdEye);
  S.px(ctx, x + 26, by + 5, 5, 1, C.clawdEye);
  // 决心光点 (闪烁)
  if (Math.sin(t * 5) > 0) S.px(ctx, x + 19, by - 6, 3, 3, C.amber);
}

function drawClawdRelieved(ctx, x, y, t) {
  S.drawClawd(ctx, x, y, t, 'smile', 0);
  const by = Math.round(y + bobOf(t));
  // 松一口气: 上浮的呼吸点
  const rise = Math.floor((t * 6) % 16);
  S.px(ctx, x + 43, by + 10 - rise, 2, 2, `rgba(126,231,135,${(1 - rise / 16).toFixed(2)})`);
  S.px(ctx, x + 46, by + 14 - rise, 1, 1, `rgba(126,231,135,${Math.max(0, 0.7 - rise / 24).toFixed(2)})`);
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_TASK, C.amber);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 0.4) S.drawStatus(ctx, S1_STATUS, C.amber);
  drawClawdDetermined(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t);
  drawClock(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, T_DEPLOY, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= ROLL_START) S.txt(ctx, S.TEXT_X, LINE_Y[5], ROLL_LOGS[rollIndex(t) % ROLL_LOGS.length], C.dim, 10);
  if (t >= 10.2) S.drawStatus(ctx, S2_STATUS, C.amber);
  drawClawdDetermined(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t);
  drawClock(ctx, t);
  drawProgress(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  // 20s 起天色微亮 (日出之前 → 天边泛光)
  const dawn = S.easeInOut((t - 21) / 8) * 0.32;
  S.drawBackground(ctx, t, dawn);
  S.drawTerminal(ctx, T_DEPLOY, C.green);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 20.2) S.drawStatus(ctx, S3_STATUS, C.green);
  drawClawdRelieved(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t);
  drawClock(ctx, t);
  drawProgress(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < 10) drawS1(ctx, t);
  else if (t < 20) drawS2(ctx, t);
  else drawS3(ctx, t);
}

// --- 键盘音: 每个打字字符 1 click + 行出现事件 ---
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
    4.9, 5.3, 5.7,
    11.2, 11.8, 12.4, 13.0,
    22.4, 22.8, 23.4, 24.4,
  ]);
}

function typingSchedule(lines, limit) {
  const typed = lines.filter((l) => l.typed !== false);
  return typed.map((line) => {
    const next = lines[lines.indexOf(line) + 1];
    return {
      text: S.lineText(line), start: line.start, charMs: line.charMs || S.TYPE_CHAR_MS,
      limit, strictBefore: next ? next.start : undefined,
    };
  });
}

const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S2_LINES, 19.8),
  ...typingSchedule(S3_LINES, 29.8),
];

function panelLayout() {
  return [
    { name: 'clock_label', box: S.textBox(CLOCK.x + 8, CLOCK.y + 8, 'DEADLINE', 10) },
    { name: 'clock_time', box: S.textBox(CLOCK.x + CLOCK.w / 2, CLOCK.y + 26, 'OO:OO', 14, 'center') },
    { name: 'clock_foot', box: S.textBox(CLOCK.x + 8, CLOCK.y + 52, 'to 00:00', 10) },
    { name: 'prog_label', box: S.textBox(PROG.x + 8, PROG.y + 6, 'DEPLOY', 10) },
    { name: 'prog_pct', box: S.textBox(PROG.x + PROG.w / 2, PROG.y + 22, '100%', 14, 'center') },
    { name: 'prog_bar', box: [PROG.x + 8, PROG.y + 44, PROG.w - 16, 6] },
  ];
}

function layoutAt(t) {
  const scene = t < 10 ? 1 : t < 20 ? 2 : 3;
  const base = scene === 1 ? S1_LINES : scene === 2 ? S2_LINES : S3_LINES;
  const status = scene === 1 ? S1_STATUS : scene === 2 ? S2_STATUS : S3_STATUS;
  const title = scene === 1 ? T_TASK : T_DEPLOY;

  let lines = base;
  if (scene === 2 && t >= ROLL_START) {
    const idx = rollIndex(t) % ROLL_LOGS.length;
    lines = [...base, { ...S2_ROLL_LINE, parts: [{ text: ROLL_LOGS[idx], color: C.dim }] }];
  }

  const fx = [];
  if (scene === 1) fx.push({ name: 'determine_spark', box: [CLAWD_ROOM.x + 19, CLAWD_ROOM.y - 7, 4, 4] });
  if (scene === 3) fx.push(
    { name: 'breath_dot_1', box: [CLAWD_ROOM.x + 41, CLAWD_ROOM.y - 6, 4, 21] },
    { name: 'breath_dot_2', box: [CLAWD_ROOM.x + 47, CLAWD_ROOM.y - 2, 3, 19] },
  );

  const groups = {
    foreground: [
      { name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] },
      { name: 'clawd', box: [CLAWD_ROOM.x, CLAWD_ROOM.y - 1, 40, 25] },
      { name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] },
    ],
    titleBar: S.titleLayout(title),
    content: S.contentLayout(lines, status),
    subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, t),
    fx,
  };

  if (scene !== 1) {
    groups.panel = panelLayout();
  } else {
    groups.panel = [
      { name: 'clock_label', box: S.textBox(CLOCK.x + 8, CLOCK.y + 8, 'DEADLINE', 10) },
      { name: 'clock_time', box: S.textBox(CLOCK.x + CLOCK.w / 2, CLOCK.y + 26, 'OO:OO', 14, 'center') },
      { name: 'clock_foot', box: S.textBox(CLOCK.x + 8, CLOCK.y + 52, 'to 00:00', 10) },
    ];
  }

  return {
    scene,
    groups,
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      titleBar: S.TITLE_BOUNDS,
      content: S.CONTENT,
      subtitle: S.SUB,
      panel: { x: CLOCK.x, y: CLOCK.y, w: CLOCK.w, h: PROG.y + PROG.h - CLOCK.y },
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
  OUT_DIR, T_TASK, T_DEPLOY,
  SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  CLOCK, PROG, ROLL_START, ROLL_EVERY, ROLL_LOGS, clockDigits, deployPct,
  CHECK_TITLE: 'E07 Determination Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ cat task.txt', size: 10, color: C.text },
    { text: '23:59', size: 14, color: C.red },
    { text: '✓ deployed   00:00', size: 10, color: C.green },
    { text: SUB_LINES[2], size: 10, color: C.white },
  ],
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
