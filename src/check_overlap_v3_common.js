#!/usr/bin/env node
'use strict';
// src/check_overlap_v3_common.js — 「companion v1.1 / reboot / dialogue / farewell」通用校验核心
//
// 四层校验（全部 0 容差）：
//   A. 几何层：逐帧（1800 帧）对每个语义分组做两两重叠 + 边界截断 + 整数坐标检查
//      分组与容器：foreground→画布、titleBar→终端标题栏、content→终端文本可用区、
//                  overlayInner_*→浮层内部、subtitle→字幕条
//   B. 文本层：全部文本宽高由 Fusion Pixel 实测，超出文本可用区即判截断
//   C. 像素层：640×360 → 1280×720 严格 2× 最近邻、文字二值化无灰边、
//              字体为 Fusion Pixel 10px 点阵、Clawd 40×17 + 4×4 眼睛、Her 16×28
//   D. 规格层：终端 440×200（标题栏 20 + 内容区 180）、行距 20px、字幕条 20px

const { createCanvas } = require('@napi-rs/canvas');

const CANVAS = { x: 0, y: 0, w: 640, h: 360 };

function overlap(a, b) {
  return (
    Math.min(a[0] + a[2], b[0] + b[2]) - Math.max(a[0], b[0]) > 0 &&
    Math.min(a[1] + a[3], b[1] + b[3]) - Math.max(a[1], b[1]) > 0
  );
}
function interArea(a, b) {
  const w = Math.min(a[0] + a[2], b[0] + b[2]) - Math.max(a[0], b[0]);
  const h = Math.min(a[1] + a[3], b[1] + b[3]) - Math.max(a[1], b[1]);
  return Math.max(0, w) * Math.max(0, h);
}
function outside(box, bounds) {
  return (
    box[0] < bounds.x ||
    box[1] < bounds.y ||
    box[0] + box[2] > bounds.x + bounds.w ||
    box[1] + box[3] > bounds.y + bounds.h
  );
}
function isInt(v) {
  return Number.isInteger(v) || Math.abs(v - Math.round(v)) < 1e-9;
}
function readPixels(canvas) {
  return canvas.getContext('2d').getImageData(0, 0, canvas.width, canvas.height);
}

// ---------------------------------------------------------------------------
// D. 规格层：终端 440×200 / 标题栏 20 / 内容区 180 / 字幕条 20
// ---------------------------------------------------------------------------
function checkSpec(story) {
  const issues = [];
  const T = story.TERM;
  if (T.w !== 440 || T.h !== 200) issues.push(`终端尺寸 ${T.w}×${T.h} ≠ 440×200`);
  if (T.x !== 100 || T.y !== 140) issues.push(`终端位置 (${T.x},${T.y}) ≠ (100,140)`);
  if (T.titleH !== 20) issues.push(`标题栏高度 ${T.titleH} ≠ 20px`);
  if (T.h - T.titleH !== 180) issues.push(`内容区高度 ${T.h - T.titleH} ≠ 180px`);
  if (T.x < 0 || T.y < 0 || T.x + T.w > 640 || T.y + T.h > 360) issues.push('终端超出画布');
  const tb = story.TEXT_BOX;
  if (tb.x < T.x + 8 || tb.x + tb.w > T.x + T.w - 8) issues.push(`文本可用区水平越出终端内边距 [${tb.x},${tb.x + tb.w}]`);
  if (tb.y < T.y + T.titleH + 2 || tb.y + tb.h > T.y + T.h - 2) issues.push(`文本可用区垂直越出内容区 [${tb.y},${tb.y + tb.h}]`);
  if (story.SUB.y !== 340 || story.SUB.h !== 20) issues.push(`字幕条 ${story.SUB.y}+${story.SUB.h} ≠ 340+20`);
  if (story.SUB.y !== T.y + T.h) issues.push(`字幕条顶边 ${story.SUB.y} 未与终端底边 ${T.y + T.h} 对齐（应 0 重叠）`);
  // 行距 20px：相邻行文本盒（13px）不得相撞
  const rows = story.pixel.ROW_Y;
  for (let i = 1; i < rows.length; i++) {
    if (rows[i] - rows[i - 1] < 16) issues.push(`终端行距 ${rows[i] - rows[i - 1]}px < 16px（行间会重叠）`);
  }
  if (rows[rows.length - 1] + 13 > story.STATUS_Y) issues.push('最后一行与状态行重叠');
  return { name: `终端规格 440×200 @(100,140) / 标题栏 20 / 内容区 180 / 7 行 ×20px / 字幕条 20`, issues };
}

