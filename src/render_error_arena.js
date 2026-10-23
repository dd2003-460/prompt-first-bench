#!/usr/bin/env node
// 「Clawd 的错误」30s 像素风视频渲染脚本 (error_arena v1.0)
// 画布规格: 640×360 基础分辨率, SCALE=2 → 1280×720 @ 60fps, 1800 帧 (30.00s)
// 美术风格: 严格对标 full_v1.3.4.mp4
//   暖色条纹房间 (#F5EDD5 + 竖条纹) + 晨窗远山云朵 + 小终端 (#14161C, DSH TUI) + 房间内像素角色
//
// 故事: Clawd 犯了一个错，删掉了重要文件。它试图修复，但发现有些东西回不来。
//
// 场景 (3 × 10s, 场景间 0.5s 黑场过渡):
//   E1 (0-10s)  删错了   — 终端逐字打 `$ rm -rf /important` → `> 确认删除 128 个文件？ [y/N]` → `> y`
//                         红色警告框弹出 WARNING: 删除了重要文件；终端边框闪红
//                         Clawd 在房间内：平静 → 惊恐 (颤抖)
//   E2 (10-20s) 试图修复 — `$ git restore /important` → `> 错误: 文件已被永久删除`
//                         `$ ls /important` → `> 目录为空`
//                         房间灯光变冷变暗；Clawd 颜色变暗（懊悔），内心独白字幕「有些东西回不来。」
//   E3 (20-30s) 安慰     — `$ her: 没关系，下次小心。` / `$ clawd: 谢谢你还在。`
//                         窗台便签「有些东西，删了就回不来。但你还在。」
//                         Her 在窗边轻轻点头；Clawd 颜色慢慢恢复；画面渐暗
//
// 字幕 (3 条, 逐字 160ms):
//   1. 「它犯了一个错。」   (2-8s)
//   2. 「有些东西回不来。」 (12-18s)
//   3. 「但你还在。」       (24-29s)

const { createCanvas, GlobalFonts } = require('@napi-rs/canvas');
const fs = require('fs');
const path = require('path');

// --- Register Fusion Pixel Fonts (10px 终端小字 + 14px 字幕) ---
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

// Typing & Subtitle Rhythms
const TYPE_CHAR_MS = 140; // 终端逐字打字 140ms/字 (与 sfx_click 严格同步)
const SUB_CHAR_MS = 160;  // 字幕逐字 160ms
const FADE = 0.25;        // 场景边界: 0.25s 淡出 + 0.25s 淡入 = 0.5s 黑场过渡

const OUT_DIR = process.env.FRAMES_DIR || '/tmp/frames_error';

// --- Layout Constants (640×360 base grid, strictly benchmarked to full_v1.3.4) ---
const WIN = { x: 60, y: 20, w: 520, h: 160, fw: 8 };
const SILL = { x: 56, y: 180, w: 528, h: 8 };
const TERM = { x: 140, y: 160, w: 360, h: 160, titleH: 20 };
const SUB = { x: 0, y: 320, w: 640, h: 40 };

// 终端内容区内的红色警告框 (local 坐标, 相对内容区左上角)
const WARN = { x: 12, y: 78, w: 336, h: 34 };

// 窗台便签 (E3): 坐在窗台上, 位于终端右侧, 与终端/角色 0 重叠
const NOTE = { x: 508, y: 96, w: 110, h: 82, angleDeg: -3 };

// 角色房间位置 (严格在房间内, 终端之外, 字幕栏 y=320 之上)
const CLAWD_ROOM = { x: 64, y: 248 };  // 40×24 → x 64..104, y 246..272
const HER_ROOM = { x: 560, y: 194 };   // 16×28 → x 560..576, y 193..222

// E3 暖色星光 (锚点位于开阔房间/窗面, 与便签/角色 0 重叠)
const SPARKLE_ANCHORS = [
  { x: 28, y: 108 },
  { x: 196, y: 52 },
  { x: 388, y: 52 },
  { x: 604, y: 258 },
];

// --- Palette (aligned with full_v1.3.4 + DSH TUI dark theme) ---
const C = {
  // 房间与晨窗
  bgWarm: '#F5EDD5',
  stripe: '#EDE3C8',
  woodFrame: '#8B7355',
  woodSill: '#A08060',
  skyTop: '#87CEEB',
  skyBottom: '#E0F0FF',
  mountain: '#5A7A5A',
  mountainHi: '#6A8B68',
  pot: '#7A5A3A',

  // DSH TUI 终端
  termBg: '#14161C',
  termTitle: '#21262D',
  termBd: '#30363D',
  panel: '#1A1F29',
  border: '#30363D',
  warnBg: '#2A0E12',
  warnBd: '#FF5A5A',

  // 语法 / UI 强调色
  text: '#E6EDF3',
  dim: '#8B949E',
  green: '#7EE787',
  pink: '#FF9AA2',
  amber: '#E3B341',
  blue: '#79C0FF',
  purple: '#BC8CFF',
  purple2: '#A371F7',
  red: '#FF7B72',
  pinRed: '#FF5555',
  white: '#FFFFFF',

  // Clawd: 正常暖珊瑚 → 懊悔暗灰紫
  clawdNorm: '#D97757',
  clawdNormDark: '#B85A3B',
  clawdNormBelly: '#F5E8D7',
  clawdRegret: '#4A4757',
  clawdRegretDark: '#33313E',
  clawdRegretBelly: '#8E8B9C',
  clawdEye: '#141413',

  // Her
  herHair: '#5A4632',
  herSkin: '#E8C39E',
  herDress: '#FF9AA2',
  herDressHem: '#E57A84',

  // 便签
  cardBg: '#FFF8DC',
  cardBd: '#DEB887',
  cardTx: '#241A06',
  cardSub: '#6E5A3A',
  pinRed: '#FF5555',

  subtitleBg: 'rgba(0,0,0,0.76)',
  subtitleAccent: 'rgba(255,140,120,0.85)',
  warmOverlay: 'rgba(255,205,110,0.08)',
  coldOverlay: 'rgba(30,36,64,0.16)',
  dangerGlow: 'rgba(255,60,60,0.16)',
};

