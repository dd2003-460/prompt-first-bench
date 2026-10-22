#!/usr/bin/env node
// 「Clawd 的梦境」30s 像素风视频渲染脚本 (dream_arena v1.0)
// 画布规格: 640×360 基础分辨率, SCALE=2 → 1280×720 @ 60fps, 1800 帧 (30s)
// 美术风格: 严格对标 full_v1.3.4 (暖色条纹房间 #F5EDD5 + 晨窗远山云朵 + 小终端 + 房间内像素角色)
// 故事线: D1 睡眠 (终端 # sleeping... + 星星闪烁) → D2 梦境 (两人并肩走在路上) → D3 醒来 (终端亮屏 + 便签)

const { createCanvas, GlobalFonts } = require('@napi-rs/canvas');
const fs = require('fs');
const path = require('path');

// --- Register pixel CJK font (Fusion Pixel) with clean fallback ---
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
const CHAR_MS = 160; // 160ms per character (与点击音同步)

const OUT_DIR = process.env.FRAMES_DIR || '/tmp/frames_dream';

// --- Layout Constants (严格对标 full_v1.3.4 / 任务书规格) ---
const WIN = { x: 60, y: 20, w: 520, h: 160, fw: 8 };
const TERM = { x: 140, y: 160, w: 360, h: 160, titleH: 20 };
const SUB = { x: 0, y: 320, w: 640, h: 40 };
// D3 便签: 100×80 米色, 倾斜 -5° (anchor = 未旋转时左上角, 绕中心旋转)
const NOTE = { x: 472, y: 56, w: 100, h: 80, angleDeg: -5 };

// 角色房间站位 (D1 睡眠 / D3 醒来, 终端两侧, 全部在字幕栏 y=320 之上)
const CLAWD_ROOM = { x: 64, y: 286 }; // 40×24 → 底沿 310
const HER_ROOM = { x: 560, y: 272 };  // 16×28 → 底沿 300
// D2 梦境路面站位 (并肩行走, 脚部基线对齐)
const CLAWD_DREAM = { x: 268, y: 268 }; // 40×24 → 底沿 292
const HER_DREAM = { x: 322, y: 264 };    // 16×28 → 底沿 292

// --- Palette (对齐 full_v1.3.4 / goodmorning arena) ---
const C = {
  // Room & Window
  bgWarm: '#F5EDD5',
  stripe: '#EDE3C8',
  woodFrame: '#8B7355',
  woodSill: '#A08060',
  skyTop: '#87CEEB',
  skyBottom: '#E0F0FF',
  mountain: '#5A7A5A',
  pot: '#7A5A3A',

  // Terminal
  termBg: '#14161C',
  termTitle: '#1E222B',
  termBd: '#30363D',
  panel: '#161B22',
  border: '#30363D',

  // Text & Accents
  text: '#E6EDF3',
  dim: '#8B949E',
  green: '#7EE787',
  pink: '#FF9AA2',
  amber: '#E3B341',
  purple: '#BC8CFF',
  purple2: '#A371F7',
  red: '#FF7B72',
  pinRed: '#FF5555',
  white: '#FFFFFF',

  // Clawd (紫色身体 + 6 条腿, 40×24)
  clawd: '#BC8CFF',
  clawdDark: '#A371F7',
  clawdBelly: '#E9D9FF',
  clawdEye: '#241A3D',

  // Her (16×28 粉色)
  herHair: '#5A4632',
  herSkin: '#E8C39E',
  herDress: '#FF9AA2',
  herDressHem: '#E57A84',

  // Sticky note (米色)
  cardBg: '#FFF8DC',
  cardBd: '#DEB887',
  cardTx: '#241A06',
  cardSub: '#6E5A3A',

  // Dream world (D2)
  dreamSkyTop: '#241B3D',
  dreamSkyMid: '#7A5AA8',
  dreamSkyLow: '#F2B8C6',
  dreamGround: '#6E8A5E',
  dreamRoad: '#8A7A6A',
  dreamRoadEdge: '#6E5E4E',
  dreamMoon: '#F5EDD5',

  subtitleBg: 'rgba(0,0,0,0.55)',
  warmOverlay: 'rgba(255,200,100,0.08)',
};

