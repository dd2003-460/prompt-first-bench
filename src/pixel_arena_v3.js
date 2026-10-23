#!/usr/bin/env node
'use strict';
// src/pixel_arena_v3.js — companion v1.1 / reboot / dialogue / farewell 共用像素美术库
//
// 与 src/pixel_arena_v2.js 的差异（v3 = v2 像素标准 + companion v1.1 的 440×200 终端）：
//   1. 终端 360×160 → 440×200，位置 (140,160) → (100,140)
//      标题栏 20px 不变，内容区 180px（v1.0 为 140px），可用文本行 4→7 行 + 状态行
//   2. 字幕条随之上移压缩为底部 20px（y=340..360），保证与终端底边 (340) 0 重叠
//   3. Clawd 配色回到 companion 的珊瑚色（#D97757 / 思考态 #6B5B95），
//      造型沿用 v2.0 标准：40×17 body + 顶部 2px 暗条 + 腹部 22×4 + 4×4 眼睛（1×1 高光）+ 4×6×7 腿
//   4. 房间背景补齐 companion 的夜景城市天际线 + 黎明渐变 + 蒸汽咖啡杯 + 独白卡片
//   5. 新增：电源灯 / 闪烁光标 / 星尘粒子 / 通用三场景时间轴（可逐场景配置黑场）
//
// 像素标准（SOP 05 §5 / v2.0）：基础画布 640×360 → nearest-neighbor 2× → 1280×720 @60fps，
//   所有最小视觉单元都是基础画布整像素（星星 2×2、窗棂 6×6、Clawd 眼睛 4×4、圆点 6×6），
//   字体 Fusion Pixel 10px（终端）/ 12px（字幕、便签），alpha 阈值二值化，无抗锯齿。

const { createCanvas, GlobalFonts } = require('@napi-rs/canvas');
const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// 字体注册（与 v2 一致）
// ---------------------------------------------------------------------------
let FONT_10 = 'monospace';
let FONT_12 = 'monospace';

function registerFonts() {
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
      GlobalFonts.registerFromPath(fp12, 'FusionPixel12');
      FONT_12 = 'FusionPixel12, monospace';
      if (FONT_10 === 'monospace') FONT_10 = 'FusionPixel12, monospace';
    }
  } catch (_) {}

  if (FONT_10 === 'monospace' || FONT_12 === 'monospace') {
    const fallbacks = [
      '/usr/local/share/fonts/NotoSansMonoCJKsc-Regular.otf',
      '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
      '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
    ];
    for (const cand of fallbacks) {
      if (fs.existsSync(cand)) {
        GlobalFonts.registerFromPath(cand, 'FallbackMono');
        if (FONT_10 === 'monospace') FONT_10 = 'FallbackMono, monospace';
        if (FONT_12 === 'monospace') FONT_12 = 'FallbackMono, monospace';
        break;
      }
    }
  }
}
registerFonts();

function fontFamilyForSize(size) {
  return size <= 11 ? FONT_10 : FONT_12;
}

// ---------------------------------------------------------------------------
// 画布 / 时间常量
// ---------------------------------------------------------------------------
const BW = 640;
const BH = 360;
const SCALE = 2;
const FW = BW * SCALE; // 1280
const FH = BH * SCALE; // 720
const FPS = 60;
const DURATION = 30;
const NFRAMES = DURATION * FPS; // 1800

const TYPE_CHAR_MS = 140; // 终端逐字 140ms/字（companion / SOP）
const SUB_CHAR_MS = 160; // 字幕逐字 160ms/字
const FADE = 0.25; // 场景黑场 0.25s 出 + 0.25s 入
const FADE_IN = 0.4;
const FADE_OUT = 0.8;

// ---------------------------------------------------------------------------
// 布局（640×360 基准网格）
// ---------------------------------------------------------------------------
const WIN = { x: 60, y: 20, w: 520, h: 160, fw: 8 }; // 木窗
const SILL = { x: 56, y: 180, w: 528, h: 8 }; // 窗台
const TERM = { x: 100, y: 140, w: 440, h: 200, titleH: 20 }; // v1.1 大终端
const CONTENT = { x: 102, y: 162, w: 436, h: 176 }; // 边框内内容区（180px 标称 = 20 title + 180 content）
const TEXT_X = 112; // 文本左起点（距终端左边 12px）
const TEXT_RIGHT = 528; // 文本右边界（距终端右边 12px）
const TEXT_BOX = { x: TEXT_X, y: 164, w: TEXT_RIGHT - TEXT_X, h: 172 }; // 文本可用区（0px 容差判定的容器）
const ROW_Y = [168, 188, 208, 228, 248, 268, 288]; // 7 行终端文本
const STATUS_Y = 322; // 终端底部状态行
const STATUS_DIVIDER = { x: TEXT_X, y: 311, w: TEXT_RIGHT - TEXT_X, h: 1 };
const SUB = { x: 0, y: 340, w: 640, h: 20 }; // 字幕条（终端底边 340，0 重叠）
const SUB_TEXT_Y = 342;

// 角色站位（房间内、终端之外）
const CLAWD_ROOM = { x: 52, y: 240, w: 40, bodyH: 17, legH: 7 };
const HER_ROOM = { x: 556, y: 194, w: 16, h: 28 };
const CLAWD_BOX = { x: 52, y: 238, w: 40, h: 26 }; // 含 bob(-1) 与 proud(-1) 包络
const HER_BOX = { x: 556, y: 193, w: 16, h: 29 };

// 通用浮层坐标（四个视频共用，互不重叠）
const RIGHT_NOTE = { x: 544, y: 244, w: 92, h: 60 }; // 右侧墙面便签
const LEFT_THOUGHT = { x: 8, y: 190, w: 84, h: 30 }; // Clawd 左侧上方思考泡泡
const TOP_CARD = { x: 210, y: 102, w: 220, h: 26 }; // 终端上方独白/提示卡
const LEFT_BUBBLE = { x: 24, y: 100, w: 112, h: 24 }; // 终端上方 Her 消息气泡
const LEFT_MUG = { x: 12, y: 268, w: 28, h: 36 }; // 左侧咖啡杯（避开 Clawd x=52）