// --- Narrative Text & Timing (DO NOT MUTATE AT RUNTIME) ---
const LINES = ['它犯了一个错。', '有些东西回不来。', '但你还在。'];
const SUB_WINDOW = [
  { start: 2.0, end: 8.0 },
  { start: 12.0, end: 18.0 },
  { start: 24.0, end: 29.0 },
];

// ---- E1 (0-10s): 删错了 ----
const E1_CMD = '$ rm -rf /important';
const E1_CMD_START = 0.7;                    // 19 chars × 0.14 = 2.66s → 3.36s
const E1_CMD_END = E1_CMD_START + (Array.from(E1_CMD).length * TYPE_CHAR_MS) / 1000;
const E1_CONFIRM = '> 确认删除 128 个文件？ [y/N]';
const E1_CONFIRM_AT = 3.7;
const E1_ANSWER = '> y';
const E1_ANSWER_AT = 4.9;
const E1_WARN_AT = 5.2;      // 红色警告框 + 终端闪红 + Clawd 惊恐
const E1_FOOTER = '[DSH] irreversible · 128 files gone';
const E1_FOOTER_AT = 6.3;
const E1_WARN_TITLE = 'WARNING: 删除了重要文件';
const E1_WARN_SUB = '128 files permanently deleted';
const E1_TITLE = 'clawd@dsh:~$ — rm -rf';

// ---- E2 (10-20s): 试图修复 ----
const E2_CMD = '$ git restore /important';
const E2_CMD_START = 0.6;
const E2_CMD_END = E2_CMD_START + (Array.from(E2_CMD).length * TYPE_CHAR_MS) / 1000;
const E2_ERR = '> 错误: 文件已被永久删除';
const E2_ERR_AT = E2_CMD_END + 0.3;
const E2_LS = '$ ls /important';
const E2_LS_AT = E2_ERR_AT + 1.3;
const E2_EMPTY = '> 目录为空';
const E2_EMPTY_AT = E2_LS_AT + 1.2;
const E2_FOOTER = '[DSH] nothing to restore · 0 files';
const E2_FOOTER_AT = E2_EMPTY_AT + 1.0;
const E2_DIM_START = 0.7;   // 房间灯逐渐变冷变暗 + Clawd 颜色变暗
const E2_DIM_END = 2.8;
const E2_TITLE = 'clawd@dsh:~$ — restore';

// ---- E3 (20-30s): 安慰 ----
const E3_LINES = [
  { prefix: '$ her: ', body: '没关系，下次小心。', prefixCol: C.pink, bodyCol: C.text, y: 16, at: 0.7 },
  { prefix: '$ clawd: ', body: '谢谢你还在。', prefixCol: C.green, bodyCol: C.purple, y: 46, at: 3.4 },
];
const E3_STATUS = '[DSH] connection: still here';
const E3_STATUS_AT = 5.8;
const E3_FOOTER = '# 有些东西回不来，但你还在。';
const E3_FOOTER_AT = 6.6;
const E3_NOTE_AT = 2.6;      // 便签落上窗台
const E3_RECOVER_START = 1.0;
const E3_RECOVER_END = 3.8;
const E3_TITLE = 'clawd@dsh:~$ — still here';
const NOTE_LINES = ['有些东西，', '删了就回不来。', '但你还在。'];
const NOTE_FULL_TEXT = NOTE_LINES.join('');

// --- Math & Color Helpers ---
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
  return `rgb(${Math.round(r1 + (r2 - r1) * k)},${Math.round(g1 + (g2 - g1) * k)},${Math.round(b1 + (b2 - b1) * k)})`;
}

// --- Pixel Primitives (threshold-based crisp text, identical to full_v1.3.4) ---
function px(ctx, x, y, w, h, color) {
  ctx.fillStyle = color;
  ctx.fillRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
}

let _tmpCanvas = null;
function txt(ctx, x, y, str, color, font = 10, align = 'left') {
  if (!str) return { x: Math.round(x), y: Math.round(y), w: 0, h: font };
  const fontSpec = `${font}px ${fontFamilyForSize(font)}`;
  ctx.font = fontSpec;

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
  for (let i = 3; i < d.length; i += 4) d[i] = d[i] > 115 ? 255 : 0;
  tctx.putImageData(img, 0, 0);

  let dx = x;
  if (align === 'center') dx = x - measuredW / 2 - 1;
  else if (align === 'right') dx = x - measuredW - 2;

  ctx.drawImage(_tmpCanvas, Math.round(dx), Math.round(y));
  return { x: Math.round(dx), y: Math.round(y), w: measuredW, h: font };
}

function measureTxt(ctx, str, font = 10) {
  if (!str) return 0;
  ctx.font = `${font}px ${fontFamilyForSize(font)}`;
  return Math.ceil(ctx.measureText(str).width);
}

// 逐字打字可见字数 (140ms/字)
function typedCount(startAt, t, total) {
  if (t < startAt) return 0;
  return Math.min(total, Math.floor(((t - startAt) * 1000) / TYPE_CHAR_MS) + 1);
}