// --- Deterministic PRNG (星星位置固定, 保证重叠检测与渲染一致) ---
function mulberry32(seed) {
  let a = seed >>> 0;
  return function rand() {
    a |= 0;
    a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// D1 终端内星星 (终端内容区局部坐标, 避开 y<32 的 sleeping 文字带)
function buildTerminalStars() {
  const rng = mulberry32(20261022);
  const stars = [];
  let guard = 0;
  while (stars.length < 14 && guard++ < 500) {
    const x = 12 + Math.floor(rng() * 324);
    const y = 40 + Math.floor(rng() * 88);
    if (stars.some((s) => Math.abs(s.x - x) < 8 && Math.abs(s.y - y) < 8)) continue;
    stars.push({ x, y, phase: rng() * Math.PI * 2 });
  }
  return stars;
}
const TERM_STARS = buildTerminalStars();

// D2 弯月 (24×24, 两圆相减的像素月牙, 直接绘制无需遮罩)
const MOON = { x: 80, y: 50, size: 24 };
function buildMoonRows() {
  const rows = [];
  const c1 = { cx: 12, cy: 12, r: 12 };
  const c2 = { cx: 17, cy: 12, r: 11 }; // 向右偏移的暗圆 → 留下左侧月牙
  for (let y = 0; y < 24; y++) {
    let x0 = -1;
    let x1 = -1;
    for (let x = 0; x < 24; x++) {
      const in1 = (x - c1.cx) ** 2 + (y - c1.cy) ** 2 <= c1.r ** 2;
      const in2 = (x - c2.cx) ** 2 + (y - c2.cy) ** 2 <= c2.r ** 2;
      if (in1 && !in2) {
        if (x0 < 0) x0 = x;
        x1 = x;
      }
    }
    if (x0 >= 0) rows.push([x0, x1 - x0 + 1]);
  }
  return rows;
}
const MOON_ROWS = buildMoonRows();

// D2 梦境漂浮粒子 (左右两侧, 远离行走角色 x=268..338)
const DREAM_SPARKS = [
  { x: 118, y0: 232, amp: 26, phase: 0.0 },
  { x: 492, y0: 240, amp: 30, phase: 1.7 },
  { x: 232, y0: 206, amp: 22, phase: 3.1 },
];

// D2 夜空星星 (全屏坐标, 避开月亮保护区)
function buildDreamStars() {
  const rng = mulberry32(778899);
  const stars = [];
  let guard = 0;
  while (stars.length < 16 && guard++ < 500) {
    const x = 16 + Math.floor(rng() * 608);
    const y = 24 + Math.floor(rng() * 136);
    if (
      x > MOON.x - 8 && x < MOON.x + MOON.size + 8 &&
      y > MOON.y - 8 && y < MOON.y + MOON.size + 8
    ) continue; // 月亮保护区
    // 梦粒子上浮通道保护 (与 check_overlap 的 spark 包络一致)
    if (DREAM_SPARKS.some((sp) => Math.abs(x - sp.x) <= 12 && y >= sp.y0 - 150 && y <= sp.y0)) continue;
    if (stars.some((s) => Math.abs(s.x - x) < 26 && Math.abs(s.y - y) < 18)) continue;
    stars.push({ x, y, phase: rng() * Math.PI * 2 });
  }
  return stars;
}
const DREAM_STARS = buildDreamStars();

// --- Reusable Pixel Primitives ---
function px(ctx, x, y, w, h, color) {
  ctx.fillStyle = color;
  ctx.fillRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h), color);
}

// Threshold pixel text renderer (与 goodmorning arena 同源, 避免假重叠残影)
let _tmpCanvas = null;
function txt(ctx, x, y, str, color, font = 12, align = 'left') {
  if (!str) return { x, y, w: 0, h: font };
  const fontSpec = `${font}px ${FONT_FAMILY}`;
  ctx.font = fontSpec;

  // <12px 像素字体: 逐字符绘制 + 1px 字距, 保持干净像素
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
    d[i] = d[i] > 118 ? 255 : 0;
  }
  tctx.putImageData(img, 0, 0);

  let dx = x;
  if (align === 'center') dx = x - measuredW / 2 - 1;
  else if (align === 'right') dx = x - measuredW - 2;

  ctx.drawImage(_tmpCanvas, Math.round(dx), Math.round(y));
  return { x: Math.round(dx), y: Math.round(y), w: measuredW, h: font };
}

