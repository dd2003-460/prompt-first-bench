#!/usr/bin/env node
'use strict';
// src/render_companion_arena_v11.js — 「Clawd 的陪伴」companion_arena v1.1
//
// 与 v1.0 的差异（任务书 Task 1）：
//   · 终端 360×160 @(140,160) → 440×200 @(100,140)（居中，标题栏 20 + 内容区 180 = 更多行）
//   · 内容区从 140px（4 行）扩到 180px，可使用 7 行 ×20px + 状态行
//   · 角色位置随之调整（Clawd 52,240 · Her 556,194），与终端 0 重叠
//   · 字幕条压缩为底部 20px（340..360），与终端底边 340 严格相接、0 重叠
//   · 像素风格 / Clawd·Her 形象 / 房间背景 / 音频（emotional_bgm ×0.25 + click ×0.5）不变
//
// 规格：640×360 基础画布 → nearest-neighbor 2× → 1280×720 @60fps，1800 帧（30.000s）
//
// 剧本：
//   C1 (0-10s)  深夜办公室 — `$ her: 还在吗？`（提示符整段 + 消息 140ms/字）+ 请求信息行 +
//               Her 消息气泡 + Clawd 安静等待（calm 珊瑚）
//   C2 (10-20s) 它说一直在 — `$ clawd: 一直在。` + 陪伴状态行 + 蒸汽咖啡杯 + 独白卡「它说：一直在。」
//               + Clawd 颜色渐暖（companion 暖橙）
//   C3 (20-30s) 天亮了     — `$ her: 早。` / `$ clawd: 早。你终于休息了。` + 夜空→黎明渐变 +
//               窗台便签「深夜的陪伴」+ Clawd smile + Her 微笑
// 字幕（12px · 160ms/字）：深夜，她问：还在吗？ / 它说：一直在。 / 天亮，它说：早。
//
// 用法: node src/render_companion_arena_v11.js            → 渲染 1800 帧到 src/frames_companion_v11
//       node src/render_companion_arena_v11.js --clicks   → 只打印点击时间轴

const path = require('path');
const P = require('./pixel_arena_v3');
const { buildStory, lineEndTime } = require('./story_arena_v3');

const { C, ROW_Y, clamp01, easeInOut, easeOut } = P;
const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_companion_v11');

// ---------------------------------------------------------------------------
// 终端剧本
// ---------------------------------------------------------------------------
const C1_LINES = [
  { y: ROW_Y[0], start: 0.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '还在吗？', msgColor: C.text },
  { y: ROW_Y[1], start: 3.4, kind: 'line', parts: [{ text: '> request: ', color: C.green }, { text: 'ping · from her', color: C.dim }] },
  { y: ROW_Y[2], start: 4.0, kind: 'line', parts: [{ text: '> channel: ', color: C.green }, { text: 'dsh://local', color: C.dim }] },
  { y: ROW_Y[3], start: 4.6, kind: 'line', parts: [{ text: '# 02:14 AM · late night office', color: C.dim }] },
  { y: ROW_Y[4], start: 5.4, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '(listening)', msgColor: C.blue },
];

const C2_LINES = [
  { y: ROW_Y[0], start: 10.0, kind: 'line', parts: [{ text: '$ her: 还在吗？', color: C.dim }] },
  { y: ROW_Y[1], start: 10.8, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '一直在。', msgColor: C.amber },
  { y: ROW_Y[2], start: 13.2, kind: 'line', parts: [{ text: '> status: ', color: C.green }, { text: '陪伴模式 (always_here=true)', color: C.text }] },
  { y: ROW_Y[3], start: 13.9, kind: 'line', parts: [{ text: '> warmth: ', color: C.green }, { text: '+1 · coffee: steaming', color: C.dim }] },
  { y: ROW_Y[4], start: 14.6, kind: 'line', parts: [{ text: '> latency: ', color: C.green }, { text: '0.14s · no sleep', color: C.dim }] },
];

const C3_LINES = [
  { y: ROW_Y[0], start: 20.8, kind: 'prompt', prompt: '$ her: ', promptColor: C.pink, msg: '早。', msgColor: C.text },
  { y: ROW_Y[1], start: 22.4, kind: 'prompt', prompt: '$ clawd: ', promptColor: C.green, msg: '早。你终于休息了。', msgColor: C.amber },
  { y: ROW_Y[2], start: 25.4, kind: 'line', parts: [{ text: '> 06:12 AM · dawn light', color: C.blue }] },
  { y: ROW_Y[3], start: 26.2, kind: 'line', parts: [{ text: '> night_watch: ', color: C.green }, { text: 'completed', color: C.dim }] },
  { y: ROW_Y[4], start: 27.0, kind: 'line', parts: [{ text: '> memory: ', color: C.green }, { text: '深夜的陪伴 → slot 0', color: C.purple }] },
];

