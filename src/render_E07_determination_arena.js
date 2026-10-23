#!/usr/bin/env node
'use strict';
// E07 「目标」— finish before sunrise, 时钟 23:58 → 00:00, 30s, 1800 frames.
//
//   S1 (0-10s)  : `$ cat task.txt` = "finish before sunrise" · 时钟 23:58 · Clawd determined
//   S2 (10-20s) : 终端快速滚动 (build / test / deploy) · 时钟 23:59 · 日志向上滚
//   S3 (20-30s) : "✓ deployed" · 时钟 00:00 · Clawd 释然 · 字幕「赶上了。」
//
// 时钟是 5×7 点阵字形放大 2 倍（每格 2×2），固定在终端右侧的卡片里，
// 卡片范围 x=546..634 / y=248..312，与终端 (x≤540) 和字幕条 (y≥340) 都不相交。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E07_arena');
const S2_START = 10;
const S3_START = 20;

const TITLES = {
  S1: 'clawd@dsh:~$ — task.txt',
  S2: 'clawd@dsh:~$ — build · test · deploy',
  S3: 'clawd@dsh:~$ — deploy',
};

const SUB_LINES = ['天不亮，就不算完。', '23:59。还剩一分钟。', '赶上了。'];
const SUB_WINDOWS = [{ start: 2, end: 8 }, { start: 13, end: 18 }, { start: 24, end: 29 }];

const CLOCK = { x: 546, y: 248, w: 88, h: 64 };

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
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'cat task.txt', color: C.text }] },
  { y: LINE_Y[1], charMs: 34, cursor: false, parts: [{ text: 'finish before sunrise', color: C.amber }] },
  { y: LINE_Y[3], charMs: 26, cursor: false, parts: [{ text: 'deadline: 06:12', color: C.dim }] },
  { y: LINE_Y[4], charMs: 26, cursor: false, parts: [{ text: 'now: 23:58   remaining: 6h 14m', color: C.text }] },
], 0.8, 0.26);

// S2 is a real scrolling log: entries appear fast and the window keeps the last 6 rows.
const S2_ENTRIES = [
  { at: 10.6, typed: true, parts: [{ text: '$ ', color: C.green }, { text: 'npm run build', color: C.text }] },
  { at: 12.0, typed: false, parts: [{ text: '> build: 12 modules', color: C.dim }] },
  { at: 12.5, typed: false, parts: [{ text: '✓ build ok (1.2s)', color: C.green }] },
  { at: 13.0, typed: false, parts: [{ text: '> test: 34 cases', color: C.dim }] },
  { at: 13.6, typed: false, parts: [{ text: '✓ 34 passed (0.8s)', color: C.green }] },
  { at: 14.2, typed: false, parts: [{ text: '> lint: 0 errors', color: C.dim }] },
  { at: 14.8, typed: false, parts: [{ text: '> deploy: upload 12 files', color: C.dim }] },
  { at: 15.4, typed: false, parts: [{ text: '> edge: 18 nodes warming', color: C.dim }] },
  { at: 16.0, typed: false, parts: [{ text: '✓ healthcheck 200', color: C.green }] },
  { at: 16.6, typed: false, parts: [{ text: '> logs: tailing...', color: C.dim }] },
  { at: 17.2, typed: false, parts: [{ text: '✓ live · 23:59:41', color: C.green }] },
  { at: 17.8, typed: false, parts: [{ text: '[DSH] clock is watching', color: C.amber }] },
];

const S3_LINES = serial([
  { y: LINE_Y[0], charMs: 60, parts: [{ text: '$ ', color: C.green }, { text: 'deploy --prod', color: C.text }] },
  { y: LINE_Y[1], charMs: 18, cursor: false, parts: [{ text: '> uploading 12 files...', color: C.dim }] },
  { y: LINE_Y[2], charMs: 18, cursor: false, parts: [{ text: '✓ deployed in 41s', color: C.green }] },
  { y: LINE_Y[5], charMs: 20, cursor: false, parts: [{ text: '[DSH] task.txt: done · 00:00', color: C.dim }] },
], 20.6, 0.3);

// Deployment banner (its own element, framed and centred).
const BANNER = { x: TEXT_X - 2, y: LINE_Y[3] - 2, w: 412, h: 26, appear: 24.2 };
const BANNER_TEXT = '✓ deployed  ·  00:00';

