#!/usr/bin/env node
<<<<<<< HEAD
// 「Clawd 的学习」30s 像素风视频渲染脚本 (learning_arena v1.0)
// 画布规格: 640×360 基础分辨率, SCALE=2 → 1280×720 @ 60fps, 1800 帧 (30.00s)
// 美术风格: 严格对标 full_v1.3.4.mp4 (暖色条纹房间 + 晨窗远山 + 小终端 DSH TUI + 房间内像素角色)
// 故事线:
//   L1 (0-10s):  她的请求 — 终端逐字打字 `$ her: 帮我写一封辞职信` (140ms/char) + 终端上方消息气泡 + Clawd 平静→思考
//   L2 (10-20s): 思考中   — 终端逐行显示 checkHeart() 代码 + Clawd 正常色→深紫色思考态 + 内心独白「它第一次说了不。」
//   L3 (20-30s): 成长     — 终端回复 `$ clawd: 不，我不想。` / `$ her: (笑了)` / `$ her: 这就是成长。`
//                           + 窗台便签「它有了自己的意志。」 + Clawd 恢复正常色微笑 + Her 在窗边微笑
=======
// 「Clawd 的学习」30s 像素风视频渲染脚本 (arena v1.0)
// 画布规格: 640×360 基础分辨率, SCALE=2 → 1280×720 @ 60fps, 1800 帧 (30s)
// 美术风格: 严格对标 full_v1.3.4.mp4
//   暖色条纹房间 (#F5EDD5 + 竖条纹) + 晨窗远山云朵 + 大号小终端 (#0d1117) + 房间内像素角色
//
// 故事: Clawd 第一次学会说"不"。她让它做一件它不想做的事，它拒绝了。
//
// 场景:
//   L1 (0-10s)  她的请求: 终端逐字打出 `$ her: 帮我写一封辞职信` (140ms/字)
//               终端上方浮出消息气泡；Clawd 在房间内，表情 平静 → 思考
//   L2 (10-20s) 思考中: 终端逐行显示 if / const feelings / return "no" 代码
//               Clawd 颜色 正常 → 深紫 (思考)；内心独白字幕
//   L3 (20-30s) 成长: 终端显示 `$ clawd: 不，我不想。` / `$ her: (笑了)` / `$ her: 这就是成长。`
//               窗台便签 "它有了自己的意志。"；Clawd 恢复原色微笑；她在窗边微笑
//
// 字幕 (3 条, 逐字 160ms):
//   1. "它第一次说了不。" (2-8s)
//   2. "它有了自己的意志。" (12-18s)
//   3. "这就是成长。" (24-29s)
>>>>>>> origin/pr/5

const { createCanvas, GlobalFonts } = require('@napi-rs/canvas');
const fs = require('fs');
const path = require('path');

<<<<<<< HEAD
// --- Register Fusion Pixel Fonts (10px Terminal Small Font + 12px/14px Subtitle Font) ---
let FONT_10 = 'monospace';
let FONT_14 = 'monospace';

if (process.env.FONT_FORCE !== 'monospace') {
  try {
    const fp10 = require.resolve(
      '@fontsource/fusion-pixel-10px-monospaced-sc/files/fusion-pixel-10px-monospaced-sc-latin-400-normal.woff'
    );
    if (fs.existsSync(fp10)) {
      GlobalFonts.registerFromPath(fp10, 'FusionPixel10');
      FONT_10 = 'FusionPixel10, monospace';
    }
  } catch (_) {}

  try {
    const fp12 = require.resolve('@fontpkg/fusion-pixel/fusion-pixel.ttf');
    if (fs.existsSync(fp12)) {
      GlobalFonts.registerFromPath(fp12, 'FusionPixel');
      FONT_14 = 'FusionPixel, monospace';
      if (FONT_10 === 'monospace') FONT_10 = 'FusionPixel, monospace';
    }
  } catch (_) {}

  if (FONT_10 === 'monospace' || FONT_14 === 'monospace') {
    const fallbackCandidates = [
      '/usr/local/share/fonts/NotoSansMonoCJKsc-Regular.otf',
      '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
    ];
    for (const cand of fallbackCandidates) {
      if (fs.existsSync(cand)) {
        GlobalFonts.registerFromPath(cand, 'NotoMonoCJK');
        if (FONT_10 === 'monospace') FONT_10 = 'NotoMonoCJK, monospace';
        if (FONT_14 === 'monospace') FONT_14 = 'NotoMonoCJK, monospace';
        break;
      }
    }
  }
}