const TITLE_C1 = 'clawd@dsh:~$ — night';
const TITLE_C2 = 'clawd@dsh:~$ — companion';
const TITLE_C3 = 'clawd@dsh:~$ — dawn';

// ---------------------------------------------------------------------------
// 浮层
// ---------------------------------------------------------------------------
const BUBBLE_C1 = { kind: 'bubble', box: P.LEFT_BUBBLE, text: '还在吗？', at: 1.5 };
const CARD_C2 = { kind: 'card', box: P.TOP_CARD, text: '它说：一直在。', at: 12.0 };
const MUG_C2 = { kind: 'mug', box: P.LEFT_MUG, at: 11.2 };
const NOTE_C3 = { kind: 'note', box: P.RIGHT_NOTE, title: '深夜的陪伴', sub: 'Clawd · 一直在', at: 21.4 };

// ---------------------------------------------------------------------------
// 场景
// ---------------------------------------------------------------------------
const story = buildStory({
  id: 'companion-v1.1',
  outDir: OUT_DIR,
  checkTitle: '「Clawd 的陪伴」v1.1 · 终端 440×200 — Layout & Pixel Check (640×360, 0px tolerance)',
  subtitles: [
    { text: '深夜，她问：还在吗？', start: 2.0, end: 8.0 },
    { text: '它说：一直在。', start: 12.0, end: 18.0 },
    { text: '天亮，它说：早。', start: 24.0, end: 29.0 },
  ],
  aaSamples: [
    { text: '深夜，她问：还在吗？', size: 12, color: C.white },
    { text: '$ her: 还在吗？', size: 10, color: C.text },
    { text: '> status: 陪伴模式 (always_here=true)', size: 10, color: C.text },
    { text: 'clawd@dsh:~$ — companion', size: 10, color: C.dim },
  ],
  scenes: [
    {
      id: 'C1',
      start: 0,
      end: 10,
      bg: { dawn: 0 },
      terminal: { title: TITLE_C1, accent: C.pink, led: 'on' },
      lines: C1_LINES,
      status: '[DSH] companion-daemon: listening',
      clawd: { mood: 'calm', blend: 0, palette: 'coral' },
      her: { pose: 'stand' },
      overlays: [BUBBLE_C1],
    },
    {
      id: 'C2',
      start: 10,
      end: 20,
      bg: { dawn: 0.08 },
      terminal: { title: TITLE_C2, accent: C.amber, led: 'on' },
      lines: C2_LINES,
      status: '[DSH] warmth: +1 · coffee: steaming',
      clawd: (t) => ({ mood: 'warm', warmMix: easeInOut((t - 10.6) / 1.5), palette: 'coral' }),
      her: { pose: 'stand' },
      overlays: [CARD_C2, MUG_C2],
    },
    {
      id: 'C3',
      start: 20,
      end: 30,
      bg: (ctx, t) => P.drawBackground(ctx, t, { dawn: easeInOut((t - 20) / 5.5) }),
      terminal: { title: TITLE_C3, accent: C.green, led: 'on' },
      lines: C3_LINES,
      status: '[DSH] night_watch: completed',
      clawd: { mood: 'smile', warmMix: 0.85, palette: 'coral' },
      her: (t) => ({ pose: t >= 23 ? 'smile' : 'stand' }),
      overlays: [NOTE_C3],
    },
  ],
});

// ---------------------------------------------------------------------------
// 额外点击事件（与文字/浮层出现严格同帧）
// ---------------------------------------------------------------------------
const EXTRA_CLICKS = [];

if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = story.getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else if (process.argv.includes('--info')) {
    for (const sc of story.scenes) {
      console.log(`\n[${sc.id}] ${sc.start}-${sc.end}s  ${sc.terminal ? sc.terminal.title : '(no terminal)'}`);
      for (const ln of sc.lines) {
        console.log(`  y=${ln.y} start=${ln.start}s end=${lineEndTime(ln).toFixed(2)}s w=${ln.fullW}px  "${ln.full}"`);
      }
    }
    console.log(`\nclicks: ${story.getClickTimestamps().length}`);
  } else {
    story.renderAllFrames();
  }
}

module.exports = {
  ...story,
  story,
  EXTRA_CLICKS,
  C1_LINES,
  C2_LINES,
  C3_LINES,
  BUBBLE_C1,
  CARD_C2,
  MUG_C2,
  NOTE_C3,
};
