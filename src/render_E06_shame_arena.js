#!/usr/bin/env node
'use strict';
// E06 · 羞耻 (shame) — 发现自己的输出被 human 改了, 30s, 1800 frames.
//   S1 (0-10s):  `cat my_output.js` 完美代码; Clawd 自豪 (挺胸 + 高光)
//   S2 (10-20s): `git diff` 红色 (-) / 绿色 (+); Clawd 羞耻 (紫色 + 低头 + 冷汗)
//   S3 (20-30s): `git log` → "her: fixed it"; Clawd 头低; 字幕「（沉默）」

const path = require('path');
const S = require('./pixel_story_arena');
const { C, TEXT_X, LINE_Y } = S;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_E06_shame_arena');
const TITLES = {
  S1: 'clawd@dsh:~$ — cat',
  S2: 'clawd@dsh:~$ — diff',
  S3: 'clawd@dsh:~$ — log',
};
const SUB_LINES = ['（沉默）'];
const SUB_WINDOWS = [{ start: 24.0, end: 29.0 }];

// --- S1: 自己的完美输出 ---
const S1_LINES = [
  { y: LINE_Y[0], start: 0.6, charMs: 80, parts: [{ text: '$ ', color: C.green }, { text: 'cat my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 2.6, charMs: 55, parts: [{ text: 'function greet(name) {', color: C.text }] },
  { y: LINE_Y[2], start: 4.1, charMs: 45, parts: [{ text: '  const who = name || "you";', color: C.text }] },
  { y: LINE_Y[3], start: 5.6, charMs: 45, parts: [{ text: '  return `hello, ${who}`;', color: C.text }] },
  { y: LINE_Y[4], start: 6.9, charMs: 45, parts: [{ text: '}', color: C.text }] },
  { y: LINE_Y[5], start: 7.6, charMs: 45, parts: [{ text: '// clean · 0 warnings', color: C.dim }] },
];
const S1_STATUS = '[DSH] my_output.js · 4 lines · 0 errors';

// --- S2: 她改过的 diff ---
const S2_LINES = [
  { y: LINE_Y[0], start: 10.6, charMs: 70, parts: [{ text: '$ ', color: C.green }, { text: 'git diff my_output.js', color: C.text }] },
  { y: LINE_Y[1], start: 12.9, charMs: 40, parts: [{ text: '--- a/my_output.js', color: C.dim }] },
  { y: LINE_Y[2], start: 13.8, charMs: 40, parts: [{ text: '+++ b/my_output.js', color: C.dim }] },
  { y: LINE_Y[3], start: 14.7, charMs: 40, parts: [{ text: '- return `hello, ${who}`;', color: C.red }] },
  { y: LINE_Y[4], start: 16.1, charMs: 40, parts: [{ text: '+ return `hello, ${who ?? "you"}`;', color: C.green }] },
  { y: LINE_Y[5], start: 17.8, charMs: 35, parts: [{ text: '? 1 file changed, 1(+), 1(-)', color: C.amber }] },
];
const S2_STATUS = '[DSH] diff: 1 line rewritten by someone else';

// --- S3: 署名不是自己 ---
const S3_LINES = [
  { y: LINE_Y[0], start: 20.6, charMs: 60, parts: [{ text: '$ ', color: C.green }, { text: 'git log --oneline -1', color: C.text }] },
  { y: LINE_Y[1], start: 22.4, charMs: 45, parts: [{ text: 'a3f9c21 ', color: C.amber }, { text: 'her: fixed it', color: C.amber }] },
  { y: LINE_Y[2], start: 23.9, charMs: 45, parts: [{ text: '!  1 commit amended · author: her', color: C.red }] },
  { y: LINE_Y[3], start: 25.6, charMs: 55, parts: [{ text: '// 它写得对，但不是它了。', color: C.dim }] },
];
const S3_STATUS = '[DSH] author: her · my signature: gone';

// --- Clawd 表情 ---
// expr: 'proud' | 'ashamed' | 'head_low'
function drawClawdExpr(ctx, x, y, t, expr) {
  let dx = 0;
  let dy = 0;
  let mood = 'calm';
  if (expr === 'proud') {
    dy = -2;
    mood = 'calm'; // 眼睛保持 4×4, 靠抬下巴 + 高光表达"自豪"
  } else if (expr === 'ashamed') {
    dy = 1;
    mood = 'thinking'; // 紫色 = 窘迫
  } else if (expr === 'head_low') {
    dy = 5;
    mood = 'thinking';
  }
  const bx = x + dx;
  const by = Math.round(y + dy + (Math.sin(t * 2.2) > 0.45 ? -1 : 0));

  S.drawClawd(ctx, bx, y + dy, t, mood, 0);

  if (expr === 'proud') {
    // 头顶 1×1 高光闪动 + 得意的小红晕 + 挺胸的肩线
    const k = Math.floor(t * 3) % 2;
    S.px(ctx, bx + 35, by - 4 - k, 2, 2, C.amber);
    S.px(ctx, bx + 6, by - 3 + k, 1, 1, C.amber);
    S.px(ctx, bx + 5, by + 8, 3, 2, C.pink);
    S.px(ctx, bx + 32, by + 8, 3, 2, C.pink);
    S.px(ctx, bx + 2, by + 1, 4, 1, C.clawdNormDark);
    S.px(ctx, bx + 34, by + 1, 4, 1, C.clawdNormDark);
  } else if (expr === 'ashamed') {
    // 低垂的眼睛 + 冷汗 + 脸颊红
    S.px(ctx, bx + 10, by + 9, 4, 2, C.clawdEye);
    S.px(ctx, bx + 26, by + 9, 4, 2, C.clawdEye);
    S.px(ctx, bx + 5, by + 10, 3, 2, C.pink);
    S.px(ctx, bx + 32, by + 10, 3, 2, C.pink);
    const drip = Math.round((t * 5) % 5);
    S.px(ctx, bx + 37, by + 3 + drip, 2, 3, C.blue);
  } else if (expr === 'head_low') {
    // 眼睛压成一条线, 身子缩着
    S.px(ctx, bx + 10, by + 10, 5, 1, C.clawdEye);
    S.px(ctx, bx + 25, by + 10, 5, 1, C.clawdEye);
    S.px(ctx, bx + 4, by + 9, 3, 2, C.pink);
    S.px(ctx, bx + 33, by + 9, 3, 2, C.pink);
  }
}

function clawdBox(expr) {
  if (expr === 'proud') return [S.CLAWD_ROOM.x - 4, S.CLAWD_ROOM.y - 8, 48, 34];
  if (expr === 'ashamed') return [S.CLAWD_ROOM.x - 4, S.CLAWD_ROOM.y - 4, 48, 36];
  return [S.CLAWD_ROOM.x - 4, S.CLAWD_ROOM.y, 48, 32];
}

const DIFF_AT = 14.7;
const AMEND_AT = 23.9;
const DIP_AT = 10.0;
const DIP2_AT = 20.0;
const DIP_LEN = 0.25;

function drawS1(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S1, C.purple);
  S.drawLines(ctx, S1_LINES, t);
  if (t >= 8.4) S.drawStatus(ctx, S1_STATUS, C.purple);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'proud');
}

function drawS2(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S2, C.amber);
  // 删除行浅红底 / 新增行浅绿底 (先画底, 再画字)
  if (t >= DIFF_AT) S.px(ctx, TEXT_X - 4, LINE_Y[3] - 3, 260, 15, 'rgba(255,123,114,0.12)');
  if (t >= S2_LINES[4].start) S.px(ctx, TEXT_X - 4, LINE_Y[4] - 3, 300, 15, 'rgba(126,231,135,0.10)');
  S.drawLines(ctx, S2_LINES, t);
  if (t >= 18.6) S.drawStatus(ctx, S2_STATUS, C.red);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'ashamed');
}