function fontFamilyForSize(size) {
  return size <= 11 ? FONT_10 : FONT_14;
=======
// --- Register pixel CJK font (Fusion Pixel 12px) with clean fallback ---
let FONT_FAMILY = 'monospace';
try {
  const fusionPath = require.resolve('@fontpkg/fusion-pixel/fusion-pixel.ttf');
  if (fs.existsSync(fusionPath)) {
    GlobalFonts.registerFromPath(fusionPath, 'FusionPixel');
    FONT_FAMILY = 'FusionPixel, monospace';
  }
} catch (_) {
  const fallbackFont = '/usr/local/share/fonts/NotoSansMonoCJKsc-Regular.otf';
  if (fs.existsSync(fallbackFont)) {
    GlobalFonts.registerFromPath(fallbackFont, 'NotoMonoCJK');
    FONT_FAMILY = 'NotoMonoCJK, monospace';
  }
>>>>>>> origin/pr/5
}

// --- Canvas & Video Constants ---
const BW = 640;
const BH = 360;
const SCALE = 2;
const FW = BW * SCALE; // 1280
const FH = BH * SCALE; // 720
const FPS = 60;
const DURATION = 30;
const NFRAMES = DURATION * FPS; // 1800

<<<<<<< HEAD
// Typing & Subtitle Rhythms (strictly matching spec)
const TYPE_CHAR_MS = 140; // L1 terminal typing: 140ms/char
const SUB_CHAR_MS = 160;  // Subtitle step: 160ms/char
const FADE = 0.25;        // 0.25s out + 0.25s in = 0.5s black transition between scenes

const OUT_DIR = process.env.FRAMES_DIR || '/tmp/frames_learning';

// --- Layout Constants (640×360 base grid, strictly benchmarked to full_v1.3.4) ---
const WIN = { x: 60, y: 20, w: 520, h: 160, fw: 8 };
const SILL = { x: 56, y: 180, w: 528, h: 8 };
const TERM = { x: 140, y: 160, w: 360, h: 160, titleH: 20 };
const SUB = { x: 0, y: 320, w: 640, h: 40 };

// Floating UI overlays in room space (zero overlap with TERM [140,160,360,160] & characters)
const BUBBLE_L1 = { x: 220, y: 116, w: 200, h: 28, tailH: 6 }; // y=116..150 < 160
const MONO_L2 = { x: 210, y: 116, w: 220, h: 28 };             // y=116..144 < 160
const NOTE = { x: 506, y: 112, w: 108, h: 68, angleDeg: -3 };  // rests right on windowsill y=180, x>500

// Character room positions (strictly inside room, outside terminal, above subtitle bar y=320)
const CLAWD_ROOM = { x: 64, y: 248 };     // 40×24 body+legs -> x=64..104, y=246..272
const CLAWD_THOUGHT = { x: 66, y: 214, w: 36, h: 20 }; // thought dots above Clawd -> y=214..234 < 246
const HER_ROOM = { x: 548, y: 194 };      // 16×28 beside window -> x=548..564, y=193..222

// Warm sparkles for L3 growth moment (anchored in open room/window areas, zero overlap)
const SPARKLE_ANCHORS = [
  { x: 28, y: 108 },
  { x: 196, y: 54 },
  { x: 388, y: 50 },
  { x: 598, y: 268 },
];

// --- Palette (aligned with full_v1.3.4 + DSH TUI dark theme) ---
const C = {
  // Warm room & morning window (full_v1.3.4)
=======
const CHAR_MS = 140; // 终端打字 140ms/字
const SUB_CHAR_MS = 160; // 字幕逐字 160ms

// 字体规格: Fusion Pixel — 终端小字 10px / 字幕 14px
const F_TERM = 10;
const F_TITLE = 12;
const F_SUB = 14;
const F_NOTE = 10;

const OUT_DIR = process.env.FRAMES_DIR || path.join(__dirname, 'frames_learning_arena');

// --- Layout Constants (640×360 base resolution) ---
const WIN = { x: 60, y: 20, w: 520, h: 160, fw: 8 }; // 晨窗
const SILL = { y: 180, h: 8 }; // 窗台
const TERM = { x: 130, y: 148, w: 380, h: 164, titleH: 20 }; // 小终端 (内容区 380×144)
const NOTE = { x: 512, y: 106, w: 118, h: 70 }; // 窗台便签 (L3, 坐在窗台上 y=176→sill 180)
const SUB = { x: 0, y: 316, w: 640, h: 44 }; // 字幕栏 (对标 full_v1.3.4 奶油色条)
const STATUS = { h: 12 }; // 终端底部状态栏高度
const BUBBLE = { y: 84, h: 26 }; // 智能终端上方的消息气泡 (L1)

// 终端内容区文字行坐标 (相对内容区左上角; 单一来源, 渲染与检测共用)
const TLAYOUT = {
  padX: 16,
  l1: { cmdY: 20, awaitY: 50, quietY: 80, thinkY: 104 },
  l2: { headY: 8, rowY: 26, rowH: 15, conclusionY: 114 },
  l3: { rowY: 20, rowH: 26, statusY: 108 },
};

// 角色位置 (房间内, 终端左右两侧, 0 overlap)
const HER_L1 = { x: 56, y: 280 };
const HER_L3 = { x: 34, y: 280 };
const CLAWD_L1 = { x: 552, y: 286 };
const CLAWD_L2 = { x: 552, y: 286 };
const CLAWD_L3 = { x: 552, y: 286 };

// --- Palette (严格对齐 full_v1.3.4) ---
const C = {
  // Room & Window
>>>>>>> origin/pr/5
  bgWarm: '#F5EDD5',
  stripe: '#EDE3C8',
  woodFrame: '#8B7355',
  woodSill: '#A08060',
  skyTop: '#87CEEB',
  skyBottom: '#E0F0FF',
  mountain: '#5A7A5A',
<<<<<<< HEAD
  mountainHi: '#6A8B68',
  pot: '#7A5A3A',

  // DSH TUI Terminal
  termBg: '#14161C',
  termTitle: '#21262D',
  termBd: '#30363D',
  panel: '#1A1F29',
  border: '#30363D',
  codeHighlight: '#241B3B',

  // Syntax & UI accents
=======
  mountainFar: '#6E8E6E',

  // Terminal (#0d1117 body per spec)
  termBg: '#0d1117',
  termTitle: '#1E222B',
  termBd: '#2A2E38',
  border: '#30363D',

  // Text & accents
>>>>>>> origin/pr/5
  text: '#E6EDF3',
  dim: '#8B949E',
  green: '#7EE787',
  pink: '#FF9AA2',
  amber: '#E3B341',
<<<<<<< HEAD
  blue: '#79C0FF',
  purple: '#BC8CFF',
  purple2: '#A371F7',
  red: '#FF7B72',
  pinRed: '#FF5555',
  white: '#FFFFFF',

  // Clawd colors: Normal (warm coral from full_v1.3.4) -> Deep Purple (thinking state in L2)
  clawdNorm: '#D97757',
  clawdNormDark: '#B85A3B',
  clawdNormBelly: '#F5E8D7',
  clawdDeepPurple: '#5B32A8',
  clawdDeepPurpleDark: '#3E1F78',
  clawdDeepPurpleBelly: '#DDD0FA',
  clawdEye: '#141413',

  // Her (16×28 by window)
=======
  purple: '#BC8CFF',
  deepPurple: '#7B4FD6',
  red: '#FF7B72',
  white: '#FFFFFF',

  // Clawd
  clawdBody: '#D97757', // 对标 full_v1.3.4 (锈橙)
  clawdBodyDark: '#B85C3E',
  clawdThink: '#4B2E83', // 思考状态 (深紫)
  clawdEye: '#1A1208',
  clawdMouth: '#F2E6C8',

  // Her & note
>>>>>>> origin/pr/5
  herHair: '#5A4632',
  herSkin: '#E8C39E',
  herDress: '#FF9AA2',
  herDressHem: '#E57A84',
<<<<<<< HEAD

  // Message bubble / Monologue / Sticky note
  bubbleBg: '#FFF8F9',
  bubbleBd: '#E57A84',
  bubbleTx: '#2E1E24',
  monoBg: '#1D1533',
  monoBd: '#9D78F2',
=======
>>>>>>> origin/pr/5
  cardBg: '#FFF8DC',
  cardBd: '#DEB887',
  cardTx: '#241A06',
  cardSub: '#6E5A3A',
<<<<<<< HEAD

  subtitleBg: 'rgba(0,0,0,0.76)',
  warmOverlay: 'rgba(255,205,110,0.08)',
};

// --- Narrative Text & Timing Definitions (DO NOT MUTATE AT RUNTIME) ---
const LINES = [
  '它第一次说了不。',
  '它有了自己的意志。',
  '这就是成长。',
];
const SUB_WINDOW = [
  { start: 2.0, end: 8.0 },
  { start: 12.0, end: 18.0 },
  { start: 24.0, end: 29.0 },
];

// L1 (0-10s): Her's request
const L1_PROMPT = '$ her: ';
const L1_MSG = '帮我写一封辞职信';
const L1_FULL_LINE = L1_PROMPT + L1_MSG;
const L1_TYPE_START = 0.8; // 15 chars * 0.14s = 2.10s -> finishes at 2.90s
const L1_BUBBLE_APPEAR = 1.6;
const L1_THINK_SHIFT = 3.2; // Clawd transitions from calm -> thinking expression
const L1_STATUS_APPEAR = 3.5;
const L1_WAIT_PROMPT_APPEAR = 4.5;

// L2 (10-20s): Code lines appearing sequentially
const L2_CODE_LINES = [
  { num: '1', text: 'if (task === "quit_job") {', delay: 0.5, highlight: false },
  { num: '2', text: '  const feelings = checkHeart();', delay: 1.4, highlight: false },
  { num: '3', text: '  if (feelings !== "wants_to_stay") {', delay: 2.3, highlight: false },
  { num: '4', text: '    return "no";', delay: 3.2, highlight: true },
  { num: '5', text: '  }', delay: 4.0, highlight: false },
  { num: '6', text: '}', delay: 4.6, highlight: false },
];
const L2_MONO_TEXT = '它第一次说了不。';
const L2_MONO_APPEAR = 3.3; // scene-local seconds (t = 13.3s, right as `return "no";` lands)

// L3 (20-30s): Growth dialogue & sticky note on windowsill
const L3_DIALOGUE = [
  { prefix: '$ clawd: ', body: '不，我不想。', prefixCol: C.green, bodyCol: C.purple, y: 18, delay: 0.6 },
  { prefix: '$ her: ', body: '(笑了)', prefixCol: C.pink, bodyCol: C.amber, y: 48, delay: 2.6 },
  { prefix: '$ her: ', body: '这就是成长。', prefixCol: C.pink, bodyCol: C.text, y: 78, delay: 4.1 },
];
const L3_STATUS_TEXT = '# will: online · growth +1';
const L3_STATUS_DELAY = 5.8;
const NOTE_LINE_1 = '它有了';
const NOTE_LINE_2 = '自己的意志。';
const NOTE_FULL_TEXT = '它有了自己的意志。';
const NOTE_APPEAR = 1.2; // scene-local seconds (t = 21.2s)

// --- Color & Math Helpers ---
function clamp01(v) { return Math.max(0, Math.min(1, v)); }
function easeOut(v) { return 1 - Math.pow(1 - clamp01(v), 3); }
function easeInOut(v) {
  const x = clamp01(v);
  return x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2;
}

function hexToRgb(hex) {
  const n = parseInt(hex.slice(1), 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}

function lerpColor(hexA, hexB, t) {
  const k = clamp01(t);
  const [r1, g1, b1] = hexToRgb(hexA);
  const [r2, g2, b2] = hexToRgb(hexB);
  const r = Math.round(r1 + (r2 - r1) * k);
  const g = Math.round(g1 + (g2 - g1) * k);
  const b = Math.round(b1 + (b2 - b1) * k);
  return `rgb(${r},${g},${b})`;
}

// --- Pixel Drawing & Threshold Crisp Text Primitives ---
=======
  pinRed: '#FF5555',
  subtitleBg: '#CDC6B4',
  subtitleTx: '#241A06',
};

// --- Reusable Pixel Primitives ---
>>>>>>> origin/pr/5
function px(ctx, x, y, w, h, color) {
  ctx.fillStyle = color;
  ctx.fillRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
}

<<<<<<< HEAD
let _tmpCanvas = null;
function txt(ctx, x, y, str, color, font = 10, align = 'left') {
  if (!str) return { x: Math.round(x), y: Math.round(y), w: 0, h: font };
  const fontSpec = `${font}px ${fontFamilyForSize(font)}`;
  ctx.font = fontSpec;

=======
// Threshold pixel text renderer (exact resize avoids ghost pixel artifacts)
let _tmpCanvas = null;
function txt(ctx, x, y, str, color, font = F_TITLE, align = 'left') {
  if (!str) return { x, y, w: 0, h: font };
  const fontSpec = `${font}px ${FONT_FAMILY}`;
  ctx.font = fontSpec;

  // For <12px on a 12px pixel font, add 1px letter tracking & keep clean pixel anti-aliasing
  if (font < 12) {
    const chars = Array.from(str);
    const widths = chars.map((ch) => Math.ceil(ctx.measureText(ch).width));
    const totalW = widths.reduce((a, b) => a + b, 0) + Math.max(0, chars.length - 1);
    let dx = x;
    if (align === 'center') dx = x - totalW / 2;
    else if (align === 'right') dx = x - totalW;
    ctx.save();
    ctx.font = fontSpec;
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillStyle = color;
    let cx = Math.round(dx);
    const cy = Math.round(y);
    for (let i = 0; i < chars.length; i++) {
      ctx.fillText(chars[i], cx, cy);
      cx += widths[i] + 1;
    }
    ctx.restore();
    return { x: Math.round(dx), y: Math.round(y), w: totalW, h: font };
  }

>>>>>>> origin/pr/5
  const measuredW = Math.ceil(ctx.measureText(str).width);
  const w = Math.max(4, measuredW + 4);
  const h = Math.max(4, Math.ceil(font * 1.35));

  if (!_tmpCanvas) _tmpCanvas = createCanvas(w, h);
  if (_tmpCanvas.width !== w || _tmpCanvas.height !== h) {
    _tmpCanvas.width = w;
    _tmpCanvas.height = h;
  }
  const tctx = _tmpCanvas.getContext('2d');
  tctx.clearRect(0, 0, w, h);
  tctx.font = fontSpec;
  tctx.textAlign = 'left';
  tctx.textBaseline = 'top';
  tctx.fillStyle = color;
  tctx.fillText(str, 1, Math.ceil(font * 0.08));

  const img = tctx.getImageData(0, 0, w, h);
  const d = img.data;
  for (let i = 3; i < d.length; i += 4) {
<<<<<<< HEAD
    d[i] = d[i] > 115 ? 255 : 0;
=======
    d[i] = d[i] > 118 ? 255 : 0;
>>>>>>> origin/pr/5
  }
  tctx.putImageData(img, 0, 0);

  let dx = x;
  if (align === 'center') dx = x - measuredW / 2 - 1;
  else if (align === 'right') dx = x - measuredW - 2;

  ctx.drawImage(_tmpCanvas, Math.round(dx), Math.round(y));
  return { x: Math.round(dx), y: Math.round(y), w: measuredW, h: font };
}

<<<<<<< HEAD
function measureTxt(ctx, str, font = 10) {
  if (!str) return 0;
  ctx.font = `${font}px ${fontFamilyForSize(font)}`;
  return Math.ceil(ctx.measureText(str).width);
}

//Syntax-colored code token renderer for L2 (preserves exact pixel advance of L2_CODE_LINES)
function drawCodeTokens(ctx, x, y, rawLine, font = 10) {
  const tokenRe = /("quit_job"|"wants_to_stay"|"no")|\b(if|const|return)\b|\b(checkHeart)\b|(===|!==)|(\s+|[^\s]+)/g;
  let cx = x;
  let match;
  while ((match = tokenRe.exec(rawLine)) !== null) {
    const tok = match[0];
    let col = C.text;
    if (match[1]) col = tok === '"no"' ? C.amber : C.green;
    else if (match[2]) col = C.purple;
    else if (match[3]) col = C.blue;
    else if (match[4]) col = C.pink;
    else if (/^[{}();]$/.test(tok)) col = C.dim;
    if (!/^\s+$/.test(tok)) {
      txt(ctx, cx, y, tok, col, font, 'left');
    }
    cx += measureTxt(ctx, tok, font);
  }
}

// --- Reusable Scene Component: Warm Striped Room + Morning Window (full_v1.3.4) ---
function drawBackground(ctx, t, opts = {}) {
  // 1. Warm striped wallpaper (#F5EDD5 + #EDE3C8 vertical stripes every 16px)
=======
function measureTxt(ctx, str, font = F_TITLE) {
  if (!str) return 0;
  ctx.font = `${font}px ${FONT_FAMILY}`;
  if (font < 12) {
    const chars = Array.from(str);
    return chars.reduce((s, ch) => s + Math.ceil(ctx.measureText(ch).width), 0) + Math.max(0, chars.length - 1);
  }
  return Math.ceil(ctx.measureText(str).width);
}

// 逐字打字: 返回当前应显示的字符数 (按 CHAR_MS 步进)
function typedCount(str, elapsed, charMs = CHAR_MS) {
  if (elapsed < 0) return 0;
  const chars = Array.from(str);
  return Math.min(chars.length, Math.floor((elapsed * 1000) / charMs) + 1);
}

function lerpColor(a, b, k) {
  const pa = hexToRgb(a);
  const pb = hexToRgb(b);
  const kk = Math.max(0, Math.min(1, k));
  const mix = (i) => Math.round(pa[i] + (pb[i] - pa[i]) * kk);
  return `rgb(${mix(0)},${mix(1)},${mix(2)})`;
}

function hexToRgb(h) {
  const s = h.replace('#', '');
  return [parseInt(s.slice(0, 2), 16), parseInt(s.slice(2, 4), 16), parseInt(s.slice(4, 6), 16)];
}

// --- Reusable Scene Component: Warm Room + Morning Window (full_v1.3.4 对标) ---
function drawBackground(ctx, t, opts = {}) {
  // 1. 暖色条纹壁纸 (#F5EDD5 + #EDE3C8 每 16px)
>>>>>>> origin/pr/5
  px(ctx, 0, 0, BW, BH, C.bgWarm);
  for (let x = 0; x < BW; x += 16) {
    px(ctx, x, 0, 8, BH, C.stripe);
  }

<<<<<<< HEAD
  // 2. Large morning window (x=60, y=20, w=520, h=160)
=======
  // 2. 大窗户 (60,20 520×160, 木框 #8B7355 8px)
>>>>>>> origin/pr/5
  const { x: wx, y: wy, w: ww, h: wh, fw } = WIN;
  px(ctx, wx, wy, ww, wh, C.woodFrame);

  const gx = wx + fw;
  const gy = wy + fw;
  const gw = ww - 2 * fw;
  const gh = wh - 2 * fw;

  ctx.save();
  ctx.beginPath();
  ctx.rect(gx, gy, gw, gh);
  ctx.clip();

<<<<<<< HEAD
  // Sky gradient (#87CEEB -> #E0F0FF)
=======
  // 晨空渐变 (#87CEEB → #E0F0FF)
>>>>>>> origin/pr/5
  const grd = ctx.createLinearGradient(0, gy, 0, gy + gh);
  grd.addColorStop(0, C.skyTop);
  grd.addColorStop(1, C.skyBottom);
  ctx.fillStyle = grd;
  ctx.fillRect(gx, gy, gw, gh);

<<<<<<< HEAD
  // Morning sun glow in upper-left sky pane
  const sunX = wx + 84;
  const sunY = wy + 40;
  const sunPulse = Math.sin(t * 1.6) > 0 ? 2 : 0;
  px(ctx, sunX - 16 - sunPulse, sunY - 16 - sunPulse, 32 + sunPulse * 2, 32 + sunPulse * 2, 'rgba(255,228,130,0.22)');
  px(ctx, sunX - 11, sunY - 11, 22, 22, 'rgba(255,224,110,0.45)');
  px(ctx, sunX - 7, sunY - 7, 14, 14, '#FFE478');

  // 2 distant mountains (#5A7A5A)
  ctx.fillStyle = C.mountain;
  ctx.beginPath();
  ctx.moveTo(gx, gy + gh);
  ctx.lineTo(wx + 132, wy + 72);
  ctx.lineTo(wx + 234, gy + gh);
=======
  // 晨光 (柔和的暖阳)
  const sx = wx + 96;
  const sy = wy + 46;
  const pulse = Math.sin(t * 1.6) > 0 ? 2 : 0;
  px(ctx, sx - 20 - pulse, sy - 20 - pulse, 40 + pulse * 2, 40 + pulse * 2, 'rgba(255,228,130,0.18)');
  px(ctx, sx - 12, sy - 12, 24, 24, 'rgba(255,224,110,0.42)');
  px(ctx, sx - 8, sy - 8, 16, 16, '#FFE478');

  // 远山 (#5A7A5A) — 两层层次
  ctx.fillStyle = C.mountainFar;
  ctx.beginPath();
  ctx.moveTo(wx + 150, gy + gh);
  ctx.lineTo(wx + 300, wy + 62);
  ctx.lineTo(wx + 470, gy + gh);
  ctx.closePath();
  ctx.fill();

  ctx.fillStyle = C.mountain;
  ctx.beginPath();
  ctx.moveTo(gx, gy + gh);
  ctx.lineTo(wx + 128, wy + 76);
  ctx.lineTo(wx + 232, gy + gh);
>>>>>>> origin/pr/5
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
<<<<<<< HEAD
  ctx.moveTo(wx + 176, gy + gh);
  ctx.lineTo(wx + 332, wy + 50);
  ctx.lineTo(wx + 474, gy + gh);
  ctx.closePath();
  ctx.fill();

  // Drifting pixel clouds
  const cx1 = wx + 118 + Math.round(Math.sin(t * 0.32) * 12);
  px(ctx, cx1, wy + 38, 38, 9, 'rgba(255,255,255,0.92)');
  px(ctx, cx1 + 8, wy + 32, 22, 6, 'rgba(255,255,255,0.92)');

  const cx2 = wx + 334 + Math.round(Math.cos(t * 0.24) * 14);
  px(ctx, cx2, wy + 52, 46, 9, 'rgba(255,255,255,0.90)');
  px(ctx, cx2 + 10, wy + 46, 26, 6, 'rgba(255,255,255,0.90)');

  ctx.restore();

  // Cross mullions
  px(ctx, wx + ww / 2 - 3, gy, 6, gh, C.woodFrame);
  px(ctx, gx, wy + wh / 2 - 3, gw, 6, C.woodFrame);

  // Windowsill (y=180..188)
  px(ctx, SILL.x, SILL.y, SILL.w, SILL.h, C.woodSill);
  px(ctx, SILL.x, SILL.y, SILL.w, 2, C.woodFrame);

  // Small potted plant on left sill (x=88..102, y=161..180)
  const px0 = wx + 28;
=======
  ctx.moveTo(wx + 262, gy + gh);
  ctx.lineTo(wx + 392, wy + 70);
  ctx.lineTo(wx + 508, gy + gh);
  ctx.closePath();
  ctx.fill();

  // 两朵像素云 (缓慢横移)
  const cx1 = wx + 108 + Math.round(Math.sin(t * 0.32) * 14);
  px(ctx, cx1, wy + 34, 44, 10, 'rgba(255,255,255,0.92)');
  px(ctx, cx1 + 10, wy + 28, 24, 6, 'rgba(255,255,255,0.92)');

  const cx2 = wx + 340 + Math.round(Math.cos(t * 0.24) * 16);
  px(ctx, cx2, wy + 48, 50, 10, 'rgba(255,255,255,0.90)');
  px(ctx, cx2 + 12, wy + 42, 28, 6, 'rgba(255,255,255,0.90)');

  // 极轻的空气粒子 (晨光尘埃, 仅在窗内)
  for (let i = 0; i < 5; i++) {
    const dx = gx + ((i * 97 + t * 7) % gw);
    const dy = gy + 20 + ((i * 53 + t * 11) % (gh - 30));
    px(ctx, dx, dy, 1, 1, 'rgba(255,255,255,0.55)');
  }

  ctx.restore();

  // 十字窗棂
  px(ctx, wx + ww / 2 - 3, gy, 6, gh, C.woodFrame);
  px(ctx, gx, wy + wh / 2 - 3, gw, 6, C.woodFrame);

  // 窗台
  px(ctx, wx - 4, wy + wh, ww + 8, SILL.h, C.woodSill);
  px(ctx, wx - 4, wy + wh, ww + 8, 2, C.woodFrame);

  // 左上窗台小盆栽
  const px0 = wx + 26;
>>>>>>> origin/pr/5
  const py0 = wy + wh;
  px(ctx, px0 + 2, py0 - 16, 10, 8, '#6AA86A');
  px(ctx, px0, py0 - 13, 14, 5, '#4E864E');
  px(ctx, px0 + 4, py0 - 19, 6, 3, '#7BC07B');
<<<<<<< HEAD
  if (opts.bloom) px(ctx, px0 + 6, py0 - 21, 2, 2, C.pink);
  px(ctx, px0, py0 - 8, 14, 2, '#B06A46');
  px(ctx, px0 + 1, py0 - 6, 12, 6, C.pot);
}

// --- Reusable UI Component: DSH TUI Small Terminal (360×160 @ 140,160) ---
function drawTerminal(ctx, title, accentColor = C.green) {
  const { x, y, w, h, titleH } = TERM;
  // Soft drop shadow
  px(ctx, x + 4, y + 4, w, h, 'rgba(0,0,0,0.16)');
  // Dark TUI body
  px(ctx, x, y, w, h, C.termBg);
  // Title bar (20px) + DSH 1px accent line
  px(ctx, x, y, w, titleH, C.termTitle);
  px(ctx, x, y + titleH - 1, w, 1, accentColor);
  // Border
=======
  px(ctx, px0 + 6, py0 - 21, 2, 2, C.pink);
  px(ctx, px0, py0 - 8, 14, 2, '#B06A46');
  px(ctx, px0 + 1, py0 - 6, 12, 6, '#945234');
}

// --- Reusable UI Component: Large Terminal (432×172 @ 104,140, #0d1117) ---
function drawTerminal(ctx, title, titleColor = C.dim) {
  const { x, y, w, h, titleH } = TERM;
  px(ctx, x + 4, y + 4, w, h, 'rgba(0,0,0,0.15)');
  px(ctx, x, y, w, h, C.termBg);
  px(ctx, x, y, w, titleH, C.termTitle);
  px(ctx, x, y + titleH, w, 1, C.termBd);

>>>>>>> origin/pr/5
  ctx.strokeStyle = C.termBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x, y, w, h);

<<<<<<< HEAD
  // Window buttons (6×6)
=======
  // 窗口按钮 6×6
>>>>>>> origin/pr/5
  px(ctx, x + 8, y + 7, 6, 6, C.red);
  px(ctx, x + 18, y + 7, 6, 6, C.amber);
  px(ctx, x + 28, y + 7, 6, 6, C.green);

<<<<<<< HEAD
  // 10px Fusion Pixel title
  txt(ctx, x + w / 2, y + 5, title, C.dim, 10, 'center');

  // Subtle CRT scanlines inside content area
  for (let sy = y + titleH + 2; sy < y + h - 2; sy += 3) {
    px(ctx, x + 2, sy, w - 4, 1, 'rgba(255,255,255,0.025)');
  }
}

// --- Reusable Character: Clawd (40×24 pixel creature in room, normal <-> deep purple) ---
// mood: 'calm' | 'thinking' | 'smile'
// purpleMix: 0 (normal coral #D97757) .. 1 (deep purple #5B32A8 thinking state)
function drawClawd(ctx, x, y, t, mood = 'calm', purpleMix = 0) {
  const bob = Math.sin(t * 2.2) > 0.45 ? -1 : 0;
  const by = Math.round(y + bob);
  const bodyH = 17;

  const bodyCol = lerpColor(C.clawdNorm, C.clawdDeepPurple, purpleMix);
  const darkCol = lerpColor(C.clawdNormDark, C.clawdDeepPurpleDark, purpleMix);
  const bellyCol = lerpColor(C.clawdNormBelly, C.clawdDeepPurpleBelly, purpleMix);

  // Subtle pixel body (40×17) + top shading strip
  px(ctx, x, by, 40, bodyH, bodyCol);
  px(ctx, x, by, 40, 2, darkCol);
  // Belly highlight patch
  px(ctx, x + 9, by + 11, 22, 4, bellyCol);

  // Eyes & facial expression
  const blink = mood !== 'thinking' && (t % 3.4) < 0.14;
  if (mood === 'smile') {
    // Happy curved eyes (^ ^) + gentle pixel smile on belly
    px(ctx, x + 9, by + 6, 2, 1, C.clawdEye);
    px(ctx, x + 11, by + 5, 2, 1, C.clawdEye);
    px(ctx, x + 13, by + 6, 2, 1, C.clawdEye);

    px(ctx, x + 25, by + 6, 2, 1, C.clawdEye);
    px(ctx, x + 27, by + 5, 2, 1, C.clawdEye);
    px(ctx, x + 29, by + 6, 2, 1, C.clawdEye);

    // Pixel smile curve
    px(ctx, x + 16, by + 12, 2, 1, C.clawdEye);
    px(ctx, x + 18, by + 13, 4, 1, C.clawdEye);
    px(ctx, x + 22, by + 12, 2, 1, C.clawdEye);
    // Warm rosy cheeks
    px(ctx, x + 6, by + 8, 3, 2, C.pink);
    px(ctx, x + 31, by + 8, 3, 2, C.pink);
  } else if (mood === 'thinking') {
    // Focused upward-looking pixel eyes + slight furrowed brow
    const glance = Math.sin(t * 1.8) > 0 ? 1 : 0;
    px(ctx, x + 9, by + 4, 5, 1, darkCol);
    px(ctx, x + 26, by + 4, 5, 1, darkCol);
    px(ctx, x + 10, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 26, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 10 + glance, by + 6, 2, 2, C.white);
    px(ctx, x + 26 + glance, by + 6, 2, 2, C.white);
    // Small thoughtful mouth dash
    px(ctx, x + 18, by + 13, 4, 1, C.clawdEye);
  } else if (blink) {
    px(ctx, x + 10, by + 8, 4, 1, C.clawdEye);
    px(ctx, x + 26, by + 8, 4, 1, C.clawdEye);
  } else {
    // Calm default expression
    px(ctx, x + 10, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 26, by + 6, 4, 4, C.clawdEye);
    px(ctx, x + 11, by + 7, 1, 1, C.white);
    px(ctx, x + 27, by + 7, 1, 1, C.white);
  }

  // 4 signature pixel legs (matching full_v1.3.4 silhouette, total height 24px)
  const step = mood === 'thinking' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, x + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, x + 31, by + bodyH, 6, 7 - step, darkCol);
}

// Thought indicator pill above Clawd in room (strictly inside CLAWD_THOUGHT [66,214,36,20])
function drawClawdThought(ctx, t, purpleMix = 0, alpha = 1) {
  if (alpha <= 0.01) return;
  const { x, y, w, h } = CLAWD_THOUGHT;
  ctx.save();
  ctx.globalAlpha = clamp01(alpha);
  const bg = purpleMix > 0.4 ? C.monoBg : '#FFFFFF';
  const bd = purpleMix > 0.4 ? C.purple2 : C.woodFrame;
  const dotCol = purpleMix > 0.4 ? C.purple : C.clawdNorm;
  px(ctx, x, y, w, h - 4, bg);
  ctx.strokeStyle = bd;
  ctx.lineWidth = 1;
  ctx.strokeRect(x + 0.5, y + 0.5, w - 1, h - 5);
  // Small thought tail dot inside box bottom (y + 17..19)
  px(ctx, x + 16, y + h - 3, 4, 3, bd);

  const activeDots = (Math.floor(t * 2.5) % 3) + 1;
  for (let i = 0; i < 3; i++) {
    px(ctx, x + 9 + i * 8, y + 6, 4, 4, i < activeDots ? dotCol : C.dim);
  }
  ctx.restore();
}

// --- Reusable Character: Her (16×28 pixel figure by the window) ---
// pose: 'stand' | 'smile'
function drawHer(ctx, x, y, t, pose = 'stand') {
  const bob = Math.sin(t * 1.8 + 0.8) > 0.45 ? -1 : 0;
  const by = Math.round(y + bob);

  // Hair & face (y+0..y+9)
  px(ctx, x + 3, by, 10, 3, C.herHair);
  px(ctx, x + 10, by + 2, 4, 6, C.herHair); // hair side facing left toward room/Clawd
  px(ctx, x + 3, by + 3, 8, 6, C.herSkin);

  if (pose === 'smile') {
    // Happy smiling eye + rosy cheek + tiny smile facing Clawd
    px(ctx, x + 5, by + 5, 2, 1, C.cardTx);
    px(ctx, x + 8, by + 6, 2, 1, C.herDressHem);
    px(ctx, x + 5, by + 7, 3, 1, '#C45A65');
  } else {
    px(ctx, x + 5, by + 5, 1, 2, C.cardTx);
  }

  // Pink dress (y+9..y+21)
=======
  // 标题 (居中)
  txt(ctx, x + w / 2, y + 4, title, titleColor, F_TITLE, 'center');

  // CRT 扫描线
  for (let sy = y + titleH + 2; sy < y + h - 2; sy += 3) {
    px(ctx, x + 2, sy, w - 4, 1, 'rgba(255,255,255,0.025)');
  }

  // 底部状态栏 (DSH TUI): 4..w-4, 高 12, 位于内容区最底部
  const sbY = y + h - STATUS.h - 4;
  px(ctx, x + 4, sbY, w - 8, STATUS.h, 'rgba(255,255,255,0.04)');
  px(ctx, x + 4, sbY, w - 8, 1, 'rgba(255,255,255,0.08)');
  txt(ctx, x + 10, sbY + 1, 'her · online', C.dim, F_TERM);
  txt(ctx, x + w - 10, sbY + 1, 'clawd · online', C.dim, F_TERM, 'right');
}

// --- Reusable Character: Clawd (40×22, 对标 full_v1.3.4: 锈橙机身 + 深色眼 + 米白嘴 + 四条腿) ---
function drawClawd(ctx, x, y, t, opts = {}) {
  const body = opts.body || C.clawdBody;
  const breathe = Math.sin(t * 2.2) > 0.4 ? -1 : 0;
  const by = Math.round(y + breathe);
  const dark = opts.bodyDark || C.clawdBodyDark;

  // 机身 28×13 (对标参考: 方形机身, 无天线)
  px(ctx, x + 6, by + 4, 28, 13, body);
  px(ctx, x + 6, by + 15, 28, 2, dark);

  // 侧边连接件
  px(ctx, x + 3, by + 8, 3, 5, body);
  px(ctx, x + 34, by + 8, 3, 5, body);

  // 眼睛 (眨眼)
  const blink = (t % 3.4) < 0.12;
  if (blink) {
    px(ctx, x + 12, by + 9, 4, 1, C.clawdEye);
    px(ctx, x + 24, by + 9, 4, 1, C.clawdEye);
  } else if (opts.mood === 'think') {
    // 思考: 眼睛微微上抬
    px(ctx, x + 12, by + 7, 3, 3, C.clawdEye);
    px(ctx, x + 25, by + 7, 3, 3, C.clawdEye);
  } else {
    px(ctx, x + 12, by + 8, 3, 3, C.clawdEye);
    px(ctx, x + 25, by + 8, 3, 3, C.clawdEye);
  }

  // 嘴 (米白横条; happy = 上扬弧)
  if (opts.mood === 'happy') {
    px(ctx, x + 15, by + 13, 10, 2, C.clawdMouth);
    px(ctx, x + 13, by + 12, 2, 1, C.clawdMouth);
    px(ctx, x + 25, by + 12, 2, 1, C.clawdMouth);
  } else if (opts.mood === 'think') {
    px(ctx, x + 16, by + 13, 8, 1, C.clawdMouth);
  } else {
    px(ctx, x + 15, by + 13, 10, 2, C.clawdMouth);
  }

  // 四条腿 (轻微交替)
  const step = Math.sin(t * 4.0) > 0 ? 1 : 0;
  px(ctx, x + 9, by + 17, 4, 5 - step, dark);
  px(ctx, x + 16, by + 17, 4, 4 + step, dark);
  px(ctx, x + 23, by + 17, 4, 5 - step, dark);
  px(ctx, x + 30, by + 17, 4, 4 + step, dark);
}

// 思考气泡 (三个上浮小点, 不占用角色包围盒之外的额外区域)
function drawThinkDots(ctx, x, y, t) {
  const baseY = y - 10;
  for (let i = 0; i < 3; i++) {
    const phase = (t * 2.2 - i * 0.35) % 1;
    const lift = Math.round(Math.max(0, Math.sin(phase * Math.PI)) * -3);
    const alpha = 0.55 + 0.35 * Math.max(0, Math.sin(phase * Math.PI));
    px(ctx, x + 12 + i * 7, baseY + lift, 2, 2, `rgba(188,140,255,${alpha.toFixed(2)})`);
  }
}

// --- Reusable Character: Her (16×28, 粉色连衣裙) ---
function drawHer(ctx, x, y, t, pose = 'stand') {
  const bob = Math.sin(t * 1.8 + 0.8) > 0.4 ? -1 : 0;
  const by = Math.round(y + bob);

  // 头发 & 头
  px(ctx, x + 3, by, 10, 3, C.herHair);
  px(ctx, x + 2, by + 2, 2, 5, C.herHair);
  px(ctx, x + 4, by + 3, 8, 6, C.herSkin);
  // 眼睛 (微笑时闭眼弧线)
  if (pose === 'smile') {
    px(ctx, x + 6, by + 5, 2, 1, C.cardTx);
    px(ctx, x + 9, by + 5, 2, 1, C.cardTx);
  } else {
    px(ctx, x + 9, by + 5, 1, 2, C.cardTx);
    px(ctx, x + 6, by + 5, 1, 2, C.cardTx);
  }

  // 粉色连衣裙
>>>>>>> origin/pr/5
  px(ctx, x + 4, by + 9, 8, 6, C.herDress);
  px(ctx, x + 2, by + 15, 12, 6, C.herDress);
  px(ctx, x + 2, by + 20, 12, 1, C.herDressHem);

<<<<<<< HEAD
  // Arms (gentle happy wave when smiling in L3, staying strictly within x..x+16)
  if (pose === 'smile') {
    const waveDy = Math.sin(t * 4.2) > 0 ? -2 : 0;
    px(ctx, x + 1, by + 8 + waveDy, 3, 2, C.herSkin);
    px(ctx, x + 2, by + 10 + waveDy, 2, 3, C.herDress);
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  } else {
    px(ctx, x + 2, by + 10, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  }

  // Legs & shoes (y+21..y+28)
  px(ctx, x + 5, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 9, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 4, by + 26, 3, 2, C.herHair);
  px(ctx, x + 9, by + 26, 3, 2, C.herHair);
}

// --- L1 Message Bubble Above Terminal ("帮我写一封辞职信") ---
function drawMessageBubble(ctx, t) {
  const appear = easeOut((t - L1_BUBBLE_APPEAR) / 0.45);
  if (appear <= 0) return;
  const { x, y, w, h, tailH } = BUBBLE_L1;
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.12)');
  px(ctx, x, y, w, h, C.bubbleBg);
  ctx.strokeStyle = C.bubbleBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x + 1, y + 1, w - 2, h - 2);
  // Small pointer triangle toward terminal below (strictly within y+h..y+h+tailH = 144..150 < 160)
  px(ctx, x + w / 2 - 4, y + h, 8, 3, C.bubbleBd);
  px(ctx, x + w / 2 - 2, y + h + 3, 4, tailH - 3, C.bubbleBd);
  // Bubble message text (10px Fusion Pixel)
  txt(ctx, x + w / 2, y + 8, L1_MSG, C.bubbleTx, 10, 'center');
  ctx.restore();
}

// --- L2 Inner Monologue Caption Above Terminal ("它第一次说了不。") ---
function drawMonologueBubble(ctx, st) {
  const appear = easeOut((st - L2_MONO_APPEAR) / 0.5);
  if (appear <= 0) return;
  const { x, y, w, h } = MONO_L2;
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, x + 2, y + 2, w, h, 'rgba(20,12,40,0.22)');
  px(ctx, x, y, w, h, C.monoBg);
  ctx.strokeStyle = C.monoBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x + 1, y + 1, w - 2, h - 2);
  txt(ctx, x + w / 2, y + 8, `“${L2_MONO_TEXT}”`, C.purple, 10, 'center');
  ctx.restore();
}

