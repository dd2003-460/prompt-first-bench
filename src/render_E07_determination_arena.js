#!/usr/bin/env node
'use strict';
// E07 · 目标 (determination) — finish before sunrise, 30s, 1800 frames.
//   S1 (0-10s):  `cat task.txt` → "finish before sunrise"; 时钟 23:58; Clawd determined
//   S2 (10-20s): 终端快速滚动 (build / test / deploy); 时钟 23:59
//   S3 (20-30s): "deployed ✓"; 时钟 00:00; Clawd 释然; 字幕「赶上了。」
// 时钟是终端上方的独立像素翻牌 (hud), 不占用 440×200 终端内容区.

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E07_determination_arena');
const TITLES = {
  S1: 'clawd@dsh:~$ — task',
  S2: 'clawd@dsh:~$ — build',
  S3: 'clawd@dsh:~$ — deploy',
};
const SUB_LINES = ['赶上了。'];
const SUB_WINDOWS = [{ start: 24.4, end: 29.0 }];

// 时钟 HUD: 终端左侧空白列 (x=4..96), 压在 Clawd 上方, 不与 440×200 终端相交
const CLOCK = { x: 4, y: 186, w: 92, h: 52 };

// --- S1 ---
const S1_LINES = [
  { y: LINE_Y[0], start: 0.6, charMs: 80, parts: [{ text: '$ ', color: C.green }, { text: 'cat task.txt', color: C.text }] },
  { y: LINE_Y[1], start: 2.4, charMs: 90, parts: [{ text: 'finish before sunrise', color: C.amber }] },
  { y: LINE_Y[2], start: 4.4, charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'date "+%H:%M"', color: C.text }] },
  { y: LINE_Y[3], start: 6.0, charMs: 90, parts: [{ text: '23:58', color: C.blue }] },
  { y: LINE_Y[4], start: 7.2, charMs: 70, parts: [{ text: '# 还有 2 分钟到天亮。', color: C.dim }] },
];
const S1_STATUS = '[DSH] target: sunrise 00:00 · remaining 2m';

// --- S2: 快速滚动 (6 行视窗内滚动, 越出视窗的行自动滚走) ---
const S2_LINES = [
  { start: 10.5, charMs: 40, parts: [{ text: '$ ', color: C.green }, { text: 'make release -j8', color: C.text }] },
  { start: 11.6, charMs: 18, parts: [{ text: 'build   ▸ 128 modules ok', color: C.text }] },
  { start: 12.5, charMs: 18, parts: [{ text: 'test    ▸ 512 passed, 0 failed', color: C.text }] },
  { start: 13.4, charMs: 18, parts: [{ text: 'bundle  ▸ 384 KB gzip', color: C.text }] },
  { start: 14.3, charMs: 18, parts: [{ text: 'push    ▸ origin/main ok', color: C.text }] },
  { start: 15.2, charMs: 18, parts: [{ text: 'deploy  ▸ waiting for slot...', color: C.amber }] },
  { start: 16.6, charMs: 20, parts: [{ text: 'deploy  ▸ 87% ...', color: C.amber }] },
  { start: 17.9, charMs: 20, parts: [{ text: 'deploy  ▸ 99% ...', color: C.amber }] },
  { start: 19.0, charMs: 20, parts: [{ text: 'deploy  ▸ slot acquired', color: C.green }] },
];

// 视窗: 只显示最近 6 行; 新行到达时整列上移一行 (滚动)
const ROWS = LINE_Y;
function latestIndex(lines, t) {
  let idx = -1;
  for (let i = 0; i < lines.length; i++) if (t >= lines[i].start) idx = i;
  return idx;
}
function s2View(t) {
  const idx = latestIndex(S2_LINES, t);
  if (idx < 0) return [];
  const scroll = Math.max(0, idx - (ROWS.length - 1));
  const out = [];
  for (let i = scroll; i <= idx; i++) out.push({ line: S2_LINES[i], y: ROWS[i - scroll], last: i === idx });
  return out;
}

const S2_STATUS = '[DSH] pipeline: running · 23:59';

// --- S3: 赶上了 ---
const S3_LINES = [
  { y: LINE_Y[0], start: 20.5, charMs: 70, parts: [{ text: '$ ', color: C.green }, { text: 'deploy --prod', color: C.text }] },
  { y: LINE_Y[1], start: 22.0, charMs: 50, parts: [{ text: '✓ deployed to prod', color: C.green }] },
  { y: LINE_Y[2], start: 23.4, charMs: 50, parts: [{ text: '  release v1.0.0 · 00:00:03', color: C.text }] },
  { y: LINE_Y[3], start: 25.0, charMs: 90, parts: [{ text: '$ ', color: C.green }, { text: 'date "+%H:%M"', color: C.text }] },
  { y: LINE_Y[4], start: 26.6, charMs: 90, parts: [{ text: '00:00', color: C.blue }] },
  { y: LINE_Y[5], start: 27.9, charMs: 60, parts: [{ text: '# 太阳还没出来。', color: C.dim }] },
];
const S3_STATUS = '[DSH] status: deployed · before sunrise';