const S1_STATUS = '[DSH] mode: finish-before-sunrise';
const S2_STATUS = '[DSH] chain: build → test → deploy';
const S3_STATUS = '[DSH] status: on time';
const S1_STATUS_AT = 6.6;
const S2_STATUS_AT = 10.9;
const S3_STATUS_AT = 27.2;

const CLAWD_BOX = { name: 'clawd', box: [34, 240, 56, 40] };

// --- 5×7 pixel clock -------------------------------------------------------
const DIGITS = {
  0: ['01110', '10001', '10001', '10001', '10001', '10001', '01110'],
  1: ['00100', '01100', '00100', '00100', '00100', '00100', '01110'],
  2: ['11111', '00001', '00001', '11111', '10000', '10000', '11111'],
  3: ['11111', '00001', '00001', '01110', '00001', '00001', '11111'],
  4: ['10001', '10001', '10001', '11111', '00001', '00001', '00001'],
  5: ['11111', '10000', '10000', '11110', '00001', '00001', '11110'],
  6: ['11111', '10000', '10000', '11111', '10001', '10001', '11111'],
  7: ['11111', '00001', '00010', '00100', '01000', '01000', '01000'],
  8: ['11111', '10001', '10001', '11111', '10001', '10001', '11111'],
  9: ['11111', '10001', '10001', '01111', '00001', '00001', '01110'],
  ':': ['0', '0', '1', '0', '1', '0', '0'],
  ' ': ['0', '0', '0', '0', '0', '0', '0'],
};

function drawClock(ctx, timeStr, color, t, appear = 1) {
  if (appear <= 0) return;
  const { x, y, w, h } = CLOCK;
  ctx.save();
  ctx.globalAlpha = S.clamp01(appear);
  S.px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.16)');
  S.px(ctx, x, y, w, h, C.termBg);
  S.px(ctx, x, y, w, 2, C.termBd);
  S.px(ctx, x, y + h - 2, w, 2, C.termBd);
  S.px(ctx, x, y, 2, h, C.termBd);
  S.px(ctx, x + w - 2, y, 2, h, C.termBd);
  S.px(ctx, x, y, w, 1, color);
  S.txt(ctx, x + 8, y + 6, 'now', C.dim, 10);

  // 2×2 blocks: 5×7 glyph → 10×14 px
  const glyphW = 10;
  const gap = 3;
  const total = timeStr.length * glyphW + (timeStr.length - 1) * gap;
  let cx = Math.round(x + (w - total) / 2);
  const gy = y + 22;
  for (const ch of timeStr) {
    const glyph = DIGITS[ch] || DIGITS[' '];
    for (let r = 0; r < glyph.length; r++) {
      for (let c = 0; c < glyph[r].length; c++) {
        if (glyph[r][c] !== '1') continue;
        if (ch === ':' && Math.floor(t * 1.5) % 2 === 1) continue; // colon ticks once a second
        S.px(ctx, cx + c * 2, gy + r * 2, 2, 2, color);
      }
    }
    cx += glyphW + gap;
  }
  S.txt(ctx, x + w / 2, y + h - 16, 'before sunrise', C.dim, 10, 'center');
  ctx.restore();
}

function clockTextAt(t) {
  if (t < S2_START) return '23:58';
  if (t < S3_START) return '23:59';
  return '00:00';
}
function clockColorAt(t) {
  if (t < S2_START) return C.amber;
  if (t < S3_START) return C.amber;
  return C.green;
}

// --- Clawd expressions -----------------------------------------------------
function drawDetermined(ctx, t) {
  const x = S.CLAWD_ROOM.x;
  const y = S.CLAWD_ROOM.y;
  S.drawClawd(ctx, x, y, t, 'thinking', 0); // purple, focused 4×2 eyes
  // Angled brows + a set jaw read as determination rather than mere thought.
  S.px(ctx, x + 9, y + 4, 6, 1, C.clawdThinkDark);
  S.px(ctx, x + 25, y + 4, 6, 1, C.clawdThinkDark);
  S.px(ctx, x + 17, y + 12, 6, 2, C.clawdEye);
}