function measureTxt(ctx, str, font = 12) {
  if (!str) return 0;
  ctx.font = `${font}px ${FONT_FAMILY}`;
  if (font < 12) {
    const chars = Array.from(str);
    return chars.reduce((s, ch) => s + Math.ceil(ctx.measureText(ch).width), 0) + Math.max(0, chars.length - 1);
  }
  return Math.ceil(ctx.measureText(str).width);
}

function clamp01(v) { return Math.max(0, Math.min(1, v)); }
function easeOut(v) { return 1 - Math.pow(1 - clamp01(v), 3); }

// --- Background: 暖色条纹壁纸 + 大窗 (full_v1.3.4 同款) ---
function drawBackground(ctx, t) {
  // 暖色竖条纹壁纸: #F5EDD5 底 + 16px 周期条纹
  px(ctx, 0, 0, BW, BH, C.bgWarm);
  for (let x = 0; x < BW; x += 16) {
    px(ctx, x, 0, 8, BH, C.stripe);
  }

  // 窗户 x=60 y=20 520×160, 木框 8px
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

  // 天空渐变 #87CEEB → #E0F0FF
  const grd = ctx.createLinearGradient(0, gy, 0, gy + gh);
  grd.addColorStop(0, C.skyTop);
  grd.addColorStop(1, C.skyBottom);
  ctx.fillStyle = grd;
  ctx.fillRect(gx, gy, gw, gh);

  // 2 座山 #5A7A5A
  ctx.fillStyle = C.mountain;
  ctx.beginPath();
  ctx.moveTo(gx, gy + gh);
  ctx.lineTo(wx + 130, wy + 72);
  ctx.lineTo(wx + 230, gy + gh);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(wx + 175, gy + gh);
  ctx.lineTo(wx + 330, wy + 50);
  ctx.lineTo(wx + 470, gy + gh);
  ctx.closePath();
  ctx.fill();

  // 2 朵像素云 (缓慢漂移)
  const cx1 = wx + 104 + Math.round(Math.sin(t * 0.35) * 14);
  px(ctx, cx1, wy + 36, 40, 10, 'rgba(255,255,255,0.92)');
  px(ctx, cx1 + 8, wy + 30, 24, 6, 'rgba(255,255,255,0.92)');
  const cx2 = wx + 326 + Math.round(Math.cos(t * 0.25) * 16);
  px(ctx, cx2, wy + 52, 48, 10, 'rgba(255,255,255,0.90)');
  px(ctx, cx2 + 10, wy + 46, 28, 6, 'rgba(255,255,255,0.90)');

  ctx.restore();

  // 十字窗棂 + 窗台 + 盆栽
  px(ctx, wx + ww / 2 - 3, gy, 6, gh, C.woodFrame);
  px(ctx, gx, wy + wh / 2 - 3, gw, 6, C.woodFrame);
  px(ctx, wx - 4, wy + wh, ww + 8, 8, C.woodSill);
  px(ctx, wx - 4, wy + wh, ww + 8, 2, C.woodFrame);
  const px0 = wx + 28;
  const py0 = wy + wh;
  px(ctx, px0 + 2, py0 - 16, 10, 8, '#6AA86A');
  px(ctx, px0, py0 - 13, 14, 5, '#4E864E');
  px(ctx, px0 + 4, py0 - 19, 6, 3, '#7BC07B');
  px(ctx, px0, py0 - 8, 14, 2, '#B06A46');
  px(ctx, px0 + 1, py0 - 6, 12, 6, C.pot);
}

