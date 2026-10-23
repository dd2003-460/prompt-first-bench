#!/usr/bin/env node
'use strict';
// src/render_dialogue_arena.js — 「Clawd 的对话」dialogue_arena v1.0
//
// 主题：Clawd 和 Her 的日常对话，展示 AI 如何理解人类语言。
// 规格：640×360 → nearest-neighbor 2× → 1280×720 @60fps，1800 帧（30.000s）
// 像素标准：SOP 05 §5（4-6px 像素块 / Fusion Pixel 10px / Clawd 40×17 / Her 16×28）
// 终端：440×200 @(100,140)（标题栏 20 + 内容区 180），与 companion v1.1 一致
//
// 剧本：
//   D1 (0-10s)  早安 — `$ her: 早上好` / `$ clawd: 早上好。今天有什么计划？` / `$ her: 写周报` /
//               `$ clawd: 需要我帮忙整理数据吗？`；Clawd calm；字幕「对话从早安开始。」
//   D2 (10-20s) 理解 — `$ her: 其实我今天有点累` / `$ clawd: 听起来你今天过得不容易。` /
//               `[clawd: 检测 → 情感: 疲惫 (0.82)]` / `$ her: 你怎么知道的？` /
//               `$ clawd: 你的消息比平时短了 40%。`；Clawd thinking；字幕「它学会了倾听。」
//   D3 (20-30s) 陪伴 — `$ her: 谢谢你` / `$ clawd: 不客气。我一直在这里。` /
//               `[clawd: 情感 → 温暖 (0.91)]`；Clawd smile；便签「陪伴。」；
//               字幕「这就是对话的意义。」
//
// 用法: node src/render_dialogue_arena.js [--info|--clicks]

const path = require('path');
const P = require('./pixel_arena_v3');
const { buildStory, lineEndTime } = require('./story_arena_v3');

const { C, ROW_Y, clamp01, easeOut } = P;
const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_dialogue');

// ---------------------------------------------------------------------------
// 终端剧本（每场景最多 5 行，行距 20px）
// ---------------------------------------------------------------------------
const D1_LINES = [
  { y: ROW_Y[0], start: 0.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '早上好', msgColor: C.text },
  { y: ROW_Y[1], start: 2.0, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '早上好。今天有什么计划？', msgColor: C.amber },
  { y: ROW_Y[2], start: 4.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '写周报', msgColor: C.text },
  { y: ROW_Y[3], start: 5.9, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '需要我帮忙整理数据吗？', msgColor: C.amber },
  { y: ROW_Y[4], start: 8.3, kind: 'line', parts: [{ text: '> intent: ', color: C.green }, { text: 'weekly_report · data', color: C.dim }] },
];

const D2_LINES = [
  { y: ROW_Y[0], start: 10.4, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '其实我今天有点累', msgColor: C.text },
  { y: ROW_Y[1], start: 12.0, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '听起来你今天过得不容易。', msgColor: C.amber },
  { y: ROW_Y[2], start: 14.2, kind: 'line', parts: [{ text: '[clawd: ', color: C.purple }, { text: '检测 → 情感: 疲惫 (0.82)', color: C.purple }, { text: ']', color: C.purple }] },
  { y: ROW_Y[3], start: 15.2, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '你怎么知道的？', msgColor: C.text },
  { y: ROW_Y[4], start: 16.8, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '你的消息比平时短了 40%。', msgColor: C.amber },
];

const D3_LINES = [
  { y: ROW_Y[0], start: 20.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '谢谢你', msgColor: C.text },
  { y: ROW_Y[1], start: 22.2, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '不客气。我一直在这里。', msgColor: C.amber },
  { y: ROW_Y[2], start: 25.4, kind: 'line', parts: [{ text: '[clawd: ', color: C.purple }, { text: '情感 → 温暖 (0.91)', color: C.purple }, { text: ']', color: C.purple }] },
  { y: ROW_Y[3], start: 26.6, kind: 'line', parts: [{ text: '> reply: ', color: C.green }, { text: 'here · always', color: C.dim }] },
  { y: ROW_Y[4], start: 27.4, kind: 'line', parts: [{ text: '> memory: ', color: C.green }, { text: '「谢谢你」→ slot 1', color: C.purple }] },
];

