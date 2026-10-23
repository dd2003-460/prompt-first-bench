#!/usr/bin/env node
'use strict';
// src/render_farewell_arena.js — 「Clawd 的告别」farewell_arena v1.0
//
// 主题：Clawd 和 Her 的告别，但不是永别。
// 规格：640×360 → nearest-neighbor 2× → 1280×720 @60fps，1800 帧（30.000s）
// 像素标准：SOP 05 §5（4-6px 像素块 / Fusion Pixel 10px / Clawd 40×17 / Her 16×28）
// 终端：440×200 @(100,140)（标题栏 20 + 内容区 180），与 companion v1.1 一致
//
// 剧本：
//   F1 (0-10s)  决定 — `$ her: 我要去旅行了，一个月` / `$ clawd: 好的。我会在这里等你。` /
//               `$ her: 你会忘记我吗？`；Clawd 犹豫（thinking）
//               字幕「一个月，对它来说是多久？」
//   F2 (10-20s) 等待 — `$ clawd: 不会。` / `[clawd: 设置提醒 → 30天后]` /
//               `[clawd: 写入 memory/her_return_date.txt]` / 第 1 天... 第 7 天... 第 15 天...
//               屏幕逐渐变暗（时间流逝，12.0s 起 7s 缓降）；字幕「它记得。」
//   F3 (20-30s) 回来 — 第 30 天... / `$ her: 我回来了` / `$ clawd: 欢迎回来。外面冷吗？` /
//               `[clawd: memory/her_return_date.txt → 已删除]`；Clawd smile；便签「欢迎回来。」
//               字幕「告别不是结束。」
//
// 用法: node src/render_farewell_arena.js [--info|--clicks]

const path = require('path');
const P = require('./pixel_arena_v3');
const { buildStory, lineEndTime } = require('./story_arena_v3');

const { C, ROW_Y, px, clamp01, easeInOut } = P;
const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_farewell');

// ---------------------------------------------------------------------------
// F1 决定
// ---------------------------------------------------------------------------
const F1_LINES = [
  { y: ROW_Y[0], start: 0.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '我要去旅行了，一个月', msgColor: C.text },
  { y: ROW_Y[1], start: 3.8, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '好的。我会在这里等你。', msgColor: C.amber },
  { y: ROW_Y[2], start: 7.0, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '你会忘记我吗？', msgColor: C.text },
  { y: ROW_Y[3], start: 8.6, kind: 'line', parts: [{ text: '> thinking...', color: C.dim }] },
];

// ---------------------------------------------------------------------------
// F2 等待
// ---------------------------------------------------------------------------
const F2_LINES = [
  { y: ROW_Y[0], start: 10.6, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '不会。', msgColor: C.amber },
  { y: ROW_Y[1], start: 12.4, kind: 'line', parts: [{ text: '[clawd: ', color: C.purple }, { text: '设置提醒 → 30天后', color: C.purple }, { text: ']', color: C.purple }] },
  { y: ROW_Y[2], start: 13.4, kind: 'line', parts: [{ text: '[clawd: ', color: C.purple }, { text: '写入 memory/her_return_date.txt', color: C.purple }, { text: ']', color: C.purple }] },
  { y: ROW_Y[3], start: 15.0, kind: 'line', parts: [{ text: '她走后的第 1 天...', color: C.dim }] },
  { y: ROW_Y[4], start: 16.2, kind: 'line', parts: [{ text: '第 7 天...', color: C.dim }] },
  { y: ROW_Y[5], start: 17.4, kind: 'line', parts: [{ text: '第 15 天...', color: C.dim }] },
];

// ---------------------------------------------------------------------------
// F3 回来
// ---------------------------------------------------------------------------
const F3_LINES = [
  { y: ROW_Y[0], start: 20.5, kind: 'line', parts: [{ text: '第 30 天...', color: C.blue }] },
  { y: ROW_Y[1], start: 21.6, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '我回来了', msgColor: C.text },
  { y: ROW_Y[2], start: 23.0, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '欢迎回来。外面冷吗？', msgColor: C.amber },
  { y: ROW_Y[3], start: 25.6, kind: 'line', parts: [{ text: '[clawd: ', color: C.purple }, { text: 'memory/her_return_date.txt → 已删除', color: C.purple }, { text: ']', color: C.purple }] },
  { y: ROW_Y[4], start: 27.0, kind: 'line', parts: [{ text: '> 她回来了。', color: C.green }] },
];