// --- Terminal (x=140 y=160 360×160, 深色 #14161C, 边框 #30363D) ---
function drawTerminal(ctx, title) {
  const { x, y, w, h, titleH } = TERM;
  px(ctx, x + 4, y + 4, w, h, 'rgba(0,0,0,0.15)');
  px(ctx, x, y, w, h, C.termBg);
  px(ctx, x, y, w, titleH, C.termTitle);
  px(ctx, x, y + titleH, w, 1, C.termBd);
  ctx.strokeStyle = C.termBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x, y, w, h);

  // 三色按钮 6×6
  px(ctx, x + 8, y + 7, 6, 6, C.red);
  px(ctx, x + 18, y + 7, 6, 6, C.amber);
  px(ctx, x + 28, y + 7, 6, 6, C.green);

  txt(ctx, x + w / 2, y + 4, title, C.dim, 10, 'center');

  // CRT 扫描线
  for (let sy = y + titleH + 2; sy < y + h - 2; sy += 3) {
    px(ctx, x + 2, sy, w - 4, 1, 'rgba(255,255,255,0.025)');
  }
}

// --- Clawd: 40×24 紫色身体 + 6 条腿 ---
// pose: 'sleep' (闭眼, 无步态) | 'idle' (睁眼站立) | 'walk' (六腿交替) | 'happy'
function drawClawd(ctx, x, y, t, pose = 'idle') {
  const bob = pose === 'walk' ? (Math.sin(t * 4.5) > 0 ? -1 : 0) : (Math.sin(t * 2.2) > 0.6 ? -1 : 0);
  const by = Math.round(y + bob);
  const bodyH = 16;

  // 紫色身体 40×16
  px(ctx, x, by, 40, bodyH, C.clawd);
  px(ctx, x, by, 40, 2, C.clawdDark);
  // 腹部亮色
  px(ctx, x + 8, by + 10, 24, 4, C.clawdBelly);

  // 眼睛 (10px 小字体风格的极简像素眼)
  const blink = pose !== 'sleep' && (t % 3.2) < 0.14;
  if (pose === 'sleep') {
    // 闭眼: 两条 1px 弧线
    px(ctx, x + 9, by + 7, 5, 1, C.clawdEye);
    px(ctx, x + 26, by + 7, 5, 1, C.clawdEye);
  } else if (blink) {
    px(ctx, x + 10, by + 7, 4, 1, C.clawdEye);
    px(ctx, x + 26, by + 7, 4, 1, C.clawdEye);
  } else {
    px(ctx, x + 10, by + 5, 4, 4, C.clawdEye);
    px(ctx, x + 26, by + 5, 4, 4, C.clawdEye);
    px(ctx, x + 11, by + 6, 1, 1, C.white);
    px(ctx, x + 27, by + 6, 1, 1, C.white);
  }
  // happy 微笑
  if (pose === 'happy') {
    px(ctx, x + 17, by + 11, 6, 1, C.clawdEye);
  }

  // 6 条腿 (4px 宽, 8px 高; 步态分两组三角交替)
  const legX = [2, 8, 14, 20, 26, 32];
  const swing = Math.sin(t * 4.5) > 0;
  for (let i = 0; i < 6; i++) {
    let lift = 0;
    if (pose === 'walk') lift = (i % 2 === 0) === swing ? 2 : 0;
    const lh = 8 - lift;
    px(ctx, x + legX[i], by + bodyH + lift, 4, lh, C.clawdDark);
  }
}