// ---------------------------------------------------------------------------
// 调色板
// ---------------------------------------------------------------------------
const C = {
  // 暖色房间
  bgWarm: '#F5EDD5',
  stripe: '#EDE3C8',
  woodFrame: '#8B7355',
  woodLight: '#A08A6A',
  woodDark: '#6E5A44',
  woodSill: '#A08060',
  pot: '#7A5A3A',
  potRim: '#B06A46',
  plant: '#5A7A5A',
  plantLight: '#7BC07B',
  plantDark: '#4E864E',

  // 夜空 / 黎明
  nightSkyTop: '#0A1224',
  nightSkyBottom: '#182644',
  dawnSkyTop: '#87CEEB',
  dawnSkyBottom: '#FFE4B5',
  mountainNight: '#16243A',
  mountainNight2: '#1D2C3F',
  mountainDawn: '#5A7A5A',
  starWarm: '#FFF6D8',
  moon: '#FFF4C4',
  cityBldg1: '#121B2E',
  cityBldg2: '#1A263E',
  cityWinWarm: '#FFD166',
  cityWinDim: '#5C7699',

  // 终端
  termBg: '#14161C',
  termTitle: '#21262D',
  termBd: '#30363D',
  termCell: '#232833',
  scanline: 'rgba(255,255,255,0.025)',

  // 文本与强调色
  text: '#E6EDF3',
  dim: '#8B949E',
  green: '#7EE787',
  pink: '#FF9AA2',
  amber: '#E3B341',
  purple: '#BC8CFF',
  blue: '#79C0FF',
  red: '#FF7B72',
  white: '#FFFFFF',

  // Clawd（companion 珊瑚 → 暖橙；思考态 v2 紫）
  clawdBody: '#D97757',
  clawdDark: '#B85A3B',
  clawdBelly: '#F5E8D7',
  clawdWarm: '#F28B50',
  clawdWarmDark: '#D46A34',
  clawdWarmBelly: '#FFF1DE',
  clawdThink: '#6B5B95',
  clawdThinkDark: '#53456F',
  clawdThinkBelly: '#B7AAD4',
  clawdEye: '#141413',
  clawdBlush: '#FF9AA2',

  // Her
  herHair: '#5A4632',
  herSkin: '#E8C39E',
  herDress: '#FF9AA2',
  herDressHem: '#E57A84',

  // 气泡 / 卡片 / 便签 / 咖啡
  bubbleBg: '#FFF8F9',
  bubbleBd: '#E57A84',
  bubbleTx: '#2E1E24',
  thoughtBg: '#FFFCEF',
  thoughtBd: '#C9B78E',
  thoughtTx: '#3A3220',
  monoBg: '#241B18',
  monoBd: '#E3B341',
  cardBg: '#FFF8DC',
  cardBd: '#DEB887',
  cardTx: '#241A06',
  cardSub: '#6E5A3A',
  tape: 'rgba(255,255,255,0.55)',
  mugBody: '#F7EFE2',
  mugRim: '#D8C7B0',
  mugCoffee: '#6F4E37',
  mugSteam: 'rgba(255,248,235,0.75)',

  subtitleBg: 'rgba(0,0,0,0.80)',
  nightTint: 'rgba(12,20,42,0.07)',
};

// Clawd 调色板：coral = companion（默认），sage = v2.0
const CLAWD_PALETTES = {
  coral: {
    body: C.clawdBody,
    dark: C.clawdDark,
    belly: C.clawdBelly,
    warm: C.clawdWarm,
    warmDark: C.clawdWarmDark,
    warmBelly: C.clawdWarmBelly,
    think: C.clawdThink,
    thinkDark: C.clawdThinkDark,
    thinkBelly: C.clawdThinkBelly,
  },
  sage: {
    body: '#7B9E6B',
    dark: '#5E7C50',
    belly: '#C6DCB7',
    warm: null,
    think: C.clawdThink,
    thinkDark: C.clawdThinkDark,
    thinkBelly: C.clawdThinkBelly,
  },
};

// ---------------------------------------------------------------------------
// 基础工具
// ---------------------------------------------------------------------------
function clamp01(v) {
  return Math.max(0, Math.min(1, v));
}
function easeOut(v) {
  return 1 - Math.pow(1 - clamp01(v), 3);
}
function easeInOut(v) {
  const x = clamp01(v);
  return x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2;
}
function hexToRgb(hex) {
  const n = parseInt(hex.slice(1), 16);
  return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
}
function lerpColor(a, b, t) {
  const k = clamp01(t);
  const [r1, g1, b1] = hexToRgb(a);
  const [r2, g2, b2] = hexToRgb(b);
  return `rgb(${Math.round(r1 + (r2 - r1) * k)},${Math.round(g1 + (g2 - g1) * k)},${Math.round(b1 + (b2 - b1) * k)})`;
}

function px(ctx, x, y, w, h, color) {
  if (w <= 0 || h <= 0) return;
  ctx.fillStyle = color;
  ctx.fillRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
}

// 6×6 像素圆点（去四角）
function dot(ctx, x, y, size, color) {
  const s = size;
  px(ctx, x + 1, y, s - 2, 1, color);
  px(ctx, x, y + 1, s, s - 2, color);
  px(ctx, x + 1, y + s - 1, s - 2, 1, color);
}

// ---------------------------------------------------------------------------
// 阈值化点阵文字（逐字形缓存，整像素绘制）
// ---------------------------------------------------------------------------
const _glyphCache = new Map();
const _measureCtx = createCanvas(8, 8).getContext('2d');
const _measureCache = new Map();

function charWidth(ch, size) {
  const key = `${size}|${ch}`;
  let w = _measureCache.get(key);
  if (w === undefined) {
    _measureCtx.font = `${size}px ${fontFamilyForSize(size)}`;
    w = Math.round(_measureCtx.measureText(ch).width);
    _measureCache.set(key, w);
  }
  return w;
}

function glyph(ch, size, color) {
  let bucket = _glyphCache.get(`${size}|${color}`);
  if (!bucket) {
    bucket = new Map();
    _glyphCache.set(`${size}|${color}`, bucket);
  }
  let g = bucket.get(ch);
  if (g) return g;

  const w = Math.max(1, charWidth(ch, size)) + 2;
  const h = Math.ceil(size * 1.5) + 2;
  const cv = createCanvas(w, h);
  const cx = cv.getContext('2d');
  cx.font = `${size}px ${fontFamilyForSize(size)}`;
  cx.textAlign = 'left';
  cx.textBaseline = 'top';
  cx.fillStyle = '#FFFFFF';
  cx.fillText(ch, 1, 1);

  const img = cx.getImageData(0, 0, w, h);
  const d = img.data;
  const [r, gg, b] = hexToRgb(color);
  for (let i = 0; i < d.length; i += 4) {
    if (d[i + 3] > 128) {
      d[i] = r;
      d[i + 1] = gg;
      d[i + 2] = b;
      d[i + 3] = 255;
    } else {
      d[i + 3] = 0;
    }
  }
  cx.putImageData(img, 0, 0);
  g = { cv, w };
  bucket.set(ch, g);
  return g;
}