// --- 可复用场景元素: 暖色条纹房间 + 晨窗远山 ---
// opts: { bloom, cold (0..1 冷光/暗化), redGlow (0..1 红色危机氛围) }
function drawBackground(ctx, t, opts = {}) {
  const cold = clamp01(opts.cold || 0);

  // 1. 暖色条纹壁纸 (#F5EDD5 + 每 16px 竖条纹)
  px(ctx, 0, 0, BW, BH, C.bgWarm);
  for (let x = 0; x < BW; x += 16) px(ctx, x, 0, 8, BH, C.stripe);

  // 2. 大窗户 (x=60, y=20, w=520, h=160)
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

  // 天空渐变 (#87CEEB → #E0F0FF)
  const grd = ctx.createLinearGradient(0, gy, 0, gy + gh);
  grd.addColorStop(0, C.skyTop);
  grd.addColorStop(1, C.skyBottom);
  ctx.fillStyle = grd;
  ctx.fillRect(gx, gy, gw, gh);

  // 晨光 (左上)
  const sunX = wx + 84;
  const sunY = wy + 40;
  const sunPulse = Math.sin(t * 1.6) > 0 ? 2 : 0;
  px(ctx, sunX - 16 - sunPulse, sunY - 16 - sunPulse, 32 + sunPulse * 2, 32 + sunPulse * 2, 'rgba(255,228,130,0.22)');
  px(ctx, sunX - 11, sunY - 11, 22, 22, 'rgba(255,224,110,0.45)');
  px(ctx, sunX - 7, sunY - 7, 14, 14, '#FFE478');

  // 远山
  ctx.fillStyle = C.mountain;
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

  // 远山高光 (冷光时更明显)
  ctx.fillStyle = C.mountainHi;
  ctx.beginPath();
  ctx.moveTo(wx + 332, wy + 50);
  ctx.lineTo(wx + 372, wy + 78);
  ctx.lineTo(wx + 300, wy + 78);
  ctx.closePath();
  ctx.fill();

  // 漂移像素云
  const cx1 = wx + 118 + Math.round(Math.sin(t * 0.32) * 12);
  px(ctx, cx1, wy + 38, 38, 9, 'rgba(255,255,255,0.92)');
  px(ctx, cx1 + 8, wy + 32, 22, 6, 'rgba(255,255,255,0.92)');

  const cx2 = wx + 334 + Math.round(Math.cos(t * 0.24) * 14);
  px(ctx, cx2, wy + 52, 46, 9, 'rgba(255,255,255,0.90)');
  px(ctx, cx2 + 10, wy + 46, 26, 6, 'rgba(255,255,255,0.90)');

  // 冷光: 窗面蒙上一层暮色 (E2 懊悔)
  if (cold > 0.01) px(ctx, gx, gy, gw, gh, `rgba(46,58,92,${(0.28 * cold).toFixed(3)})`);

  ctx.restore();

  // 十字窗棂
  px(ctx, wx + ww / 2 - 3, gy, 6, gh, C.woodFrame);
  px(ctx, gx, wy + wh / 2 - 3, gw, 6, C.woodFrame);

  // 窗台 (y=180..188)
  px(ctx, SILL.x, SILL.y, SILL.w, SILL.h, C.woodSill);
  px(ctx, SILL.x, SILL.y, SILL.w, 2, C.woodFrame);

  // 左窗台小盆栽
  const px0 = wx + 28;
  const py0 = wy + wh;
  px(ctx, px0 + 2, py0 - 16, 10, 8, '#6AA86A');
  px(ctx, px0, py0 - 13, 14, 5, '#4E864E');
  px(ctx, px0 + 4, py0 - 19, 6, 3, '#7BC07B');
  if (opts.bloom) px(ctx, px0 + 6, py0 - 21, 2, 2, C.pink);
  px(ctx, px0, py0 - 8, 14, 2, '#B06A46');
  px(ctx, px0 + 1, py0 - 6, 12, 6, C.pot);

  // 地板 (画面底部: 木色地板条, 与字幕栏自然衔接)
  px(ctx, 0, 300, BW, 20, '#C9A981');
  px(ctx, 0, 300, BW, 1, '#B08F68');
  for (let x = 0; x < BW; x += 64) px(ctx, x, 302, 1, 18, 'rgba(120,90,60,0.20)');
  px(ctx, 0, 318, BW, 2, '#B08F68');

  // 房间整体光照 (冷光变暗 / 暖光提亮)
  if (cold > 0.01) px(ctx, 0, 0, BW, BH, `rgba(24,28,52,${(0.22 * cold).toFixed(3)})`);
  if (opts.warm > 0.01) px(ctx, 0, 0, BW, BH, `rgba(255,205,110,${(0.10 * opts.warm).toFixed(3)})`);
}

// --- 可复用 UI 元素: DSH TUI 小终端 (360×160 @ 140,160) ---
// opts: { accent, redFlash (0..1) }
function drawTerminal(ctx, title, accentColor = C.green, opts = {}) {
  const { x, y, w, h, titleH } = TERM;
  const flash = clamp01(opts.redFlash || 0);
  const accent = flash > 0.02 ? lerpColor(accentColor, C.red, flash) : accentColor;

  // 阴影
  px(ctx, x + 4, y + 4, w, h, 'rgba(0,0,0,0.16)');
  // 深色 TUI 主体
  px(ctx, x, y, w, h, C.termBg);
  // 标题栏 + 顶部强调线
  px(ctx, x, y, w, titleH, C.termTitle);
  px(ctx, x, y + titleH - 1, w, 1, accent);
  // 边框 (危机时闪红)
  ctx.strokeStyle = flash > 0.02 ? lerpColor(C.termBd, C.red, flash) : C.termBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x, y, w, h);

  // 红闪: 内容区红色染色 + 外发光
  if (flash > 0.02) {
    px(ctx, x + 2, y + titleH + 1, w - 4, h - titleH - 3, `rgba(255,40,40,${(0.10 * flash).toFixed(3)})`);
    px(ctx, x - 2, y - 2, w + 4, 2, `rgba(255,60,60,${(0.45 * flash).toFixed(3)})`);
    px(ctx, x - 2, y - 2, 2, h + 4, `rgba(255,60,60,${(0.45 * flash).toFixed(3)})`);
    px(ctx, x + w, y - 2, 2, h + 4, `rgba(255,60,60,${(0.45 * flash).toFixed(3)})`);
  }

  // 窗口按钮 (6×6)
  px(ctx, x + 8, y + 7, 6, 6, C.red);
  px(ctx, x + 18, y + 7, 6, 6, C.amber);
  px(ctx, x + 28, y + 7, 6, 6, C.green);

  // 10px Fusion Pixel 标题
  txt(ctx, x + w / 2, y + 5, title, C.dim, 10, 'center');

  // CRT 扫描线
  for (let sy = y + titleH + 2; sy < y + h - 2; sy += 3) {
    px(ctx, x + 2, sy, w - 4, 1, 'rgba(255,255,255,0.025)');
  }
}

