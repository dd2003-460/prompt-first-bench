#!/usr/bin/env node
'use strict';
// E05 惊讶 (surprise) — 30s, 1800 frames @ 60fps, 1280×720.
// 事实源 (episodes.md, batch-6 任务书): `df -h` 突然 100%，整个终端白屏 0.5 秒，再亮时多了一个陌生进程。
//   S1 (0-10s)  日常检查: `$ df -h` → 25% (Clawd calm / 眼睛半闭)；字幕「一切正常。」
//   S2 (10-20s) 白屏 0.5s: 10.0-10.5s 终端整块纯白 (硬切、无过渡、白屏期间无键盘音)，
//               10.5s 再亮 → 同一行变成 500G/500G/0/100%；15s 起追加 `$ ps aux | grep -v grep`
//               → `user  9999  99.9  45.2  unknown_process`；18.6s 起 `$ lsof -p 9999`
//   S3 (20-30s) 陌生进程: 22s 起 `$ ps -o etime= -p 9999` → `00:00:10`；
//               字幕「它出现了 10 秒。」(25s) /「谁放进来的？」(28s)
// 画布 640×360 × SCALE=2 → 1280×720; 终端 440×200 @ (100,140); Fusion Pixel 10px。
// Clawd 40×17: idle (4×2 半闭眼) → surprised (6×6 圆眼 + 2×2 高光 + 张嘴) → startled (后仰 2px + 抬眉)。
//
// 本集与 batch-5 的两点有意差异（都写进 check_overlap_E05_arena.js 做硬校验）:
//   1) 场景切换用硬切而不是 0.25s 黑场：任务书要求白屏「前后帧无过渡」，
//      10s 的转场就是白屏本身；20s 处终端内容是连续时间轴，硬切在画面上不可见。
//   2) 终端内容是一条贯穿 30s 的连续时间轴 (df → ps → lsof → etime)，
//      所以 PID 9999 从 16.5s 一直可见到 30s（验收: 「陌生进程 PID 9999 在 S3 持续可见」）。
//   键盘音口径: 每字符出现 1 次 click，charMs ≥ 50ms（帧量化 + 0.035s 去重的下限）。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E05_surprise_arena');

const TITLES = {
  S1: 'clawd@dsh:~ — df -h',
  S2: 'clawd@dsh:~ — Capacity 100%',
  S3: 'clawd@dsh:~ — unknown_process',
};

// 任务书字幕: S1「一切正常。」/ S3 25s「它出现了 10 秒。」/ 28s「谁放进来的？」
const SUB_LINES = ['一切正常。', '它出现了 10 秒。', '谁放进来的？'];
const SUB_WINDOWS = [{ start: 2.2, end: 8.6 }, { start: 25.0, end: 27.8 }, { start: 28.0, end: 29.6 }];

// 白屏: 恰好 30 帧 (10.0s ≤ t < 10.5s @60fps)，硬边、无淡入淡出。
const FLASH_START = 10.0;
const FLASH_END = 10.5;
const FLASH_FRAMES = Math.round((FLASH_END - FLASH_START) * S.FPS); // 30

// 9 行连续时间轴，18px 行距 (10px 字号 + 14px 文本盒 → 4px 行间隙)，y 168..312 全在 CONTENT 内。
const ROW_Y = [168, 186, 204, 222, 240, 258, 276, 294, 312];

const LINE_DF_CMD = {
  y: ROW_Y[0], start: 0.9, charMs: 100,
  parts: [{ text: '$ ', color: C.green }, { text: 'df -h', color: C.text }],
};
const LINE_DF_HEAD = {
  y: ROW_Y[1], start: 2.6, charMs: 50,
  parts: [{ text: 'Filesystem   Size  Used Avail Capacity', color: C.dim }],
};
// 25% 行：白屏前有效（until = FLASH_END）
const LINE_DF_25 = {
  y: ROW_Y[2], start: 5.0, charMs: 50, until: FLASH_END,
  parts: [
    { text: '/dev/disk3   ', color: C.text },
    { text: '500G  120G  380G', color: C.blue },
    { text: '    25%', color: C.green },
  ],
};
// 100% 行：白屏后瞬时出现（typed:false → 整行 1 次 click，无逐字打字）
const LINE_DF_100 = {
  y: ROW_Y[2], start: FLASH_END, charMs: 1, typed: false, from: FLASH_END,
  parts: [
    { text: '/dev/disk3   ', color: C.text },
    { text: '500G  500G     0', color: C.red },
    { text: '   100%', color: C.red },
  ],
};
const LINE_PS_CMD = {
  y: ROW_Y[3], start: 15.0, charMs: 55,
  parts: [{ text: '$ ', color: C.green }, { text: 'ps aux | grep -v grep', color: C.text }],
};
const LINE_PS_ROW = {
  y: ROW_Y[4], start: 16.5, charMs: 50,
  parts: [
    { text: 'user  ', color: C.dim },
    { text: '9999', color: C.red },
    { text: '  99.9  45.2  ', color: C.dim },
    { text: 'unknown_process', color: C.purple },
  ],
};
const LINE_LSOF_CMD = {
  y: ROW_Y[5], start: 18.6, charMs: 60,
  parts: [{ text: '$ ', color: C.green }, { text: 'lsof -p 9999', color: C.text }],
};
const LINE_LSOF_ROW = {
  y: ROW_Y[6], start: 19.7, charMs: 50,
  parts: [
    { text: 'unknown_process', color: C.purple },
    { text: '  /dev/null  ', color: C.dim },
    { text: '???', color: C.red },
  ],
};
const LINE_ETIME_CMD = {
  y: ROW_Y[7], start: 22.0, charMs: 55,
  parts: [{ text: '$ ', color: C.green }, { text: 'ps -o etime= -p 9999', color: C.text }],
};
const LINE_ETIME_ROW = {
  y: ROW_Y[8], start: 23.6, charMs: 90,
  parts: [{ text: '00:00:10', color: C.amber }],
};