// 时钟: [时, 分] + 秒针式进度
function clockAt(t) {
  if (t < 10) return { hh: '23', mm: '58', sub: 'to sunrise', accent: C.blue, k: 0 };
  if (t < 20) {
    // 23:59 在这一幕里从 :58 跳到 :59 (10.0-10.4 之间), 之后一直 23:59
    return { hh: '23', mm: '59', sub: 'to sunrise', accent: C.amber, k: S.clamp01((t - 10) / 9.5) };
  }
  const k = S.clamp01((t - 20) / 6);
  return { hh: '00', mm: '00', sub: t < 22.4 ? 'to sunrise' : 'made it', accent: C.green, k };
}

function drawClock(ctx, t) {
  const { hh, mm, sub, accent, k } = clockAt(t);
  const { x, y, w, h } = CLOCK;
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.14)');
  S.px(ctx, x, y, w, h, C.panel);
  S.px(ctx, x, y, w, 2, C.border);
  S.px(ctx, x, y + h - 2, w, 2, C.border);
  S.px(ctx, x, y, 2, h, C.border);
  S.px(ctx, x + w - 2, y, 2, h, C.border);
  S.px(ctx, x + w / 2 - 2, y + 3, 4, 1, accent); // 顶部电源色条
  // 大号数字 (14px 点阵) + 闪烁冒号
  const colon = Math.floor(t * 2) % 2 === 0 ? ':' : ' ';
  S.txt(ctx, x + w / 2, y + 8, `${hh}${colon}${mm}`, accent, 14, 'center');
  S.txt(ctx, x + w / 2, y + 26, sub, C.dim, 10, 'center');
  // 分钟进度条
  const barW = w - 16;
  S.px(ctx, x + 8, y + h - 9, barW, 2, 'rgba(255,255,255,0.10)');
  S.px(ctx, x + 8, y + h - 9, Math.max(2, Math.round(barW * k)), 2, accent);
}

// --- Clawd ---
// expr: 'determined' | 'focused' | 'relieved'
function drawClawdExpr(ctx, x, y, t, expr) {
  let dy = 0;
  let mood = 'calm';
  if (expr === 'determined') {
    mood = 'thinking'; // 专注紫
    dy = 0;
  } else if (expr === 'focused') {
    mood = 'thinking';
    dy = Math.sin(t * 12) > 0 ? -1 : 0; // 紧绷的抖动
  } else if (expr === 'relieved') {
    mood = 'smile';
    dy = -1;
  }
  const by = Math.round(y + dy + (Math.sin(t * 2.2) > 0.45 ? -1 : 0));
  S.drawClawd(ctx, x, y + dy, t, mood, 0);

  if (expr === 'determined') {
    // 眉: 中间低两边高的斜线 (4×1 + 2×1)
    S.px(ctx, x + 9, by + 5, 4, 1, C.clawdEye);
    S.px(ctx, x + 26, by + 5, 4, 1, C.clawdEye);
    S.px(ctx, x + 13, by + 6, 2, 1, C.clawdEye);
    S.px(ctx, x + 25, by + 6, 2, 1, C.clawdEye);
    S.px(ctx, x + 8, by + 4, 2, 1, C.clawdNormDark);
    S.px(ctx, x + 30, by + 4, 2, 1, C.clawdNormDark);
  } else if (expr === 'focused') {
    // 只保留 4×2 的凝视眼 (drawClawd thinking 已画) + 咬牙线
    S.px(ctx, x + 16, by + 13, 8, 1, C.clawdEye);
  } else if (expr === 'relieved') {
    // 闭眼弧线 + 呼气
    S.px(ctx, x + 9, by + 7, 2, 1, C.clawdEye);
    S.px(ctx, x + 11, by + 6, 2, 1, C.clawdEye);
    S.px(ctx, x + 13, by + 7, 2, 1, C.clawdEye);
    S.px(ctx, x + 25, by + 7, 2, 1, C.clawdEye);
    S.px(ctx, x + 27, by + 6, 2, 1, C.clawdEye);
    S.px(ctx, x + 29, by + 7, 2, 1, C.clawdEye);
    const puff = Math.round((t * 4) % 6);
    S.px(ctx, x + 41 + puff, by + 6 - Math.round(puff / 2), 3, 2, 'rgba(255,255,255,0.35)');
  }
}