// ---------------------------------------------------------------------------
// 浮层
// ---------------------------------------------------------------------------
const BUBBLE_D1 = { kind: 'bubble', box: P.LEFT_BUBBLE, text: '早上好', at: 1.4 };
const THOUGHT_D2 = {
  kind: 'thought',
  box: P.LEFT_THOUGHT,
  at: 13.6,
  symbols: [
    { text: '...', at: 13.6 },
    { text: '?', at: 15.2 },
    { text: '!', at: 17.6 },
  ],
};
const NOTE_D3 = { kind: 'note', box: P.RIGHT_NOTE, title: '陪伴。', sub: 'Clawd · 对话', at: 26.0 };
const SPARK_D3 = { kind: 'sparkles', region: { x: 56, y: 206, w: 32, h: 26 }, count: 3, at: 27.6, click: false };
const SPARK_D3_REGION = { x: 56, y: 206, w: 32, h: 26 };

// ---------------------------------------------------------------------------
const story = buildStory({
  id: 'dialogue-v1.0',
  outDir: OUT_DIR,
  checkTitle: '「Clawd 的对话」v1.0 — Layout & Pixel Check (640×360, 0px tolerance)',
  subtitles: [
    { text: '对话从早安开始。', start: 2.0, end: 8.0 },
    { text: '它学会了倾听。', start: 12.0, end: 18.0 },
    { text: '这就是对话的意义。', start: 24.0, end: 29.0 },
  ],
  aaSamples: [
    { text: '这就是对话的意义。', size: 12, color: C.white },
    { text: '$ clawd: 早上好。今天有什么计划？', size: 10, color: C.amber },
    { text: '[clawd: 检测 → 情感: 疲惫 (0.82)]', size: 10, color: C.purple },
    { text: '> memory: 「谢谢你」→ slot 1', size: 10, color: C.purple },
  ],
  scenes: [
    {
      id: 'D1',
      start: 0,
      end: 10,
      bg: { dawn: 0.06 },
      terminal: { title: 'clawd@dsh:~$ — morning', accent: C.green, led: 'on' },
      lines: D1_LINES,
      status: '[DSH] dialogue: 4 turns · tone: calm',
      clawd: { mood: 'calm', blend: 0, palette: 'coral' },
      her: { pose: 'stand' },
      overlays: [BUBBLE_D1],
    },
    {
      id: 'D2',
      start: 10,
      end: 20,
      bg: { dawn: 0.12 },
      terminal: { title: 'clawd@dsh:~$ — listening', accent: C.purple, led: 'on' },
      lines: D2_LINES,
      status: '[DSH] sentiment: tired (0.82) · empathy: on',
      statusColor: C.purple,
      clawd: (t) => (t < 12.6 ? { mood: 'calm', blend: 0 } : { mood: 'thinking', blend: 1 }),
      her: { pose: 'stand' },
      overlays: [THOUGHT_D2],
    },
    {
      id: 'D3',
      start: 20,
      end: 30,
      bg: { dawn: 0.2 },
      terminal: { title: 'clawd@dsh:~$ — together', accent: C.amber, led: 'on' },
      lines: D3_LINES,
      status: '[DSH] warmth: 0.91 · memory: saved',
      statusColor: C.amber,
      clawd: { mood: 'smile', blend: 0, palette: 'coral' },
      her: (t) => ({ pose: t >= 23.4 ? 'smile' : 'stand' }),
      // D3 后半段：Clawd 身侧的温暖星尘（x∈[96,104)、y∈[272,318)，与终端/字幕条 0 重叠）
      overlays: [NOTE_D3, { kind: 'sparkles', region: SPARK_D3_REGION, count: 3, at: 27.6, click: false, color: '255,214,160' }],
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
  D1_LINES,
  D2_LINES,
  D3_LINES,
  BUBBLE_D1,
  THOUGHT_D2,
  NOTE_D3,
  EXTRA_CLICKS,
};