// ---------------------------------------------------------------------------
// C-1 输出必须是 640×360 的严格 2× 最近邻
// ---------------------------------------------------------------------------
function checkScale2x(story, frames) {
  const issues = [];
  let blocks = 0;
  for (const n of frames) {
    const { baseCanvas, outCanvas } = story.renderFrameToCanvas(n);
    const base = readPixels(baseCanvas).data;
    const out = readPixels(outCanvas).data;
    const BW = baseCanvas.width;
    const BH = baseCanvas.height;
    const OW = outCanvas.width;
    let bad = 0;
    for (let y = 0; y < BH; y++) {
      for (let x = 0; x < BW; x++) {
        const si = (y * BW + x) * 4;
        const r = base[si];
        const g = base[si + 1];
        const b = base[si + 2];
        const ox = x * 2;
        const oy = y * 2;
        for (let dy = 0; dy < 2; dy++) {
          for (let dx = 0; dx < 2; dx++) {
            const di = ((oy + dy) * OW + (ox + dx)) * 4;
            blocks++;
            if (Math.abs(out[di] - r) > 1 || Math.abs(out[di + 1] - g) > 1 || Math.abs(out[di + 2] - b) > 1) bad++;
          }
        }
      }
    }
    if (bad > 0) issues.push(`帧 ${n}: ${bad} 输出像素与 2× 最近邻不一致`);
  }
  return { name: `像素放大 SCALE=2 最近邻 (${frames.length} 帧, ${blocks} 块)`, issues };
}

// ---------------------------------------------------------------------------
// C-2 文本二值化（区域内只有前景/背景两色）
// ---------------------------------------------------------------------------
function checkTextNoAA(P, samples) {
  const issues = [];
  const cv = createCanvas(560, 80);
  const ctx = cv.getContext('2d');
  let total = 0;
  for (const s of samples) {
    ctx.clearRect(0, 0, 560, 80);
    ctx.fillStyle = '#14161C';
    ctx.fillRect(0, 0, 560, 80);
    const box = P.txt(ctx, 8, 8, s.text, s.color, s.size);
    const d = readPixels(cv).data;
    const colors = new Set();
    for (let y = 0; y < 60; y++) {
      for (let x = 0; x < Math.min(552, box.w + 16); x++) {
        const i = (y * 560 + x) * 4;
        colors.add(`${d[i]},${d[i + 1]},${d[i + 2]}`);
      }
    }
    total++;
    if (colors.size !== 2) {
      issues.push(`文本「${s.text}」(${s.size}px) 出现 ${colors.size} 种颜色（应为 2 种，抗锯齿会产生过渡色）`);
    }
    if (box.w > 540) issues.push(`文本「${s.text}」样本超宽`);
  }
  return { name: `文本二值化无灰边 (${total} 条样本)`, issues };
}

// ---------------------------------------------------------------------------
// C-3 字体
// ---------------------------------------------------------------------------
function checkFonts(P) {
  const issues = [];
  if (!/FusionPixel/i.test(P.FONT_10)) issues.push(`终端字体 FONT_10 不是 Fusion Pixel: ${P.FONT_10}`);
  if (!/FusionPixel/i.test(P.FONT_12)) issues.push(`字幕字体 FONT_12 不是 Fusion Pixel: ${P.FONT_12}`);
  const aw = P.measureTxt('A', 10);
  const cw = P.measureTxt('她', 10);
  if (aw !== 5) issues.push(`10px 字体 ASCII 宽度应为 5px，实测 ${aw}px`);
  if (cw !== 10) issues.push(`10px 字体 CJK 宽度应为 10px，实测 ${cw}px`);
  return { name: `字体 Fusion Pixel 10px 点阵 (ASCII=${aw}px, CJK=${cw}px)`, issues };
}

