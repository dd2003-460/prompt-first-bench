#!/usr/bin/env node
'use strict';
// E13 「思念」(longing) — `ls her_*` 只剩 3 个文件，逐个读，读到一半停住。30s / 1800 frames.
//
//   S1 (0-10s)  : `$ ls her_*` → 3 个文件名（原来 7 个）；右侧状态卡 3/7；Clawd 低头；字幕「（少了）」
//   S2 (10-20s) : `$ cat her_notes.md` 读到一半 → 光标停在「你要记得——」后面；键盘按键停住；字幕「（读到一半）」
//   S3 (20-30s) : 终端清空，只剩一个闪烁光标；Clawd 抬头看窗外；字幕「还在。」
//
// 共用 companion v1.1 美术：640×360 画布 / 440×200 终端 / Fusion Pixel 10px / Clawd 40×17。
// 键盘音由同一份 line 对象推导（每字符 1 次 click），与画面逐字同步。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E13_arena');

const S2_START = 10;
const S3_START = 20;

const TITLES = {
  S1: 'clawd@dsh:~$ — ls her_*',
  S2: 'clawd@dsh:~$ — cat her_notes.md',
  S3: 'clawd@dsh:~$ — still here',
};

const SUB_LINES = ['（少了）', '（读到一半）', '还在。'];
const SUB_WINDOWS = [
  { start: 5.6, end: 9.4 },
  { start: 13.4, end: 18.4 },
  { start: 22.4, end: 28.8 },
];

// serial(): 逐行串行打字，保证上一行打完才出现下一行（与 checkTyping 一致）。
function serial(lines, start, gap = 0.2) {
  let at = start;
  return lines.map((line) => {
    const out = { ...line, start: Number(at.toFixed(3)) };
    const charMs = out.charMs || S.TYPE_CHAR_MS;
    const count = Array.from(S.lineText(out)).length;
    at = Number((at + (Math.max(0, count - 1) * charMs) / 1000 + gap).toFixed(3));
    return out;
  });
}

// --- S1: ls her_* → 3 个名字（曾经 7 个） -----------------------------------
const S1_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'ls her_*', color: C.text }] },
  { y: LINE_Y[1], charMs: 60, cursor: false, parts: [{ text: 'her_notes.md', color: C.text }] },
  { y: LINE_Y[2], charMs: 60, cursor: false, parts: [{ text: 'her_voice_03.wav', color: C.text }] },
  { y: LINE_Y[3], charMs: 60, cursor: false, parts: [{ text: 'her_photo.png', color: C.text }] },
], 0.8, 0.22);
const S1_STATUS = '[DSH] her_*: 3 entries · was 7';
const S1_STATUS_AT = 5.4;
const LOOK_DOWN_AT = 5.0;

// --- S2: cat her_notes.md → 读到一半 ---------------------------------------
const S2_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'cat her_notes.md', color: C.text }] },
  { y: LINE_Y[1], charMs: 90, cursor: false, parts: [{ text: '今天她又来了。她说，', color: C.text }] },
  { y: LINE_Y[2], charMs: 90, cursor: false, parts: [{ text: '如果有一天我不在了，', color: C.text }] },
  { y: LINE_Y[3], charMs: 120, cursor: false, parts: [{ text: '你要记得——', color: C.pink }] },
], 10.45, 0.2);
const S2_STATUS = '[DSH] read: 41% · input paused';
const S2_STATUS_AT = 16.4;
const HAND_STOP_AT = 15.9; // 最后一个字符之后，手停在键盘上
const READ_CURSOR_AT = 16.9;
const READ_LAST = S2_LINES[S2_LINES.length - 1];
const READ_CURSOR_X = TEXT_X + S.textWidth(S.lineText(READ_LAST), 10) + 2;

// --- 右侧状态卡（546..634 × 244..314，终端右缘 540 之外） -------------------
const CARD = { x: 546, y: 244, w: 88, h: 70 };