function measureTxt(str, size = 10) {
  if (!str) return 0;
  let w = 0;
  for (const ch of Array.from(str)) w += charWidth(ch, size);
  return w;
}

function txt(ctx, x, y, str, color, size = 10, align = 'left') {
  if (!str) return { x: Math.round(x), y: Math.round(y), w: 0, h: size };
  const chars = Array.from(str);
  const width = measureTxt(str, size);
  let cx = Math.round(x);
  if (align === 'center') cx = Math.round(x - width / 2);
  else if (align === 'right') cx = Math.round(x - width);
  const cy = Math.round(y);
  for (const ch of chars) {
    const g = glyph(ch, size, color);
    ctx.drawImage(g.cv, cx, cy);
    cx += charWidth(ch, size);
  }
  return { x: cx - width, y: cy, w: width, h: size };
}

// 文字包围盒（与 txt 完全一致，供 check_overlap 使用）
function textBox(x, y, str, size, align = 'left') {
  const w = measureTxt(str, size);
  const h = Math.ceil(size * 1.3);
  let dx = x;
  if (align === 'center') dx = x - w / 2;
  else if (align === 'right') dx = x - w;
  return [Math.floor(dx), Math.round(y), Math.ceil(w), h];
}

function typedCount(t, startT, totalChars, charMs = TYPE_CHAR_MS) {
  if (t < startT) return 0;
  return Math.min(totalChars, Math.floor(((t - startT) * 1000) / charMs) + 1);
}

// 通用一行：parts 逐段着色，可逐字打字
function drawLine(ctx, x, y, parts, startT, t, opts = {}) {
  const size = opts.size || 10;
  const total = parts.reduce((s, p) => s + Array.from(p.text).length, 0);
  const n = typedCount(t, startT, total, opts.charMs || TYPE_CHAR_MS);
  let remaining = n;
  let cx = x;
  let lastColor = parts[0].color;
  for (const p of parts) {
    if (remaining <= 0) break;
    const chars = Array.from(p.text);
    const take = Math.min(chars.length, remaining);
    if (take > 0) {
      const shown = chars.slice(0, take).join('');
      txt(ctx, cx, y, shown, p.color, size);
      cx += measureTxt(shown, size);
    }
    remaining -= take;
    lastColor = p.color;
  }
  if (opts.cursor !== false && n < total) {
    const on = Math.floor(t * 2.5) % 2 === 0;
    if (on) px(ctx, cx + 1, y + 1, 6, 10, lastColor);
  }
  return { typed: n, total, x: cx };
}

// 「提示符立即出现 + 消息逐字」——对话/故事线统一写法
//   prompt 出现时 1 次 click（instant），消息每个字符 1 次 click
function drawPromptMessage(ctx, x, y, prompt, promptColor, msg, msgColor, startT, t, opts = {}) {
  const cursorOn = Math.floor(t * 2.5) % 2 === 0;
  if (t < startT) {
    if (opts.cursor !== false && cursorOn) px(ctx, x, y + 1, 6, 10, promptColor);
    return { typed: 0, x };
  }
  txt(ctx, x, y, prompt, promptColor, 10);
  const px0 = x + measureTxt(prompt, 10);
  const n = typedCount(t, startT, Array.from(msg).length, opts.charMs || TYPE_CHAR_MS);
  const shown = Array.from(msg).slice(0, n).join('');
  if (shown) txt(ctx, px0, y, shown, msgColor, 10);
  const cx = px0 + measureTxt(shown, 10);
  if (n < Array.from(msg).length && opts.cursor !== false && cursorOn) px(ctx, cx + 1, y + 1, 6, 10, msgColor);
  return { typed: n, x: cx };
}

// 整行出现（instant），可选光标
function drawStaticLine(ctx, x, y, str, color, size, t, cursor = false) {
  const box = txt(ctx, x, y, str, color, size);
  if (cursor) {
    const on = Math.floor(t * 2.5) % 2 === 0;
    if (on) px(ctx, box.x + box.w + 1, y + 1, 6, 10, color);
  }
  return box;
}

// 多段着色整行
function drawStaticParts(ctx, x, y, parts, size = 10) {
  let cx = x;
  for (const p of parts) {
    txt(ctx, cx, y, p.text, p.color, size);
    cx += measureTxt(p.text, size);
  }
  return cx - x;
}

function partsText(parts) {
  return parts.map((p) => p.text).join('');
}

// ---------------------------------------------------------------------------
// 背景：暖色条纹墙 + 木窗（夜空/黎明 + 远山 + 城市 + 云）+ 窗台盆栽
// opts: { dawn 0..1, city bool, stars bool, dim 0..1 }
// ---------------------------------------------------------------------------
const NIGHT_STARS = [
  { dx: 30, dy: 84, s: 2 }, { dx: 68, dy: 96, s: 2 }, { dx: 112, dy: 74, s: 2 },
  { dx: 150, dy: 104, s: 2 }, { dx: 196, dy: 88, s: 2 }, { dx: 238, dy: 72, s: 2 },
  { dx: 268, dy: 100, s: 2 }, { dx: 306, dy: 80, s: 2 }, { dx: 342, dy: 108, s: 2 },
  { dx: 386, dy: 76, s: 2 }, { dx: 420, dy: 98, s: 2 }, { dx: 452, dy: 82, s: 2 },
  { dx: 470, dy: 112, s: 2 }, { dx: 246, dy: 118, s: 2 }, { dx: 96, dy: 116, s: 2 },
  { dx: 176, dy: 34, s: 2 }, { dx: 330, dy: 30, s: 2 }, { dx: 402, dy: 26, s: 2 },
];

