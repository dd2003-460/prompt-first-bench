#!/usr/bin/env node
'use strict';
// E08 · 愿望 (wish) — 深夜打字又删掉，只剩光标, 30s, 1800 frames.
//   S1 (0-10s):  打出「我想」→ 逐字删掉
//   S2 (10-20s): 打出「如果我能」→ 逐字删掉
//   S3 (20-30s): 只剩光标闪烁; 字幕「（什么都不写了）」
// 每敲一个字 1 click; 每删一个字 1 click (与像素删除同一时钟).

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y, STATUS_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E08_wish_arena');
const TITLES = {
  S1: 'clawd@dsh:~$ — draft',
  S2: 'clawd@dsh:~$ — draft',
  S3: 'clawd@dsh:~$ — draft',
};
const SUB_LINES = ['（什么都不写了）'];
const SUB_WINDOWS = [{ start: 21.6, end: 28.4 }];

const PROMPT = '> ';
const INPUT_Y = LINE_Y[1];

// --- 输入 / 删除 时间线 ---
const DRAFTS = [
  { text: '我想', start: 0.9, charMs: 180, del: 4.2, delMs: 150 },
  { text: '如果我能', start: 10.9, charMs: 180, del: 15.4, delMs: 150 },
];

// 纯函数: t → { typed, visible, deleting, done }
function draftState(t) {
  let out = { typed: 0, visible: '', deleting: false, active: false };
  for (const d of DRAFTS) {
    const chars = Array.from(d.text);
    if (t < d.start) continue;
    out.typed = chars.length;
    if (t < d.del) {
      const n = Math.min(chars.length, Math.floor(((t - d.start) * 1000) / d.charMs) + 1);
      out.visible = chars.slice(0, n).join('');
      out.active = n < chars.length; // 正在打字
    } else {
      const k = Math.floor(((t - d.del) * 1000) / d.delMs);
      const keep = Math.max(0, chars.length - k);
      out.visible = chars.slice(0, keep).join('');
      out.deleting = keep > 0;
      out.active = keep > 0;
    }
  }
  return out;
}

function draftEnd(d) {
  return { typed: d.del, deleted: d.del + (Array.from(d.text).length * d.delMs) / 1000 };
}

// --- 装饰: 深夜终端里的浮尘 (低密度, 纯装饰) ---
const DUST = [
  { x: 40, y: 20, ph: 0.0 }, { x: 150, y: 96, ph: 1.1 }, { x: 250, y: 54, ph: 2.3 },
  { x: 330, y: 128, ph: 0.7 }, { x: 96, y: 118, ph: 3.1 }, { x: 292, y: 24, ph: 4.2 },
  { x: 200, y: 140, ph: 5.0 }, { x: 60, y: 60, ph: 2.8 },
];

function drawDust(ctx, t, alpha) {
  for (const d of DUST) {
    const yy = d.y + Math.round(Math.sin(t * 0.5 + d.ph) * 6);
    const a = alpha * (0.10 + 0.10 * (0.5 + 0.5 * Math.sin(t * 1.4 + d.ph)));
    S.px(ctx, TEXT_X - 6 + d.x, S.TERM.y + S.TERM.titleH + 4 + yy, 2, 2, `rgba(255,255,255,${a.toFixed(3)})`);
  }
}

// --- Clawd ---
// expr: 'wanting' | 'hesitate' | 'silent'
function drawClawdExpr(ctx, x, y, t, expr) {
  const mood = 'thinking'; // 深夜独处 = 冷紫
  const dy = expr === 'silent' ? 3 : 0;
  const by = Math.round(y + dy + (Math.sin(t * 2.2) > 0.45 ? -1 : 0));
  S.drawClawd(ctx, x, y + dy, t, mood, 0);
  if (expr === 'wanting') {
    // 向上看的小眼睛 (愿望) + 头顶 1×1 微光
    S.px(ctx, x + 10, y + dy + 6, 4, 2, C.clawdEye);
    S.px(ctx, x + 26, y + dy + 6, 4, 2, C.clawdEye);
    const k = Math.floor(t * 2) % 3;
    S.px(ctx, x + 19, by - 3 - (k === 0 ? 1 : 0), 2, 2, C.amber);
  } else if (expr === 'hesitate') {
    // 眼睛半垂 + 轻微左顾
    S.px(ctx, x + 10, by + 8, 4, 2, C.clawdEye);
    S.px(ctx, x + 26, by + 8, 4, 2, C.clawdEye);
    S.px(ctx, x + 6, by + 5, 2, 1, C.clawdThinkDark);
    S.px(ctx, x + 32, by + 5, 2, 1, C.clawdThinkDark);
  } else {
    // 闭眼
    S.px(ctx, x + 10, by + 8, 4, 1, C.clawdEye);
    S.px(ctx, x + 26, by + 8, 4, 1, C.clawdEye);
  }
}

function clawdBox(expr) {
  const top = expr === 'wanting' ? 6 : 4;
  return [S.CLAWD_ROOM.x - 4, S.CLAWD_ROOM.y - top, 48, 32 + top];
}

const DIP_AT = 10.0;
const DIP2_AT = 20.0;
const DIP_LEN = 0.3;