// --- Her: 16×28 粉色小人 ---
// pose: 'stand' | 'wave' | 'walk'
function drawHer(ctx, x, y, t, pose = 'stand') {
  const bob = pose === 'walk' ? (Math.sin(t * 4.5 + Math.PI) > 0 ? -1 : 0) : (Math.sin(t * 1.8 + 0.8) > 0.4 ? -1 : 0);
  const by = Math.round(y + bob);

  // 头发 + 脸
  px(ctx, x + 3, by, 10, 3, C.herHair);
  px(ctx, x + 2, by + 2, 2, 5, C.herHair);
  px(ctx, x + 4, by + 3, 8, 6, C.herSkin);
  px(ctx, x + 9, by + 5, 1, 2, C.cardTx);

  // 粉色裙子
  px(ctx, x + 4, by + 9, 8, 6, C.herDress);
  px(ctx, x + 2, by + 15, 12, 6, C.herDress);
  px(ctx, x + 2, by + 20, 12, 1, C.herDressHem);

  // 手臂
  if (pose === 'walk') {
    const armSwing = Math.sin(t * 4.5) > 0 ? -1 : 1;
    px(ctx, x + 2, by + 10 + armSwing, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 10 - armSwing, 2, 4, C.herSkin);
  } else if (pose === 'wave') {
    const waveDy = Math.sin(t * 5.0) > 0 ? -2 : 0;
    px(ctx, x + 2, by + 10, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 9 + waveDy, 2, 3, C.herDress);
    px(ctx, x + 13, by + 7 + waveDy, 3, 2, C.herSkin);
  } else {
    px(ctx, x + 2, by + 10, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  }

  // 腿 + 鞋 (行走时左右交替)
  if (pose === 'walk') {
    const step = Math.sin(t * 4.5) > 0;
    px(ctx, x + 5, by + 21, 2, 5 - (step ? 1 : 0), C.herSkin);
    px(ctx, x + 9, by + 21, 2, 5 - (step ? 0 : 1), C.herSkin);
    px(ctx, x + 5, by + 26 - (step ? 1 : 0), 3, 2, C.herHair);
    px(ctx, x + 9, by + 26 - (step ? 0 : 1), 3, 2, C.herHair);
  } else {
    px(ctx, x + 5, by + 21, 2, 5, C.herSkin);
    px(ctx, x + 9, by + 21, 2, 5, C.herSkin);
    px(ctx, x + 5, by + 26, 3, 2, C.herHair);
    px(ctx, x + 9, by + 26, 3, 2, C.herHair);
  }
}

// --- 字幕 (y=320 h=40, 14px, 半透明黑底, 逐字 160ms) ---
const LINES = [
  '它也做梦。',
  '梦里，它有了身体。',
  '醒来，还在等你。',
];
const SUB_WINDOW = [
  { start: 2, end: 8 },
  { start: 12, end: 18 },
  { start: 24, end: 29 },
];

function curSubtitle(t) {
  for (let i = 0; i < LINES.length; i++) {
    const w = SUB_WINDOW[i];
    if (t >= w.start && t < w.end) return { idx: i, elapsed: t - w.start };
  }
  return null;
}

function drawSubtitle(ctx, t) {
  px(ctx, SUB.x, SUB.y, SUB.w, SUB.h, C.subtitleBg);
  px(ctx, SUB.x, SUB.y, SUB.w, 1, 'rgba(255,255,255,0.12)');
  const sub = curSubtitle(t);
  if (!sub) return;
  const chars = Array.from(LINES[sub.idx]);
  const shown = Math.min(chars.length, Math.floor((sub.elapsed * 1000) / CHAR_MS) + 1);
  const visible = chars.slice(0, shown).join('');
  if (visible) txt(ctx, BW / 2, SUB.y + 12, visible, C.white, 14, 'center');
}

// --- D1 终端文字时序 (与点击音同步) ---
const SLEEP_TEXT = '# sleeping...';
const SLEEP_TYPE_START = 0.8;
const D3_WAKE_LINES = [
  { text: '# awake', color: C.green, y: 16, delay: 0.6 },
  { text: '> sleep cycle complete', color: C.dim, y: 42, delay: 1.6 },
  { text: '> 等待她的消息', color: C.purple, y: 68, delay: 2.6 },
];
const NOTE_APPEAR = 0.8; // D3 内相对秒

// ================= Scene D1: 睡眠 (0-10s) =================
function drawD1(ctx, t) {
  drawBackground(ctx, t);
  drawTerminal(ctx, 'clawd@dream:~$');

  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);

  // 星星闪烁 (随机固定位置小白点, 各自相位)
  for (const s of TERM_STARS) {
    const a = 0.25 + 0.75 * (0.5 + 0.5 * Math.sin(t * 2.4 + s.phase));
    px(ctx, s.x, s.y, 2, 2, `rgba(255,255,255,${a.toFixed(3)})`);
  }

  // `# sleeping...` 逐字出现 (10px 小字体)
  const chars = Array.from(SLEEP_TEXT);
  const typed = t >= SLEEP_TYPE_START
    ? Math.min(chars.length, Math.floor(((t - SLEEP_TYPE_START) * 1000) / CHAR_MS) + 1)
    : 0;
  if (typed > 0) {
    let dx = 14;
    txt(ctx, dx, 16, '#', C.green, 10);
    dx += measureTxt(ctx, '#', 10) + 1;
    const rest = chars.slice(1, typed).join('');
    if (rest) txt(ctx, dx, 16, rest, C.dim, 10);
  }
  ctx.restore();

  // 房间内: Clawd 安睡 (左侧) + Her 静立 (右侧)
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'sleep');
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'stand');

  // Zzz 睡眠气泡 (Clawd 右上方, 循环上浮 + 淡出)
  const zPhase = (t * 0.9) % 3;
  for (let i = 0; i < 3; i++) {
    const p = (zPhase + i) % 3;
    const zx = CLAWD_ROOM.x + 44 + i * 10;
    const zy = CLAWD_ROOM.y - 6 - p * 9;
    ctx.globalAlpha = 0.15 + clamp01(1 - p / 3) * 0.85;
    txt(ctx, zx, zy, 'z', C.purple2, 10, 'left');
    ctx.globalAlpha = 1;
  }

  drawSubtitle(ctx, t);
}