// 城市天际线（相对 WIN 左上角；底边贴合玻璃下沿）
const CITY_BUILDINGS = [
  { dx: 24, w: 34, h: 44, col: C.cityBldg1, lights: [[6, 8], [18, 8], [6, 20], [18, 28]] },
  { dx: 62, w: 42, h: 60, col: C.cityBldg2, lights: [[8, 10], [22, 10], [8, 24], [22, 24], [14, 40]] },
  { dx: 112, w: 30, h: 36, col: C.cityBldg1, lights: [[6, 8], [16, 18]] },
  { dx: 180, w: 46, h: 54, col: C.cityBldg2, lights: [[8, 8], [26, 8], [8, 22], [26, 34]] },
  { dx: 284, w: 38, h: 58, col: C.cityBldg1, lights: [[8, 10], [20, 10], [8, 26], [20, 38]] },
  { dx: 328, w: 50, h: 46, col: C.cityBldg2, lights: [[8, 8], [22, 8], [34, 20], [12, 30]] },
  { dx: 416, w: 36, h: 64, col: C.cityBldg1, lights: [[8, 10], [20, 10], [8, 24], [20, 24], [8, 42]] },
  { dx: 458, w: 38, h: 40, col: C.cityBldg2, lights: [[8, 8], [22, 18], [12, 28]] },
];

function drawBackground(ctx, t, opts = {}) {
  const dp = clamp01(opts.dawn || 0);
  const cityOn = opts.city !== false;
  const starsOn = opts.stars !== false;

  // 1. 暖色条纹墙
  px(ctx, 0, 0, BW, BH, C.bgWarm);
  for (let x = 0; x < BW; x += 16) px(ctx, x, 0, 8, BH, C.stripe);
  if (dp < 0.5) px(ctx, 0, 0, BW, BH, `rgba(12,20,42,${((1 - dp * 2) * 0.07).toFixed(3)})`);
  else px(ctx, 0, 0, BW, BH, `rgba(255,205,110,${((dp - 0.5) * 2 * 0.08).toFixed(3)})`);

  // 2. 木窗
  const { x: wx, y: wy, w: ww, h: wh, fw } = WIN;
  px(ctx, wx, wy, ww, wh, C.woodFrame);
  px(ctx, wx, wy, ww, 2, C.woodLight);
  px(ctx, wx, wy, 2, wh, C.woodLight);
  px(ctx, wx, wy + wh - 2, ww, 2, C.woodDark);
  px(ctx, wx + ww - 2, wy, 2, wh, C.woodDark);

  const gx = wx + fw;
  const gy = wy + fw;
  const gw = ww - 2 * fw;
  const gh = wh - 2 * fw;

  ctx.save();
  ctx.beginPath();
  ctx.rect(gx, gy, gw, gh);
  ctx.clip();

  const topCol = lerpColor(C.nightSkyTop, C.dawnSkyTop, dp);
  const botCol = lerpColor(C.nightSkyBottom, C.dawnSkyBottom, dp);
  const grd = ctx.createLinearGradient(0, gy, 0, gy + gh);
  grd.addColorStop(0, topCol);
  grd.addColorStop(1, botCol);
  ctx.fillStyle = grd;
  ctx.fillRect(gx, gy, gw, gh);

  // 星星 + 月亮（黎明时淡出）
  if (starsOn && dp < 0.85) {
    const starAlpha = (1 - dp / 0.85) * 0.85;
    for (let i = 0; i < NIGHT_STARS.length; i++) {
      const s = NIGHT_STARS[i];
      const tw = 0.55 + 0.45 * Math.abs(Math.sin(t * 2.4 + i * 1.7));
      px(ctx, wx + s.dx, wy + s.dy, s.s, s.s, `rgba(255,246,216,${(starAlpha * tw).toFixed(3)})`);
    }
    const moonX = wx + 436;
    const moonY = wy + 26;
    px(ctx, moonX, moonY, 12, 12, `rgba(255,244,196,${(starAlpha * 0.92).toFixed(3)})`);
    px(ctx, moonX + 4, moonY + 1, 9, 10, `rgba(10,18,36,${(starAlpha * 0.92).toFixed(3)})`);
  }

  // 日出光晕
  if (dp > 0.2) {
    const sunK = clamp01((dp - 0.2) / 0.8);
    const sunX = wx + 196;
    const sunY = Math.round(wy + 116 - sunK * 52);
    px(ctx, sunX - 18, sunY - 18, 36, 36, `rgba(255,216,120,${(sunK * 0.26).toFixed(3)})`);
    px(ctx, sunX - 11, sunY - 11, 22, 22, `rgba(255,228,132,${(sunK * 0.52).toFixed(3)})`);
    px(ctx, sunX - 7, sunY - 7, 14, 14, `rgba(255,238,160,${(sunK * 0.9).toFixed(3)})`);
  }

  // 远山两层
  const mtCol = lerpColor(C.mountainNight, C.mountainDawn, dp);
  ctx.fillStyle = mtCol;
  ctx.beginPath();
  ctx.moveTo(gx, gy + gh);
  ctx.lineTo(wx + 132, wy + 72);
  ctx.lineTo(wx + 234, gy + gh);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(wx + 176, gy + gh);
  ctx.lineTo(wx + 332, wy + 50);
  ctx.lineTo(wx + 474, gy + gh);
  ctx.closePath();
  ctx.fill();
  ctx.fillStyle = lerpColor(C.mountainNight2, C.mountainDawn, dp);
  ctx.beginPath();
  ctx.moveTo(wx + 300, gy + gh);
  ctx.lineTo(wx + 392, wy + 88);
  ctx.lineTo(wx + 500, gy + gh);
  ctx.closePath();
  ctx.fill();

  // 城市天际线 + 亮窗（黎明淡入薄雾）
  if (cityOn) {
    const cityFade = clamp01(1 - dp * 0.75);
    for (let bi = 0; bi < CITY_BUILDINGS.length; bi++) {
      const b = CITY_BUILDINGS[bi];
      const bx = wx + b.dx;
      const by = gy + gh - b.h;
      px(ctx, bx, by, b.w, b.h, lerpColor(b.col, '#4E6B58', dp * 0.7));
      if (dp < 0.9) {
        for (let li = 0; li < b.lights.length; li++) {
          const [lx, ly] = b.lights[li];
          const flicker = Math.sin(t * 1.4 + bi * 2.1 + li * 1.3) > -0.65;
          const col = flicker
            ? `rgba(255,209,102,${(cityFade * 0.92).toFixed(3)})`
            : `rgba(92,118,153,${(cityFade * 0.55).toFixed(3)})`;
          px(ctx, bx + lx, by + ly, 6, 6, col);
        }
      }
    }
  }

  // 云
  const cloudAlpha = (0.16 + dp * 0.7).toFixed(3);
  const c1x = wx + 118 + Math.round(Math.sin(t * 0.32) * 12);
  px(ctx, c1x, wy + 38, 38, 9, `rgba(255,255,255,${cloudAlpha})`);
  px(ctx, c1x + 8, wy + 32, 22, 6, `rgba(255,255,255,${cloudAlpha})`);
  const c2x = wx + 334 + Math.round(Math.cos(t * 0.24) * 14);
  px(ctx, c2x, wy + 52, 46, 9, `rgba(255,255,255,${cloudAlpha})`);
  px(ctx, c2x + 10, wy + 46, 26, 6, `rgba(255,255,255,${cloudAlpha})`);

  ctx.restore();

  // 十字窗棂（6px）
  px(ctx, wx + ww / 2 - 3, gy, 6, gh, C.woodFrame);
  px(ctx, gx, wy + wh / 2 - 3, gw, 6, C.woodFrame);
  px(ctx, wx + ww / 2 - 3, gy, 1, gh, C.woodLight);
  px(ctx, gx, wy + wh / 2 - 3, gw, 1, C.woodLight);

  // 窗台
  px(ctx, SILL.x, SILL.y, SILL.w, SILL.h, C.woodSill);
  px(ctx, SILL.x, SILL.y, SILL.w, 2, C.woodFrame);
  px(ctx, SILL.x, SILL.y + SILL.h - 1, SILL.w, 1, C.woodDark);

  // 左下角盆栽（窗台内，不进入终端）
  const px0 = wx + 28;
  const py0 = wy + wh;
  px(ctx, px0 + 2, py0 - 16, 10, 8, C.plantLight);
  px(ctx, px0, py0 - 13, 14, 5, C.plantDark);
  px(ctx, px0 + 4, py0 - 19, 6, 3, C.plant);
  px(ctx, px0 + 6, py0 - 21, 2, 2, C.pink);
  px(ctx, px0, py0 - 8, 14, 2, C.potRim);
  px(ctx, px0 + 1, py0 - 6, 12, 6, C.pot);
}

