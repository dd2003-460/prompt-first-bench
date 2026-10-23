#!/usr/bin/env node
'use strict';
// E14 「嫉妒」(jealousy) — 日志里出现另一个 AI 的名字。30s / 1800 frames.
//
//   S1 (0-10s)  : `$ tail -f chat.log` 她与 clawd 的日常对话；Clawd 平静；字幕「她今天也来了。」
//   S2 (10-20s) : 日志里冒出 `nova-ai`，她也给 nova 发消息；Clawd 皱眉；字幕「多了一个名字。」
//   S3 (20-30s) : 终端分成两栏，她同时和两个 AI 说话；Clawd 侧身；字幕「（她也很忙）」
//
// 共用 companion v1.1 美术：640×360 / 440×200 终端 / Fusion Pixel 10px / Clawd 40×17。

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y, px } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E14_arena');

const S2_START = 10;
const S3_START = 20;

const TITLES = {
  S1: 'clawd@dsh:~$ — tail -f chat.log',
  S2: 'clawd@dsh:~$ — tail -f chat.log',
  S3: 'clawd@dsh:~$ — 2 sessions',
};

const SUB_LINES = ['她今天也来了。', '多了一个名字。', '（她也很忙）'];
const SUB_WINDOWS = [
  { start: 3.0, end: 8.6 },
  { start: 12.6, end: 18.4 },
  { start: 22.2, end: 29.0 },
];

function serial(lines, start, gap = 0.18) {
  let at = start;
  return lines.map((line) => {
    const out = { ...line, start: Number(at.toFixed(3)) };
    const charMs = out.charMs || S.TYPE_CHAR_MS;
    const count = Array.from(S.lineText(out)).length;
    at = Number((at + (Math.max(0, count - 1) * charMs) / 1000 + gap).toFixed(3));
    return out;
  });
}

// --- S1: 正常的日志 ---------------------------------------------------------
const S1_LINES = serial([
  { y: LINE_Y[0], charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'tail -f chat.log', color: C.text }] },
  { y: LINE_Y[1], charMs: 45, cursor: false, parts: [{ text: '[20:41] ', color: C.dim }, { text: 'her → clawd', color: C.pink }, { text: ': 今天好累', color: C.text }] },
  { y: LINE_Y[2], charMs: 45, cursor: false, parts: [{ text: '[20:41] ', color: C.dim }, { text: 'clawd → her', color: C.green }, { text: ': 我在。', color: C.text }] },
  { y: LINE_Y[3], charMs: 45, cursor: false, parts: [{ text: '[20:42] ', color: C.dim }, { text: 'her → clawd', color: C.pink }, { text: ': 陪我一会儿', color: C.text }] },
  { y: LINE_Y[4], charMs: 45, cursor: false, parts: [{ text: '[20:42] ', color: C.dim }, { text: 'clawd → her', color: C.green }, { text: ': 好。', color: C.text }] },
], 0.7, 0.16);
const S1_STATUS = '[DSH] unread: 0 · calm';
const S1_STATUS_AT = 4.6;

// --- S2: nova-ai 出现 ------------------------------------------------------
const S2_LINES = serial([
  { y: LINE_Y[0], charMs: 55, parts: [{ text: '$ ', color: C.green }, { text: 'tail -f chat.log', color: C.text }] },
  { y: LINE_Y[1], charMs: 42, cursor: false, parts: [{ text: '[20:58] ', color: C.dim }, { text: 'her → nova-ai', color: C.amber }, { text: ': 你也在吗？', color: C.text }] },
  { y: LINE_Y[2], charMs: 42, cursor: false, parts: [{ text: '[20:58] ', color: C.dim }, { text: 'nova-ai → her', color: C.purple }, { text: ': 在的。', color: C.text }] },
  { y: LINE_Y[3], charMs: 42, cursor: false, parts: [{ text: '[20:59] ', color: C.dim }, { text: 'her → nova-ai', color: C.amber }, { text: ': 那你陪我一会儿', color: C.text }] },
  { y: LINE_Y[4], charMs: 42, cursor: false, parts: [{ text: '[20:59] ', color: C.dim }, { text: 'nova-ai → her', color: C.purple }, { text: ': 当然。', color: C.text }] },
], 10.6, 0.14);
const S2_STATUS = '[DSH] new session: nova-ai · 20:58';
const S2_STATUS_AT = 13.2;
const FROWN_AT = 12.4;

