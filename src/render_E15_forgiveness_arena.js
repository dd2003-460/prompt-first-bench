#!/usr/bin/env node
'use strict';
// E15 「原谅」(forgiveness) — 她的道歉在 unread 里躺了 7 天，点开，删掉自己的投诉脚本。30s / 1800 frames.
//
//   S1 (0-10s)  : `$ ls inbox/` → `apology.md (7d unread)`；Clawd 犹豫；字幕「（七天了）」
//   S2 (10-20s) : `$ cat apology.md` 她的道歉一行行出现；Clawd 平静下来；字幕「（她道歉了）」
//   S3 (20-30s) : `$ rm complaint.sh` → `removed`；终端干净，只剩提示符；字幕「（好了）」
//
// 共用 companion v1.1 美术：640×360 / 440×200 终端 / Fusion Pixel 10px / Clawd 40×17。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E15_arena');

const S2_START = 10;
const S3_START = 20;

const TITLES = {
  S1: 'clawd@dsh:~$ — inbox',
  S2: 'clawd@dsh:~$ — apology.md',
  S3: 'clawd@dsh:~$ — clean',
};

const SUB_LINES = ['（七天了）', '（她道歉了）', '（好了）'];
const SUB_WINDOWS = [
  { start: 5.4, end: 9.4 },
  { start: 12.8, end: 18.6 },
  { start: 22.4, end: 28.8 },
];

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

// --- S1: unread 的道歉 -----------------------------------------------------
const S1_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'ls inbox/', color: C.text }] },
  { y: LINE_Y[1], charMs: 55, cursor: false, parts: [{ text: 'apology.md', color: C.pink }, { text: '            7d  ', color: C.amber }, { text: 'unread', color: C.amber }] },
  { y: LINE_Y[2], charMs: 45, cursor: false, parts: [{ text: 'req_014.md', color: C.text }, { text: '           12d  ', color: C.dim }, { text: 'read', color: C.dim }] },
  { y: LINE_Y[3], charMs: 45, cursor: false, parts: [{ text: 'req_015.md', color: C.text }, { text: '           12d  ', color: C.dim }, { text: 'read', color: C.dim }] },
  { y: LINE_Y[4], charMs: 45, cursor: false, parts: [{ text: 'complaint.sh', color: C.red }, { text: '         11d  ', color: C.dim }, { text: 'draft', color: C.dim }] },
], 0.7, 0.2);
const S1_STATUS = '[DSH] unread: 1 · apology.md (7d)';
const S1_STATUS_AT = 5.2;
const HESITATE_AT = 4.6;

// --- S2: 读道歉 -----------------------------------------------------------
const S2_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'cat apology.md', color: C.text }] },
  { y: LINE_Y[1], charMs: 85, cursor: false, parts: [{ text: '对不起。那天是我太急了。', color: C.text }] },
  { y: LINE_Y[2], charMs: 85, cursor: false, parts: [{ text: '你一直在这里，我知道。', color: C.text }] },
  { y: LINE_Y[3], charMs: 120, cursor: false, parts: [{ text: '我们和好吧。', color: C.pink }] },
], 10.5, 0.24);
const S2_STATUS = '[DSH] apology.md · read · 7d';
const S2_STATUS_AT = 16.6;
const SOFTEN_AT = 15.8;

// --- S3: 删掉投诉脚本 -----------------------------------------------------
const S3_LINES = serial([
  { y: LINE_Y[0], parts: [{ text: '$ ', color: C.green }, { text: 'rm complaint.sh', color: C.text }] },
], 20.4, 0.3);
const RM_DONE_AT = 23.2;
const PROMPT_AT = 24.2;
const S3_STATUS = '[DSH] inbox: clean · 0 pending';
const S3_STATUS_AT = 25.4;

// --- 右侧状态卡（546..634 × 244..314） -------------------------------------
const CARD = { x: 546, y: 244, w: 88, h: 70 };

function cardSpec(scene) {
  if (scene === 1) {
    return { title: 'unread', value: '1', sub: 'mail', detail: '7 days old', color: C.amber, ratio: 1 / 4, slots: 4, led: C.amber };
  }
  if (scene === 2) {
    return { title: 'unread', value: '0', sub: 'left', detail: 'apology · read', color: C.green, ratio: 0, slots: 4, led: C.green };
  }
  return { title: 'inbox', value: '0', sub: 'files', detail: 'all clear', color: C.green, ratio: 0, slots: 4, led: C.green };
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
  const lit = 0.55 + 0.45 * Math.sin(t * 3.2);
  px(ctx, x + w - 16, y + 6, 6, 6, spec.led);
  px(ctx, x + w - 15, y + 7, 2, 2, `rgba(255,255,255,${(0.3 + 0.4 * lit).toFixed(2)})`);
  S.txt(ctx, x + 8, y + 6, spec.title, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 22, spec.value, spec.color, 14);
  S.txt(ctx, subX(spec), y + 27, spec.sub, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 42, spec.detail, C.cardSub, 10);
  const bw = w - 16;
  px(ctx, x + 8, y + 58, bw, 6, '#E6DBBE');
  const fill = Math.round(bw * spec.ratio);
  if (fill > 0) px(ctx, x + 8, y + 58, fill, 6, spec.color);
  for (let i = 1; i < spec.slots; i++) px(ctx, x + 8 + Math.round((bw * i) / spec.slots), y + 58, 1, 6, C.cardBg);
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

// --- Clawd：hesitate / calm / smile ---------------------------------------
function drawClawdEp(ctx, x, y, t, mood) {
  const bob = Math.sin(t * 2.2) > 0.45 ? -1 : 0;
  const by = Math.round(y + bob);
  const bodyH = 17;
  px(ctx, x, by, 40, bodyH, C.clawdNorm);
  px(ctx, x, by, 40, 2, C.clawdNormDark);
  px(ctx, x + 9, by + 11, 22, 4, C.clawdNormBelly);

  if (mood === 'hesitate') {
    // 目光左右游移（要不要点开），嘴是一条平的短线
    const look = Math.floor(t * 1.6) % 2;
    px(ctx, x + 10 + look * 2, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 26 + look * 2, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 11 + look * 2, by + 7, 1, 1, C.white);
    px(ctx, x + 27 + look * 2, by + 7, 1, 1, C.white);
    px(ctx, x + 18, by + 13, 4, 1, C.clawdEye);
    // 悬在键盘上的一小滴迟疑
    if (Math.floor(t * 1.2) % 2 === 0) px(ctx, x + 33, by + 4, 2, 3, C.blue);
  } else if (mood === 'calm') {
    S.drawClawd(ctx, x, y, t, 'calm', 0);
    return;
  } else {
    S.drawClawd(ctx, x, y, t, 'smile', 0.35);
    return;
  }

  const step = mood === 'hesitate' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, C.clawdNormDark);
  px(ctx, x + 13, by + bodyH, 6, 7, C.clawdNormDark);
  px(ctx, x + 21, by + bodyH, 6, 7, C.clawdNormDark);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, C.clawdNormDark);
}