// ---------------------------------------------------------------------------
// 终端 440×200 @ (100,140)：标题栏 20px + 红黄绿圆点 + 电源灯 + 内容区 180px
// led: 'on' | 'off'
// ---------------------------------------------------------------------------
function ledBox() {
  return [TERM.x + TERM.w - 16, TERM.y + 7, 6, 6];
}

function drawTerminal(ctx, title, accentColor = C.green, led = 'on') {
  const { x, y, w, h, titleH } = TERM;
  px(ctx, x + 4, y + 4, w, h, 'rgba(0,0,0,0.16)'); // 投影
  px(ctx, x, y, w, h, C.termBg);
  px(ctx, x, y, w, titleH, C.termTitle);
  px(ctx, x, y + titleH - 1, w, 1, accentColor);
  px(ctx, x, y, w, 2, C.termBd);
  px(ctx, x, y + h - 2, w, 2, C.termBd);
  px(ctx, x, y, 2, h, C.termBd);
  px(ctx, x + w - 2, y, 2, h, C.termBd);

  dot(ctx, x + 8, y + 7, 6, C.red);
  dot(ctx, x + 18, y + 7, 6, C.amber);
  dot(ctx, x + 28, y + 7, 6, C.green);

  txt(ctx, x + w / 2, y + 5, title, C.dim, 10, 'center');

  const [lx, ly] = ledBox();
  px(ctx, lx, ly, 6, 6, led === 'off' ? '#2A2F38' : C.green);
  px(ctx, lx + 1, ly + 1, 2, 2, led === 'off' ? '#3A414C' : '#C8FFD4');

  for (let sy = y + titleH + 3; sy < y + h - 3; sy += 3) {
    px(ctx, x + 2, sy, w - 4, 1, C.scanline);
  }
}

function drawStatusDivider(ctx) {
  px(ctx, STATUS_DIVIDER.x, STATUS_DIVIDER.y, STATUS_DIVIDER.w, STATUS_DIVIDER.h, 'rgba(255,255,255,0.07)');
}

function drawStatusLine(ctx, text, color = C.dim) {
  txt(ctx, TEXT_X, STATUS_Y, text, color, 10);
}