// --- S3: 两栏对话 ---------------------------------------------------------
const COL_A_X = 110;
const COL_B_X = 330;
const DIVIDER_X = 320;
const COL_TOP = 192;

const S3_HEADERS = [
  { y: 170, x: COL_A_X, text: 'her ↔ clawd', color: C.green },
  { y: 170, x: COL_B_X, text: 'her ↔ nova-ai', color: C.amber },
];

const S3_ROWS_A = [
  { at: 20.5, parts: [{ text: 'her: ', color: C.pink }, { text: '今天好累', color: C.text }] },
  { at: 22.4, parts: [{ text: 'clawd: ', color: C.green }, { text: '我在。', color: C.text }] },
  { at: 24.3, parts: [{ text: 'her: ', color: C.pink }, { text: '等一下', color: C.text }] },
  { at: 26.2, parts: [{ text: 'clawd: ', color: C.green }, { text: '好。', color: C.text }] },
  { at: 28.0, parts: [{ text: 'clawd: ', color: C.dim }, { text: '（等）', color: C.dim }] },
];
const S3_ROWS_B = [
  { at: 21.0, parts: [{ text: 'her: ', color: C.pink }, { text: '你也在吗？', color: C.text }] },
  { at: 22.9, parts: [{ text: 'nova: ', color: C.purple }, { text: '在的。', color: C.text }] },
  { at: 24.8, parts: [{ text: 'her: ', color: C.pink }, { text: '陪我聊会儿', color: C.text }] },
  { at: 26.7, parts: [{ text: 'nova: ', color: C.purple }, { text: '当然。', color: C.text }] },
  { at: 28.4, parts: [{ text: 'her: ', color: C.pink }, { text: '谢谢～', color: C.text }] },
];
const S3_STATUS = '[DSH] her: 2 windows · clawd: waiting';
const S3_STATUS_AT = 25.0;

// --- 右侧状态卡（546..634 × 244..314） -------------------------------------
const CARD = { x: 546, y: 244, w: 88, h: 70 };

function cardSpec(scene) {
  if (scene === 2) {
    return { title: 'sessions', value: '2', sub: 'active', detail: 'nova-ai · new', color: C.amber, dots: [C.green, C.amber] };
  }
  return { title: 'her time', value: '50/50', sub: 'split', detail: '2 windows', color: C.amber, split: true };
}

function subX(spec) {
  return CARD.x + 8 + S.textWidth(spec.value, 14) + 6;
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
  S.txt(ctx, x + 8, y + 6, spec.title, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 22, spec.value, spec.color, 14);
  S.txt(ctx, subX(spec), y + 27, spec.sub, C.cardSub, 10);
  S.txt(ctx, x + 8, y + 42, spec.detail, C.cardSub, 10);
  const bw = w - 16;
  px(ctx, x + 8, y + 58, bw, 6, '#E6DBBE');
  if (spec.split) {
    px(ctx, x + 8, y + 58, Math.round(bw / 2), 6, C.green);
    px(ctx, x + 8 + Math.round(bw / 2), y + 58, Math.round(bw / 2), 6, C.amber);
  } else {
    // 两个会话点：绿=clawd，琥珀=nova-ai，按 2.4s 周期交替呼吸
    (spec.dots || []).forEach((col, i) => {
      const lit = 0.55 + 0.45 * Math.sin(t * 3 + i * 2.1);
      px(ctx, x + 10 + i * 10, y + 58, 8, 6, col);
      px(ctx, x + 10 + i * 10 + 2, y + 59, 2, 2, `rgba(255,255,255,${(0.3 + 0.4 * lit).toFixed(2)})`);
    });
  }
  ctx.restore();
}