// ---------------------------------------------------------------------------
// C-4 Clawd 造型
// ---------------------------------------------------------------------------
function checkClawdArt(P, drawX = 60, drawY = 40) {
  const issues = [];
  const CW = 240;
  const CH2 = 140;
  const cv = createCanvas(CW, CH2);
  const ctx = cv.getContext('2d');
  const BG = '#F5EDD5';
  const x = drawX;
  const y = drawY;
  const C = P.C;
  const draw = (mood) => {
    ctx.fillStyle = BG;
    ctx.fillRect(0, 0, CW, CH2);
    P.drawClawd(ctx, x, y, 1.2, mood);
    return readPixels(cv).data;
  };
  const at = (d, X, Y) => {
    const i = (Y * CW + X) * 4;
    if (i < 0 || i + 3 >= d.length) return '#out_of_bounds';
    return `#${[d[i], d[i + 1], d[i + 2]].map((v) => v.toString(16).padStart(2, '0')).join('')}`;
  };
  const lc = (v) => String(v).toLowerCase();
  const isBg = (col) => lc(col) === lc(BG);

  const d = draw('calm');
  if (!isBg(at(d, x - 1, y + 6))) issues.push(`Clawd body 左侧越界：(${x - 1},${y + 6}) 非背景`);
  if (!isBg(at(d, x + 40, y + 6))) issues.push(`Clawd body 右侧越界：(${x + 40},${y + 6}) 非背景`);
  if (isBg(at(d, x + 2, y + 16))) issues.push('Clawd body 高度不足 17px');
  if (at(d, x + 20, y) !== lc(C.clawdDark)) issues.push(`Clawd 顶部暗条缺失：${at(d, x + 20, y)}`);
  if (at(d, x + 20, y + 1) !== lc(C.clawdDark)) issues.push('Clawd 顶部暗条应为 2px');
  if (at(d, x + 20, y + 2) !== lc(C.clawdBody)) issues.push('Clawd 顶部暗条过厚（应为 2px）');
  if (at(d, x + 9, y + 11) !== lc(C.clawdBelly)) issues.push('Clawd 腹部浅色块起点错误');
  if (at(d, x + 30, y + 11) !== lc(C.clawdBelly)) issues.push('Clawd 腹部浅色块宽度不足 22px');
  if (at(d, x + 31, y + 11) !== lc(C.clawdBody)) issues.push('Clawd 腹部浅色块宽度超过 22px');
  if (at(d, x + 20, y + 14) !== lc(C.clawdBelly)) issues.push('Clawd 腹部浅色块高度不足 4px');
  if (at(d, x + 20, y + 15) !== lc(C.clawdBody)) issues.push('Clawd 腹部浅色块高度超过 4px');
  for (const ex of [10, 26]) {
    for (let dy = 6; dy <= 9; dy++) {
      for (let dx = 0; dx <= 3; dx++) {
        const col = at(d, x + ex + dx, y + dy);
        if (!(col === lc(C.clawdEye) || col === '#ffffff')) {
          issues.push(`Clawd 眼睛非 4×4 实心：(${x + ex + dx},${y + dy})=${col}`);
        }
      }
    }
    if (at(d, x + ex + 4, y + 6) !== lc(C.clawdBody)) issues.push(`Clawd 眼睛宽度超过 4px (x+${ex})`);
    if (at(d, x + ex, y + 5) !== lc(C.clawdBody)) issues.push(`Clawd 眼睛高度超过 4px (x+${ex})`);
    if (at(d, x + ex + 1, y + 7) !== '#ffffff') issues.push(`Clawd 眼睛缺少 1×1 白色高光 (x+${ex})`);
  }

  const dt = draw('thinking');
  if (at(dt, x + 20, y + 3) !== lc(C.clawdThink)) issues.push(`thinking 主体色应为 ${C.clawdThink}，实测 ${at(dt, x + 20, y + 3)}`);
  if (at(dt, x + 20, y + 1) !== lc(C.clawdThinkDark)) issues.push('thinking 顶部暗条色错误');
  if (at(dt, x + 10, y + 7) !== lc(C.clawdEye) || at(dt, x + 10, y + 8) !== lc(C.clawdEye)) issues.push('thinking 眯眼高度不足 2px');
  if (at(dt, x + 10, y + 9) !== lc(C.clawdThink)) issues.push('thinking 眯眼高度超过 2px');

  const ds = draw('smile');
  if (at(ds, x + 5, y + 8) !== lc(C.clawdBlush)) issues.push('smile 表情缺少粉色腮红');
  if (at(ds, x + 33, y + 8) !== lc(C.clawdBlush)) issues.push('smile 表情右侧腮红缺失');
  if (at(ds, x + 19, y + 13) !== lc(C.clawdEye)) issues.push('smile 表情缺少微笑弧');

  return { name: 'Clawd 造型 40×17 / 眼睛 4×4+1px 高光 / 顶部 2px 暗条 / 腹部 22×4 / calm·thinking·smile', issues };
}