// ================= Scene D2: 梦境 — 两人走在路上 (10-20s) =================
function drawD2(ctx, t) {
  const st = t - 10;

  // 梦境天空: 深紫 → 紫 → 粉的三段渐变
  const sky = ctx.createLinearGradient(0, 0, 0, 210);
  sky.addColorStop(0, C.dreamSkyTop);
  sky.addColorStop(0.62, C.dreamSkyMid);
  sky.addColorStop(1, C.dreamSkyLow);
  px(ctx, 0, 0, BW, 210, sky);

  // 星星 + 弯月
  for (const s of DREAM_STARS) {
    const a = 0.3 + 0.7 * (0.5 + 0.5 * Math.sin(t * 2.2 + s.phase));
    px(ctx, s.x, s.y, 2, 2, `rgba(255,255,255,${a.toFixed(3)})`);
  }
  // 弯月 (逐像素月牙, 奶油色)
  MOON_ROWS.forEach(([rx, rw], ry) => {
    px(ctx, MOON.x + rx, MOON.y + ry, rw, 1, C.dreamMoon);
  });

  // 远山 + 地面
  ctx.fillStyle = C.mountain;
  ctx.beginPath();
  ctx.moveTo(0, 210);
  ctx.lineTo(120, 158);
  ctx.lineTo(240, 210);
  ctx.closePath();
  ctx.fill();
  ctx.beginPath();
  ctx.moveTo(380, 210);
  ctx.lineTo(520, 150);
  ctx.lineTo(640, 210);
  ctx.closePath();
  ctx.fill();
  px(ctx, 0, 210, BW, 110, C.dreamGround);

  // 透视路面 (梯形, 地平线收窄)
  ctx.fillStyle = C.dreamRoad;
  ctx.beginPath();
  ctx.moveTo(300, 210);
  ctx.lineTo(340, 210);
  ctx.lineTo(404, 320);
  ctx.lineTo(236, 320);
  ctx.closePath();
  ctx.fill();
  // 路缘
  ctx.strokeStyle = C.dreamRoadEdge;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(300, 210);
  ctx.lineTo(236, 320);
  ctx.moveTo(340, 210);
  ctx.lineTo(404, 320);
  ctx.stroke();

  // 中央虚线 (向镜头流动, 营造行进感)
  for (let i = 0; i < 5; i++) {
    const p = ((st * 0.14 + i * 0.2) % 1 + 1) % 1;
    const y = 210 + p * 104;
    const dw = 3 + p * 4;
    const dh = 4 + p * 6;
    ctx.fillStyle = `rgba(245,237,213,${(0.35 + p * 0.55).toFixed(3)})`;
    ctx.fillRect(Math.round(320 - dw / 2), Math.round(y), Math.round(dw), Math.round(dh));
  }

  // 漂浮的梦粒子 (两侧)
  for (const sp of DREAM_SPARKS) {
    const sx = sp.x + Math.round(Math.sin(t * 1.6 + sp.phase) * 10);
    const sy = sp.y0 - ((st * 14 + sp.phase * 40) % 150);
    const a = 0.35 + 0.5 * (0.5 + 0.5 * Math.sin(t * 3 + sp.phase));
    px(ctx, sx, sy, 3, 3, `rgba(255,215,160,${a.toFixed(3)})`);
    px(ctx, sx + 1, sy - 2, 1, 7, `rgba(255,215,160,${(a * 0.8).toFixed(3)})`);
    px(ctx, sx - 2, sy + 1, 7, 1, `rgba(255,215,160,${(a * 0.8).toFixed(3)})`);
  }

  // Clawd + Her 并肩行走 (脚部基线 ~292)
  drawClawd(ctx, CLAWD_DREAM.x, CLAWD_DREAM.y, t, 'walk');
  drawHer(ctx, HER_DREAM.x, HER_DREAM.y, t, 'walk');

  drawSubtitle(ctx, t);
}