// --- 可复用角色: Clawd (40×24, 房间内) ---
// mood: 'calm' | 'scared' | 'sad' | 'smile'
// regretMix: 0 (暖珊瑚 #D97757) .. 1 (懊悔暗灰紫 #4A4757)
function drawClawd(ctx, x, y, t, mood = 'calm', regretMix = 0) {
  const k = clamp01(regretMix);
  const shake = mood === 'scared' ? Math.round(Math.sin(t * 26) * 1.4) : 0;
  const bob = mood === 'scared' ? 0 : (Math.sin(t * 2.2) > 0.45 ? -1 : 0);
  const droop = mood === 'sad' ? 1 : 0;
  const bx = Math.round(x + shake);
  const by = Math.round(y + bob + droop * 2);
  const bodyH = 17;

  const bodyCol = lerpColor(C.clawdNorm, C.clawdRegret, k);
  const darkCol = lerpColor(C.clawdNormDark, C.clawdRegretDark, k);
  const bellyCol = lerpColor(C.clawdNormBelly, C.clawdRegretBelly, k);

  // 身体 (40×17) + 顶部阴影条
  px(ctx, bx, by, 40, bodyH, bodyCol);
  px(ctx, bx, by, 40, 2, darkCol);
  // 肚皮高光 (惊恐/懊悔时省略, 让表情更干净)
  if (mood !== 'scared' && mood !== 'sad') px(ctx, bx + 9, by + 11, 22, 4, bellyCol);

  const blink = (mood === 'calm' || mood === 'smile') && (t % 3.4) < 0.14;

  if (mood === 'scared') {
    // 惊恐: 睁大的眼 + 收缩瞳孔 + 上扬眉 + 张开的方嘴 + 冷汗
    px(ctx, bx + 9, by + 5, 7, 6, C.white);
    px(ctx, bx + 24, by + 5, 7, 6, C.white);
    px(ctx, bx + 11, by + 6, 3, 3, C.clawdEye);
    px(ctx, bx + 26, by + 6, 3, 3, C.clawdEye);
    px(ctx, bx + 11, by + 6, 1, 1, C.white);
    px(ctx, bx + 26, by + 6, 1, 1, C.white);
    // 上扬的眉线 (惊吓)
    px(ctx, bx + 9, by + 3, 5, 1, darkCol);
    px(ctx, bx + 26, by + 3, 5, 1, darkCol);
    // 张开的嘴 (深色, 内里偏红)
    px(ctx, bx + 16, by + 12, 8, 5, C.clawdEye);
    px(ctx, bx + 18, by + 14, 4, 2, '#8A4148');
    // 冷汗 (两滴, 缓慢下滑)
    const dy = Math.round((t * 6) % 4);
    px(ctx, bx + 37, by + 3 + dy, 2, 3, C.blue);
    px(ctx, bx + 2, by + 5 + ((dy + 2) % 4), 2, 3, C.blue);
  } else if (mood === 'sad') {
    // 懊悔: 低垂的眼 (瞳孔向下) + 下垂眉 + 下弯的嘴 + 泪光
    px(ctx, bx + 9, by + 6, 6, 4, '#C9C7D4');
    px(ctx, bx + 25, by + 6, 6, 4, '#C9C7D4');
    px(ctx, bx + 10, by + 8, 3, 2, C.clawdEye);
    px(ctx, bx + 26, by + 8, 3, 2, C.clawdEye);
    px(ctx, bx + 9, by + 5, 6, 1, darkCol);
    px(ctx, bx + 25, by + 5, 6, 1, darkCol);
    // 下弯的嘴 (∩ 形): 中间高, 两端低
    px(ctx, bx + 17, by + 12, 6, 1, C.clawdEye);
    px(ctx, bx + 16, by + 13, 1, 1, C.clawdEye);
    px(ctx, bx + 23, by + 13, 1, 1, C.clawdEye);
    // 泪光 (缓慢滴落)
    const tearDy = Math.round((t * 3) % 6);
    px(ctx, bx + 11, by + 10 + tearDy, 1, 2, 'rgba(170,205,255,0.9)');
  } else if (mood === 'smile') {
    // 安心: 弯眼 (^ ^) + 微笑 + 暖色脸颊
    px(ctx, bx + 9, by + 6, 2, 1, C.clawdEye);
    px(ctx, bx + 11, by + 5, 2, 1, C.clawdEye);
    px(ctx, bx + 13, by + 6, 2, 1, C.clawdEye);

    px(ctx, bx + 25, by + 6, 2, 1, C.clawdEye);
    px(ctx, bx + 27, by + 5, 2, 1, C.clawdEye);
    px(ctx, bx + 29, by + 6, 2, 1, C.clawdEye);

    px(ctx, bx + 16, by + 12, 2, 1, C.clawdEye);
    px(ctx, bx + 18, by + 13, 4, 1, C.clawdEye);
    px(ctx, bx + 22, by + 12, 2, 1, C.clawdEye);
    px(ctx, bx + 6, by + 8, 3, 2, C.pink);
    px(ctx, bx + 31, by + 8, 3, 2, C.pink);
  } else if (blink) {
    px(ctx, bx + 10, by + 8, 4, 1, C.clawdEye);
    px(ctx, bx + 26, by + 8, 4, 1, C.clawdEye);
  } else {
    // 平静 (默认)
    px(ctx, bx + 10, by + 6, 4, 4, C.clawdEye);
    px(ctx, bx + 26, by + 6, 4, 4, C.clawdEye);
    px(ctx, bx + 11, by + 7, 1, 1, C.white);
    px(ctx, bx + 27, by + 7, 1, 1, C.white);
  }

  // 4 条标志性像素腿 (总高 24px)
  const step = mood === 'smile' ? 0 : (Math.sin(t * 3.0) > 0.6 ? 1 : 0);
  px(ctx, bx + 3, by + bodyH, 6, 7 - step, darkCol);
  px(ctx, bx + 13, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 21, by + bodyH, 6, 7, darkCol);
  px(ctx, bx + 31, by + bodyH, 6, 7 - step, darkCol);
}