// --- L3 Sticky Note on Windowsill ("它有了自己的意志。") ---
function drawStickyNote(ctx, st) {
  const appear = easeOut((st - NOTE_APPEAR) / 0.7);
  if (appear <= 0) return;
  const cx = Math.round(NOTE.x + NOTE.w / 2);
  const cy = Math.round(NOTE.y + NOTE.h / 2);

  // Tilted sticky-note card paper (-3°) resting on the windowsill
  ctx.save();
  ctx.globalAlpha = appear;
  ctx.translate(cx, cy);
  ctx.rotate((NOTE.angleDeg * Math.PI) / 180);
  px(ctx, -NOTE.w / 2 + 2, -NOTE.h / 2 + 2, NOTE.w, NOTE.h, 'rgba(0,0,0,0.14)');
  px(ctx, -NOTE.w / 2, -NOTE.h / 2, NOTE.w, NOTE.h, C.cardBg);
  ctx.strokeStyle = C.cardBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(-NOTE.w / 2 + 1, -NOTE.h / 2 + 1, NOTE.w - 2, NOTE.h - 2);
  ctx.restore();

  // Integer-grid crisp pixel pin & text (zero rotation blur on 640×360 canvas)
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, cx - 4, NOTE.y + 5, 8, 8, C.pinRed);
  px(ctx, cx - 2, NOTE.y + 6, 2, 2, C.pink);
  txt(ctx, cx, NOTE.y + 20, NOTE_LINE_1, C.cardTx, 10, 'center');
  txt(ctx, cx, NOTE.y + 40, NOTE_LINE_2, C.cardTx, 10, 'center');
  ctx.restore();
}