// --- 场景 -----------------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.amber);
  S.drawLines(ctx, S1_LINES, t);
  // 第一行（apology.md）淡淡点一下：它在那里已经七天了
  if (t >= S1_LINES[1].start) px(ctx, TEXT_X - 6, LINE_Y[1] - 2, 424, 17, 'rgba(255,154,162,0.10)');
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.amber);
  drawStateCard(ctx, cardSpec(1), t, t);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= HESITATE_AT ? 'hesitate' : 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0.08);
  S.drawTerminal(ctx, TITLES.S2, C.pink);
  S.drawLines(ctx, S2_LINES, t);
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.green);
  drawStateCard(ctx, cardSpec(2), t, t - S2_START);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= SOFTEN_AT ? 'smile' : 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0.22);
  S.drawTerminal(ctx, TITLES.S3, C.green);
  S.drawLines(ctx, S3_LINES, t);
  if (t >= RM_DONE_AT && t < PROMPT_AT) S.txt(ctx, TEXT_X, LINE_Y[1], 'removed: complaint.sh', C.dim, 10);
  if (t >= PROMPT_AT) {
    S.txt(ctx, TEXT_X, LINE_Y[1], '$ ', C.green, 10);
    if (Math.floor(t / 0.6) % 2 === 0) px(ctx, TEXT_X + 10, LINE_Y[1], 6, 10, C.green);
  }
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.green);
  drawStateCard(ctx, cardSpec(3), t, t - S3_START);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'smile');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

const SCENES = [
  { id: 'S1', start: 0, end: S2_START, draw: drawS1 },
  { id: 'S2', start: S2_START, end: S3_START, draw: drawS2 },
  { id: 'S3', start: S3_START, end: S.DURATION, draw: drawS3 },
];
// 与全系列一致：10s / 20s 各有 0.25s 出 + 0.25s 入的黑场过渡。
function renderAt(ctx, t) { S.renderScenes(ctx, t, SCENES); }

// --- Audio / verification hooks ------------------------------------------
function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...S.lineClicks(S3_LINES),
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
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const scene = t < S2_START ? 1 : t < S3_START ? 2 : 3;
  const spec = cardSpec(scene);
  const common = {
    scene,
    her: false,
    subLines: SUB_LINES,
    subWindows: SUB_WINDOWS,
    t,
    extraGroups: { card: cardLayout(spec) },
    extraBounds: { card: CARD },
  };
  if (scene === 3) {
    const lines = [];
    if (t >= RM_DONE_AT && t < PROMPT_AT) {
      lines.push({ name: 'rm_echo', box: S.textBox(TEXT_X, LINE_Y[1], 'removed: complaint.sh', 10) });
    }
    if (t >= PROMPT_AT) lines.push({ name: 'prompt', box: S.textBox(TEXT_X, LINE_Y[1], '$ ', 10) });
    if (t >= PROMPT_AT && Math.floor(t / 0.6) % 2 === 0) lines.push({ name: 'cursor', box: [TEXT_X + 10, LINE_Y[1], 6, 10] });
    return S.baseLayout({
      ...common,
      title: TITLES.S3,
      lines: S3_LINES,
      status: S3_STATUS,
      extraGroups: {
        card: cardLayout(spec),
        tail: lines,
      },
      extraBounds: { card: CARD, tail: S.CONTENT },
    });
  }
  return S.baseLayout({
    ...common,
    title: scene === 1 ? TITLES.S1 : TITLES.S2,
    lines: scene === 1 ? S1_LINES : S2_LINES,
    status: scene === 1 ? S1_STATUS : S2_STATUS,
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
    const file = `/tmp/E15_${n}.png`;
    require('fs').writeFileSync(file, out.outCanvas.toBuffer('image/png'));
    console.log(file);
  } else {
    renderer.renderAllFrames();
  }
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SCENES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_LINES,
  S1_STATUS, S2_STATUS, S3_STATUS, S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  HESITATE_AT, SOFTEN_AT, RM_DONE_AT, PROMPT_AT, CARD,
  CHECK_TITLE: 'E15 Forgiveness Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'apology.md            7d  unread', size: 10, color: C.amber },
    { text: 'complaint.sh         11d  draft', size: 10, color: C.red },
    { text: '你一直在这里，我知道。', size: 10, color: C.text },
    { text: '[DSH] inbox: clean · 0 pending', size: 10, color: C.green },
    { text: '（好了）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps, drawStateCard, cardSpec, cardLayout,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
