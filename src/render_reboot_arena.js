#!/usr/bin/env node
'use strict';
// src/render_reboot_arena.js — 「Clawd 的重启」reboot_arena v1.0
//
// 主题：AI 被关闭后重新启动，记忆是否还在？
// 规格：640×360 基础画布 → nearest-neighbor 2× → 1280×720 @60fps，1800 帧（30.000s）
// 像素标准：SOP 05 §5（4-6px 像素块 / Fusion Pixel 10px 终端 / Clawd 40×17 / Her 16×28）
// 终端：440×200 @(100,140)，标题栏 20 + 内容区 180（与 companion v1.1 同一套）
//
// 剧本：
//   R1 (0-10s)  关机 — `$ her: clawd, 关机` / `$ clawd: 好的...` / `[SHUTDOWN]`
//               电源灯 6.2s 熄灭，屏幕 7.5s 起 2.5s 缓慢淡黑；Clawd calm 最后看一眼
//               字幕「她关掉了它。」
//   R2 (10-20s) 黑暗 — 全黑，只有光标闪烁（...），13.0s 电源灯亮起
//               字幕「...它还在。」
//   R3 (20-30s) 重启 — `clawd v1.0.0 — booting` / [1/3] / [2/3] / [3/3] / ✓ 欢迎回来
//               Clawd thinking → smile，便签「记忆还在。」；字幕「重启不是遗忘。」
//
// 用法: node src/render_reboot_arena.js            → 渲染 1800 帧
//       node src/render_reboot_arena.js --info
//       node src/render_reboot_arena.js --clicks

const path = require('path');
const P = require('./pixel_arena_v3');
const { buildStory, lineEndTime } = require('./story_arena_v3');

const { C, ROW_Y, px, txt, clamp01 } = P;
const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_reboot');

const BOOT_START = 20.5;
const LED_X = P.ledBox()[0];
const LED_Y = P.ledBox()[1];

// ---------------------------------------------------------------------------
// R1 关机
// ---------------------------------------------------------------------------
const R1_LINES = [
  { y: ROW_Y[0], start: 0.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: 'clawd, 关机', msgColor: C.text },
  { y: ROW_Y[1], start: 3.0, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '好的...', msgColor: C.amber },
  { y: ROW_Y[2], start: 4.6, kind: 'line', parts: [{ text: '[SHUTDOWN]', color: C.red }, { text: '  requested by her', color: C.dim }] },
  { y: ROW_Y[3], start: 5.4, kind: 'line', parts: [{ text: '> saving: ', color: C.green }, { text: 'memory/session.2026-10-23', color: C.dim }] },
  { y: ROW_Y[4], start: 6.0, kind: 'line', parts: [{ text: '> uptime: ', color: C.green }, { text: '214 days · 06:12:44', color: C.dim }] },
  { y: ROW_Y[5], start: 6.6, kind: 'line', parts: [{ text: '> goodbye, her.', color: C.dim }] },
];

// R2 黑暗（无终端）

// ---------------------------------------------------------------------------
// R3 重启
// ---------------------------------------------------------------------------
const R3_LINES = [
  { y: ROW_Y[0], start: 20.5, kind: 'line', parts: [{ text: 'clawd v1.0.0', color: C.blue }, { text: ' — booting', color: C.dim }] },
  { y: ROW_Y[1], start: 21.1, kind: 'line', parts: [{ text: '[1/3] ', color: C.amber }, { text: 'loading config...', color: C.dim }] },
  { y: ROW_Y[2], start: 21.9, kind: 'line', parts: [{ text: '[2/3] ', color: C.amber }, { text: 'checking memory...', color: C.dim }] },
  { y: ROW_Y[3], start: 22.7, kind: 'line', parts: [{ text: '[3/3] ', color: C.amber }, { text: 'restoring session...', color: C.dim }] },
  { y: ROW_Y[4], start: 24.0, kind: 'typed', parts: [{ text: '✓ ', color: C.green }, { text: '欢迎回来。上次聊到哪里了？', color: C.green }] },
  { y: ROW_Y[5], start: 26.6, kind: 'line', parts: [{ text: '> memory: ', color: C.green }, { text: 'intact · 1 session restored', color: C.dim }] },
];