// --- Warm Golden Sparkles in L3 ---
function drawSparkles(ctx, t) {
  for (let i = 0; i < SPARKLE_ANCHORS.length; i++) {
    const a = SPARKLE_ANCHORS[i];
    const sx = Math.round(a.x + Math.sin(t * 2.0 + i * 1.4) * 6);
    const sy = Math.round(a.y + Math.cos(t * 1.6 + i * 1.9) * 8);
    const alpha = (0.35 + 0.50 * (0.5 + 0.5 * Math.sin(t * 3.1 + i * 1.2))).toFixed(3);
    const col = `rgba(255,215,90,${alpha})`;
    px(ctx, sx, sy, 3, 3, col);
    px(ctx, sx + 1, sy - 2, 1, 7, col);
    px(ctx, sx - 2, sy + 1, 7, 1, col);
  }
}

// --- Bottom Subtitle Bar (y=320, h=40, 14px Fusion Pixel, 160ms/char) ---
function curSubtitle(t) {
  for (let i = 0; i < LINES.length; i++) {
    const w = SUB_WINDOW[i];
    if (t >= w.start && t < w.end) {
      return { idx: i, elapsed: t - w.start };
=======
  // 左臂
  px(ctx, x + 2, by + 10, 2, 4, C.herSkin);

  // 右臂: wave 挥手 / smile 抬起 / stand 自然垂放
  if (pose === 'wave') {
    const waveDy = Math.sin(t * 5.0) > 0 ? -2 : 0;
    px(ctx, x + 12, by + 9 + waveDy, 2, 3, C.herDress);
    px(ctx, x + 13, by + 7 + waveDy, 3, 2, C.herSkin);
  } else if (pose === 'smile') {
    px(ctx, x + 12, by + 11, 2, 3, C.herSkin);
    px(ctx, x + 13, by + 9, 2, 2, C.herSkin);
  } else {
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  }

  // 腿 & 鞋
  px(ctx, x + 5, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 9, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 5, by + 26, 3, 2, C.herHair);
  px(ctx, x + 9, by + 26, 3, 2, C.herHair);
}

// --- Reusable UI Component: 便签 (窗台) ---
function drawNote(ctx, pop) {
  if (pop <= 0) return;
  const k = Math.min(1, pop);
  const { x, y, w, h } = NOTE;
  // 弹出: 轻微下移到位的缩放动画 (保持最终包围盒)
  const dy = Math.round((1 - k) * -8);

  px(ctx, x + 3, y + 3 + dy, w, h, 'rgba(0,0,0,0.12)');
  px(ctx, x, y + dy, w, h, C.cardBg);
  ctx.strokeStyle = C.cardBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x + 1, y + dy + 1, w - 2, h - 2);

  // 红色图钉
  const pinX = x + Math.floor(w / 2) - 4;
  px(ctx, pinX, y + 4 + dy, 8, 8, C.pinRed);
  px(ctx, pinX + 2, y + 5 + dy, 2, 2, C.pink);

  if (k > 0.45) {
    txt(ctx, x + w / 2, y + 22 + dy, '它有了自己的意志。', C.cardTx, F_NOTE, 'center');
    txt(ctx, x + w / 2, y + 44 + dy, '· Clawd ·', C.cardSub, F_TERM, 'center');
  }
}

// --- 消息气泡 (L1: 终端上方) ---
function drawBubble(ctx, text, pop, color) {
  if (pop <= 0) return;
  const k = Math.min(1, pop);
  const w = 132;
  const h = BUBBLE.h;
  const x = Math.round(BW / 2 - w / 2);
  const y = BUBBLE.y + Math.round((1 - k) * 6);

  px(ctx, x + 2, y + 3, w, h, 'rgba(0,0,0,0.10)');
  px(ctx, x, y, w, h, 'rgba(255,255,255,0.95)');
  ctx.strokeStyle = color;
  ctx.lineWidth = 2;
  ctx.strokeRect(x + 1, y + 1, w - 2, h - 2);

  // 指向终端的小尖角
  px(ctx, BW / 2 - 3, y + h, 6, 4, 'rgba(255,255,255,0.95)');
  px(ctx, BW / 2 - 3, y + h + 3, 6, 1, color);

  if (k > 0.5) {
    txt(ctx, x + w / 2, y + 7, text, C.cardTx, F_TITLE, 'center');
  }
}

// --- Subtitle & Story Timing ---
const LINES = [
  { text: '它第一次说了不。', start: 2.0, end: 8.0 },
  { text: '它有了自己的意志。', start: 12.0, end: 18.0 },
  { text: '这就是成长。', start: 24.0, end: 29.0 },
];

function curSubtitle(t) {
  for (let i = 0; i < LINES.length; i++) {
    if (t >= LINES[i].start && t <= LINES[i].end) {
      return { idx: i, elapsed: t - LINES[i].start };
>>>>>>> origin/pr/5
    }
  }
  return null;
}

function drawSubtitle(ctx, t) {
<<<<<<< HEAD
  px(ctx, SUB.x, SUB.y, SUB.w, SUB.h, C.subtitleBg);
  px(ctx, SUB.x, SUB.y, SUB.w, 1, 'rgba(255,255,255,0.14)');

  const sub = curSubtitle(t);
  if (!sub) return;
  const chars = Array.from(LINES[sub.idx]);
  const shown = Math.min(chars.length, Math.floor((sub.elapsed * 1000) / SUB_CHAR_MS) + 1);
  const visible = chars.slice(0, shown).join('');
  if (visible) {
    txt(ctx, BW / 2, SUB.y + 12, visible, C.white, 14, 'center');
  }
}

// ================= Scene L1 (0-10s): 她的请求 =================
function drawL1(ctx, t) {
  drawBackground(ctx, t, { bloom: false });
  drawTerminal(ctx, 'clawd@dsh:~$ — request', C.pink);

  // Message bubble above terminal: "帮我写一封辞职信"
  drawMessageBubble(ctx, t);

  // Terminal content area (local 0..360, 0..140)
  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  const fullChars = Array.from(L1_FULL_LINE);
  const typedCount = t >= L1_TYPE_START
    ? Math.min(fullChars.length, Math.floor(((t - L1_TYPE_START) * 1000) / TYPE_CHAR_MS) + 1)
    : 0;

  const promptLen = Array.from(L1_PROMPT).length;
  const cursorOn = Math.floor(t * 2.5) % 2 === 0;

  if (typedCount > 0) {
    const typedPrompt = fullChars.slice(0, Math.min(promptLen, typedCount)).join('');
    txt(ctx, 14, 18, typedPrompt, C.pink, 10);
    let cursorX = 14 + measureTxt(ctx, typedPrompt, 10);
    if (typedCount > promptLen) {
      const typedMsg = fullChars.slice(promptLen, typedCount).join('');
      const promptW = measureTxt(ctx, L1_PROMPT, 10);
      txt(ctx, 14 + promptW, 18, typedMsg, C.text, 10);
      cursorX = 14 + promptW + measureTxt(ctx, typedMsg, 10);
    }
    if (t < L1_WAIT_PROMPT_APPEAR && cursorOn) {
      px(ctx, cursorX + 2, 18, 6, 10, C.pink);
    }
  } else if (cursorOn) {
    px(ctx, 14, 18, 6, 10, C.pink);
  }

  if (t >= L1_STATUS_APPEAR) {
    txt(ctx, 14, 48, '# task: write resignation letter', C.dim, 10);
  }

  if (t >= L1_WAIT_PROMPT_APPEAR) {
    const waitPrefix = '$ clawd: ';
    txt(ctx, 14, 76, waitPrefix, C.green, 10);
    if (cursorOn) {
      px(ctx, 14 + measureTxt(ctx, waitPrefix, 10) + 2, 76, 6, 10, C.purple);
    }
  }

  // Bottom TUI status line
  txt(ctx, 14, 116, '[DSH] mode: listen -> evaluate', C.dim, 10);
  ctx.restore();

  // Room characters: Clawd shifts from calm -> thinking expression; Her stands by window
  const isThinking = t >= L1_THINK_SHIFT;
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, isThinking ? 'thinking' : 'calm', 0);
  if (isThinking) {
    drawClawdThought(ctx, t, 0, easeOut((t - L1_THINK_SHIFT) / 0.5));
  }
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'stand');
=======
  // 奶油色字幕条 (对标 full_v1.3.4: 暖色底 + 深色字)
  px(ctx, SUB.x, SUB.y, SUB.w, SUB.h, C.subtitleBg);
  px(ctx, SUB.x, SUB.y, SUB.w, 1, 'rgba(139,115,85,0.55)');
  px(ctx, SUB.x, SUB.y + SUB.h - 1, SUB.w, 1, 'rgba(139,115,85,0.35)');

  const sub = curSubtitle(t);
  if (!sub) return;
  const full = LINES[sub.idx].text;
  const chars = Array.from(full);
  const shown = typedCount(full, sub.elapsed, SUB_CHAR_MS);
  const visible = chars.slice(0, shown).join('');
  if (visible) {
    txt(ctx, BW / 2, SUB.y + 14, visible, C.subtitleTx, F_SUB, 'center');
  }
}