// ================= Scene D3: 醒来 (20-30s) =================
function drawStickyNote(ctx, t) {
  const st = t - 20;
  const appear = easeOut((st - NOTE_APPEAR) / 0.8);
  if (appear <= 0) return;
  const cx = NOTE.x + NOTE.w / 2;
  const cy = NOTE.y + NOTE.h / 2;
  ctx.save();
  ctx.globalAlpha = appear;
  ctx.translate(cx, cy);
  ctx.rotate((NOTE.angleDeg * Math.PI) / 180);
  // 阴影 + 米色纸面
  px(ctx, -NOTE.w / 2 + 3, -NOTE.h / 2 + 3, NOTE.w, NOTE.h, 'rgba(0,0,0,0.12)');
  px(ctx, -NOTE.w / 2, -NOTE.h / 2, NOTE.w, NOTE.h, C.cardBg);
  ctx.strokeStyle = C.cardBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(-NOTE.w / 2, -NOTE.h / 2, NOTE.w, NOTE.h);
  // 红色图钉
  px(ctx, -4, -NOTE.h / 2 + 6, 8, 8, C.pinRed);
  px(ctx, -2, -NOTE.h / 2 + 7, 2, 2, C.pink);
  // 两行留言 (10px)
  txt(ctx, 0, -18, '刚才的梦，', C.cardTx, 10, 'center');
  txt(ctx, 0, 2, '有点暖。', C.cardTx, 10, 'center');
  ctx.restore();
}

function drawD3(ctx, t) {
  const st = t - 20;
  drawBackground(ctx, t);
  px(ctx, 0, 0, BW, BH, C.warmOverlay);
  drawTerminal(ctx, 'clawd@dream:~$');

  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);
  // 亮屏日志 (逐行出现)
  for (const line of D3_WAKE_LINES) {
    if (st >= line.delay) txt(ctx, 14, line.y, line.text, line.color, 10);
  }
  // 闪烁光标
  if (st >= D3_WAKE_LINES[2].delay + 0.4 && Math.floor(t * 2) % 2 === 0) {
    px(ctx, 14, 104, 7, 12, C.green);
  }
  ctx.restore();

  // 便签 (倾斜 -5°)
  drawStickyNote(ctx, t);

  // 房间内: Clawd 醒来 (左) + Her 挥手 (右)
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'happy');
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'wave');

  drawSubtitle(ctx, t);
}

// --- 场景切换: 10s / 20s 处各 0.5s 黑场过渡 (dip-to-black, 避免重影) ---
const SCENES = [
  { id: 'D1', start: 0, end: 10, draw: drawD1 },
  { id: 'D2', start: 10, end: 20, draw: drawD2 },
  { id: 'D3', start: 20, end: 30, draw: drawD3 },
];
const FADE = 0.25;