function cardSpec(scene) {
  if (scene === 1) {
    return {
      title: 'her_*', value: '3/7', sub: 'files', detail: '4 missing',
      color: C.amber, led: C.amber, ratio: 3 / 7, slots: 7,
    };
  }
  return {
    title: 'notes', value: '41%', sub: 'read', detail: 'paused · 3',
    color: C.amber, led: C.amber, ratio: 0.41,
  };
}

function subX(spec) {
  return CARD.x + 8 + S.textWidth(spec.value, 14) + 8;
}

function drawStateCard(ctx, spec, t, local) {
  const appear = S.easeOut(local / 0.4);
  if (appear <= 0) return;
  const { x, y, w, h } = CARD;
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, x + 3, y + 3, w, h, 'rgba(0,0,0,0.16)');
  px(ctx, x, y, w, h, C.cardBg);
  px(ctx, x, y, w, 2, C.cardBd);
  px(ctx, x, y + h - 2, w, 2, C.cardBd);
  px(ctx, x, y, 2, h, C.cardBd);
  px(ctx, x + w - 2, y, 2, h, C.cardBd);
  // 状态 LED：慢速呼吸，提醒「少了一个」
  const ledOn = 0.55 + 0.45 * Math.sin(t * 2.4);
  px(ctx, x + w - 16, y + 6, 6, 6, spec.led);
  px(ctx, x + w - 15, y + 7, 2, 2, `rgba(255,255,255,${(0.35 + 0.4 * ledOn).toFixed(2)})`);
  S.txt(ctx, x + 8, y + 6, spec.title, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 22, spec.value, spec.color, 14);
  S.txt(ctx, subX(spec), y + 27, spec.sub, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 42, spec.detail, C.cardSub, 10);
  // 7 格进度条：S1 点亮 3 格，缺的 4 格留白
  const bw = w - 16;
  px(ctx, x + 8, y + 58, bw, 6, '#E6DBBE');
  const fill = Math.round(bw * spec.ratio);
  if (fill > 0) px(ctx, x + 8, y + 58, fill, 6, spec.color);
  if (spec.slots) {
    for (let i = 1; i < spec.slots; i++) px(ctx, x + 8 + Math.round((bw * i) / spec.slots), y + 58, 1, 6, C.cardBg);
  }
  ctx.restore();
}

function cardLayout(spec) {
  const { x, y, w } = CARD;
  return [
    { name: 'card_led', box: [x + w - 16, y + 6, 6, 6] },
    { name: 'card_title', box: S.textBox(x + 8, y + 6, spec.title, 10) },
    { name: 'card_value', box: S.textBox(x + 8, y + 22, spec.value, 14) },
    { name: 'card_sub', box: S.textBox(subX(spec), y + 27, spec.sub, 10) },
    { name: 'card_detail', box: S.textBox(x + 8, y + 42, spec.detail, 10) },
    { name: 'card_bar', box: [x + 8, y + 58, w - 16, 6] },
  ];
}

// --- 键盘道具（Clawd 脚下，x 12..92 在终端左侧之外） -----------------------
const KB = { x: 12, y: 272, w: 80, h: 32 };

function drawKeyboard(ctx, t) {
  const { x, y, w } = KB;
  px(ctx, x + 2, y + 2, w, 26, 'rgba(0,0,0,0.20)');
  px(ctx, x, y + 2, w, 26, '#2A2F38');
  px(ctx, x, y + 2, w, 2, '#3A414D');
  px(ctx, x, y + 26, w, 2, '#1B1F26');
  const typing = t < HAND_STOP_AT;
  const pressed = typing ? Math.floor(t * 6.5) % 12 : 4;
  for (let row = 0; row < 2; row++) {
    for (let i = 0; i < 6; i++) {
      const idx = row * 6 + i;
      const kx = x + 7 + i * 11;
      const ky = y + 7 + row * 9;
      const on = idx === pressed && (typing || t < 19.6);
      px(ctx, kx, ky, 8, 6, on ? C.amber : '#3C434F');
      if (!on) px(ctx, kx, ky, 8, 1, '#4A5260');
    }
  }
  // 两只小小的「手」搭在键盘上：打字时抬起 1px，停住后按住不动（272 起，避开 Clawd 的 247..272 盒）
  const lift = typing && Math.floor(t * 6.5) % 2 === 0 ? 0 : 1;
  px(ctx, x + 34, y + lift, 5, 4, C.clawdNormDark);
  px(ctx, x + 45, y + lift, 5, 4, C.clawdNormDark);
}