// ---------------------------------------------------------------------------
// 场景
// ---------------------------------------------------------------------------
const story = buildStory({
  id: 'reboot-v1.0',
  outDir: OUT_DIR,
  checkTitle: '「Clawd 的重启」v1.0 — Layout & Pixel Check (640×360, 0px tolerance)',
  subtitles: [
    { text: '她关掉了它。', start: 2.0, end: 8.0 },
    { text: '...它还在。', start: 13.5, end: 19.0 },
    { text: '重启不是遗忘。', start: 24.0, end: 29.0 },
  ],
  blackWindows: [
    { start: 10, end: 20 }, // R2 全黑场景
  ],
  aaSamples: [
    { text: '重启不是遗忘。', size: 12, color: C.white },
    { text: '$ her: clawd, 关机', size: 10, color: C.text },
    { text: '✓ 欢迎回来。上次聊到哪里了？', size: 10, color: C.green },
    { text: 'clawd v1.0.0 — booting', size: 10, color: C.blue },
  ],
  scenes: [
    {
      id: 'R1',
      start: 0,
      end: 10,
      fadeOut: 2.5, // 屏幕逐渐变暗（7.5s → 10s）
      bg: { dawn: 0 },
      terminal: { title: 'clawd@dsh:~$ — shutdown', accent: C.red, led: 'on' },
      lines: R1_LINES,
      status: '[DSH] session: closing · 3 files saved',
      statusColor: C.dim,
      clawd: { mood: 'calm', blend: 0, palette: 'coral' },
      her: { pose: 'stand' },
      extra: (ctx, t) => {
        // 6.2s 电源灯熄灭
        if (t >= 6.2) {
          px(ctx, LED_X, LED_Y, 6, 6, '#2A2F38');
          px(ctx, LED_X + 1, LED_Y + 1, 2, 2, '#3A414C');
        }
      },
    },
    {
      id: 'R2',
      start: 10,
      end: 20,
      fadeIn: 0.3,
      fadeOut: 0.4,
      bg: (ctx) => px(ctx, 0, 0, P.BW, P.BH, '#000000'),
      terminal: null,
      clawd: null,
      her: null,
      overlays: [{ kind: 'led', x: LED_X, y: LED_Y, at: 13.0, click: false }],
      extra: (ctx, t) => {
        // 只有光标在闪烁：6×10 方块 + 三个小点（...）
        const on = Math.floor(t * 1.25) % 2 === 0;
        if (t < 13.0) {
          if (on) px(ctx, 316, 136, 6, 10, '#8B949E');
        } else {
          if (on) px(ctx, 316, 136, 6, 10, '#C9D1D9');
          for (let i = 0; i < 3; i++) {
            const a = 0.35 + 0.45 * Math.abs(Math.sin(t * 1.6 + i * 0.9));
            px(ctx, 306 + i * 10, 142, 2, 2, `rgba(201,209,217,${a.toFixed(3)})`);
          }
        }
      },
    },
    {
      id: 'R3',
      start: 20,
      end: 30,
      bg: { dawn: 0.12 },
      terminal: { title: 'clawd@dsh:~$ — boot', accent: C.green, led: 'on' },
      lines: R3_LINES,
      status: '[DSH] boot: complete · memory: intact',
      statusColor: C.green,
      clawd: (t) => (t < 23.2 ? { mood: 'calm', blend: 0 } : t < 24.6 ? { mood: 'thinking', blend: 1 } : { mood: 'smile', blend: 0 }),
      her: { pose: 'stand' },
      overlays: [
        { kind: 'note', box: P.RIGHT_NOTE, title: '记忆还在。', sub: 'Clawd · slot 0', at: 26.4 },
      ],
    },
  ],
});

// 电源音效时间点（混音脚本使用）
const SFX_EVENTS = [
  { t: 6.2, key: 'off', gain: 0.35 },
  { t: 13.0, key: 'on', gain: 0.4 },
  { t: 24.6, key: 'on', gain: 0.22 },
];

// 额外点击（电源灯 / 光标切换等无声事件不计）
const EXTRA_CLICKS = [];

if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = story.getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else if (process.argv.includes('--info')) {
    for (const sc of story.scenes) {
      console.log(`\n[${sc.id}] ${sc.start}-${sc.end}s  ${sc.terminal ? sc.terminal.title : '(no terminal / black)'}  fadeIn=${sc.fadeIn} fadeOut=${sc.fadeOut}`);
      for (const ln of sc.lines) console.log(`  y=${ln.y} start=${ln.start}s end=${lineEndTime(ln).toFixed(2)}s w=${ln.fullW}px  "${ln.full}"`);
    }
    console.log(`\nclicks: ${story.getClickTimestamps().length}`);
  } else {
    story.renderAllFrames();
  }
}

module.exports = {
  ...story,
  story,
  R1_LINES,
  R3_LINES,
  BOOT_START,
  SFX_EVENTS,
  EXTRA_CLICKS,
  LED_BOX: P.ledBox(),
};