function renderScenes(ctx, t) {
  let blackAlpha = 0;
  if (t < 10) {
    drawD1(ctx, t);
    if (t >= 10 - FADE) blackAlpha = (t - (10 - FADE)) / FADE; // → 全黑
  } else if (t < 10 + FADE) {
    drawD2(ctx, t);
    blackAlpha = 1 - (t - 10) / FADE; // 全黑 → 正常
  } else if (t < 20) {
    drawD2(ctx, t);
    if (t >= 20 - FADE) blackAlpha = (t - (20 - FADE)) / FADE;
  } else if (t < 20 + FADE) {
    drawD3(ctx, t);
    blackAlpha = 1 - (t - 20) / FADE;
  } else {
    drawD3(ctx, t);
  }
  if (blackAlpha > 0) {
    px(ctx, 0, 0, BW, BH, `rgba(0,0,0,${blackAlpha.toFixed(3)})`);
  }
}

// --- 点击音时间戳 (字幕逐字 + 终端打字 + 场景切换 + 便签/亮屏事件) ---
function getClickTimestamps() {
  const clicks = [];
  // 1. 字幕逐字 (160ms/字)
  for (let li = 0; li < LINES.length; li++) {
    const chars = Array.from(LINES[li]);
    for (let ci = 0; ci < chars.length; ci++) {
      clicks.push(SUB_WINDOW[li].start + (ci * CHAR_MS) / 1000);
    }
  }
  // 2. D1 `# sleeping...` 逐字打字
  const sleepChars = Array.from(SLEEP_TEXT);
  for (let ci = 0; ci < sleepChars.length; ci++) {
    clicks.push(SLEEP_TYPE_START + (ci * CHAR_MS) / 1000);
  }
  // 3. 场景切换 (10s / 20s)
  clicks.push(10, 20);
  // 4. D3 亮屏三行 + 便签出现
  for (const line of D3_WAKE_LINES) clicks.push(20 + line.delay);
  clicks.push(20 + NOTE_APPEAR);

  const uniq = [];
  for (const c of clicks.sort((a, b) => a - b)) {
    if (!uniq.length || Math.abs(uniq[uniq.length - 1] - c) > 0.02) uniq.push(Number(c.toFixed(3)));
  }
  return uniq;
}

// --- Canvases & Frame Renderer ---
const baseCanvas = createCanvas(BW, BH);
const baseCtx = baseCanvas.getContext('2d');
const outCanvas = createCanvas(FW, FH);
const outCtx = outCanvas.getContext('2d');
outCtx.imageSmoothingEnabled = false;

function renderFrameToCanvas(n) {
  const t = n / FPS;
  baseCtx.clearRect(0, 0, BW, BH);
  renderScenes(baseCtx, t);

  // 片头/片尾黑场淡入淡出 (0.4s)
  const fadeDur = 0.4;
  let alpha = 1;
  if (t < fadeDur) alpha = t / fadeDur;
  else if (t > DURATION - fadeDur) alpha = (DURATION - t) / fadeDur;
  if (alpha < 1) {
    px(baseCtx, 0, 0, BW, BH, `rgba(0,0,0,${(1 - Math.max(0, alpha)).toFixed(3)})`);
  }

  outCtx.clearRect(0, 0, FW, FH);
  outCtx.imageSmoothingEnabled = false;
  outCtx.drawImage(baseCanvas, 0, 0, FW, FH);
  return { baseCanvas, outCanvas };
}

function renderAllFrames(outDir = OUT_DIR) {
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  console.log(`「Clawd 的梦境」: ${BW}×${BH} (SCALE=${SCALE}) → ${FW}×${FH} @ ${FPS}fps, ${NFRAMES} frames`);
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

if (require.main === module) {
  renderAllFrames();
}

module.exports = {
  BW, BH, SCALE, FW, FH, FPS, DURATION, NFRAMES, CHAR_MS,
  WIN, TERM, SUB, NOTE,
  CLAWD_ROOM, HER_ROOM, CLAWD_DREAM, HER_DREAM,
  TERM_STARS, DREAM_STARS, DREAM_SPARKS, MOON,
  LINES, SUB_WINDOW, SLEEP_TEXT, SLEEP_TYPE_START, D3_WAKE_LINES, NOTE_APPEAR,
  SCENES, FADE,
  C, FONT_FAMILY,
  px, txt, measureTxt,
  drawBackground, drawTerminal, drawClawd, drawHer, drawStickyNote,
  drawSubtitle, curSubtitle, getClickTimestamps,
  renderFrameToCanvas, renderAllFrames,
};
