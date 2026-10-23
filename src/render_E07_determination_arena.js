#!/usr/bin/env node
'use strict';
// E07 目标 (determination) — 30s, 1800 frames @ 60fps, 1280×720.
// 事实源 (episodes.md, batch-6 任务书): 任务栏只有一行 `finish before sunrise`，时钟 23:58→00:00。
//   S1 (0-10s)  深夜任务: `$ cat task.txt` → `finish before sunrise`；右上角墙钟 23:58；
//               Clawd determined（睁眼 + 2×2 高光 + 抿嘴 + 压眉）；字幕「天亮之前。」
//   S2 (10-20s) 疯狂工作: 10 行 build/test/deploy 日志快速打出，第 9/10 行到来时终端内容向上
//               平滑滚动 17px×2（0.3s easeInOut，逐帧整数像素）；10s 时钟跳 23:59；字幕「还差一点。」
//   S3 (20-30s) 完成: `> deployed ✓` / `$ echo "done"` / `done`；22s 时钟跳 00:00；
//               24s `$ date` → `Thu Oct 24 00:00:01 CST 2026`；Clawd determined → relieved；
//               字幕 27s「赶上了。」/ 28.6s「（天还没亮）」（任务书写作 30s，30s 起在 30s 片长里不可见，故提前到 28.6s）
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// 窗外保持深夜（dawnProgress=0）——「天还没亮」。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, CONTENT, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E07_determination_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — task.txt',
  S2: 'clawd@dsh:~ — npm run build',
  S3: 'clawd@dsh:~ — deploy --prod',
};
const SUB_LINES = ['天亮之前。', '还差一点。', '赶上了。', '（天还没亮）'];
const SUB_WINDOWS = [
  { start: 2.2, end: 8.6 },
  { start: 12.0, end: 18.0 },
  { start: 27.0, end: 28.4 },
  { start: 28.6, end: 29.9 },
];

// --- 右上角墙钟 (52×22 @ 584,26)：23:58 → 23:59 (10s) → 00:00 (22s) -------
const CLOCK = { x: 584, y: 26, w: 52, h: 22 };
const CLOCK_CHANGES = [10, 22];
const CLOCK_FLASH = 0.2;
// 10s 的跳变正好落在 0.25s 场景黑场里，闪光推迟到黑场结束 (10.25s) 之后才打；22s 无黑场。
const CLOCK_FLASH_AT = [10.3, 22.0];
function clockAt(t) { return t < CLOCK_CHANGES[0] ? '23:58' : t < CLOCK_CHANGES[1] ? '23:59' : '00:00'; }
function clockLit(t) { return CLOCK_FLASH_AT.some((c) => t >= c && t < c + CLOCK_FLASH); }
function drawClock(ctx, t) {
  const { x, y, w, h } = CLOCK;
  const lit = clockLit(t);
  px(ctx, x, y, w, h, C.termTitle);
  px(ctx, x, y, w, 2, lit ? C.amber : C.termBd);
  px(ctx, x, y + h - 2, w, 2, lit ? C.amber : C.termBd);
  px(ctx, x, y, 2, h, lit ? C.amber : C.termBd);
  px(ctx, x + w - 2, y, 2, h, lit ? C.amber : C.termBd);
  // 小圆钟图标 10×10
  const ic = lit ? C.white : C.dim;
  px(ctx, x + 8, y + 6, 6, 1, ic);
  px(ctx, x + 7, y + 7, 8, 6, ic);
  px(ctx, x + 8, y + 13, 6, 1, ic);
  px(ctx, x + 11, y + 8, 1, 3, lit ? C.amber : C.text);
  px(ctx, x + 11, y + 10, 3, 1, lit ? C.amber : C.text);
  S.txt(ctx, x + 22, y + 5, clockAt(t), lit ? C.white : C.amber, 10);
}

// --- S1: the single task line ---------------------------------------------
const S1_LINES = [
  {
    y: S.LINE_Y[0], start: 0.9, charMs: 90,
    parts: [{ text: '$ ', color: C.green }, { text: 'cat task.txt', color: C.text }],
  },
  { y: S.LINE_Y[1], start: 2.6, charMs: 80, parts: [{ text: 'finish before sunrise', color: C.amber }] },
];
const S1_STATUS = '[DSH] task.txt · 1 line · deadline: sunrise';
const S1_STATUS_AT = 5.0;