function drawCompose(ctx, t) {
  const state = draftState(t);
  const expr = t < 10 ? 'wanting' : t < 20 ? 'hesitate' : 'silent';

  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES[t < 10 ? 'S1' : t < 20 ? 'S2' : 'S3'], t < 10 ? C.purple : t < 20 ? C.blue : C.dim);
  drawDust(ctx, t, t < 20 ? 1 : 0.6);

  // 收件人: 她 (但从未发送)
  S.txt(ctx, TEXT_X, LINE_Y[0], '// to: her', C.dim, 10);
  S.txt(ctx, TEXT_X + S.textWidth('// to: her', 10) + 10, LINE_Y[0], '// draft 03:12', 'rgba(139,148,158,0.7)', 10);

  // 输入行
  S.txt(ctx, TEXT_X, INPUT_Y, PROMPT, C.green, 10);
  const px0 = TEXT_X + S.textWidth(PROMPT, 10);
  if (state.visible) S.txt(ctx, px0, INPUT_Y, state.visible, C.text, 10);
  const cursorX = px0 + S.textWidth(state.visible, 10) + 1;
  let cursorOn;
  if (state.active) cursorOn = true;              // 打字/删除时实心
  else if (t >= 20) cursorOn = Math.floor(t * 1.2) % 2 === 0; // 结尾: 慢闪
  else cursorOn = Math.floor(t * 2.5) % 2 === 0;
  if (cursorOn) S.px(ctx, cursorX, INPUT_Y, 6, 10, state.deleting ? C.red : C.text);

  // 状态行: 只显示草稿状态, 不显示"发送"
  if (t >= 0.6) {
    const label = state.visible
      ? '[DSH] draft: unsaved'
      : t < 20 ? '[DSH] draft: empty · nothing sent' : '[DSH] draft: empty · 03:12';
    S.drawStatus(ctx, label, t < 20 ? C.dim : 'rgba(139,148,158,0.8)');
  }

  // 删除中的轻微回退闪光
  if (state.deleting) S.px(ctx, TEXT_X - 4, INPUT_Y - 3, 120, 15, 'rgba(255,123,114,0.07)');

  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, expr);
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);

  // 深夜压暗
  const night = 0.10 + S.easeInOut((t - 20) / 9) * 0.14;
  S.px(ctx, 0, 0, S.BW, S.BH, `rgba(6,10,26,${night.toFixed(3)})`);
}

function renderAt(ctx, t) {
  drawCompose(ctx, t);
  for (const d of [DIP_AT, DIP2_AT]) {
    if (t >= d && t < d + DIP_LEN) {
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${S.clamp01(1 - (t - d) / DIP_LEN).toFixed(3)})`);
    }
  }
}

function getClickTimestamps() {
  const raw = [DIP_AT, DIP2_AT];
  for (const d of DRAFTS) {
    const chars = Array.from(d.text);
    for (let i = 0; i < chars.length; i++) raw.push(d.start + (i * d.charMs) / 1000);
    for (let i = 0; i < chars.length; i++) raw.push(d.del + (i * d.delMs) / 1000);
  }
  return S.quantizeClicks(raw);
}

function layoutAt(t) {
  const state = draftState(t);
  const expr = t < 10 ? 'wanting' : t < 20 ? 'hesitate' : 'silent';
  const prefix = PROMPT;
  const px0 = TEXT_X + S.textWidth(prefix, 10);
  const content = [
    { name: 'to_line', box: S.textBox(TEXT_X, LINE_Y[0], '// to: her', 10) },
    { name: 'to_meta', box: S.textBox(TEXT_X + S.textWidth('// to: her', 10) + 10, LINE_Y[0], '// draft 03:12', 10) },
    { name: 'prompt', box: S.textBox(TEXT_X, INPUT_Y, prefix, 10) },
  ];
  if (state.visible) {
    content.push({ name: 'input', box: S.textBox(px0, INPUT_Y, state.visible, 10) });
  }
  content.push({ name: 'input_cursor', box: [Math.floor(px0 + S.textWidth(state.visible, 10) + 1), INPUT_Y, 6, 10] });
  content.push({ name: 'status', box: S.textBox(TEXT_X, STATUS_Y, '[DSH] draft: unsaved', 10) });

  return {
    scene: t < 10 ? 1 : t < 20 ? 2 : 3,
    groups: {
      foreground: S.foregroundLayout({
        terminal: true, clawd: false, her: false,
        extra: [{ name: 'clawd', box: clawdBox(expr) }],
      }),
      titleBar: S.titleLayout(TITLES[t < 10 ? 'S1' : t < 20 ? 'S2' : 'S3']),
      content,
      subtitle: S.subtitleLayout(SUB_LINES, SUB_WINDOWS, t),
    },
    bounds: {
      foreground: S.CANVAS_BOUNDS,
      titleBar: S.TITLE_BOUNDS,
      content: S.CONTENT,
      subtitle: S.SUB,
    },
  };
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
  OUT_DIR, TITLES, SUB_LINES, SUB_WINDOWS, PROMPT, INPUT_Y, DRAFTS,
  DIP_AT, DIP2_AT, DIP_LEN, draftState, draftEnd,
  CHECK_TITLE: 'E08 · Wish v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE: [
    { text: '我想', start: 0.9, charMs: 180, limit: 4.2 },
    { text: '如果我能', start: 10.9, charMs: 180, limit: 15.4 },
  ],
  AA_SAMPLES: [
    { text: '> 我想', size: 10, color: C.text },
    { text: '> 如果我能', size: 10, color: C.text },
    { text: '// to: her', size: 10, color: C.dim },
    { text: '[DSH] draft: empty · nothing sent', size: 10, color: C.dim },
    { text: '（什么都不写了）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