// 时间顺序（check_overlap 的 strictBefore 串行校验按此顺序）
const ALL_LINES = [
  LINE_DF_CMD, LINE_DF_HEAD, LINE_DF_25, LINE_DF_100, LINE_PS_CMD,
  LINE_PS_ROW, LINE_LSOF_CMD, LINE_LSOF_ROW, LINE_ETIME_CMD, LINE_ETIME_ROW,
];

// 某一时刻终端里「在场上」的行：25% 行在 10.5s 被 100% 行原地替换，其余全程保留。
function activeLines(t) {
  return ALL_LINES.filter((line) => {
    if (line.until !== undefined && t >= line.until) return false;
    if (line.from !== undefined && t < line.from) return false;
    return true;
  });
}

// PID 9999 落地的时刻（验收: 从落地起一直到 30s 都可见）
const PID_CHAR_INDEX = S.lineText(LINE_PS_ROW).indexOf('9999');
const PID_LANDED_AT = LINE_PS_ROW.start + (PID_CHAR_INDEX * LINE_PS_ROW.charMs) / 1000;

const CLAWD_BOX = [S.CLAWD_ROOM.x - 2, 243, 42, 29]; // 后仰 dx=-2/dy=-2 与 bob=-1 都在盒内

// --- Clawd: idle / surprised / startled ------------------------------------
// calm·thinking·smile·warm 全部委托给 companion v1.1 原始 sprite（逐像素一致）。
function drawClawdEp(ctx, x, y, t, mood = 'calm', warmMix = 0, opts = {}) {
  if (mood !== 'idle' && mood !== 'surprised' && mood !== 'startled') {
    S.art.drawClawd(ctx, x, y, t, mood, warmMix);
    return;
  }
  const dy = opts.dy === undefined ? 0 : opts.dy;
  const dx = opts.dx === undefined ? 0 : opts.dx;
  const bob = opts.noBob ? 0 : (Math.sin(t * 2.2) > 0.45 ? -1 : 0);
  const bx = Math.round(x + dx);
  const by = Math.round(y + bob + dy);
  const bodyH = 17;
  const lerp = S.art.lerpColor;
  const bodyCol = lerp(C.clawdNorm, C.clawdWarm, warmMix);
  const darkCol = lerp(C.clawdNormDark, C.clawdWarmDark, warmMix);
  const bellyCol = lerp(C.clawdNormBelly, C.clawdWarmBelly, warmMix);

  px(ctx, bx, by, 40, bodyH, bodyCol);
  px(ctx, bx, by, 40, 2, darkCol);
  px(ctx, bx + 9, by + 11, 22, 4, bellyCol);

  // 圆眼: 6×6 去角（像素圆），2×2 高光
  const roundEye = (ex) => {
    px(ctx, bx + ex + 1, by + 5, 4, 1, C.clawdEye);
    px(ctx, bx + ex, by + 6, 6, 4, C.clawdEye);
    px(ctx, bx + ex + 1, by + 10, 4, 1, C.clawdEye);
    px(ctx, bx + ex + 1, by + 6, 2, 2, C.white);
  };

  if (mood === 'idle') {
    // 半闭眼: 4×2 眼下移一行，无高光；无嘴（放松）
    if (!opts.noBob && (t % 3.4) < 0.14) {
      px(ctx, bx + 10, by + 8, 4, 1, C.clawdEye);
      px(ctx, bx + 26, by + 8, 4, 1, C.clawdEye);
    } else {
      px(ctx, bx + 10, by + 8, 4, 2, C.clawdEye);
      px(ctx, bx + 26, by + 8, 4, 2, C.clawdEye);
    }
  } else {
    // surprised / startled: 眼睛突然变圆
    roundEye(9);
    roundEye(25);
    if (mood === 'startled') {
      // 抬眉 + 更大的张嘴（后仰由 dx/dy 给出）
      px(ctx, bx + 9, by + 3, 6, 1, C.clawdEye);
      px(ctx, bx + 25, by + 3, 6, 1, C.clawdEye);
      px(ctx, bx + 19, by + 12, 2, 1, C.clawdEye);
      px(ctx, bx + 18, by + 13, 4, 2, C.clawdEye);
      px(ctx, bx + 19, by + 15, 2, 1, C.clawdEye);
    } else {
      // 惊讶的小圆嘴
      px(ctx, bx + 19, by + 12, 2, 1, C.clawdEye);
      px(ctx, bx + 18, by + 13, 4, 1, C.clawdEye);
      px(ctx, bx + 19, by + 14, 2, 1, C.clawdEye);
    }
  }

  const step = Math.sin(t * 3.0) > 0.6 ? 1 : 0;
  px(ctx, bx + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, bx + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 31, by + bodyH, 6, 7 - step, darkCol);
}
const ART = { ...S.art, drawClawd: drawClawdEp };