// --- S2: frantic build log, 10 rows @17px with two smooth 17px scrolls ----
const ROW_TOP = 160; // = CONTENT.y：滚出的行靠 clip 逐像素滑出，停稳时 8 行正好铺满 160..293
const ROW_GAP = 17;
const VIEW_ROWS = 8;
const SCROLL_MS = 0.3;
const S2_LINES = [
  { y: 0, start: 10.4, charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'npm run build', color: C.text }] },
  { y: 1, start: 11.4, charMs: 55, parts: [{ text: '> building...', color: C.dim }] },
  { y: 2, start: 12.3, charMs: 60, parts: [{ text: '> 99.9%', color: C.amber }] },
  { y: 3, start: 13.0, charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'npm test', color: C.text }] },
  { y: 4, start: 13.8, charMs: 50, parts: [{ text: '> 47 passed, 0 failed', color: C.green }] },
  { y: 5, start: 15.1, charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'npm run build', color: C.text }] },
  { y: 6, start: 16.1, charMs: 55, parts: [{ text: '> building...', color: C.dim }] },
  { y: 7, start: 17.0, charMs: 60, parts: [{ text: '> 100%', color: C.green }] },
  { y: 8, start: 17.6, charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'deploy --prod', color: C.text }] },
  { y: 9, start: 18.6, charMs: 55, parts: [{ text: '> deploying...', color: C.blue }] },
];
const S2_STATUS = '[DSH] build · test · deploy';
const S2_STATUS_AT = 19.6;
// 先滚后打：滚动在新行开打前 0.02s 完成，新行直接落在末行槽位（终端行为）
const SCROLL_STEPS = [
  { at: S2_LINES[8].start - 0.32, value: ROW_GAP },
  { at: S2_LINES[9].start - 0.32, value: ROW_GAP * 2 },
];
function scrollAt(t) {
  let value = 0;
  for (const step of SCROLL_STEPS) {
    if (t >= step.at + SCROLL_MS) { value = step.value; continue; }
    if (t >= step.at) {
      return Math.round(value + (step.value - value) * S.easeInOut((t - step.at) / SCROLL_MS));
    }
    break;
  }
  return value;
}
// 某一时刻 S2 的可见行（带裁剪后的 box；完全滚出的行不画也不申报）
function s2Visible(t) {
  const scroll = scrollAt(t);
  const out = [];
  for (const line of S2_LINES) {
    if (t < line.start) continue;
    const yRaw = ROW_TOP + line.y * ROW_GAP - scroll;
    const top = Math.max(yRaw, CONTENT.y);
    const hh = Math.min(yRaw + 14, CONTENT.y + CONTENT.h) - top;
    if (hh <= 0) continue;
    const hhCur = Math.min(yRaw + 10, CONTENT.y + CONTENT.h) - top;
    out.push({ line, yRaw, top, hh, hhCur: Math.max(0, hhCur) });
  }
  return out;
}
function drawS2Rows(ctx, t) {
  ctx.save();
  ctx.beginPath();
  ctx.rect(CONTENT.x, CONTENT.y, CONTENT.w, CONTENT.h);
  ctx.clip();
  for (const row of s2Visible(t)) {
    const line = row.line;
    const shifted = { ...line, y: row.yRaw };
    S.drawTypedLine(ctx, shifted, t);
  }
  ctx.restore();
}

// --- S3: done before sunrise ----------------------------------------------
const S3_LINES = [
  { y: S.LINE_Y[0], start: 20.6, charMs: 70, parts: [{ text: '> deployed ✓', color: C.green }] },
  { y: S.LINE_Y[1], start: 21.7, charMs: 70, parts: [{ text: '$ ', color: C.green }, { text: 'echo "done"', color: C.text }] },
  { y: S.LINE_Y[2], start: 22.9, charMs: 90, parts: [{ text: 'done', color: C.text }] },
  { y: S.LINE_Y[3], start: 24.0, charMs: 80, parts: [{ text: '$ ', color: C.green }, { text: 'date', color: C.text }] },
  { y: S.LINE_Y[4], start: 24.8, charMs: 50, parts: [{ text: 'Thu Oct 24 00:00:01 CST 2026', color: C.blue }] },
];
const S3_STATUS = '[DSH] task done · 00:00:01 · sunrise pending';
const S3_STATUS_AT = 26.5;
const RELIEF_AT = 26.4;

const CLAWD_BOX = [S.CLAWD_ROOM.x, 244, 40, 31];