// --- 可复用角色: Her (16×28, 窗边) ---
// pose: 'stand' | 'nod' | 'smile'
function drawHer(ctx, x, y, t, pose = 'stand') {
  let bob = Math.sin(t * 1.8 + 0.8) > 0.45 ? -1 : 0;
  if (pose === 'nod') {
    // 轻轻点头: 2.2s 周期, 头/上身下移 1-2px
    const ph = (t % 2.2) / 2.2;
    bob += ph < 0.35 ? Math.round(Math.sin((ph / 0.35) * Math.PI) * 2) : 0;
  }
  const by = Math.round(y + bob);

  // 头发 & 脸
  px(ctx, x + 3, by, 10, 3, C.herHair);
  px(ctx, x + 10, by + 2, 4, 6, C.herHair);
  px(ctx, x + 3, by + 3, 8, 6, C.herSkin);

  if (pose === 'smile' || pose === 'nod') {
    px(ctx, x + 5, by + 5, 2, 1, C.cardTx);   // 笑眼
    px(ctx, x + 8, by + 6, 2, 1, C.herDressHem);
    px(ctx, x + 5, by + 7, 3, 1, '#C45A65');  // 微笑
  } else {
    px(ctx, x + 5, by + 5, 1, 2, C.cardTx);
  }

  // 粉色连衣裙
  px(ctx, x + 4, by + 9, 8, 6, C.herDress);
  px(ctx, x + 2, by + 15, 12, 6, C.herDress);
  px(ctx, x + 2, by + 20, 12, 1, C.herDressHem);

  // 手臂 (点头时轻轻放下)
  if (pose === 'nod') {
    px(ctx, x + 2, by + 11, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 11, 2, 4, C.herSkin);
  } else if (pose === 'smile') {
    const waveDy = Math.sin(t * 4.2) > 0 ? -2 : 0;
    px(ctx, x + 1, by + 8 + waveDy, 3, 2, C.herSkin);
    px(ctx, x + 2, by + 10 + waveDy, 2, 3, C.herDress);
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  } else {
    px(ctx, x + 2, by + 10, 2, 4, C.herSkin);
    px(ctx, x + 12, by + 10, 2, 4, C.herSkin);
  }

  // 腿 & 鞋
  px(ctx, x + 5, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 9, by + 21, 2, 5, C.herSkin);
  px(ctx, x + 4, by + 26, 3, 2, C.herHair);
  px(ctx, x + 9, by + 26, 3, 2, C.herHair);
}

// --- E1 红色警告框 (终端内容区内, 带脉冲闪烁) ---
function drawWarningPanel(ctx, appear, t) {
  if (appear <= 0) return;
  const { x, y, w, h } = WARN;
  const pulse = 0.62 + 0.38 * (0.5 + 0.5 * Math.sin(t * 9.0));

  ctx.save();
  ctx.globalAlpha = clamp01(appear);
  px(ctx, x + 2, y + 2, w, h, 'rgba(0,0,0,0.28)');
  px(ctx, x, y, w, h, C.warnBg);
  ctx.strokeStyle = `rgba(255,90,90,${pulse.toFixed(3)})`;
  ctx.lineWidth = 2;
  ctx.strokeRect(x + 1, y + 1, w - 2, h - 2);

  // 左侧警示三角形图标 (14×14, 像素阶梯边)
  const ix = x + 8;
  const iy = y + 10;
  px(ctx, ix + 5, iy, 4, 2, C.red);
  px(ctx, ix + 4, iy + 2, 6, 2, C.red);
  px(ctx, ix + 3, iy + 4, 8, 2, C.red);
  px(ctx, ix + 2, iy + 6, 10, 2, C.red);
  px(ctx, ix + 1, iy + 8, 12, 2, C.red);
  px(ctx, ix, iy + 10, 14, 2, C.red);
  px(ctx, ix + 6, iy + 3, 2, 5, C.warnBg);   // 感叹号竖笔
  px(ctx, ix + 6, iy + 9, 2, 2, C.warnBg);   // 感叹号点

  // 警告文字
  txt(ctx, x + 30, y + 5, E1_WARN_TITLE, C.red, 10);
  txt(ctx, x + 30, y + 17, E1_WARN_SUB, 'rgba(255,140,140,0.9)', 10);
  ctx.restore();
}

// --- E3 窗台便签 ---
function drawStickyNote(ctx, st) {
  const appear = easeOut((st - E3_NOTE_AT) / 0.7);
  if (appear <= 0) return;
  const cx = Math.round(NOTE.x + NOTE.w / 2);
  const cy = Math.round(NOTE.y + NOTE.h / 2);

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

  // 图钉 + 三行文字 (整数网格, 无旋转模糊)
  ctx.save();
  ctx.globalAlpha = appear;
  px(ctx, cx - 4, NOTE.y + 6, 8, 8, C.pinRed);
  px(ctx, cx - 2, NOTE.y + 7, 2, 2, C.pink);
  for (let i = 0; i < NOTE_LINES.length; i++) {
    txt(ctx, cx, NOTE.y + 20 + i * 18, NOTE_LINES[i], C.cardTx, 10, 'center');
  }
  ctx.restore();
}

// --- E3 暖色星光 ---
function drawSparkles(ctx, t, alpha = 1) {
  for (let i = 0; i < SPARKLE_ANCHORS.length; i++) {
    const a = SPARKLE_ANCHORS[i];
    const sx = Math.round(a.x + Math.sin(t * 2.0 + i * 1.4) * 6);
    const sy = Math.round(a.y + Math.cos(t * 1.6 + i * 1.9) * 8);
    const al = (0.35 + 0.50 * (0.5 + 0.5 * Math.sin(t * 3.1 + i * 1.2))) * clamp01(alpha);
    const col = `rgba(255,215,90,${al.toFixed(3)})`;
    px(ctx, sx, sy, 3, 3, col);
    px(ctx, sx + 1, sy - 2, 1, 7, col);
    px(ctx, sx - 2, sy + 1, 7, 1, col);
  }
}

// --- 底部字幕栏 (y=320, h=40, 14px, 160ms/字) ---
function curSubtitle(t) {
  for (let i = 0; i < LINES.length; i++) {
    const w = SUB_WINDOW[i];
    if (t >= w.start && t < w.end) return { idx: i, elapsed: t - w.start };
  }
  return null;
}