// ---------------------------------------------------------------------------
// Clawd：40×17 body + 顶部 2px 暗条 + 腹部 22×4 + 4×4 眼睛（1×1 高光）+ 4×6×7 腿
// mood: calm | warm | thinking | smile | curious
// opts: { palette:'coral'|'sage', warmMix 0..1, blend 0..1 (→ thinking 紫) }
// ---------------------------------------------------------------------------
function drawClawd(ctx, x, y, t, mood = 'calm', blend = null, opts = {}) {
  const pal = CLAWD_PALETTES[opts.palette || 'coral'];
  const thinking = mood === 'thinking';
  const k = clamp01(blend === null ? (thinking ? 1 : 0) : blend);
  const warmMix = clamp01(opts.warmMix || 0);

  let body = pal.body;
  let dark = pal.dark;
  let belly = pal.belly;
  if (pal.warm && warmMix > 0) {
    body = lerpColor(body, pal.warm, warmMix);
    dark = lerpColor(dark, pal.warmDark, warmMix);
    belly = lerpColor(belly, pal.warmBelly, warmMix);
  }
  if (k > 0) {
    body = lerpColor(body, pal.think, k);
    dark = lerpColor(dark, pal.thinkDark, k);
    belly = lerpColor(belly, pal.thinkBelly, k);
  }

  const phase = x * 0.01;
  const bob = Math.sin(t * 2.2 + phase) > 0.45 ? -1 : 0;
  const proud = mood === 'proud';
  const by = Math.round(y + bob + (proud ? -1 : 0));

  px(ctx, x, by, 40, 17, body);
  px(ctx, x, by, 40, 2, dark);
  px(ctx, x + 9, by + 11, 22, 4, belly);

  const blink = (t % 3.4) < 0.14;
  const eyeY = by + 6;

  const closedEyes = () => {
    px(ctx, x + 10, by + 8, 4, 1, C.clawdEye);
    px(ctx, x + 26, by + 8, 4, 1, C.clawdEye);
  };

  if (mood === 'thinking') {
    px(ctx, x + 10, by + 7, 4, 2, C.clawdEye);
    px(ctx, x + 26, by + 7, 4, 2, C.clawdEye);
    px(ctx, x + 10, by + 9, 4, 1, body);
    px(ctx, x + 26, by + 9, 4, 1, body);
    px(ctx, x + 17, by + 13, 6, 1, C.clawdEye);
  } else if (mood === 'smile') {
    if (blink) closedEyes();
    else {
      px(ctx, x + 9, by + 6, 2, 1, C.clawdEye);
      px(ctx, x + 11, by + 5, 2, 1, C.clawdEye);
      px(ctx, x + 13, by + 6, 2, 1, C.clawdEye);
      px(ctx, x + 25, by + 6, 2, 1, C.clawdEye);
      px(ctx, x + 27, by + 5, 2, 1, C.clawdEye);
      px(ctx, x + 29, by + 6, 2, 1, C.clawdEye);
    }
    px(ctx, x + 16, by + 12, 2, 1, C.clawdEye);
    px(ctx, x + 18, by + 13, 4, 1, C.clawdEye);
    px(ctx, x + 22, by + 12, 2, 1, C.clawdEye);
    px(ctx, x + 5, by + 8, 3, 2, C.clawdBlush);
    px(ctx, x + 32, by + 8, 3, 2, C.clawdBlush);
  } else if (mood === 'warm') {
    if (blink) closedEyes();
    else {
      px(ctx, x + 10, eyeY, 4, 4, C.clawdEye);
      px(ctx, x + 26, eyeY, 4, 4, C.clawdEye);
      px(ctx, x + 11, eyeY + 1, 1, 1, C.white);
      px(ctx, x + 27, eyeY + 1, 1, 1, C.white);
    }
    px(ctx, x + 16, by + 12, 2, 1, C.clawdEye);
    px(ctx, x + 18, by + 13, 4, 1, C.clawdEye);
    px(ctx, x + 22, by + 12, 2, 1, C.clawdEye);
    px(ctx, x + 5, by + 8, 3, 2, C.clawdBlush);
    px(ctx, x + 32, by + 8, 3, 2, C.clawdBlush);
  } else if (mood === 'curious') {
    if (blink) closedEyes();
    else {
      px(ctx, x + 9, by + 5, 5, 5, C.clawdEye);
      px(ctx, x + 26, by + 5, 5, 5, C.clawdEye);
      px(ctx, x + 10, by + 6, 2, 2, C.white);
      px(ctx, x + 27, by + 6, 2, 2, C.white);
    }
    px(ctx, x + 18, by + 12, 3, 3, C.clawdEye);
  } else {
    // calm
    if (blink) closedEyes();
    else {
      px(ctx, x + 10, eyeY, 4, 4, C.clawdEye);
      px(ctx, x + 26, eyeY, 4, 4, C.clawdEye);
      px(ctx, x + 11, eyeY + 1, 1, 1, C.white);
      px(ctx, x + 27, eyeY + 1, 1, 1, C.white);
    }
    px(ctx, x + 17, by + 12, 6, 1, C.clawdEye);
  }

  const legH = 7 - (proud ? 0 : Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, x + 3, by + 17, 6, legH, dark);
  px(ctx, x + 13, by + 17, 6, 7, dark);
  px(ctx, x + 21, by + 17, 6, 7, dark);
  px(ctx, x + 31, by + 17, 6, legH, dark);
}

// ---------------------------------------------------------------------------
// Her：16×28（粉色裙子）
// pose: stand | smile | wave
// ---------------------------------------------------------------------------
function drawHer(ctx, x, y, t, pose = 'stand') {
  const bob = Math.sin(t * 1.8 + 0.8) > 0.45 ? -1 : 0;
  const by = Math.round(y + bob);

  px(ctx, x + 3, by, 10, 3, C.herHair);
  px(ctx, x + 10, by + 2, 4, 6, C.herHair);
  px(ctx, x + 3, by + 3, 8, 6, C.herSkin);

  if (pose === 'smile') {
    px(ctx, x + 5, by + 5, 2, 1, C.cardTx);
    px(ctx, x + 8, by + 6, 2, 1, C.herDressHem);
    px(ctx, x + 5, by + 7, 3, 1, '#C45A65');
  } else {
    px(ctx, x + 5, by + 5, 1, 2, C.cardTx);
  }

  px(ctx, x + 4, by + 9, 8, 6, C.herDress);
  px(ctx, x + 2, by + 15, 12, 6, C.herDress);
  px(ctx, x + 2, by + 20, 12, 1, C.herDressHem);

  if (pose === 'wave') {
    const dy = Math.sin(t * 5.0) > 0 ? -2 : 0;
    px(ctx, x + 12, by + 9 + dy, 2, 3, C.herDress);
    px(ctx, x + 13, by + 6 + dy, 3, 2, C.herSkin);
  } else if (pose === 'smile') {
    px(ctx, x + 2, by + 10, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 13, 2, 2, C.herSkin);
    px(ctx, x + 11, by + 14, 3, 2, C.herSkin);
  } else {
    px(ctx, x + 2, by + 10, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  }

  px(ctx, x + 5, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 9, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 4, by + 26, 3, 2, C.herHair);
  px(ctx, x + 9, by + 26, 3, 2, C.herHair);
}

// ---------------------------------------------------------------------------
// Her 消息气泡（白底粉边 + 阶梯尾巴）
// ---------------------------------------------------------------------------
function drawMessageBubble(ctx, box, text, appear = 1) {
  if (appear <= 0) return;
  const { x, y, w, h } = box;
  const grow = appear < 1 ? 1 : 0;
  const bx = x + grow;
  const bw = w - grow * 2;

  px(ctx, bx + 3, y + 3, bw, h, 'rgba(0,0,0,0.10)');
  px(ctx, bx, y, bw, h, C.bubbleBg);
  px(ctx, bx, y, bw, 2, C.bubbleBd);
  px(ctx, bx, y + h - 2, bw, 2, C.bubbleBd);
  px(ctx, bx, y, 2, h, C.bubbleBd);
  px(ctx, bx + bw - 2, y, 2, h, C.bubbleBd);
  px(ctx, bx + bw - 18, y + h, 8, 2, C.bubbleBd);
  px(ctx, bx + bw - 16, y + h + 2, 5, 2, C.bubbleBd);
  px(ctx, bx + bw - 14, y + h + 4, 3, 2, C.bubbleBd);

  txt(ctx, bx + bw / 2, y + Math.round((h - 10) / 2), text, C.bubbleTx, 10, 'center');
}

// ---------------------------------------------------------------------------
// 思考泡泡（奶油底 + 2px 描边 + 阶梯尾巴）
// ---------------------------------------------------------------------------
function drawThoughtBubble(ctx, box, symbol, t, appear = 1) {
  if (appear <= 0) return;
  const { x, y, w, h } = box;
  const grow = appear < 1 ? 1 : 0;
  const bx = x + grow;
  const by = y + grow;
  const bw = w - grow * 2;
  const bh = h - grow * 2;

  px(ctx, bx + 2, by + 2, bw, bh, 'rgba(0,0,0,0.10)');
  px(ctx, bx, by, bw, bh, C.thoughtBg);
  px(ctx, bx, by, bw, 2, C.thoughtBd);
  px(ctx, bx, by + bh - 2, bw, 2, C.thoughtBd);
  px(ctx, bx, by, 2, bh, C.thoughtBd);
  px(ctx, bx + bw - 2, by, 2, bh, C.thoughtBd);
  px(ctx, bx + bw - 26, by + bh, 4, 4, C.thoughtBd);
  px(ctx, bx + bw - 21, by + bh + 4, 3, 3, C.thoughtBd);
  px(ctx, bx + bw - 16, by + bh + 7, 2, 2, C.thoughtBd);

  const bob = Math.sin(t * 2.0) > 0.3 ? -1 : 0;
  txt(ctx, bx + bw / 2, by + Math.round(bh / 2) - 7 + bob, symbol, C.thoughtTx, 12, 'center');
}

// ---------------------------------------------------------------------------
// 便签（纸 + 胶带 + 标题 12px + 副标题 10px + 折角）
// ---------------------------------------------------------------------------
function drawStickyNote(ctx, box, title, sub, t, appear = 1) {
  if (appear <= 0) return;
  const { x, y, w, h } = box;
  const grow = appear < 1 ? 2 : 0;
  const bx = x + grow;
  const by = y + grow;
  const bw = w - grow * 2;
  const bh = h - grow * 2;

  px(ctx, bx + 2, by + 3, bw, bh, 'rgba(0,0,0,0.12)');
  px(ctx, bx, by, bw, bh, C.cardBg);
  px(ctx, bx, by, bw, 2, C.cardBd);
  px(ctx, bx, by + bh - 2, bw, 2, C.cardBd);
  px(ctx, bx, by, 2, bh, C.cardBd);
  px(ctx, bx + bw - 2, by, 2, bh, C.cardBd);
  px(ctx, bx + bw / 2 - 9, by - 3, 18, 6, C.tape);
  px(ctx, bx + bw / 2 - 9, by - 3, 18, 1, 'rgba(255,255,255,0.30)');

  txt(ctx, bx + bw / 2, by + 12, title, C.cardTx, 12, 'center');
  if (sub) txt(ctx, bx + bw / 2, by + 32, sub, C.cardSub, 10, 'center');

  px(ctx, bx + bw - 6, by + bh - 6, 4, 4, C.cardBd);
}

// ---------------------------------------------------------------------------
// 终端上方独白卡（暗底金边）
// ---------------------------------------------------------------------------
function drawMonologueCard(ctx, box, text, appear = 1) {
  if (appear <= 0) return;
  const { x, y, w, h } = box;
  px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.20)');
  px(ctx, x, y, w, h, C.monoBg);
  px(ctx, x, y, w, 2, C.monoBd);
  px(ctx, x, y + h - 2, w, 2, C.monoBd);
  px(ctx, x, y, 2, h, C.monoBd);
  px(ctx, x + w - 2, y, 2, h, C.monoBd);
  txt(ctx, x + w / 2, y + 7, text, C.amber, 10, 'center');
}