// ---------------------------------------------------------------------------
const story = buildStory({
  id: 'farewell-v1.0',
  outDir: OUT_DIR,
  checkTitle: '「Clawd 的告别」v1.0 — Layout & Pixel Check (640×360, 0px tolerance)',
  subtitles: [
    { text: '一个月，对它来说是多久？', start: 2.0, end: 8.0 },
    { text: '它记得。', start: 13.0, end: 19.0 },
    { text: '告别不是结束。', start: 24.0, end: 29.0 },
  ],
  aaSamples: [
    { text: '一个月，对它来说是多久？', size: 12, color: C.white },
    { text: '$ her: 我要去旅行了，一个月', size: 10, color: C.text },
    { text: '[clawd: memory/her_return_date.txt → 已删除]', size: 10, color: C.purple },
    { text: '欢迎回来。外面冷吗？', size: 10, color: C.amber },
  ],
  scenes: [
    {
      id: 'F1',
      start: 0,
      end: 10,
      bg: { dawn: 0.1 },
      terminal: { title: 'clawd@dsh:~$ — a trip', accent: C.pink, led: 'on' },
      lines: F1_LINES,
      status: '[DSH] session: open · next visit: unknown',
      clawd: (t) => (t < 8.0 ? { mood: 'calm', blend: 0 } : { mood: 'thinking', blend: 1 }),
      her: { pose: 'stand' },
      overlays: [
        { kind: 'bubble', box: P.LEFT_BUBBLE, text: '你会忘记我吗？', at: 7.0 },
        { kind: 'thought', box: P.LEFT_THOUGHT, at: 8.2, symbols: [{ text: '...', at: 8.2 }, { text: '?', at: 9.0 }] },
      ],
    },
    {
      id: 'F2',
      start: 10,
      end: 20,
      bg: { dawn: 0.16 },
      terminal: { title: 'clawd@dsh:~$ — waiting', accent: C.blue, led: 'on' },
      lines: F2_LINES,
      status: '[DSH] reminder: 30 days · watching door',
      statusColor: C.blue,
      clawd: { mood: 'calm', blend: 0, palette: 'coral' },
      her: { pose: 'stand', visible: false },
      extra: (ctx, t) => {
        // 时间流逝：12.0s 起 7s 内房间缓慢变暗（透明度 0 → 0.55），20s 前回到 0.5 并保持
        const k = clamp01((t - 12.0) / 7.0);
        const a = 0.5 * k;
        if (a > 0.001) px(ctx, 0, 0, P.BW, P.BH, `rgba(0,0,0,${a.toFixed(3)})`);
      },
    },
    {
      id: 'F3',
      start: 20,
      end: 30,
      bg: { dawn: 0.28 },
      terminal: { title: 'clawd@dsh:~$ — welcome back', accent: C.green, led: 'on' },
      lines: F3_LINES,
      status: '[DSH] memory: cleared · she is here',
      statusColor: C.green,
      clawd: (t) => (t < 23.0 ? { mood: 'thinking', blend: 1 } : { mood: 'smile', blend: 0 }),
      her: (t) => ({ pose: t >= 22.4 ? 'smile' : 'stand' }),
      overlays: [
        { kind: 'note', box: P.RIGHT_NOTE, title: '欢迎回来。', sub: 'Clawd · 30 天', at: 25.8 },
        { kind: 'sparkles', region: { x: 56, y: 206, w: 32, h: 26 }, count: 3, at: 26.2, click: false, color: '255,214,160' },
      ],
    },
  ],
});

const EXTRA_CLICKS = [];

if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = story.getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else if (process.argv.includes('--info')) {
    for (const sc of story.scenes) {
      console.log(`\n[${sc.id}] ${sc.start}-${sc.end}s  ${sc.terminal ? sc.terminal.title : '(no terminal)'}`);
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
  F1_LINES,
  F2_LINES,
  F3_LINES,
  EXTRA_CLICKS,
};