function clawdBox(expr) {
  const top = expr === 'relieved' ? 6 : 6;
  return [S.CLAWD_ROOM.x - 4, S.CLAWD_ROOM.y - top, 54, 32 + top];
}

const DIP_AT = 10.0;
const DIP2_AT = 20.0;
const DIP_LEN = 0.25;

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.blue);
  drawClock(ctx, t);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 8.0) S.drawStatus(ctx, S1_STATUS, C.blue);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'determined');
  // 倒计时紧迫感: 逐渐加深的蓝色压角
  const press = S.clamp01((t - 6) / 3) * 0.12;
  if (press > 0) S.px(ctx, 0, 0, S.BW, S.BH, `rgba(10,20,60,${press.toFixed(3)})`);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  drawClock(ctx, t);
  const view = s2View(t);
  view.forEach((item) => {
    if (item.last) {
      S.px(ctx, TEXT_X - 4, item.y - 3, 300, 15, 'rgba(227,179,65,0.10)');
    }
    S.drawTypedLine(ctx, { ...item.line, y: item.y, cursor: item.last }, t);
  });
  if (t >= 19.6) S.drawStatus(ctx, S2_STATUS, C.amber);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'focused');
}

function drawS3(ctx, t) {
  const dawn = S.easeInOut((t - 20.5) / 8) * 0.35;
  S.drawBackground(ctx, t, dawn);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  drawClock(ctx, t);
  if (t >= S3_LINES[1].start) S.px(ctx, TEXT_X - 4, LINE_Y[1] - 3, 260, 15, 'rgba(126,231,135,0.12)');
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 28.0) S.drawStatus(ctx, S3_STATUS, C.green);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'relieved');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function renderAt(ctx, t) {
  if (t < 10) drawS1(ctx, t);
  else if (t < 20) drawS2(ctx, t);
  else drawS3(ctx, t);
  for (const d of [DIP_AT, DIP2_AT]) {
    if (t >= d && t < d + DIP_LEN) {
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${S.clamp01(1 - (t - d) / DIP_LEN).toFixed(3)})`);
    }
  }
}

function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    DIP_AT,
    ...S.lineClicks(S2_LINES),
    DIP2_AT,
    ...S.lineClicks(S3_LINES),
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

function sceneLayout(scene, title, lines, status, expr, contentOverride) {
  const content = contentOverride || S.contentLayout(lines || [], status);
  return {
    scene,
    groups: {
      foreground: S.foregroundLayout({
        terminal: true, clawd: false, her: false,
        extra: [{ name: 'clawd', box: clawdBox(expr) }],
      }),
      titleBar: S.titleLayout(title),
      content,
      subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, arguments[6] === undefined ? 0 : arguments[6]),
      hud: [{ name: 'clock', box: [CLOCK.x, CLOCK.y, CLOCK.w, CLOCK.h] }],
    },
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      titleBar: S.TITLE_BOUNDS,
      content: S.CONTENT,
      subtitle: S.SUB,
      hud: S.CANVAS_BOUNDS,
    },
  };
}

function layoutAt(t) {
  if (t < 10) return sceneLayout(1, TITLES.S1, S1_LINES, S1_STATUS, 'determined', null, t);
  if (t < 20) {
    const content = [];
    const view = s2View(t);
    view.forEach((item, i) => {
      const full = S.lineText(item.line);
      content.push({ name: `row_${i + 1}`, box: S.textBox(TEXT_X, item.y, full, 10) });
      if (item.last) {
        content.push({ name: `cursor_${i + 1}`, box: [TEXT_X + S.textWidth(full, 10) + 2, item.y, 6, 10] });
      }
    });
    content.push({ name: 'status', box: S.textBox(TEXT_X, S.STATUS_Y, S2_STATUS, 10) });
    return sceneLayout(2, TITLES.S2, null, S2_STATUS, 'focused', content, t);
  }
  return sceneLayout(3, TITLES.S3, S3_LINES, S3_STATUS, 'relieved', null, t);
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
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS, CLOCK,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  DIP_AT, DIP2_AT, DIP_LEN, clockAt,
  CHECK_TITLE: 'E07 · Determination v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ cat task.txt', size: 10, color: C.text },
    { text: 'finish before sunrise', size: 10, color: C.amber },
    { text: 'test    ▸ 512 passed, 0 failed', size: 10, color: C.text },
    { text: '✓ deployed to prod', size: 10, color: C.green },
    { text: '赶上了。', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