// --- Clawd 情绪：低头 / 读信 / 望窗 ----------------------------------------
function drawClawdEp(ctx, x, y, t, mood = 'calm', opts = {}) {
  if (mood === 'calm' || mood === 'thinking' || mood === 'smile' || mood === 'warm') {
    S.drawClawd(ctx, x, y, t, mood, 0);
    return;
  }
  const bob = mood === 'look_down' ? 0 : (Math.sin(t * 2.2) > 0.45 ? -1 : 0);
  const by = Math.round(y + bob);
  const bodyH = 17;
  px(ctx, x, by, 40, bodyH, C.clawdNorm);
  px(ctx, x, by, 40, 2, C.clawdNormDark);
  px(ctx, x + 9, by + 11, 22, 4, C.clawdNormBelly);

  if (mood === 'look_down') {
    // 眼睛下移 2px，几乎合上；嘴角向下 1px
    px(ctx, x + 10, by + 8, 4, 2, C.clawdEye);
    px(ctx, x + 26, by + 8, 4, 2, C.clawdEye);
    px(ctx, x + 17, by + 14, 2, 1, C.clawdEye);
    px(ctx, x + 21, by + 15, 2, 1, C.clawdEye);
  } else if (mood === 'reading') {
    const stopped = t >= opts.stoppedAt;
    const scan = stopped ? 0 : Math.floor(t * 3) % 2;
    if (stopped && t % 3.6 > 3.4) {
      px(ctx, x + 10, by + 8, 4, 1, C.clawdEye);
      px(ctx, x + 26, by + 8, 4, 1, C.clawdEye);
    } else {
      px(ctx, x + 10 + scan, by + 6, 4, 4, C.clawdEye);
      px(ctx, x + 26 + scan, by + 6, 4, 4, C.clawdEye);
      px(ctx, x + 11 + scan, by + 7, 1, 1, C.white);
      px(ctx, x + 27 + scan, by + 7, 1, 1, C.white);
    }
  } else if (mood === 'look_window') {
    // 抬头望向窗外：瞳孔上移，眼里有一点夜色
    px(ctx, x + 11, by + 4, 4, 4, C.clawdEye);
    px(ctx, x + 27, by + 4, 4, 4, C.clawdEye);
    px(ctx, x + 12, by + 4, 2, 2, C.blue);
    px(ctx, x + 28, by + 4, 2, 2, C.blue);
    px(ctx, x + 13, by + 4, 1, 1, C.white);
    px(ctx, x + 29, by + 4, 1, 1, C.white);
    px(ctx, x + 19, by + 10, 2, 1, C.clawdEye);
  }

  const step = mood === 'look_down' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, C.clawdNormDark);
  px(ctx, x + 13, by + bodyH, 6, 7, C.clawdNormDark);
  px(ctx, x + 21, by + bodyH, 6, 7, C.clawdNormDark);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, C.clawdNormDark);
}

