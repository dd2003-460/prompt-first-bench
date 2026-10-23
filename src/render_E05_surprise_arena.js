#!/usr/bin/env node
'use strict';
// E05 · 惊讶 (surprise) — df -h 突然 100%，陌生进程出现, 30s, 1800 frames.
// 画布 640×360, SCALE=2 → 1280×720 @ 60fps. 布局严格复用 companion v1.1 的 440×200 终端.
// 故事线 (docs 见 README/批次说明):
//   S1 (0-10s):  `df -h` 一切正常 25%; Clawd calm; 字幕「一切正常。」
//   S2 (10-15s): 白屏 0.5s → 终端 100% (全红); Clawd surprised (跳动 + 睁大眼 + ! 记号)
//   S3 (15-30s): `ps aux` 出现陌生进程 PID 9999; Clawd 后仰 (lean-back + 冷汗); 字幕「谁放进来的？」
// 打字像素与键盘点击时间戳共用同一批 line 对象 (每字符 1 click).

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, STATUS_Y, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E05_surprise_arena');
const TITLES = {
  S1: 'clawd@dsh:~$ — df',
  S2: 'clawd@dsh:~$ — disk full',
  S3: 'clawd@dsh:~$ — ps',
};
const SUB_LINES = ['一切正常。', '', '谁放进来的？'];
const SUB_WINDOWS = [{ start: 1.6, end: 8.6 }, { start: -1, end: -1 }, { start: 21.0, end: 28.6 }];

// --- S1: 25% 一切正常 ---
const S1_LINES = [
  { y: LINE_Y[0], start: 0.8, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], start: 2.4, charMs: 45, parts: [{ text: 'Filesystem    Size  Used  Avail  Use%', color: C.dim }] },
  { y: LINE_Y[2], start: 4.2, charMs: 45, parts: [{ text: '/dev/sda1    128G   32G   96G   25%', color: C.text }] },
  { y: LINE_Y[3], start: 6.0, charMs: 45, parts: [{ text: '/dev/sdb1    512G   64G  448G   13%', color: C.text }] },
];
const S1_STATUS = '[DSH] disk: healthy · 25% used';

// --- S2: 白屏之后的 100% ---
const S2_LINES = [
  { y: LINE_Y[0], start: 10.6, charMs: 100, parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }] },
  { y: LINE_Y[1], start: 11.4, charMs: 40, parts: [{ text: 'Filesystem  Size  Used  Use%', color: C.dim }] },
  { y: LINE_Y[2], start: 12.7, charMs: 40, parts: [{ text: '/dev/sda1   128G  128G  100%', color: C.red }] },
  { y: LINE_Y[3], start: 13.9, charMs: 40, parts: [{ text: '! no space left on device', color: C.red }] },
];
const S2_STATUS = '[DSH] disk: CRITICAL · 100% full';

// --- S3: 陌生进程 ---
const S3_LINES = [
  { y: LINE_Y[0], start: 15.8, charMs: 120, parts: [{ text: '$ ', color: C.green }, { text: 'ps aux', color: C.text }] },
  { y: LINE_Y[1], start: 17.2, charMs: 45, parts: [{ text: 'USER   PID  %CPU  COMMAND', color: C.dim }] },
  { y: LINE_Y[2], start: 18.4, charMs: 45, parts: [{ text: 'root     1   0.1  /sbin/init', color: C.text }] },
  { y: LINE_Y[3], start: 19.8, charMs: 45, parts: [{ text: '????  9999  99.0  ./unknown', color: C.red }] },
  { y: LINE_Y[4], start: 21.2, charMs: 45, parts: [{ text: '! pid 9999 not in baseline', color: C.amber }] },
];
const S3_STATUS = '[DSH] unknown process · pid 9999 · origin: ?';

// --- 时间常量 ---
const FLASH_AT = 10.0;
const FLASH_LEN = 0.5;
const DIP_AT = 15.0;
const DIP_LEN = 0.2;
const S2_ALERT_AT = 12.7;
const S3_ALERT_AT = 19.8;

