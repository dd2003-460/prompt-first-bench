#!/usr/bin/env node
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

const { createCanvas, GlobalFonts } = require('@napi-rs/canvas');
const fs = require('fs');
const path = require('path');

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
  bgWarm: '#F5EDD5',
  stripe: '#EDE3C8',
  woodFrame: '#8B7355',
  woodSill: '#A08060',
  skyTop: '#87CEEB',
  skyBottom: '#E0F0FF',
  mountain: '#5A7A5A',
  mountainFar: '#6E8E6E',

  // Terminal (#0d1117 body per spec)
  termBg: '#0d1117',
  termTitle: '#1E222B',
  termBd: '#2A2E38',
  border: '#30363D',

  // Text & accents
  text: '#E6EDF3',
  dim: '#8B949E',
  green: '#7EE787',
  pink: '#FF9AA2',
  amber: '#E3B341',
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
  herHair: '#5A4632',
  herSkin: '#E8C39E',
  herDress: '#FF9AA2',
  herDressHem: '#E57A84',
  cardBg: '#FFF8DC',
  cardBd: '#DEB887',
  cardTx: '#241A06',
  cardSub: '#6E5A3A',
  pinRed: '#FF5555',
  subtitleBg: '#CDC6B4',
  subtitleTx: '#241A06',
};

// --- Reusable Pixel Primitives ---
function px(ctx, x, y, w, h, color) {
  ctx.fillStyle = color;
  ctx.fillRect(Math.round(x), Math.round(y), Math.round(w), Math.round(h));
}

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
  px(ctx, 0, 0, BW, BH, C.bgWarm);
  for (let x = 0; x < BW; x += 16) {
    px(ctx, x, 0, 8, BH, C.stripe);
  }

  // 2. 大窗户 (60,20 520×160, 木框 #8B7355 8px)
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

  // 晨空渐变 (#87CEEB → #E0F0FF)
  const grd = ctx.createLinearGradient(0, gy, 0, gy + gh);
  grd.addColorStop(0, C.skyTop);
  grd.addColorStop(1, C.skyBottom);
  ctx.fillStyle = grd;
  ctx.fillRect(gx, gy, gw, gh);

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
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
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
  const py0 = wy + wh;
  px(ctx, px0 + 2, py0 - 16, 10, 8, '#6AA86A');
  px(ctx, px0, py0 - 13, 14, 5, '#4E864E');
  px(ctx, px0 + 4, py0 - 19, 6, 3, '#7BC07B');
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

  ctx.strokeStyle = C.termBd;
  ctx.lineWidth = 2;
  ctx.strokeRect(x, y, w, h);

  // 窗口按钮 6×6
  px(ctx, x + 8, y + 7, 6, 6, C.red);
  px(ctx, x + 18, y + 7, 6, 6, C.amber);
  px(ctx, x + 28, y + 7, 6, 6, C.green);

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
  px(ctx, x + 4, by + 9, 8, 6, C.herDress);
  px(ctx, x + 2, by + 15, 12, 6, C.herDress);
  px(ctx, x + 2, by + 20, 12, 1, C.herDressHem);

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
    }
  }
  return null;
}

function drawSubtitle(ctx, t) {
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

  drawSubtitle(ctx, t);
}

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

  drawSubtitle(ctx, t);
}

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
      }
    }
  }

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

  drawSubtitle(ctx, t);
}

// ============ 场景 / 帧 ============
const SCENES = [
  { id: 'L1', start: 0, end: 10, draw: drawL1 },
  { id: 'L2', start: 10, end: 20, draw: drawL2 },
  { id: 'L3', start: 20, end: 30, draw: drawL3 },
];

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
const baseCanvas = createCanvas(BW, BH);
const baseCtx = baseCanvas.getContext('2d');
const outCanvas = createCanvas(FW, FH);
const outCtx = outCanvas.getContext('2d');
outCtx.imageSmoothingEnabled = false;

function renderFrameToCanvas(n) {
  const t = n / FPS;
  baseCtx.clearRect(0, 0, BW, BH);

  const scene = SCENES.find((s) => t >= s.start && t < s.end) || SCENES[SCENES.length - 1];
  scene.draw(baseCtx, t);

  const a = blackAlpha(t);
  if (a > 0) px(baseCtx, 0, 0, BW, BH, `rgba(0,0,0,${a.toFixed(3)})`);

  outCtx.clearRect(0, 0, FW, FH);
  outCtx.imageSmoothingEnabled = false;
  outCtx.drawImage(baseCanvas, 0, 0, FW, FH);
  return { baseCanvas, outCanvas };
}

function renderAllFrames(outDir = OUT_DIR) {
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
  console.log(`「Clawd 的学习」: ${BW}×${BH} (SCALE=${SCALE}) → ${FW}×${FH} @ ${FPS}fps, ${NFRAMES} frames`);
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

if (require.main === module) {
  renderAllFrames();
}

module.exports = {
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
};