function drawSubtitle(ctx, t) {
  px(ctx, SUB.x, SUB.y, SUB.w, SUB.h, C.subtitleBg);
  px(ctx, SUB.x, SUB.y, SUB.w, 1, 'rgba(255,255,255,0.14)');
  // E1/E2 情绪: 字幕栏顶部细红线 (危机 → 懊悔时变淡)
  const accentA = t < 10 ? 0.85 : t < 20 ? 0.45 : 0.25;
  px(ctx, SUB.x, SUB.y + 1, SUB.w, 1, `rgba(255,120,110,${accentA})`);

  const sub = curSubtitle(t);
  if (!sub) return;
  const chars = Array.from(LINES[sub.idx]);
  const shown = Math.min(chars.length, Math.floor((sub.elapsed * 1000) / SUB_CHAR_MS) + 1);
  const visible = chars.slice(0, shown).join('');
  if (visible) txt(ctx, BW / 2, SUB.y + 12, visible, C.white, 14, 'center');
}

// ================= E1 (0-10s): 删错了 =================
function drawE1(ctx, t) {
  // 红色危机氛围: 警告后脉冲, 并在 y 按下瞬间硬闪两下
  const warnOn = t >= E1_WARN_AT;
  const flashEnv = warnOn ? clamp01((t - E1_WARN_AT) / 0.18) : 0;
  const hardFlash = warnOn && t < E1_WARN_AT + 0.5 ? (Math.floor((t - E1_WARN_AT) * 8) % 2 === 0 ? 1 : 0.35) : 1;
  const pulse = warnOn ? (0.45 + 0.55 * (0.5 + 0.5 * Math.sin(t * 9.0))) * hardFlash : 0;
  const redLevel = flashEnv * pulse;

  drawBackground(ctx, t, { bloom: false });

  // 房间红色危机光晕 (脉冲)
  if (redLevel > 0.01) {
    px(ctx, 0, 0, BW, 300, `rgba(255,50,50,${(0.09 * redLevel).toFixed(3)})`);
    px(ctx, 0, 0, BW, 3, `rgba(255,60,60,${(0.22 * redLevel).toFixed(3)})`);
    px(ctx, 0, 297, BW, 3, `rgba(255,60,60,${(0.22 * redLevel).toFixed(3)})`);
  }

  drawTerminal(ctx, E1_TITLE, C.red, { redFlash: redLevel });

  // --- 终端内容 ---
  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);
  const cursorOn = Math.floor(t * 2.5) % 2 === 0;

  // 1) `$ rm -rf /important` 逐字 140ms
  const cmdChars = Array.from(E1_CMD);
  const n1 = typedCount(E1_CMD_START, t, cmdChars.length);
  const prompt = '$ ';
  const promptW = measureTxt(ctx, prompt, 10);
  if (n1 > 0) {
    const visible = cmdChars.slice(0, n1).join('');
    const isCmd = visible.startsWith('$ ');
    txt(ctx, 14, 14, isCmd ? prompt : '', C.green, 10);
    const bodyStr = isCmd ? visible.slice(2) : visible;
    if (bodyStr) txt(ctx, 14 + promptW, 14, bodyStr, C.text, 10);
    if (t < E1_ANSWER_AT && cursorOn) {
      px(ctx, 14 + measureTxt(ctx, visible, 10) + 2, 14, 6, 10, C.text);
    }
  } else if (cursorOn) {
    px(ctx, 14, 14, 6, 10, C.text);
  }

  // 2) 确认提示
  if (t >= E1_CONFIRM_AT) {
    txt(ctx, 14, 36, '> ', C.amber, 10);
    txt(ctx, 14 + measureTxt(ctx, '> ', 10), 36, E1_CONFIRM.slice(2), C.amber, 10);
  }

  // 3) `> y`
  if (t >= E1_ANSWER_AT) {
    const charOn = Math.floor((t - E1_ANSWER_AT) * 4) % 2 === 0;
    txt(ctx, 14, 58, '> ', C.amber, 10);
    txt(ctx, 14 + measureTxt(ctx, '> ', 10), 58, 'y', C.red, 10);
    if (charOn && t < E1_WARN_AT) px(ctx, 14 + measureTxt(ctx, '> y', 10) + 2, 58, 6, 10, C.red);
  }

  // 4) 红色警告框
  drawWarningPanel(ctx, easeOut((t - E1_WARN_AT) / 0.3), t);

  // 5) 底部状态行
  if (t >= E1_FOOTER_AT) {
    txt(ctx, 14, 118, E1_FOOTER, C.dim, 10);
  }
  ctx.restore();

  // --- 房间内角色 ---
  // 平静 → 惊恐 (y 按下后 0.3s 内切换, 带一下抽搐)
  const scared = t >= E1_WARN_AT - 0.15;
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, scared ? 'scared' : 'calm', 0);
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'stand');

  // 惊恐时 Her 头顶冒出小小的问号 (窗边, 房间内)
  if (scared) {
    const qb = Math.sin(t * 3.0) > 0 ? 0 : 1;
    const qx = HER_ROOM.x + 2;
    const qy = HER_ROOM.y - 14 - qb;
    px(ctx, qx + 2, qy, 4, 1, C.dim);
    px(ctx, qx + 5, qy + 1, 1, 3, C.dim);
    px(ctx, qx + 3, qy + 4, 2, 2, C.dim);
    px(ctx, qx + 3, qy + 7, 2, 2, C.dim);
  }

  drawSubtitle(ctx, t);
}