// --- Clawd: determined (睁眼+高光+抿嘴+压眉) / relieved (微闭+嘴角微扬) ----
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  if (mood !== 'determined' && mood !== 'relieved') {
    S.art.drawClawd(ctx, x, y + (opts.dy || 0), t, mood, warmMix);
    return;
  }
  const dy = opts.dy === undefined ? 0 : opts.dy;
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

  if (mood === 'determined') {
    // 完全睁开 (4×4 + 2×2 高光) + 压眉 + 抿嘴（一条 6px 直线）
    px(ctx, x + 9, by + 4, 5, 1, C.clawdEye);
    px(ctx, x + 26, by + 4, 5, 1, C.clawdEye);
    px(ctx, x + 10, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 26, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 11, by + 7, 2, 2, C.white);
    px(ctx, x + 27, by + 7, 2, 2, C.white);
    px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);
  } else {
    // relieved: 眼睛微闭 (4×2) + 嘴角微扬
    px(ctx, x + 10, by + 7, 4, 2, C.clawdEye);
    px(ctx, x + 26, by + 7, 4, 2, C.clawdEye);
    px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);
    px(ctx, x + 16, by + 12, 1, 1, C.clawdEye);
    px(ctx, x + 23, by + 12, 1, 1, C.clawdEye);
  }

  const step = Math.sin(t * 3.0) > 0.6 ? 1 : 0;
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

// --- Scene painters -------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  drawClock(ctx, t);
  S.drawTerminal(ctx, TITLES.S1, C.amber);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'determined', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  drawClock(ctx, t);
  S.drawTerminal(ctx, TITLES.S2, C.blue);
  drawS2Rows(ctx, t);
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'determined', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  drawClock(ctx, t);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= RELIEF_AT ? 'relieved' : 'determined', 0);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { start: 0, draw: drawS1 },
  { start: 10, draw: drawS2 },
  { start: 20, draw: drawS3 },
];

function renderAt(ctx, t) { S.renderScenes(ctx, t, SCENES); }

// --- Keyboard clicks: 每行逐字 1 次 click（密集但 ≥50ms/字）---------------
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
  ...typingSchedule(S1_LINES, 9.5),
  ...typingSchedule(S2_LINES, 19.6),
  ...typingSchedule(S3_LINES, 29.5),
];

// --- Layout groups (0px tolerance, per frame) -----------------------------
// 23:58 / 23:59 / 00:00 都是 5 个 ASCII 字符 = 25px，盒子尺寸与读数无关。
function clockLayout(t) {
  return [
    { name: 'clock_icon', box: [CLOCK.x + 6, CLOCK.y + 6, 10, 10] },
    { name: 'clock_digits', box: [CLOCK.x + 22, CLOCK.y + 5, S.textWidth(clockAt(t), 10), 14] },
  ];
}

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  let layout;
  if (t < 10) {
    layout = S.baseLayout({
      ...common, scene: 1, title: TITLES.S1, lines: S1_LINES,
      status: t >= S1_STATUS_AT ? S1_STATUS : null,
    });
  } else if (t < 20) {
    layout = S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: [],
      status: t >= S2_STATUS_AT ? S2_STATUS : null,
    });
    const rows = s2Visible(t);
    layout.groups.content = [];
    rows.forEach((row, i) => {
      const full = S.lineText(row.line);
      const w = S.textWidth(full, 10);
      layout.groups.content.push({ name: `row_${i + 1}`, box: [TEXT_X, row.top, w, row.hh] });
      if (row.line.cursor !== false && row.hhCur > 0) {
        layout.groups.content.push({ name: `cursor_${i + 1}`, box: [TEXT_X + w + 2, row.top, 6, row.hhCur] });
      }
    });
  } else {
    layout = S.baseLayout({
      ...common, scene: 3, title: TITLES.S3, lines: S3_LINES,
      status: t >= S3_STATUS_AT ? S3_STATUS : null,
    });
  }
  layout.groups.clock = clockLayout(t);
  layout.bounds.clock = CLOCK;
  layout.groups.foreground = S.foregroundLayout({
    terminal: true, clawd: false, her: false,
    extra: [
      { name: 'clawd', box: CLAWD_BOX },
      { name: 'clock', box: [CLOCK.x, CLOCK.y, CLOCK.w, CLOCK.h] },
    ],
  });
  return layout;
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR, { fadeIn: 0.4, fadeOut: 0.4 });

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
  S1_LINES, S1_STATUS, S1_STATUS_AT,
  S2_LINES, S2_STATUS, S2_STATUS_AT, ROW_TOP, ROW_GAP, VIEW_ROWS, SCROLL_MS, SCROLL_STEPS,
  S3_LINES, S3_STATUS, S3_STATUS_AT, RELIEF_AT,
  CLOCK, CLOCK_CHANGES, CLOCK_FLASH, CLOCK_FLASH_AT, clockAt, clockLit, scrollAt, s2Visible,
  CLAWD_BOX,
  CHECK_TITLE: 'E07 目标 (determination) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'finish before sunrise', size: 10, color: C.amber },
    { text: '> 47 passed, 0 failed', size: 10, color: C.green },
    { text: '> deployed ✓', size: 10, color: C.green },
    { text: 'Thu Oct 24 00:00:01 CST 2026', size: 10, color: C.blue },
    { text: '（天还没亮）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt,
  renderAt,
  drawClock,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