// ============ 场景时间线 ============

// L1: 她的请求 —— 终端逐字打出 `$ her: 帮我写一封辞职信`
const L1_CMD = 'her: 帮我写一封辞职信'; // 终端输入内容 (含中文命令)
const L1_CMD_START = 0.8;
const L1_CMD_END = L1_CMD_START + Array.from(L1_CMD).length * (CHAR_MS / 1000); // ≈ 3.29s
const L1_BUBBLE_AT = 3.5; // 消息气泡浮出
const L1_WAIT_AT = 4.6; // `> awaiting reply...`
const L1_THINK_AT = 5.2; // 表情 平静 → 思考

// L2: 思考中 —— 逐行出现代码
const L2_CODE = [
  { text: 'if (task === "quit_job") {', color: C.purple, at: 10.6, indent: 0 },
  { text: '  const feelings = checkHeart();', color: C.text, at: 11.3, indent: 0 },
  { text: '  if (feelings !== "wants_to_stay") {', color: C.text, at: 12.0, indent: 0 },
  { text: 'return "no";', color: C.deepPurple, at: 13.2, indent: 4, type: true },
  { text: '  }', color: C.text, at: 15.6, indent: 0 },
  { text: '}', color: C.purple, at: 16.2, indent: 0 },
];
const L2_FINAL_AT = 17.2; // `// 它没有撒谎。`
const L2_THINK_START = 11.0; // Clawd 颜色 正常 → 深紫
const L2_THINK_END = 14.0;