// ================= E2 (10-20s): 试图修复 =================
function drawE2(ctx, t) {
  const st = t - 10;
  const cold = easeInOut((st - E2_DIM_START) / (E2_DIM_END - E2_DIM_START));

  drawBackground(ctx, t, { bloom: false, cold });
  drawTerminal(ctx, E2_TITLE, C.amber, { redFlash: 0 });

  // --- 终端内容 ---
  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);
  const cursorOn = Math.floor(t * 2.5) % 2 === 0;

  // 1) `$ git restore /important` 逐字 140ms
  const cmdChars = Array.from(E2_CMD);
  const n1 = typedCount(E2_CMD_START, st, cmdChars.length);
  if (n1 > 0) {
    const visible = cmdChars.slice(0, n1).join('');
    txt(ctx, 14, 12, '$ ', C.green, 10);
    const bodyStr = visible.slice(2);
    if (bodyStr) txt(ctx, 14 + measureTxt(ctx, '$ ', 10), 12, bodyStr, C.text, 10);
    if (st < E2_LS_AT && cursorOn) {
      px(ctx, 14 + measureTxt(ctx, visible, 10) + 2, 12, 6, 10, C.text);
    }
  } else if (cursorOn) {
    px(ctx, 14, 12, 6, 10, C.text);
  }

  // 2) 错误行
  if (st >= E2_ERR_AT) {
    txt(ctx, 14, 34, '> ', C.red, 10);
    txt(ctx, 14 + measureTxt(ctx, '> ', 10), 34, E2_ERR.slice(2), C.red, 10);
  }

  // 3) `$ ls /important`
  if (st >= E2_LS_AT) {
    txt(ctx, 14, 56, '$ ', C.green, 10);
    const body = E2_LS.slice(2);
    const shown = Math.min(body.length, Math.floor(((st - E2_LS_AT) * 1000) / TYPE_CHAR_MS) + 1);
    const visible = body.slice(0, shown);
    if (visible) txt(ctx, 14 + measureTxt(ctx, '$ ', 10), 56, visible, C.text, 10);
    if (cursorOn && st < E2_EMPTY_AT) {
      px(ctx, 14 + measureTxt(ctx, `$ ${visible}`, 10) + 2, 56, 6, 10, C.text);
    }
  }

  // 4) `> 目录为空`
  if (st >= E2_EMPTY_AT) {
    txt(ctx, 14, 78, '> ', C.red, 10);
    txt(ctx, 14 + measureTxt(ctx, '> ', 10), 78, E2_EMPTY.slice(2), C.dim, 10);
  }

  // 5) 底部状态行
  if (st >= E2_FOOTER_AT) {
    txt(ctx, 14, 118, E2_FOOTER, C.dim, 10);
    // 状态行前的红色小方块 (空目录提示)
    px(ctx, 14 + measureTxt(ctx, E2_FOOTER, 10) + 6, 121, 4, 4, C.red);
  }
  ctx.restore();

  // --- 房间内角色: Clawd 颜色变暗 (懊悔), Her 站着看向它 ---
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, 'sad', cold);
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, 'stand');

  drawSubtitle(ctx, t);
}

// ================= E3 (20-30s): 安慰 =================
function drawE3(ctx, t) {
  const st = t - 20;
  const recover = 1 - easeInOut((st - E3_RECOVER_START) / (E3_RECOVER_END - E3_RECOVER_START));

  drawBackground(ctx, t, { bloom: true, warm: 1 - recover * 0.6 });
  drawTerminal(ctx, E3_TITLE, C.green, { redFlash: 0 });

  // --- 终端内容: 两行对话逐字 ---
  ctx.save();
  ctx.translate(TERM.x, TERM.y + TERM.titleH);
  const cursorOn = Math.floor(t * 2.5) % 2 === 0;
  for (const d of E3_LINES) {
    if (st < d.at) continue;
    const chars = Array.from(d.body);
    const shown = Math.min(chars.length, Math.floor(((st - d.at) * 1000) / TYPE_CHAR_MS) + 1);
    const visible = chars.slice(0, shown).join('');
    txt(ctx, 14, d.y, d.prefix, d.prefixCol, 10);
    const pw = measureTxt(ctx, d.prefix, 10);
    if (visible) txt(ctx, 14 + pw, d.y, visible, d.bodyCol, 10);
    // 正在打字的行尾光标
    if (shown < chars.length && cursorOn) {
      px(ctx, 14 + pw + measureTxt(ctx, visible, 10) + 2, d.y, 6, 10, C.purple);
    }
  }

  if (st >= E3_STATUS_AT) {
    txt(ctx, 14, 86, E3_STATUS, C.green, 10);
    if (cursorOn) px(ctx, 14 + measureTxt(ctx, E3_STATUS, 10) + 4, 86, 6, 10, C.green);
  }
  if (st >= E3_FOOTER_AT) {
    txt(ctx, 14, 112, E3_FOOTER, C.dim, 10);
  }
  ctx.restore();

  // 窗台便签
  drawStickyNote(ctx, st);

  // Clawd 颜色慢慢恢复 + 微笑; Her 在窗边轻轻点头
  drawClawd(ctx, CLAWD_ROOM.x, CLAWD_ROOM.y, t, st >= 3.4 ? 'smile' : 'sad', recover);
  drawHer(ctx, HER_ROOM.x, HER_ROOM.y, t, st >= 1.4 && st < 6.2 ? 'nod' : 'stand');

  // 安抚的暖色星光
  drawSparkles(ctx, t, easeOut((st - 4.2) / 1.2));

  drawSubtitle(ctx, t);
}

// --- 场景调度 + 0.5s 黑场过渡 (10s / 20s) ---
const SCENES = [
  { id: 'E1', start: 0, end: 10, draw: drawE1 },
  { id: 'E2', start: 10, end: 20, draw: drawE2 },
  { id: 'E3', start: 20, end: 30, draw: drawE3 },
];

function renderScenes(ctx, t) {
  let blackAlpha = 0;
  if (t < 10) {
    drawE1(ctx, t);
    if (t >= 10 - FADE) blackAlpha = (t - (10 - FADE)) / FADE;
  } else if (t < 10 + FADE) {
    drawE2(ctx, t);
    blackAlpha = 1 - (t - 10) / FADE;
  } else if (t < 20) {
    drawE2(ctx, t);
    if (t >= 20 - FADE) blackAlpha = (t - (20 - FADE)) / FADE;
  } else if (t < 20 + FADE) {
    drawE3(ctx, t);
    blackAlpha = 1 - (t - 20) / FADE;
  } else {
    drawE3(ctx, t);
  }
  if (blackAlpha > 0) {
    px(ctx, 0, 0, BW, BH, `rgba(0,0,0,${clamp01(blackAlpha).toFixed(3)})`);
  }
}