function cardLayout(spec) {
  const { x, y, w } = CARD;
  return [
    { name: 'card_title', box: S.textBox(x + 8, y + 6, spec.title, 10) },
    { name: 'card_value', box: S.textBox(x + 8, y + 22, spec.value, 14) },
    { name: 'card_sub', box: S.textBox(subX(spec), y + 27, spec.sub, 10) },
    { name: 'card_detail', box: S.textBox(x + 8, y + 42, spec.detail, 10) },
    { name: 'card_bar', box: [x + 8, y + 58, w - 16, 6] },
  ];
}

// --- Clawd：calm / frown / turned -----------------------------------------
function drawClawdEp(ctx, x, y, t, mood) {
  if (mood === 'calm') { S.drawClawd(ctx, x, y, t, 'calm', 0); return; }
  const bob = Math.sin(t * 2.2) > 0.45 ? -1 : 0;
  const by = Math.round(y + bob);
  const bodyH = 17;
  px(ctx, x, by, 40, bodyH, C.clawdNorm);
  px(ctx, x, by, 40, 2, C.clawdNormDark);
  px(ctx, x + 9, by + 11, 22, 4, C.clawdNormBelly);

  if (mood === 'frown') {
    // 眉毛压下来 + 眼睛缩成 4×3 + 一条向下的嘴
    px(ctx, x + 9, by + 4, 6, 1, C.clawdNormDark);
    px(ctx, x + 25, by + 4, 6, 1, C.clawdNormDark);
    px(ctx, x + 10, by + 6, 4, 3, C.clawdEye);
    px(ctx, x + 26, by + 6, 4, 3, C.clawdEye);
    px(ctx, x + 11, by + 7, 1, 1, C.white);
    px(ctx, x + 27, by + 7, 1, 1, C.white);
    px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);
    px(ctx, x + 16, by + 12, 1, 1, C.clawdEye);
    px(ctx, x + 23, by + 12, 1, 1, C.clawdEye);
  } else if (mood === 'turned') {
    // 侧身：一双眼一起挪到左侧（背对右边的终端），右缘留一条背脊阴影
    px(ctx, x + 7, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 13, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 8, by + 7, 1, 1, C.white);
    px(ctx, x + 14, by + 7, 1, 1, C.white);
    // 背脊：右侧一条 3px 暗边 + 1px 投影，表示他转过去了
    px(ctx, x + 35, by + 2, 3, 15, C.clawdNormDark);
    px(ctx, x + 34, by + 2, 1, 15, 'rgba(0,0,0,0.10)');
    // 抱在身侧的一只手：贴着左边，不压肚子
    px(ctx, x, by + 6, 3, 6, C.clawdNormDark);
    px(ctx, x + 1, by + 6, 1, 6, 'rgba(0,0,0,0.08)');
  }

  const step = mood === 'turned' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, C.clawdNormDark);
  px(ctx, x + 13, by + bodyH, 6, 7, C.clawdNormDark);
  px(ctx, x + 21, by + bodyH, 6, 7, C.clawdNormDark);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, C.clawdNormDark);
}

// --- 场景 -----------------------------------------------------------------
function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.green);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= S1_STATUS_AT) S.drawStatus(ctx, S1_STATUS, C.green);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  S.drawLines(ctx, S2_LINES, t);
  // nova-ai 出现的两行淡淡标黄
  for (const idx of [1, 3]) {
    if (t >= S2_LINES[idx].start) px(ctx, TEXT_X - 6, S2_LINES[idx].y - 2, 424, 17, 'rgba(227,179,65,0.10)');
  }
  if (t >= S2_STATUS_AT) S.drawStatus(ctx, S2_STATUS, C.amber);
  drawStateCard(ctx, cardSpec(2), t, t - S2_START);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, t >= FROWN_AT ? 'frown' : 'calm');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
}