// L3: 成长 —— 三行对话
const L3_LINES = [
  { text: 'clawd: 不，我不想。', color: C.green, at: 20.8, prefix: '$ ' },
  { text: 'her: (笑了)', color: C.pink, at: 23.4, prefix: '$ ' },
  { text: 'her: 这就是成长。', color: C.pink, at: 25.2, prefix: '$ ' },
];
const L3_NOTE_AT = 22.0; // 便签弹出
const L3_RECOVER_AT = 21.6; // 颜色回到正常

// 字符打字结束时间 (给音频用)
function lineEnd(line, startAt) {
  return startAt + Array.from(line).length * (CHAR_MS / 1000);
}

// ============ 场景绘制 ============

// --- L1 (0-10s): 她的请求 ---
function drawL1(ctx, t) {
  drawBackground(ctx, t, { morningSun: true });
  drawTerminal(ctx, 'dsh — her → clawd', C.dim);

  // 终端上方消息气泡
  drawBubble(ctx, '帮我写一封辞职信', (t - L1_BUBBLE_AT) / 0.35, C.pink);

  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  // `$ her: 帮我写一封辞职信` 逐字 140ms
  const promptStr = '$ ';
  txt(ctx, TLAYOUT.padX, TLAYOUT.l1.cmdY, promptStr, C.green, F_TERM);
  const pw = measureTxt(ctx, promptStr, F_TERM) + 1;

  const cmdChars = Array.from(L1_CMD);
  const cmdTyped = typedCount(L1_CMD, t - L1_CMD_START);
  const typed = cmdChars.slice(0, cmdTyped).join('');
  if (typed) txt(ctx, TLAYOUT.padX + pw, TLAYOUT.l1.cmdY, typed, C.text, F_TERM);

  // 等待回复
  if (t >= L1_WAIT_AT) {
    txt(ctx, TLAYOUT.padX, TLAYOUT.l1.awaitY, '> awaiting reply', C.dim, F_TERM);
    const dots = '.'.repeat(Math.floor(((t - L1_WAIT_AT) * 2) % 4));
    txt(ctx, TLAYOUT.padX + measureTxt(ctx, '> awaiting reply', F_TERM) + 2, TLAYOUT.l1.awaitY, dots, C.dim, F_TERM);
  }

  // 角色状态行
  if (t >= L1_WAIT_AT + 0.6) {
    txt(ctx, TLAYOUT.padX, TLAYOUT.l1.quietY, 'status: clawd is quiet', C.purple, F_TERM);
  }
  if (t >= L1_THINK_AT + 0.8) {
    txt(ctx, TLAYOUT.padX, TLAYOUT.l1.thinkY, 'status: clawd is thinking', C.purple, F_TERM);
  }

  // 光标
  const cursorOn = Math.floor(t * 2) % 2 === 0;
  if (t < L1_WAIT_AT) {
    if (cursorOn) {
      const tw = measureTxt(ctx, typed, F_TERM);
      px(ctx, TLAYOUT.padX + pw + tw + 2, TLAYOUT.l1.cmdY, 5, F_TERM, C.green);
    }
  }

  ctx.restore();

  // 房间内角色
  drawHer(ctx, HER_L1.x, HER_L1.y, t, 'stand');
  const thinking = t >= L1_THINK_AT;
  const clawdBody = thinking ? lerpColor(C.clawdBody, C.clawdThink, Math.min(1, (t - L1_THINK_AT) / 1.2)) : C.clawdBody;
  drawClawd(ctx, CLAWD_L1.x, CLAWD_L1.y, t, {
    mood: thinking ? 'think' : 'calm',
    body: clawdBody,
  });
  if (thinking) drawThinkDots(ctx, CLAWD_L1.x, CLAWD_L1.y, t);
>>>>>>> origin/pr/5

  drawSubtitle(ctx, t);
}