// ---------------------------------------------------------------------------
// 蒸汽咖啡杯（28×36 盒）
// ---------------------------------------------------------------------------
function drawCoffeeMug(ctx, box, t, appear = 1) {
  if (appear <= 0) return;
  const { x, y } = box;
  ctx.save();
  ctx.globalAlpha = clamp01(appear);

  px(ctx, x + 2, y + 32, 22, 4, C.woodFrame);
  px(ctx, x + 4, y + 16, 18, 16, C.mugBody);
  px(ctx, x + 4, y + 16, 18, 3, C.mugRim);
  px(ctx, x + 6, y + 17, 14, 2, C.mugCoffee);
  px(ctx, x + 11, y + 23, 4, 4, C.clawdWarm);

  px(ctx, x + 22, y + 19, 4, 2, C.mugRim);
  px(ctx, x + 24, y + 21, 2, 5, C.mugRim);
  px(ctx, x + 22, y + 26, 4, 2, C.mugRim);

  for (let i = 0; i < 3; i++) {
    const phase = (t * 2.2 + i * 0.9) % 1;
    const sy = Math.round(y + 12 - phase * 9);
    const sway = Math.round(Math.sin(t * 4.0 + i * 2.0) * 1.5);
    const sx = x + 7 + i * 5 + sway;
    const a = (1 - Math.abs(phase - 0.5) * 1.6) * 0.75 * appear;
    if (a > 0.05) px(ctx, sx, sy, 2, 3, `rgba(255,248,235,${a.toFixed(3)})`);
  }
  ctx.restore();
}

// ---------------------------------------------------------------------------
// 闪烁光标 / 电源灯 / 星尘
// ---------------------------------------------------------------------------
function drawCursor(ctx, x, y, t, color, on = true) {
  if (!on) return;
  const blink = Math.floor(t * 2.5) % 2 === 0;
  if (blink) px(ctx, x, y, 6, 10, color);
}

function drawPowerLed(ctx, x, y, t, lit, color = C.green) {
  if (!lit) return;
  const pulse = 0.55 + 0.45 * Math.abs(Math.sin(t * 2.2));
  px(ctx, x - 6, y - 6, 18, 18, `rgba(126,231,135,${(0.10 * pulse).toFixed(3)})`);
  px(ctx, x - 3, y - 3, 12, 12, `rgba(126,231,135,${(0.20 * pulse).toFixed(3)})`);
  px(ctx, x, y, 6, 6, color);
  px(ctx, x + 1, y + 1, 2, 2, '#D6FFE0');
}

// 星尘粒子列表（绘制与布局共用；限定在区域内）
function sparkleList(t, region, count, startT) {
  const out = [];
  if (t < startT) return out;
  for (let i = 0; i < count; i++) {
    const ph = ((t - startT) * 0.5 + i * 0.33) % 1;
    const sx = region.x + 3 + ((i * 11) % Math.max(1, region.w - 6)) + Math.round(Math.sin(t * 1.3 + i) * 1);
    const sy = region.y + region.h - 2 - Math.round(ph * (region.h - 4));
    const a = (1 - Math.abs(ph - 0.5) * 1.8) * 0.9;
    if (a > 0.06) out.push({ x: sx, y: sy, a, s: 2 });
  }
  return out;
}

function drawSparkles(ctx, list, color = '255,246,216') {
  for (const p of list) px(ctx, p.x, p.y, p.s, p.s, `rgba(${color},${p.a.toFixed(3)})`);
}