// ---------------------------------------------------------------------------
// C-5 Her 16×28
// ---------------------------------------------------------------------------
function checkHerArt(P, drawX = 100, drawY = 40) {
  const issues = [];
  const CW = 240;
  const CH2 = 140;
  const cv = createCanvas(CW, CH2);
  const ctx = cv.getContext('2d');
  const BG = '#F5EDD5';
  ctx.fillStyle = BG;
  ctx.fillRect(0, 0, CW, CH2);
  P.drawHer(ctx, drawX, drawY, 1.2, 'stand');
  const d = readPixels(cv).data;
  const isBg = (X, Y) => {
    const i = (Y * CW + X) * 4;
    return d[i] === 245 && d[i + 1] === 237 && d[i + 2] === 213;
  };
  let minX = 999;
  let maxX = -1;
  let minY = 999;
  let maxY = -1;
  for (let Y = 20; Y < CH2; Y++) {
    for (let X = 0; X < CW; X++) {
      if (!isBg(X, Y)) {
        if (X < minX) minX = X;
        if (X > maxX) maxX = X;
        if (Y < minY) minY = Y;
        if (Y > maxY) maxY = Y;
      }
    }
  }
  const w = maxX - minX + 1;
  const h = maxY - minY + 1;
  if (minX < drawX || maxX > drawX + 15) issues.push(`Her 超出 16px 槽位：x∈[${minX - drawX}, ${maxX - drawX}]`);
  if (minY !== drawY) issues.push(`Her 顶部未对齐槽位：y=${minY - drawY}`);
  if (h !== 28) issues.push(`Her 高度应为 28px，实测 ${h}px`);
  if (w < 12) issues.push(`Her 视觉宽度异常：${w}px`);
  return { name: `Her 造型 ${w}×${h} / 16×28 槽位（粉色裙子）`, issues };
}