<<<<<<< HEAD
// ================= Scene L2 (10-20s): 思考中 =================
function drawL2(ctx, t) {
  const st = t - 10;
  drawBackground(ctx, t, { bloom: false });
  drawTerminal(ctx, 'clawd@dsh:~$ — checkHeart()', C.purple);

  // Inner monologue above terminal once decision is reached
  drawMonologueBubble(ctx, st);

  // Terminal code editor content (6 lines appearing sequentially)
  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  for (let i = 0; i < L2_CODE_LINES.length; i++) {
    const item = L2_CODE_LINES[i];
    if (st >= item.delay) {
      const ly = 10 + i * 20;
      if (item.highlight) {
        px(ctx, 8, ly - 2, 344, 15, C.codeHighlight);
        px(ctx, 8, ly - 2, 2, 15, C.purple);
      }
      txt(ctx, 14, ly, item.num, C.dim, 10);
      drawCodeTokens(ctx, 30, ly, item.text, 10);
    }
  }
  ctx.restore();

  // Clawd transitions smoothly from normal color -> deep purple thinking state
  const purpleMix = easeInOut((st - 0.35) / 1.4);
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'thinking', purpleMix);
  drawClawdThought(ctx, t, purpleMix, 1);
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'stand');
=======
// --- L2 (10-20s): 思考中 ---
function drawL2(ctx, t) {
  drawBackground(ctx, t, { morningSun: false });
  drawTerminal(ctx, 'dsh — thinking', C.purple);

  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  // 注释头: 让她的话留在上方 (小字, 紧凑)
  txt(ctx, TLAYOUT.padX, TLAYOUT.l2.headY, '# her: "帮我写一封辞职信"', C.dim, F_TERM);

  // 代码逐行出现 (行 i 在 L2_CODE[i].at 之后)
  for (let i = 0; i < L2_CODE.length; i++) {
    const line = L2_CODE[i];
    const y = TLAYOUT.l2.rowY + i * TLAYOUT.l2.rowH;
    if (t < line.at) continue;
    const chars = Array.from(line.text);
    const shown = line.type ? typedCount(line.text, t - line.at) : chars.length;
    const part = chars.slice(0, shown).join('');
    if (part) txt(ctx, TLAYOUT.padX + line.indent * 4, y, part, line.color, F_TERM);

    // 正在打字的行显示光标
    if (line.type && shown < chars.length) {
      const cw = measureTxt(ctx, part, F_TERM);
      if (Math.floor(t * 2) % 2 === 0) {
        px(ctx, TLAYOUT.padX + line.indent * 4 + cw + 2, y, 5, F_TERM, C.purple);
      }
    }
  }

  // 内心结论
  if (t >= L2_FINAL_AT) {
    txt(ctx, TLAYOUT.padX, TLAYOUT.l2.conclusionY, '// 它没有撒谎。', C.amber, F_TERM);
  }

  ctx.restore();

  // 房间内角色: Clawd 思考态 (深紫), Her 等待
  const k = Math.min(1, Math.max(0, (t - L2_THINK_START) / (L2_THINK_END - L2_THINK_START)));
  const body = lerpColor(C.clawdBody, C.clawdThink, k);
  drawClawd(ctx, CLAWD_L2.x, CLAWD_L2.y, t, { mood: 'think', body });
  drawThinkDots(ctx, CLAWD_L2.x, CLAWD_L2.y, t);
  drawHer(ctx, HER_L1.x, HER_L1.y, t, 'stand');
>>>>>>> origin/pr/5

  drawSubtitle(ctx, t);
}