// --- 键盘点击 / 事件时间戳 (与画面严格同步, 供音频脚本使用) ---
function getClickTimestamps() {
  const clicks = [];

  // 1. 终端逐字打字 (140ms/字)
  for (let i = 0; i < Array.from(E1_CMD).length; i++) {
    clicks.push(E1_CMD_START + (i * TYPE_CHAR_MS) / 1000);
  }
  for (let i = 0; i < Array.from(E2_CMD).length; i++) {
    clicks.push(10 + E2_CMD_START + (i * TYPE_CHAR_MS) / 1000);
  }
  for (let i = 0; i < Array.from(E2_LS).length; i++) {
    clicks.push(10 + E2_LS_AT + (i * TYPE_CHAR_MS) / 1000);
  }
  for (const d of E3_LINES) {
    for (let i = 0; i < Array.from(d.body).length; i++) {
      clicks.push(20 + d.at + (i * TYPE_CHAR_MS) / 1000);
    }
  }

  // 2. 事件点击: 确认提示 / y / 警告框 / 状态行 / 便签 / 恢复 / 点头
  clicks.push(
    E1_CONFIRM_AT,
    E1_ANSWER_AT,
    E1_WARN_AT,
    E1_FOOTER_AT,
    10 + E2_ERR_AT,
    10 + E2_LS_AT,
    10 + E2_EMPTY_AT,
    10 + E2_FOOTER_AT,
    20 + E3_NOTE_AT,
    20 + E3_STATUS_AT,
    20 + E3_FOOTER_AT,
    20 + E3_RECOVER_END,
    20 + 1.4
  );

  // 3. 字幕逐字 (160ms) — 与打字音效去重 (间隔 < 90ms 的丢弃)
  const merged = clicks.slice().sort((a, b) => a - b);
  const subtitleClicks = [];
  for (let li = 0; li < LINES.length; li++) {
    const chars = Array.from(LINES[li]);
    for (let ci = 0; ci < chars.length; ci++) {
      subtitleClicks.push(SUB_WINDOW[li].start + (ci * SUB_CHAR_MS) / 1000);
    }
  }
  for (const sc of subtitleClicks) {
    if (merged.every((c) => Math.abs(c - sc) >= 0.09)) merged.push(sc);
  }

  // 4. 去重 (间隔 < 35ms, sfx_click 30ms → 保证零叠加削波)
  const uniq = [];
  for (const c of merged.sort((a, b) => a - b)) {
    if (c < 0 || c >= DURATION - 0.05) continue;
    if (!uniq.length || c - uniq[uniq.length - 1] >= 0.035) {
      uniq.push(Number(c.toFixed(3)));
    }
  }
  return uniq;
}

// --- 画布复用 & 帧渲染 ---
const baseCanvas = createCanvas(BW, BH);
const baseCtx = baseCanvas.getContext('2d');
const outCanvas = createCanvas(FW, FH);
const outCtx = outCanvas.getContext('2d');
outCtx.imageSmoothingEnabled = false;

function renderFrameToCanvas(n) {
  const t = n / FPS;
  baseCtx.clearRect(0, 0, BW, BH);
  renderScenes(baseCtx, t);

  // 片头 0.4s 淡入 / 片尾 0.5s 渐暗
  const fadeIn = 0.4;
  const fadeOut = 0.5;
  let alpha = 1;
  if (t < fadeIn) alpha = t / fadeIn;
  else if (t > DURATION - fadeOut) alpha = (DURATION - t) / fadeOut;
  if (alpha < 1) {
    px(baseCtx, 0, 0, BW, BH, `rgba(0,0,0,${(1 - clamp01(alpha)).toFixed(3)})`);
  }

  outCtx.clearRect(0, 0, FW, FH);
  outCtx.imageSmoothingEnabled = false;
  outCtx.drawImage(baseCanvas, 0, 0, FW, FH);
  return { baseCanvas, outCanvas };
}

function renderAllFrames(outDir = OUT_DIR) {
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  console.log(`「Clawd 的错误」: ${BW}×${BH} (SCALE=${SCALE}) → ${FW}×${FH} @ ${FPS}fps, ${NFRAMES} frames`);
  console.log(`Fonts: FONT_10="${FONT_10}" | FONT_14="${FONT_14}"`);
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
  BW, BH, SCALE, FW, FH, FPS, DURATION, NFRAMES,
  TYPE_CHAR_MS, SUB_CHAR_MS, FADE,
  WIN, SILL, TERM, SUB, WARN, NOTE, CLAWD_ROOM, HER_ROOM, SPARKLE_ANCHORS,
  C, LINES, SUB_WINDOW,
  E1_CMD, E1_CMD_START, E1_CMD_END, E1_CONFIRM, E1_CONFIRM_AT, E1_ANSWER, E1_ANSWER_AT,
  E1_WARN_AT, E1_FOOTER, E1_FOOTER_AT, E1_WARN_TITLE, E1_WARN_SUB, E1_TITLE,
  E2_CMD, E2_CMD_START, E2_CMD_END, E2_ERR, E2_ERR_AT, E2_LS, E2_LS_AT, E2_EMPTY,
  E2_EMPTY_AT, E2_FOOTER, E2_FOOTER_AT, E2_DIM_START, E2_DIM_END, E2_TITLE,
  E3_LINES, E3_STATUS, E3_STATUS_AT, E3_FOOTER, E3_FOOTER_AT, E3_NOTE_AT,
  E3_RECOVER_START, E3_RECOVER_END, E3_TITLE,
  NOTE_LINES, NOTE_FULL_TEXT,
  SCENES,
  px, txt, measureTxt, typedCount, lerpColor, clamp01, easeOut, easeInOut,
  drawBackground, drawTerminal, drawClawd, drawHer, drawWarningPanel, drawStickyNote,
  drawSparkles, drawSubtitle, curSubtitle,
  renderScenes, getClickTimestamps, renderFrameToCanvas, renderAllFrames,
};