// ---------------------------------------------------------------------------
// A+B 层：逐帧几何与截断
// ---------------------------------------------------------------------------
function checkFrames(story, frames) {
  const issues = [];
  let checks = 0;
  let groupCount = 0;
  const seen = new Set();

  for (let n = 0; n < frames; n++) {
    const t = n / story.FPS;
    const { scene, sceneIndex, groups } = story.layoutAt(t);
    const sc = story.scenes[sceneIndex];
    for (const [gname, list] of Object.entries(groups)) {
      if (!list.length) continue;
      seen.add(gname);
      groupCount += list.length;

      for (let i = 0; i < list.length; i++) {
        for (let j = i + 1; j < list.length; j++) {
          checks++;
          if (overlap(list[i].box, list[j].box)) {
            issues.push(
              `帧 ${n} (${t.toFixed(2)}s) ${gname}: OVERLAP ${list[i].name}[${list[i].box}] × ${list[j].name}[${list[j].box}] area=${interArea(list[i].box, list[j].box)}`
            );
          }
        }
      }
      // fx（粒子）必须与前景层两两不重叠（跨组校验）
      if (gname === 'fx' && groups.foreground) {
        for (const el of list) {
          for (const fgEl of groups.foreground) {
            checks++;
            if (overlap(el.box, fgEl.box)) {
              issues.push(`帧 ${n} (${t.toFixed(2)}s) fx×foreground: OVERLAP ${el.name}[${el.box}] × ${fgEl.name}[${fgEl.box}]`);
            }
          }
        }
      }
      const container = story.containerFor(gname, t, sc);
      for (const el of list) {
        checks++;
        if (el.box.some((v) => !isInt(v))) issues.push(`帧 ${n} ${gname}/${el.name}: 坐标非整数 [${el.box}]`);
        if (outside(el.box, container)) {
          issues.push(`帧 ${n} (${scene}) ${gname}/${el.name}: TRUNCATED [${el.box}] 超出容器 ${JSON.stringify(container)}`);
        }
      }
    }
  }
  return {
    name: `逐帧几何/截断 (${frames} 帧, ${groupCount} 个元素实例, ${checks} 次判定, 分组: ${[...seen].sort().join('/')})`,
    issues,
  };
}

// ---------------------------------------------------------------------------
// 黑场：只允许出现在转场、片头片尾与剧本显式声明的窗口
// ---------------------------------------------------------------------------
function checkBlackFrames(story, sampleEvery = 20) {
  const issues = [];
  const N = story.NFRAMES;
  const isAllowed = (t) =>
    t < P_FADE_IN(story) + 0.02 ||
    t > story.DURATION - P_FADE_OUT(story) - 0.02 ||
    story.BLACK_WINDOWS.some((w) => t >= w.start - 0.02 && t <= w.end + 0.02);
  let black = 0;
  let checked = 0;
  for (let n = 0; n < N; n += sampleEvery) {
    const t = n / story.FPS;
    const { baseCanvas } = story.renderFrameToCanvas(n);
    const d = readPixels(baseCanvas).data;
    let dark = 0;
    const total = baseCanvas.width * baseCanvas.height;
    for (let i = 0; i < d.length; i += 4) if (d[i] < 8 && d[i + 1] < 8 && d[i + 2] < 8) dark++;
    checked++;
    if (dark / total > 0.98) {
      black++;
      if (!isAllowed(t)) issues.push(`帧 ${n} (${t.toFixed(2)}s) 非转场区间出现黑场`);
    }
  }
  return { name: `黑场区间 (${checked} 个采样帧, ${black} 个黑场帧, 允许窗口 ${story.BLACK_WINDOWS.map((w) => `${w.start.toFixed(2)}-${w.end.toFixed(2)}s`).join(',')})`, issues };
}
function P_FADE_IN(story) {
  return story.pixel.FADE_IN;
}
function P_FADE_OUT(story) {
  return story.pixel.FADE_OUT;
}