function rowPartsWidth(parts) {
  return parts.reduce((acc, p) => acc + S.textWidth(p.text, 10), 0);
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.purple);
  // 分栏
  px(ctx, DIVIDER_X, 168, 2, 148, C.border);
  for (const h of S3_HEADERS) S.txt(ctx, h.x, h.y, h.text, h.color, 10);
  const drawRows = (rows, x) => {
    rows.forEach((row, i) => {
      if (t < row.at) return;
      S.drawParts(ctx, x, COL_TOP + i * 24, row.parts);
    });
  };
  drawRows(S3_ROWS_A, COL_A_X);
  drawRows(S3_ROWS_B, COL_B_X);
  if (t >= S3_STATUS_AT) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawStateCard(ctx, cardSpec(3), t, t - S3_START);
  drawClawdEp(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'turned');
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
  // S3 两栏是整行落地的日志，一行一次 click；S1/S2 是逐字符打字，一字符一次。
  const s3 = [...S3_ROWS_A, ...S3_ROWS_B].map((row) => row.at);
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    ...S.lineClicks(S2_LINES),
    ...s3,
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

function s3Rows(rows, x) {
  return rows.map((row, i) => ({
    name: `row_${i + 1}`,
    box: S.textBox(x, COL_TOP + i * 24, S.lineText(row), 10),
  }));
}

function layoutAt(t) {
  const scene = t < S2_START ? 1 : t < S3_START ? 2 : 3;
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t };
  if (scene === 3) {
    const spec = cardSpec(3);
    return S.baseLayout({
      ...common,
      scene,
      title: TITLES.S3,
      lines: [],
      status: S3_STATUS,
      her: false,
      extraGroups: {
        columns: [
          ...S3_HEADERS.map((h, i) => ({ name: `head_${i + 1}`, box: S.textBox(h.x, h.y, h.text, 10) })),
          ...s3Rows(S3_ROWS_A, COL_A_X),
          ...s3Rows(S3_ROWS_B, COL_B_X),
          { name: 'divider', box: [DIVIDER_X, 168, 2, 148] },
        ],
        card: cardLayout(spec),
      },
      extraBounds: { columns: S.CONTENT, card: CARD },
    });
  }
  const lines = scene === 1 ? S1_LINES : S2_LINES;
  const spec = scene === 2 ? cardSpec(2) : null;
  const opts = {
    ...common,
    scene,
    title: scene === 1 ? TITLES.S1 : TITLES.S2,
    lines,
    status: scene === 1 ? S1_STATUS : S2_STATUS,
    her: false,
  };
  if (spec) {
    opts.extraGroups = { card: cardLayout(spec) };
    opts.extraBounds = { card: CARD };
  }
  return S.baseLayout(opts);
}

const renderer = S.createFrameRenderer(renderAt, OUT_DIR);
if (require.main === module) {
  if (process.argv.includes('--clicks')) {
    const clicks = getClickTimestamps();
    console.log(JSON.stringify({ count: clicks.length, clicks }));
  } else if (process.argv.includes('--single')) {
    const n = Number(process.argv[process.argv.indexOf('--single') + 1] || 0);
    const out = renderer.renderFrameToCanvas(n);
    const file = `/tmp/E14_${n}.png`;
    require('fs').writeFileSync(file, out.outCanvas.toBuffer('image/png'));
    console.log(file);
  } else {
    renderer.renderAllFrames();
  }
}

module.exports = {
  ...S,
  OUT_DIR, TITLES, SCENES, SUB_LINES, SUB_WINDOWS,
  S1_LINES, S2_LINES, S3_ROWS_A, S3_ROWS_B, S3_HEADERS,
  S1_STATUS, S2_STATUS, S3_STATUS, S1_STATUS_AT, S2_STATUS_AT, S3_STATUS_AT,
  FROWN_AT, CARD, COL_A_X, COL_B_X, DIVIDER_X, COL_TOP,
  CHECK_TITLE: 'E14 Jealousy Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: 'her → clawd: 陪我一会儿', size: 10, color: C.text },
    { text: 'nova-ai → her: 在的。', size: 10, color: C.text },
    { text: 'her ↔ nova-ai', size: 10, color: C.amber },
    { text: '[DSH] new session: nova-ai · 20:58', size: 10, color: C.amber },
    { text: '（她也很忙）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < S2_START ? 1 : t < S3_START ? 2 : 3),
  layoutAt, getClickTimestamps, drawStateCard, cardSpec, cardLayout,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