function clawdPose(t) {
  if (t < FLASH_START) return { mood: 'idle', dx: 0, dy: 0 };
  if (t < LINE_PS_CMD.start) return { mood: 'surprised', dx: 0, dy: 0 };
  return { mood: 'startled', dx: -2, dy: -2 }; // 身体后仰 2px
}

// --- Scenes (hard cuts: the 10s transition IS the white flash) -------------
const SCENES = [
  { start: 0, title: TITLES.S1, accent: C.green },
  { start: 10, title: TITLES.S2, accent: C.red },
  { start: 20, title: TITLES.S3, accent: C.purple },
];

function sceneIndexOf(t) { return t < 10 ? 0 : t < 20 ? 1 : 2; }

function renderAt(ctx, t) {
  const sc = SCENES[sceneIndexOf(t)];
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, sc.title, sc.accent);
  S.drawLines(ctx, activeLines(t), t);
  // 白屏 0.5s: 整块终端纯白，硬边（前后帧无过渡），期间无任何文字/光标。
  if (t >= FLASH_START && t < FLASH_END) px(ctx, S.TERM.x, S.TERM.y, S.TERM.w, S.TERM.h, C.white);
  const pose = clawdPose(t);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, pose.mood, 0, { dx: pose.dx, dy: pose.dy });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

// --- Keyboard clicks: 每字符 1 次；白屏期间 (10.0-10.5) 静音 ---------------
function getClickTimestamps() {
  const raw = S.lineClicks(ALL_LINES).filter((t) => !(t >= FLASH_START && t < FLASH_END));
  return S.quantizeClicks(raw);
}

function typingSchedule(lines, limit) {
  return lines.map((line, i) => ({
    text: S.lineText(line),
    start: line.start,
    charMs: line.typed === false ? 1 : (line.charMs || S.TYPE_CHAR_MS),
    limit,
    strictBefore: i + 1 < lines.length ? lines[i + 1].start : undefined,
  }));
}
const TYPING_SCHEDULE = typingSchedule(ALL_LINES, 29.6);

// --- Layout groups (0px tolerance, per frame) ------------------------------
function layoutAt(t) {
  const layout = S.baseLayout({
    scene: sceneIndexOf(t) + 1,
    title: SCENES[sceneIndexOf(t)].title,
    lines: activeLines(t),
    status: null,
    subLines: SUB_LINES, subWindows: SUB_WINDOWS, t,
  });
  layout.groups.foreground = S.foregroundLayout({
    terminal: true, clawd: false, her: false,
    extra: [{ name: 'clawd', box: CLAWD_BOX }],
  });
  // 白屏期间终端内没有可见文字：只申报白屏块本身，避免申报看不见的文本盒。
  if (t >= FLASH_START && t < FLASH_END) {
    layout.groups.content = [{ name: 'white_flash', box: [S.TERM.x + 2, S.TERM.y + S.TERM.titleH, S.TERM.w - 4, S.TERM.h - S.TERM.titleH - 2] }];
    layout.bounds.content = S.CONTENT;
  }
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
  ALL_LINES, ROW_Y, activeLines,
  LINE_DF_25, LINE_DF_100, LINE_PS_CMD, LINE_PS_ROW, LINE_LSOF_CMD, LINE_LSOF_ROW,
  LINE_ETIME_CMD, LINE_ETIME_ROW,
  FLASH_START, FLASH_END, FLASH_FRAMES, PID_LANDED_AT, CLAWD_BOX, SCENES,
  CHECK_TITLE: 'E05 惊讶 (surprise) Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'Filesystem   Size  Used Avail Capacity', size: 10, color: C.dim },
    { text: '/dev/disk3   500G  500G     0   100%', size: 10, color: C.red },
    { text: 'user  9999  99.9  45.2  unknown_process', size: 10, color: C.purple },
    { text: '谁放进来的？', size: 10, color: C.white },
  ],
  sceneOf: (t) => sceneIndexOf(t) + 1,
  layoutAt,
  renderAt,
  clawdPose,
  drawClawdEp,
  getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