// ---------------------------------------------------------------------------
// 打字完整性：场景结束前必须全部打完，且不晚于下一行
// ---------------------------------------------------------------------------
function checkTypingComplete(story) {
  const issues = [];
  const P = story.pixel;
  for (const item of story.TYPING_SCHEDULE) {
    const chars = Array.from(item.text).length;
    const charMs = item.charMs || P.TYPE_CHAR_MS;
    const end = item.start + (chars * charMs) / 1000;
    if (end > item.limit) issues.push(`[${item.scene}] 「${item.text}」打字结束于 ${end.toFixed(2)}s，超过区间上限 ${item.limit}s`);
    if (item.strictBefore !== undefined && end > item.strictBefore + 1e-6) {
      issues.push(`[${item.scene}] 「${item.text}」打字结束于 ${end.toFixed(2)}s，晚于下一行 ${item.strictBefore}s`);
    }
    const typed = P.typedCount(item.limit - 0.001, item.start, chars, charMs);
    if (typed < chars) issues.push(`[${item.scene}] 「${item.text}」在 ${item.limit}s 仅显示 ${typed}/${chars} 字`);
  }
  const maxEnd = Math.max(...story.TYPING_SCHEDULE.map((i) => i.start + (Array.from(i.text).length * (i.charMs || P.TYPE_CHAR_MS)) / 1000));
  return { name: `打字完整性 (${story.TYPING_SCHEDULE.length} 行, 最后一行 ${maxEnd.toFixed(2)}s)`, issues };
}

// ---------------------------------------------------------------------------
// 主流程
// ---------------------------------------------------------------------------
function run(story, opts = {}) {
  console.log(`=== ${story.CHECK_TITLE} ===`);
  console.log(`画布 ${story.BW}×${story.BH} → ${story.FW}×${story.FH} @ ${story.FPS}fps, ${story.NFRAMES} 帧`);
  console.log(`终端 ${story.TERM.w}×${story.TERM.h} @(${story.TERM.x},${story.TERM.y}) · 标题栏 ${story.TERM.titleH} · 内容区 ${story.TERM.h - story.TERM.titleH}\n`);

  const P = story.pixel;
  const results = [];
  const t0 = Date.now();

  results.push(checkSpec(story));
  results.push(checkFonts(P));
  results.push(checkTextNoAA(P, story.AA_SAMPLES));
  results.push(checkClawdArt(P));
  results.push(checkHerArt(P));
  results.push(checkTypingComplete(story));
  results.push(checkFrames(story, story.NFRAMES));
  results.push(checkScale2x(story, [0, 240, 300, 900, 1200, 1500, 1799]));
  results.push(checkBlackFrames(story, 20));

  let issues = 0;
  for (const r of results) {
    if (r.issues.length) {
      issues += r.issues.length;
      console.log(`[FAIL] ${r.name}`);
      for (const m of r.issues.slice(0, 40)) console.log(`   - ${m}`);
      if (r.issues.length > 40) console.log(`   ... 其余 ${r.issues.length - 40} 条省略`);
    } else {
      console.log(`[PASS] ${r.name}`);
    }
  }

  const passed = results.filter((r) => r.issues.length === 0).length;
  console.log(`\n=== Summary: ${passed}/${results.length} checks PASSED, ${issues} issue(s), ${((Date.now() - t0) / 1000).toFixed(1)}s ===`);

  if (opts.reportPath) {
    const fs = require('fs');
    const path = require('path');
    const report = {
      status: issues === 0 ? 'PASSED' : 'FAILED',
      generatedAt: new Date().toISOString(),
      title: story.CHECK_TITLE,
      canvas: { width: story.BW, height: story.BH, scale: story.SCALE, outputWidth: story.FW, outputHeight: story.FH, fps: story.FPS, frames: story.NFRAMES },
      terminal: { x: story.TERM.x, y: story.TERM.y, w: story.TERM.w, h: story.TERM.h, titleBar: story.TERM.titleH, content: story.TERM.h - story.TERM.titleH },
      summary: { checksPassed: passed, checksTotal: results.length, issues },
      checks: results.map((r) => ({ name: r.name, status: r.issues.length ? 'FAILED' : 'PASSED', issues: r.issues })),
      clicks: story.getClickTimestamps().length,
    };
    fs.mkdirSync(path.dirname(opts.reportPath), { recursive: true });
    fs.writeFileSync(opts.reportPath, JSON.stringify(report, null, 2) + '\n');
    console.log(`报告: ${opts.reportPath}`);
  }
  return issues === 0;
}

module.exports = { run, overlap, interArea, outside, readPixels, CANVAS };