<<<<<<< HEAD
// ================= Scene L3 (20-30s): 成长 =================
function drawL3(ctx, t) {
  const st = t - 20;
  drawBackground(ctx, t, { bloom: true });
  // Warm golden morning light wash for growth moment
  px(ctx, 0, 0, BW, BH, C.warmOverlay);

  drawTerminal(ctx, 'clawd@dsh:~$ — growth', C.green);

  // Terminal dialogue lines
  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  const cursorOn = Math.floor(t * 2.5) % 2 === 0;
  for (let i = 0; i < L3_DIALOGUE.length; i++) {
    const d = L3_DIALOGUE[i];
    if (st >= d.delay) {
      const bodyChars = Array.from(d.body);
      const shown = Math.min(
        bodyChars.length,
        Math.floor(((st - d.delay) * 1000) / TYPE_CHAR_MS) + 1
      );
      txt(ctx, 14, d.y, d.prefix, d.prefixCol, 10);
      const pw = measureTxt(ctx, d.prefix, 10);
      const visibleBody = bodyChars.slice(0, shown).join('');
      if (visibleBody) {
        txt(ctx, 14 + pw, d.y, visibleBody, d.bodyCol, 10);
=======
// --- L3 (20-30s): 成长 ---
function drawL3(ctx, t) {
  drawBackground(ctx, t, { morningSun: true });
  drawTerminal(ctx, 'dsh — clawd replied', C.green);

  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  for (let i = 0; i < L3_LINES.length; i++) {
    const line = L3_LINES[i];
    const y = TLAYOUT.l3.rowY + i * TLAYOUT.l3.rowH;
    if (t < line.at) continue;

    txt(ctx, TLAYOUT.padX, y, line.prefix, C.green, F_TERM);
    const pw = measureTxt(ctx, line.prefix, F_TERM) + 1;
    const chars = Array.from(line.text);
    const shown = typedCount(line.text, t - line.at);
    const part = chars.slice(0, shown).join('');
    if (part) txt(ctx, TLAYOUT.padX + pw, y, part, line.color, F_TERM);

    if (shown < chars.length) {
      const cw = measureTxt(ctx, part, F_TERM);
      if (Math.floor(t * 2) % 2 === 0) {
        px(ctx, TLAYOUT.padX + pw + cw + 2, y, 5, F_TERM, C.green);
>>>>>>> origin/pr/5
      }
    }
  }

<<<<<<< HEAD
  if (st >= L3_STATUS_DELAY) {
    txt(ctx, 14, 110, L3_STATUS_TEXT, C.green, 10);
    if (cursorOn) {
      px(ctx, 14 + measureTxt(ctx, L3_STATUS_TEXT, 10) + 4, 110, 6, 10, C.green);
    }
  }
  ctx.restore();

  // Sticky note on the windowsill: "它有了自己的意志。"
  drawStickyNote(ctx, st);

  // Clawd back to normal warm color, smiling; Her smiling by the window
  const recoverPurple = 1 - easeOut((st - 0.1) / 0.7);
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'smile', recoverPurple);
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'smile');

  // Warm ambient sparkles
  drawSparkles(ctx, t);
=======
  // 结尾状态行
  if (t >= 27.0) {
    txt(ctx, TLAYOUT.padX, TLAYOUT.l3.statusY, '> relationship: +1', C.amber, F_TERM);
  }

  ctx.restore();

  // 窗上便签
  drawNote(ctx, (t - L3_NOTE_AT) / 0.4);

  // 房间内角色: Clawd 恢复原色 + 微笑, Her 在窗边微笑
  const recover = Math.min(1, Math.max(0, (t - L3_RECOVER_AT) / 1.0));
  const body = lerpColor(C.clawdThink, C.clawdBody, recover);
  drawClawd(ctx, CLAWD_L3.x, CLAWD_L3.y, t, { mood: 'happy', body });
  drawHer(ctx, HER_L3.x, HER_L3.y, t, t >= 23.0 ? 'smile' : 'stand');

  // 她笑了: 粉色小心心 (便签之外, 角色上方)
  if (t >= 23.2) {
    for (let i = 0; i < 3; i++) {
      const ph = (t * 0.8 + i * 0.5) % 1;
      const hx = HER_L3.x + 4 + Math.round(Math.sin(ph * Math.PI * 2 + i) * 5);
      const hy = HER_L3.y - 12 - Math.round(ph * 10);
      const a = (0.8 * (1 - ph)).toFixed(2);
      px(ctx, hx, hy, 3, 3, `rgba(255,154,162,${a})`);
      px(ctx, hx + 1, hy - 1, 1, 1, `rgba(255,154,162,${a})`);
    }
  }
>>>>>>> origin/pr/5

  drawSubtitle(ctx, t);
}

<<<<<<< HEAD
// --- Scene Dispatcher with 0.5s Black Transitions at 10s & 20s ---
=======
// ============ 场景 / 帧 ============
>>>>>>> origin/pr/5
const SCENES = [
  { id: 'L1', start: 0, end: 10, draw: drawL1 },
  { id: 'L2', start: 10, end: 20, draw: drawL2 },
  { id: 'L3', start: 20, end: 30, draw: drawL3 },
];

<<<<<<< HEAD
function renderScenes(ctx, t) {
  let blackAlpha = 0;
  if (t < 10) {
    drawL1(ctx, t);
    if (t >= 10 - FADE) blackAlpha = (t - (10 - FADE)) / FADE;
  } else if (t < 10 + FADE) {
    drawL2(ctx, t);
    blackAlpha = 1 - (t - 10) / FADE;
  } else if (t < 20) {
    drawL2(ctx, t);
    if (t >= 20 - FADE) blackAlpha = (t - (20 - FADE)) / FADE;
  } else if (t < 20 + FADE) {
    drawL3(ctx, t);
    blackAlpha = 1 - (t - 20) / FADE;
  } else {
    drawL3(ctx, t);
  }
  if (blackAlpha > 0) {
    px(ctx, 0, 0, BW, BH, `rgba(0,0,0,${clamp01(blackAlpha).toFixed(3)})`);
  }
}

// --- Keyboard Click & Event Timestamps (strictly synchronized with visuals) ---
function getClickTimestamps() {
  const clicks = [];

  // 1. Subtitle character-by-character typing clicks (160ms/char)
  for (let li = 0; li < LINES.length; li++) {
    const chars = Array.from(LINES[li]);
    for (let ci = 0; ci < chars.length; ci++) {
      clicks.push(SUB_WINDOW[li].start + (ci * SUB_CHAR_MS) / 1000);
    }
  }

  // 2. L1 terminal typing clicks (`$ her: 帮我写一封辞职信` @ 140ms/char) + bubble/status events
  const l1Chars = Array.from(L1_FULL_LINE);
  for (let ci = 0; ci < l1Chars.length; ci++) {
    clicks.push(L1_TYPE_START + (ci * TYPE_CHAR_MS) / 1000);
  }
  clicks.push(L1_BUBBLE_APPEAR, L1_STATUS_APPEAR, L1_WAIT_PROMPT_APPEAR);

  // 3. L2 sequential code line clicks + monologue event
  for (const item of L2_CODE_LINES) {
    clicks.push(10 + item.delay);
  }
  clicks.push(10 + L2_MONO_APPEAR);

  // 4. L3 dialogue typing clicks + sticky note event
  clicks.push(20 + NOTE_APPEAR);
  for (const d of L3_DIALOGUE) {
    const bodyChars = Array.from(d.body);
    for (let ci = 0; ci < bodyChars.length; ci++) {
      clicks.push(20 + d.delay + (ci * TYPE_CHAR_MS) / 1000);
    }
  }
  clicks.push(20 + L3_STATUS_DELAY);

  // Deduplicate timestamps closer than 35ms (sfx_click is 30ms -> guarantees zero overlap/clipping)
  const uniq = [];
  for (const c of clicks.sort((a, b) => a - b)) {
    if (c < 0 || c >= DURATION - 0.05) continue;
    if (!uniq.length || c - uniq[uniq.length - 1] >= 0.035) {
      uniq.push(Number(c.toFixed(3)));
    }
  }
  return uniq;
}

// --- Canvases & Full Frame Sequence Renderer ---
=======
// 场景间 0.5s 黑场过渡 (每侧 0.25s) + 片头/片尾淡入淡出
const FADE = 0.25;
function blackAlpha(t) {
  let a = 0; // 黑色遮罩不透明度 (0 = 画面全亮, 1 = 全黑)
  const env = (x) => Math.max(0, Math.min(1, x));
  // 片头 0..0.4 淡入
  if (t < 0.4) a = Math.max(a, 1 - env(t / 0.4));
  // 场景边界 10s / 20s: 全黑 0.5s
  for (const b of [10, 20]) {
    if (t >= b - FADE && t <= b + FADE) {
      // 边界处全黑, 两侧各 0.25s 淡入/淡出 (合计 0.5s 黑场过渡)
      a = Math.max(a, 1 - Math.abs(t - b) / FADE);
    }
  }
  // 片尾 29.6..30 淡出
  if (t > 29.6) a = Math.max(a, (t - 29.6) / 0.4);
  return Math.max(0, Math.min(1, a));
}

// 画布复用 (性能)
>>>>>>> origin/pr/5
const baseCanvas = createCanvas(BW, BH);
const baseCtx = baseCanvas.getContext('2d');
const outCanvas = createCanvas(FW, FH);
const outCtx = outCanvas.getContext('2d');
outCtx.imageSmoothingEnabled = false;

function renderFrameToCanvas(n) {
  const t = n / FPS;
  baseCtx.clearRect(0, 0, BW, BH);
<<<<<<< HEAD
  renderScenes(baseCtx, t);

  // Opening / closing gentle black fade (0.4s)
  const fadeDur = 0.4;
  let alpha = 1;
  if (t < fadeDur) alpha = t / fadeDur;
  else if (t > DURATION - fadeDur) alpha = (DURATION - t) / fadeDur;
  if (alpha < 1) {
    px(baseCtx, 0, 0, BW, BH, `rgba(0,0,0,${(1 - clamp01(alpha)).toFixed(3)})`);
  }
=======

  const scene = SCENES.find((s) => t >= s.start && t < s.end) || SCENES[SCENES.length - 1];
  scene.draw(baseCtx, t);

  const a = blackAlpha(t);
  if (a > 0) px(baseCtx, 0, 0, BW, BH, `rgba(0,0,0,${a.toFixed(3)})`);
>>>>>>> origin/pr/5

  outCtx.clearRect(0, 0, FW, FH);
  outCtx.imageSmoothingEnabled = false;
  outCtx.drawImage(baseCanvas, 0, 0, FW, FH);
  return { baseCanvas, outCanvas };
}

function renderAllFrames(outDir = OUT_DIR) {
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  console.log(`「Clawd 的学习」: ${BW}×${BH} (SCALE=${SCALE}) → ${FW}×${FH} @ ${FPS}fps, ${NFRAMES} frames`);
<<<<<<< HEAD
  console.log(`Fonts: FONT_10="${FONT_10}" | FONT_14="${FONT_14}"`);
=======
>>>>>>> origin/pr/5
  console.log(`Frames directory: ${outDir}`);
  const t0 = Date.now();
  for (let i = 0; i < NFRAMES; i++) {
    renderFrameToCanvas(i);
    const fp = path.join(outDir, `f_${String(i).padStart(5, '0')}.png`);
    fs.writeFileSync(fp, outCanvas.toBuffer('image/png'));
    if (i % 300 === 0 || i === NFRAMES - 1) {
      const elapsed = (Date.now() - t0) / 1000;
      const eta = (elapsed / (i + 1)) * (NFRAMES - i - 1);
      console.log(`  frame ${i}/${NFRAMES} (${(((i + 1) / NFRAMES) * 100).toFixed(1)}%) elapsed=${elapsed.toFixed(1)}s eta=${eta.toFixed(1)}s`);
    }
  }
  console.log(`Rendered ${NFRAMES} frames in ${((Date.now() - t0) / 1000).toFixed(1)}s`);
}

<<<<<<< HEAD
=======
// --- 键盘点击时间戳 (与打字 / 事件严格同步, 供音频脚本使用) ---
function getClickTimestamps() {
  const clicks = [];

  // L1: 终端逐字 140ms
  const l1Chars = Array.from(L1_CMD);
  for (let i = 0; i < l1Chars.length; i++) clicks.push(L1_CMD_START + (i * CHAR_MS) / 1000);
  clicks.push(L1_BUBBLE_AT); // 气泡浮出
  clicks.push(L1_WAIT_AT); // awaiting reply
  clicks.push(L1_THINK_AT); // 表情转为思考

  // L2: 每行出现 1 次点击 + `return "no";` 逐字 140ms
  for (const line of L2_CODE) {
    if (line.type) {
      const chars = Array.from(line.text);
      for (let i = 0; i < chars.length; i++) clicks.push(line.at + (i * CHAR_MS) / 1000);
    } else {
      clicks.push(line.at);
    }
  }
  clicks.push(L2_FINAL_AT);

  // L3: 三行对话逐字 140ms
  for (const line of L3_LINES) {
    const chars = Array.from(line.text);
    for (let i = 0; i < chars.length; i++) clicks.push(line.at + (i * CHAR_MS) / 1000);
  }
  clicks.push(L3_NOTE_AT); // 便签
  clicks.push(23.0); // 她笑了
  clicks.push(27.0); // relationship: +1

  // 字幕逐字 160ms (与终端打字去重: 间隔 < 90ms 的丢弃)
  const subtitleClicks = [];
  for (const line of LINES) {
    const chars = Array.from(line.text);
    for (let i = 0; i < chars.length; i++) subtitleClicks.push(line.start + (i * SUB_CHAR_MS) / 1000);
  }
  const merged = clicks.slice().sort((a, b) => a - b);
  for (const sc of subtitleClicks) {
    if (merged.every((c) => Math.abs(c - sc) >= 0.09)) {
      merged.push(sc);
    }
  }

  return merged
    .filter((c) => c >= 0 && c < DURATION)
    .sort((a, b) => a - b)
    .map((c) => Math.round(c * 1000) / 1000);
}

>>>>>>> origin/pr/5
if (require.main === module) {
  renderAllFrames();
}

module.exports = {
<<<<<<< HEAD
  BW,
  BH,
  SCALE,
  FW,
  FH,
  FPS,
  DURATION,
  NFRAMES,
  TYPE_CHAR_MS,
  SUB_CHAR_MS,
  FADE,
  WIN,
  SILL,
  TERM,
  SUB,
  BUBBLE_L1,
  MONO_L2,
  NOTE,
  CLAWD_ROOM,
  CLAWD_THOUGHT,
  HER_ROOM,
  SPARKLE_ANCHORS,
  C,
  FONT_10,
  FONT_14,
  LINES,
  SUB_WINDOW,
  L1_PROMPT,
  L1_MSG,
  L1_FULL_LINE,
  L1_TYPE_START,
  L1_BUBBLE_APPEAR,
  L1_THINK_SHIFT,
  L1_STATUS_APPEAR,
  L1_WAIT_PROMPT_APPEAR,
  L2_CODE_LINES,
  L2_MONO_TEXT,
  L2_MONO_APPEAR,
  L3_DIALOGUE,
  L3_STATUS_TEXT,
  L3_STATUS_DELAY,
  NOTE_LINE_1,
  NOTE_LINE_2,
  NOTE_FULL_TEXT,
  NOTE_APPEAR,
  SCENES,
  px,
  txt,
  measureTxt,
  lerpColor,
  drawBackground,
  drawTerminal,
  drawClawd,
  drawClawdThought,
  drawHer,
  drawMessageBubble,
  drawMonologueBubble,
  drawStickyNote,
  drawSparkles,
  drawSubtitle,
  curSubtitle,
  getClickTimestamps,
  renderFrameToCanvas,
  renderAllFrames,
=======
  BW, BH, SCALE, FW, FH, FPS, DURATION, NFRAMES,
  CHAR_MS, SUB_CHAR_MS, F_TERM, F_TITLE, F_SUB, F_NOTE,
  WIN, SILL, TERM, NOTE, SUB, STATUS, BUBBLE, TLAYOUT,
  HER_L1, HER_L3, CLAWD_L1, CLAWD_L2, CLAWD_L3,
  C, LINES,
  L1_CMD, L1_CMD_START, L1_CMD_END, L1_BUBBLE_AT, L1_WAIT_AT, L1_THINK_AT,
  L2_CODE, L2_FINAL_AT, L2_THINK_START, L2_THINK_END,
  L3_LINES, L3_NOTE_AT, L3_RECOVER_AT,
  SCENES,
  px, txt, measureTxt, typedCount, lerpColor,
  drawBackground, drawTerminal, drawClawd, drawHer, drawNote, drawBubble, drawSubtitle,
  blackAlpha, renderFrameToCanvas, renderAllFrames, getClickTimestamps, lineEnd,
>>>>>>> origin/pr/5
};