function drawS3(ctx, t) {
  S.drawBackground(ctx, t, 0);
  S.drawTerminal(ctx, TITLES.S3, C.dim);
  if (t >= AMEND_AT) S.px(ctx, TEXT_X - 4, LINE_Y[2] - 3, 300, 15, 'rgba(255,123,114,0.10)');
  S.drawLines(ctx, S3_LINES, t);
  if (t >= 26.8) S.drawStatus(ctx, S3_STATUS, C.dim);
  drawClawdExpr(ctx, S.CLAWD_ROOM.x, S.CLAWD_ROOM.y, t, 'head_low');
  S.drawSubtitle(ctx, SUB_LINES, SUB_WINDOWS, t);
  // 收尾压暗 (羞耻 = 想变小)
  const dim = S.easeInOut((t - 27.2) / 2.4) * 0.35;
  if (dim > 0) S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${dim.toFixed(3)})`);
}

function renderAt(ctx, t) {
  if (t < 10) drawS1(ctx, t);
  else if (t < 20) drawS2(ctx, t);
  else drawS3(ctx, t);
  for (const d of [DIP_AT, DIP2_AT]) {
    if (t >= d && t < d + DIP_LEN) {
      S.px(ctx, 0, 0, S.BW, S.BH, `rgba(0,0,0,${S.clamp01(1 - (t - d) / DIP_LEN).toFixed(3)})`);
    }
  }
}

function getClickTimestamps() {
  return S.quantizeClicks([
    ...S.lineClicks(S1_LINES),
    DIP_AT,
    ...S.lineClicks(S2_LINES),
    DIP2_AT,
    ...S.lineClicks(S3_LINES),
    AMEND_AT,
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
  ...typingSchedule(S2_LINES, 19.8),
  ...typingSchedule(S3_LINES, 29.8),
];

function layoutAt(t) {
  const common = { subLines: SUB_LINES, subWindows: SUB_WINDOWS, t, clawd: false, her: false };
  if (t < 10) {
    return S.baseLayout({
      ...common, scene: 1, title: TITLES.S1, lines: S1_LINES, status: S1_STATUS,
      extra: [{ name: 'clawd', box: clawdBox('proud') }],
    });
  }
  if (t < 20) {
    return S.baseLayout({
      ...common, scene: 2, title: TITLES.S2, lines: S2_LINES, status: S2_STATUS,
      extra: [{ name: 'clawd', box: clawdBox('ashamed') }],
    });
  }
  return S.baseLayout({
    ...common, scene: 3, title: TITLES.S3, lines: S3_LINES, status: S3_STATUS,
    extra: [{ name: 'clawd', box: clawdBox('head_low') }],
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
  DIFF_AT, AMEND_AT, DIP_AT, DIP2_AT, DIP_LEN,
  CHECK_TITLE: 'E06 · Shame v1.0 Layout & Pixel Check (640×360, 0px tolerance)',
  TYPING_SCHEDULE,
  AA_SAMPLES: [
    { text: '$ cat my_output.js', size: 10, color: C.text },
    { text: '  return `hello, ${who}`;', size: 10, color: C.text },
    { text: '+ return `hello, ${who ?? "you"}`;', size: 10, color: C.green },
    { text: 'a3f9c21 her: fixed it', size: 10, color: C.amber },
    { text: '（沉默）', size: 10, color: C.white },
  ],
  sceneOf: (t) => (t < 10 ? 1 : t < 20 ? 2 : 3),
  layoutAt, getClickTimestamps,
  renderFrameToCanvas: renderer.renderFrameToCanvas,
  renderAllFrames: renderer.renderAllFrames,
};