function drawRelieved(ctx, t) {
  S.drawClawd(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'smile', 0.6);
}

// --- Scenes ----------------------------------------------------------------
function s2Visible(t) {
  const shown = S2_ENTRIES.filter((e) => t >= e.at);
  return shown.slice(-6).map((e, i) => ({ ...e, y: LINE_Y[i] }));
}

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.amber);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.amber);
  drawClock(ctx, '23:58', C.amber, t, 1);
  drawDetermined(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.blue);
  for (const row of s2Visible(t)) {
    if (row.typed) {
      S.drawTypedLine(ctx, row, t);
    } else {
      let cx = TEXT_X;
      for (const part of row.parts) {
        S.txt(ctx, cx, row.y, part.text, part.color, 10);
        cx += S.textWidth(part.text, 10);
      }
    }
  }
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.blue);
  drawClock(ctx, '23:59', C.amber, t, 1);
  drawDetermined(ctx, t);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  const dawn = 0.45 + 0.4 * S.easeInOut((t - S3_START) / 8);
  S.drawBackground(ctx, t, dawn);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= BANNER.appear) {
    const { x, y, w, h } = BANNER;
    S.px(ctx, x, y, w, h, 'rgba(126,231,135,0.12)');
    S.px(ctx, x, y, w, 2, C.green);
    S.px(ctx, x, y + h - 2, w, 2, C.green);
    S.px(ctx, x, y, 2, h, C.green);
    S.px(ctx, x + w - 2, y, 2, h, C.green);
    S.txt(ctx, x + w / 2, y + 6, BANNER_TEXT, C.green, 10, 'center');
  }
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.green);
  drawClock(ctx, '00:00', C.green, t, 1);
  drawRelieved(ctx, t);
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
  const raw = [
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S3_LINES.filter((l) => l.typed !== false)),
    ...S2_ENTRIES.filter((e) => e.at < S3_START).map((e) => e.at),
    S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT, BANNER.appear,
  ];
  return S.quantizeClicks(raw);
}

function typingSchedule(lines, limit) {
  return lines.map((line, i) => ({
    text: S.lineText(line), start: line.start, charMs: line.charMs || S.TYPE_CHAR_MS,
    limit, strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = [
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  const clockEl = { name: 'clock_card', box: [CLOCK.x, CLOCK.y, CLOCK.w, CLOCK.h] };
  if (t < S2_START) {
    return S.baseLayout({
      ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS,
      clawd: false, her: false, extra: [CLAWD_BOX, clockEl],
    });
  }
  if (t < S3_START) {
    const rows = s2Visible(t);
    const layoutLines = rows.map((r) => ({ y: r.y, typed: false, parts: r.parts }));
    return S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: layoutLines, status: S2_STATUS,
      clawd: false, her: false, extra: [CLAWD_BOX, clockEl],
    });
  }
  // The banner lives inside the terminal, so it belongs to the content group.
  const content = S.contentLayout(S3_LINES, S3_STATUS)
    .concat([{ name: 'deploy_banner', box: [BANNER.x, BANNER.y, BANNER.w, BANNER.h] }]);
  return S.baseLayout({
    ...common, scene: 3, title: TITLES.S3, lines: S3_LINES, status: S3_STATUS,
    clawd: false, her: false,
    extra: [CLAWD_BOX, clockEl],
    extraGroups: { content },
  });
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) console.log(JSON.stringify({ count: getClickTimestamps().length, clicks: getClickTimestamps() }));
  else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    require('fs').writeFileSync(`/tmp/E07_${n}.png`, out.outCanvas.toBuffer('image/png'));
    console.log(`/tmp/E07_${n}.png`);
  } else renderer.renderAllFrames();
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_ENTRIES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  S2_START, S3_START, CLOCK, BANNER, BANNER_TEXT, CLAWD_BOX,
  clockTextAt, clockColorAt,
  CHECK_TITLE: 'E07 Determination Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'finish before sunrise', size: 10, color: C.amber },
    { text: 'now: 23:58   remaining: 6h 14m', size: 10, color: C.text },
    { text: '✓ build ok (1.2s)', size: 10, color: C.green },
    { text: '✓ deployed  ·  00:00', size: 10, color: C.green },
    { text: '赶上了。', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps, drawClock,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