// --- Clawd 表情叠加 (base 造型仍来自 companion v1.1: 40×17, 无嘴无天线无轮廓) ---
// expr: 'calm' | 'surprised' | 'lean'
function drawClawdExpr(ctx, x, y, t, expr) {
  let dx = 0;
  let dy = 0;
  let mood = 'calm';
  if (expr === 'surprised') {
    dy = Math.sin(t * 9) > 0 ? -3 : -2; // 受惊弹跳
  } else if (expr === 'lean') {
    dx = -6; // 后仰
    dy = 1;
  }
  const bx = x + dx;
  const by = Math.round(y + dy + (Math.sin(t * 2.2) > 0.45 ? -1 : 0));

  S.drawClawd(ctx, bx, y + dy, t, mood, 0);

  if (expr === 'surprised') {
    // 6×6 睁大眼 + 2×2 高光
    S.px(ctx, bx + 9, by + 5, 6, 6, C.clawdEye);
    S.px(ctx, bx + 25, by + 5, 6, 6, C.clawdEye);
    S.px(ctx, bx + 10, by + 6, 2, 2, C.white);
    S.px(ctx, bx + 26, by + 6, 2, 2, C.white);
    // 小圆形嘴巴 (压在肚皮上, 深色可读)
    S.px(ctx, bx + 17, by + 12, 6, 2, C.clawdEye);
    // 右上角单个「!」: 惊吓记号 (不放在头顶, 避免像天线)
    const blink = Math.floor(t * 7) % 2 === 0;
    if (blink) {
      S.px(ctx, bx + 44, by + 2, 2, 5, C.red);
      S.px(ctx, bx + 44, by + 9, 2, 2, C.red);
      S.px(ctx, bx + 47, by + 1, 1, 1, C.amber);
    }
  } else if (expr === 'lean') {
    // 后仰: 瞳孔上移 + 冷汗
    S.px(ctx, bx + 10, by + 6, 4, 3, C.clawdEye);
    S.px(ctx, bx + 26, by + 6, 4, 3, C.clawdEye);
    S.px(ctx, bx + 11, by + 6, 1, 1, C.white);
    S.px(ctx, bx + 27, by + 6, 1, 1, C.white);
    const drip = Math.round((t * 6) % 4);
    S.px(ctx, bx + 37, by + 2 + drip, 2, 3, C.blue);
    S.px(ctx, bx + 6, by + 1 + (drip % 3), 2, 2, C.blue);
  }
}

function clawdBox(expr) {
  const dx = expr === 'lean' ? -3 : 0;
  const top = expr === 'surprised' ? 4 : 4;
  return [S.CLAWD_ROOM.x - 4 + dx, S.CLAWD_ROOM.y - top, expr === 'surprised' ? 56 : 48, 32 + top];
}

// --- 场景绘制 ---
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 7.8) S.drawStatus(ctx, S1_STATUS, C.green);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.red);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= S2_ALERT_AT) {
    const pulse = 0.10 + 0.08 * (0.5 + 0.5 * Math.sin(t * 7));
    // 内容区红色压力感 (装饰, 不参与布局)
    S.px(ctx, S.TERM.x + 2, S.TERM.y + S.TERM.titleH, S.TERM.w - 4, S.TERM.h - S.TERM.titleH - 2,
      `rgba(255,80,70,${pulse.toFixed(3)})`);
    S.drawStatus(ctx, S2_STATUS, C.red);
  }
  // 白屏 0.5s: 10.0 纯白 → 10.5 完全消失
  if (t < FLASH_AT + FLASH_LEN) {
    const a = S.clamp01(1 - (t - FLASH_AT) / FLASH_LEN);
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(255,255,255,${a.toFixed(3)})`);
  }
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'surprised');
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.amber);
  // 陌生进程整行高亮 (画在文字下面)
  if (t >= S3_ALERT_AT) {
    S.px(ctx, TEXT_X - 4, LINE_Y[3] - 3, 300, 15, 'rgba(255,123,114,0.16)');
  }
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 22.6) S.drawStatus(ctx, S3_STATUS, C.amber);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'lean');
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
  // S3 入场: 0.2s 黑场
  if (t >= DIP_AT && t < DIP_AT + DIP_LEN) {
    const a = S.clamp01(1 - (t - DIP_AT) / DIP_LEN);
    S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${a.toFixed(3)})`);
  }
}

function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    FLASH_AT,
    ...S.lineClicks(S2_LINES),
    S2_ALERT_AT,
    DIP_AT,
    ...S.lineClicks(S3_LINES),
    S3_ALERT_AT,
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
  ...typingSchedule(S2_LINES, 14.9),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t, clawd: false, her: false };
  if (t < 10) {
    return S.baseLayout({
      ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS,
      extra: [{ name: 'clawd', box: clawdBox('calm') }],
    });
  }
  if (t < 15) {
    return S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: S2_LINES, status: S2_STATUS,
      extra: [{ name: 'clawd', box: clawdBox('surprised') }],
    });
  }
  return S.baseLayout({
    ...common, scene: 3, title: TITLES.S3, lines: S3_LINES, status: S3_STATUS,
    extra: [{ name: 'clawd', box: clawdBox('lean') }],
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
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS,
  FLASH_AT, FLASH_LEN, DIP_AT, DIP_LEN, S2_ALERT_AT, S3_ALERT_AT,
  CHECK_TITLE: 'E05 · Surprise v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ df -h', size: 10, color: C.text },
    { text: 'Filesystem    Size  Used  Avail  Use%', size: 10, color: C.dim },
    { text: '/dev/sda1    128G  128G     0G  100%', size: 10, color: C.red },
    { text: '! pid 9999 not in baseline', size: 10, color: C.amber },
    { text: '谁放进来的？', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 15 ? 2 : 3),
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