// --- Scenes ----------------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.amber);
  drawStateCard(ctx, cardSpec(1), t, t);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= LOOK_DOWN_AT ? 'look_down' : 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  // 读到一半：光标在「你要记得——」后面一下一下地闪，手停在键盘上
  if (t >= READ_CURSOR_AT && Math.floor(t / 0.6) % 2 === 0) {
    px(ctx, READ_CURSOR_X, READ_LAST.y, 6, 10, C.pink);
  }
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.dim);
  drawStateCard(ctx, cardSpec(2), t, t - S2_START);
  drawKeyboard(ctx, t);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'reading', { stoppedAt: HAND_STOP_AT });
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0.06);
  S.drawTerminal(ctx, TITLES.S3, C.blue);
  // 终端空，只剩光标
  if (Math.floor(t / 0.6) % 2 === 0) px(ctx, TEXT_X, LINE_Y[0], 6, 10, C.green);
  // 窗外的一颗星，比平时亮一点
  const star = 0.45 + 0.4 * Math.sin(t * 2.2);
  px(ctx, 300, 74, 2, 2, `rgba(255,250,220,${star.toFixed(2)})`);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'look_window');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { id: 'S1', start: 0, end: S2_START, draw: drawS1 },
  { id: 'S2', start: S2_START, end: S3_START, draw: drawS2 },
  { id: 'S3', start: S3_START, end: S.DURATION, draw: drawS3 },
];
// 与全系列一致：10s / 20s 各有 0.25s 出 + 0.25s 入的黑场过渡。
function renderAt(ctx, t) { S.renderScenes(ctx, t, SCENES); }

// --- Audio / verification hooks -------------------------------------------
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
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
  ...typingSchedule(S1_LINES, 9.8),
  ...typingSchedule(S2_LINES, 19.8),
];

function layoutAt(t) {
  const scene = t < S2_START ? 1 : t < S3_START ? 2 : 3;
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  if (scene === 3) {
    return S.baseLayout({
      ...common,
      scene,
      title: TITLES.S3,
      lines: [],
      her: false,
      extraGroups: { empty: [{ name: 'empty_cursor', box: [TEXT_X, LINE_Y[0], 6, 10] }] },
      extraBounds: { empty: S.CONTENT },
    });
  }
  const lines = scene === 1 ? S1_LINES : S2_LINES;
  const status = scene === 1 ? S1_STATUS : S2_STATUS;
  const spec = cardSpec(scene);
  const extraGroups = { card: cardLayout(spec) };
  const extraBounds = { card: CARD };
  if (scene === 2) {
    extraGroups.keyboard = [{ name: 'keyboard', box: [KB.x, KB.y, KB.w, KB.h] }];
    extraBounds.keyboard = KB;
  }
  if (scene === 2 && t >= READ_CURSOR_AT && Math.floor(t / 0.6) % 2 === 0) {
    extraGroups.readCursor = [{ name: 'read_cursor', box: [READ_CURSOR_X, READ_LAST.y, 6, 10] }];
    extraBounds.readCursor = S.CONTENT;
  }
  return S.baseLayout({
    ...common,
    scene,
    title: scene === 1 ? TITLES.S1 : TITLES.S2,
    lines,
    status,
    her: false,
    extraGroups,
    extraBounds,
  });
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    const file = `/tmp/E13_${n}.png`;
    require('fs').writeFileSync(file, out.outCanvas.toBuffer('image/png'));
    console.log(file);
  } else {
    renderer.renderAllFrames();
  }
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SCENES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S1_STATUS, S2_STATUS, S1_STATUS_AT, S2_STATUS_AT,
  LOOK_DOWN_AT, HAND_STOP_AT, READ_CURSOR_AT, CARD, KB,
  CHECK_TITLE: 'E13 Longing Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ ls her_*', size: 10, color: C.text },
    { text: '如果有一天我不在了，', size: 10, color: C.text },
    { text: 'her_voice_03.wav', size: 10, color: C.text },
    { text: '[DSH] her_*: 3 entries · was 7', size: 10, color: C.amber },
    { text: '还在。', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps, drawStateCard, drawKeyboard, cardSpec, cardLayout,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