// ---------------------------------------------------------------------------
// 字幕条（640×20 @ y=340，12px 点阵白字逐字出现）
// ---------------------------------------------------------------------------
function drawSubtitle(ctx, lines, windows, t) {
  px(ctx, SUB.x, SUB.y, SUB.w, SUB.h, C.subtitleBg);
  px(ctx, SUB.x, SUB.y, SUB.w, 1, 'rgba(255,255,255,0.14)');
  for (let i = 0; i < lines.length; i++) {
    const w = windows[i];
    if (t >= w.start && t < w.end) {
      const chars = Array.from(lines[i]);
      const shown = Math.min(chars.length, Math.floor(((t - w.start) * 1000) / SUB_CHAR_MS) + 1);
      const visible = chars.slice(0, shown).join('');
      if (visible) txt(ctx, BW / 2, SUB_TEXT_Y, visible, C.white, 12, 'center');
      return;
    }
  }
}

// 字幕当前显示文本（供布局使用）
function subtitleTextAt(lines, windows, t) {
  for (let i = 0; i < lines.length; i++) {
    const w = windows[i];
    if (t >= w.start && t < w.end) {
      const chars = Array.from(lines[i]);
      const shown = Math.min(chars.length, Math.floor(((t - w.start) * 1000) / SUB_CHAR_MS) + 1);
      const visible = chars.slice(0, shown).join('');
      if (visible) return visible;
    }
  }
  return null;
}

// ---------------------------------------------------------------------------
// 三场景时间轴（逐场景可配置 fadeIn / fadeOut；缺省 = FADE）
// ---------------------------------------------------------------------------
function sceneIndexAt(t, scenes) {
  let idx = 0;
  for (let i = 0; i < scenes.length; i++) if (t >= scenes[i].start) idx = i;
  return idx;
}

function drawScenes(ctx, t, scenes) {
  const idx = sceneIndexAt(t, scenes);
  const sc = scenes[idx];
  sc.draw(ctx, t);

  let a = 0;
  if (idx > 0) {
    const fin = sc.fadeIn === undefined ? FADE : sc.fadeIn;
    if (fin > 0 && t < sc.start + fin) a = Math.max(a, 1 - (t - sc.start) / fin);
  }
  if (idx < scenes.length - 1) {
    const fo = sc.fadeOut === undefined ? FADE : sc.fadeOut;
    if (fo > 0 && t >= sc.end - fo) a = Math.max(a, (t - (sc.end - fo)) / fo);
  }
  if (a > 0) px(ctx, 0, 0, BW, BH, `rgba(0,0,0,${clamp01(a).toFixed(3)})`);
}

function createFrameRenderer(scenes, outDir) {
  const baseCanvas = createCanvas(BW, BH);
  const baseCtx = baseCanvas.getContext('2d');
  const outCanvas = createCanvas(FW, FH);
  const outCtx = outCanvas.getContext('2d');
  outCtx.imageSmoothingEnabled = false;

  function renderFrameToCanvas(n) {
    const t = n / FPS;
    baseCtx.clearRect(0, 0, BW, BH);
    drawScenes(baseCtx, t, scenes);

    let alpha = 1;
    if (t < FADE_IN) alpha = t / FADE_IN;
    else if (t > DURATION - FADE_OUT) alpha = (DURATION - t) / FADE_OUT;
    if (alpha < 1) px(baseCtx, 0, 0, BW, BH, `rgba(0,0,0,${(1 - clamp01(alpha)).toFixed(3)})`);

    outCtx.clearRect(0, 0, FW, FH);
    outCtx.imageSmoothingEnabled = false;
    outCtx.drawImage(baseCanvas, 0, 0, FW, FH);
    return { baseCanvas, outCanvas };
  }

  function renderAllFrames(dir = outDir) {
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    console.log(`「pixel_arena_v3」: ${BW}×${BH} (SCALE=${SCALE}) → ${FW}×${FH} @ ${FPS}fps, ${NFRAMES} frames`);
    console.log(`Fonts: FONT_10="${FONT_10}" | FONT_12="${FONT_12}"`);
    console.log(`Frames directory: ${dir}`);
    const t0 = Date.now();
    for (let i = 0; i < NFRAMES; i++) {
      renderFrameToCanvas(i);
      const fp = path.join(dir, `f_${String(i).padStart(5, '0')}.png`);
      fs.writeFileSync(fp, outCanvas.toBuffer('image/png'));
      if (i % 300 === 0 || i === NFRAMES - 1) {
        const elapsed = (Date.now() - t0) / 1000;
        const eta = (elapsed / (i + 1)) * (NFRAMES - i - 1);
        console.log(`  frame ${i}/${NFRAMES} (${(((i + 1) / NFRAMES) * 100).toFixed(1)}%) elapsed=${elapsed.toFixed(1)}s eta=${eta.toFixed(1)}s`);
      }
    }
    console.log(`Rendered ${NFRAMES} frames in ${((Date.now() - t0) / 1000).toFixed(1)}s`);
  }

  return { baseCanvas, baseCtx, outCanvas, outCtx, renderFrameToCanvas, renderAllFrames };
}

module.exports = {
  BW, BH, SCALE, FW, FH, FPS, DURATION, NFRAMES,
  TYPE_CHAR_MS, SUB_CHAR_MS, FADE, FADE_IN, FADE_OUT,
  WIN, SILL, TERM, CONTENT, TEXT_X, TEXT_RIGHT, TEXT_BOX, ROW_Y, STATUS_Y, STATUS_DIVIDER, SUB, SUB_TEXT_Y,
  CLAWD_ROOM, HER_ROOM, CLAWD_BOX, HER_BOX,
  RIGHT_NOTE, LEFT_THOUGHT, TOP_CARD, LEFT_BUBBLE, LEFT_MUG,
  C, CLAWD_PALETTES,
  FONT_10, FONT_12, fontFamilyForSize,
  clamp01, easeOut, easeInOut, lerpColor, px, dot,
  txt, textBox, measureTxt, charWidth, typedCount, drawLine, drawPromptMessage, drawStaticLine, drawStaticParts, partsText,
  drawBackground, ledBox, drawTerminal, drawStatusDivider, drawStatusLine, drawClawd, drawHer,
  drawMessageBubble, drawThoughtBubble, drawStickyNote, drawMonologueCard, drawCoffeeMug,
  drawCursor, drawPowerLed, sparkleList, drawSparkles, drawSubtitle, subtitleTextAt,
  sceneIndexAt, drawScenes, createFrameRenderer,
};
