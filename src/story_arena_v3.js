#!/usr/bin/env node
'use strict';
// src/story_arena_v3.js — 「companion v1.1 / reboot / dialogue / farewell」共用故事引擎
//
// 以声明式剧本描述一个 30s 三场景像素短片，统一产出：
//   · 逐帧渲染（drawSceneAt / renderFrameToCanvas / renderAllFrames）
//   · 布局模型 layoutAt(t)（与绘制同一批常量，供 check_overlap 0px 容差校验）
//   · 敲击音时间轴 getClickTimestamps()（与文字出现严格同帧）
//   · 校验元数据（TYPING_SCHEDULE / AA_SAMPLES / BOUNDS / BLACK_WINDOWS）
//
// 剧本 schema（每个 scene）：
//   { id, start, end, fadeIn?, fadeOut?,          // 0.25s 黑场（缺省）；reboot R1 用 2.5s 慢速淡黑
//     bg: { dawn, city, stars } | (ctx,t)=>void,   // 房间背景或完全自绘
//     terminal: { title, accent, led },           // null → 无终端（纯黑场景）
//     lines: [ line ], status, statusColor,
//     clawd: { x, y, mood, blend, palette, warmMix, from, to } | (t)=>state,
//     her:   { x, y, pose, from, to } | (t)=>state,
//     overlays: [ overlay ],
//     extra: (ctx, t, scene) => void }
//
// line.kind:
//   'prompt' — 提示符整段出现（1 次 click），消息逐字 140ms（每字 1 次 click）
//   'typed'  — 整行逐字 140ms（每字 1 次 click）
//   'line'   — 整行一次性出现（1 次 click）
//
// overlay.kind: 'note' | 'bubble' | 'thought' | 'card' | 'mug' | 'sparkles' | 'led'

const path = require('path');
const P = require('./pixel_arena_v3');

const {
  BW, BH, FW, FH, SCALE, FPS, DURATION, NFRAMES, TYPE_CHAR_MS, SUB_CHAR_MS,
  TERM, TEXT_X, TEXT_BOX, STATUS_Y, STATUS_DIVIDER, SUB, SUB_TEXT_Y,
  C, px, txt, textBox, measureTxt, partsText, clamp01, easeOut,
  drawBackground, drawTerminal, drawStatusDivider, drawStatusLine,
  drawClawd, drawHer, drawMessageBubble, drawThoughtBubble, drawStickyNote,
  drawMonologueCard, drawCoffeeMug, drawCursor, drawPowerLed, sparkleList, drawSparkles,
  drawSubtitle, subtitleTextAt, drawScenes, createFrameRenderer,
} = P;

// ---------------------------------------------------------------------------
// 行规格归一化
// ---------------------------------------------------------------------------
function normalizeLine(spec, sceneId) {
  const kind = spec.kind || 'prompt';
  let parts;
  if (kind === 'prompt') {
    parts = [
      { text: spec.prompt, color: spec.promptColor || C.dim },
      { text: spec.msg, color: spec.msgColor || C.text },
    ];
  } else {
    parts = spec.parts;
  }
  const full = partsText(parts);
  const chars = Array.from(full);
  const fullW = measureTxt(full, 10);
  const ln = {
    ...spec,
    kind,
    sceneId,
    parts,
    full,
    chars,
    fullW,
    charMs: spec.charMs || TYPE_CHAR_MS,
    promptLen: kind === 'prompt' ? Array.from(parts[0].text).length : 0,
    msgLen: kind === 'prompt' ? Array.from(parts[1].text).length : chars.length,
  };
  if (ln.fullW > TEXT_BOX.w) {
    throw new Error(`[${sceneId}] 终端行超宽 ${ln.fullW}px > ${TEXT_BOX.w}px: "${full}"`);
  }
  if (ln.x !== undefined && ln.x + ln.fullW > TEXT_BOX.x + TEXT_BOX.w) {
    throw new Error(`[${sceneId}] 终端行越界: "${full}"`);
  }
  return ln;
}

// 一行完全打完的时刻（秒）
function lineEndTime(ln) {
  if (ln.kind === 'line') return ln.start;
  const n = ln.kind === 'prompt' ? ln.msgLen : ln.chars.length;
  return ln.start + ((n - 1 + 1) * ln.charMs) / 1000;
}

// 行内点击时间（绝对值）
function lineClickTimes(ln) {
  const out = [];
  if (ln.kind === 'line') {
    out.push(ln.start);
    return out;
  }
  if (ln.kind === 'prompt') {
    out.push(ln.start); // 提示符出现（与首字同一帧，最终去重合并）
    for (let i = 1; i < ln.msgLen; i++) out.push(ln.start + (i * ln.charMs) / 1000);
    return out;
  }
  for (let i = 0; i < ln.chars.length; i++) out.push(ln.start + (i * ln.charMs) / 1000);
  return out;
}

// ---------------------------------------------------------------------------
// 单行绘制
// ---------------------------------------------------------------------------
function lineTextX(ln) {
  return ln.x === undefined ? TEXT_X : ln.x;
}

function drawLineItem(ctx, ln, t) {
  const x = lineTextX(ln);
  const idleCursor = ln.cursor !== false;

  if (t < ln.start) {
    if (ln.kind === 'prompt' && idleCursor) drawCursor(ctx, x, ln.y + 1, t, ln.parts[0].color);
    return;
  }

  if (ln.kind === 'prompt') {
    const curOn = Math.floor(t * 2.5) % 2 === 0;
    txt(ctx, x, ln.y, ln.parts[0].text, ln.parts[0].color, 10);
    const px0 = x + ln.fullW - measureTxt(ln.parts[1].text, 10);
    const n = Math.min(ln.msgLen, Math.floor(((t - ln.start) * 1000) / ln.charMs) + 1);
    const shown = Array.from(ln.parts[1].text).slice(0, n).join('');
    if (shown) txt(ctx, px0, ln.y, shown, ln.parts[1].color, 10);
    const cx = px0 + measureTxt(shown, 10);
    if (n < ln.msgLen && idleCursor && curOn) px(ctx, cx + 1, ln.y + 1, 6, 10, ln.parts[1].color);
    return;
  }

  if (ln.kind === 'typed') {
    const n = Math.min(ln.chars.length, Math.floor(((t - ln.start) * 1000) / ln.charMs) + 1);
    let cx = x;
    let remaining = n;
    let lastColor = ln.parts[0].color;
    for (const p of ln.parts) {
      if (remaining <= 0) break;
      const chs = Array.from(p.text);
      const take = Math.min(chs.length, remaining);
      if (take > 0) {
        const shown = chs.slice(0, take).join('');
        txt(ctx, cx, ln.y, shown, p.color, 10);
        cx += measureTxt(shown, 10);
      }
      remaining -= take;
      lastColor = p.color;
    }
    if (n < ln.chars.length && idleCursor && Math.floor(t * 2.5) % 2 === 0) px(ctx, cx + 1, ln.y + 1, 6, 10, lastColor);
    return;
  }

  // 'line'
  let cx = x;
  for (const p of ln.parts) {
    txt(ctx, cx, ln.y, p.text, p.color, 10);
    cx += measureTxt(p.text, 10);
  }
  if (ln.cursor && Math.floor(t * 2.5) % 2 === 0) px(ctx, cx + 1, ln.y + 1, 6, 10, ln.parts[ln.parts.length - 1].color);
}

// 行在 t 时刻的可见文本（用于布局与校验；未开始 = null）
function lineVisibleText(ln, t) {
  if (t < ln.start) {
    return ln.kind === 'prompt' && ln.cursor !== false ? '' : null;
  }
  if (ln.kind === 'prompt') {
    const n = Math.min(ln.msgLen, Math.floor(((t - ln.start) * 1000) / ln.charMs) + 1);
    return ln.parts[0].text + Array.from(ln.parts[1].text).slice(0, n).join('');
  }
  if (ln.kind === 'typed') {
    const n = Math.min(ln.chars.length, Math.floor(((t - ln.start) * 1000) / ln.charMs) + 1);
    return ln.chars.slice(0, n).join('');
  }
  return ln.full;
}

// 行布局盒（打字中只算已显示的宽度；未出现返回 null）
// 额外返回光标盒（若该帧正在闪烁/打字）
function lineBoxes(ln, t) {
  const x = lineTextX(ln);
  const out = [];
  if (t < ln.start) {
    if (ln.kind === 'prompt' && ln.cursor !== false) out.push({ name: `${ln.sceneId}_idleCursor`, box: [x, ln.y + 1, 6, 10] });
    return out;
  }
  const vis = lineVisibleText(ln, t);
  const w = measureTxt(vis, 10);
  if (w > 0) out.push({ name: `${ln.sceneId}_row@${ln.y}`, box: textBox(x, ln.y, vis, 10) });
  // 打字中 / 整行带光标时，光标盒（只在显示的那一帧计）
  const typing = ln.kind !== 'line' && (ln.kind === 'prompt' ? vis.length < ln.full.length : Array.from(vis).length < ln.chars.length);
  if ((typing || ln.cursor) && Math.floor(t * 2.5) % 2 === 0) {
    out.push({ name: `${ln.sceneId}_cursor@${ln.y}`, box: [x + w + 1, ln.y + 1, 6, 10] });
  }
  return out;
}

// ---------------------------------------------------------------------------
// 浮层（overlay）
// ---------------------------------------------------------------------------
const THOUGHT_TAIL = 9;
const BUBBLE_TAIL = 6;

function overlayWorldBox(ov) {
  if (ov.kind === 'sparkles') return [ov.region.x, ov.region.y, ov.region.w, ov.region.h];
  if (ov.kind === 'led') return [ov.x - 6, ov.y - 6, 18, 18];
  if (ov.kind === 'note') return [ov.box.x, ov.box.y - 3, ov.box.w, ov.box.h + 3];
  if (ov.kind === 'bubble') return [ov.box.x, ov.box.y, ov.box.w, ov.box.h + BUBBLE_TAIL];
  if (ov.kind === 'thought') return [ov.box.x, ov.box.y, ov.box.w, ov.box.h + THOUGHT_TAIL];
  return [ov.box.x, ov.box.y, ov.box.w, ov.box.h];
}

function overlayInnerBox(ov) {
  if (ov.kind === 'note') return { x: ov.box.x + 4, y: ov.box.y - 3, w: ov.box.w - 8, h: ov.box.h + 3 };
  if (ov.kind === 'bubble') return { x: ov.box.x + 4, y: ov.box.y + 4, w: ov.box.w - 8, h: ov.box.h - 8 };
  if (ov.kind === 'thought') return { x: ov.box.x + 4, y: ov.box.y + 4, w: ov.box.w - 8, h: ov.box.h - 8 };
  return { x: ov.box.x, y: ov.box.y, w: ov.box.w, h: ov.box.h };
}

function overlayActive(ov, t) {
  if (ov.kind === 'led') return t >= ov.at;
  if (ov.kind === 'mug') return t >= ov.at;
  return t >= ov.at;
}

function overlaySymbol(ov, t) {
  if (!ov.symbols) return ov.symbol || '...';
  let s = ov.symbols[0].text;
  for (const it of ov.symbols) if (t >= it.at) s = it.text;
  return s;
}

function drawOverlayItem(ctx, ov, t) {
  if (!overlayActive(ov, t)) return;
  const appear = ov.appear === undefined ? 1 : ov.appear;
  if (ov.kind === 'note') {
    const a = appear === 1 ? clamp01((t - ov.at) / 0.24) : appear;
    drawStickyNote(ctx, ov.box, ov.title, ov.sub || '', t, a);
  } else if (ov.kind === 'bubble') {
    const a = appear === 1 ? clamp01((t - ov.at) / 0.22) : appear;
    drawMessageBubble(ctx, ov.box, ov.text, a);
  } else if (ov.kind === 'thought') {
    const sym = overlaySymbol(ov, t);
    let changedAt = ov.at;
    if (ov.symbols) for (const it of ov.symbols) if (t >= it.at && it.text === sym) changedAt = it.at;
    const a = clamp01((t - changedAt) / 0.16);
    if (a > 0) drawThoughtBubble(ctx, ov.box, sym, t, a);
  } else if (ov.kind === 'card') {
    const a = clamp01((t - ov.at) / 0.5);
    if (a > 0) drawMonologueCard(ctx, ov.box, ov.text, a);
  } else if (ov.kind === 'mug') {
    drawCoffeeMug(ctx, ov.box, t, clamp01((t - ov.at) / 0.5));
  } else if (ov.kind === 'sparkles') {
    drawSparkles(ctx, sparkleList(t, ov.region, ov.count || 5, ov.at), ov.color || '255,246,216');
  } else if (ov.kind === 'led') {
    drawPowerLed(ctx, ov.x, ov.y, t, true, ov.color || C.green);
  }
}

function overlayBoxes(ov, t) {
  if (!overlayActive(ov, t)) return [];
  const out = [];
  if (ov.kind === 'note') {
    const { x, y, w } = ov.box;
    out.push({ name: 'tape', box: [x + w / 2 - 9, y - 3, 18, 6] });
    out.push({ name: 'note_title', box: textBox(x + w / 2, y + 12, ov.title, 12, 'center') });
    if (ov.sub) out.push({ name: 'note_sub', box: textBox(x + w / 2, y + 32, ov.sub, 10, 'center') });
  } else if (ov.kind === 'bubble') {
    const { x, y, w, h } = ov.box;
    out.push({ name: 'bubble_txt', box: textBox(x + w / 2, y + Math.round((h - 10) / 2), ov.text, 10, 'center') });
  } else if (ov.kind === 'thought') {
    const { x, y, w, h } = ov.box;
    out.push({ name: 'thought_txt', box: textBox(x + w / 2, y + Math.round(h / 2) - 7, overlaySymbol(ov, t), 12, 'center') });
  } else if (ov.kind === 'card') {
    const { x, y, w, h } = ov.box;
    out.push({ name: 'card_txt', box: textBox(x + w / 2, y + 7, ov.text, 10, 'center') });
  } else if (ov.kind === 'sparkles') {
    for (const p of sparkleList(t, ov.region, ov.count || 5, ov.at)) out.push({ name: 'sparkle', box: [p.x, p.y, p.s, p.s] });
  }
  return out;
}

// ---------------------------------------------------------------------------
// 角色状态求值
// ---------------------------------------------------------------------------
function resolveChar(spec, t, defaultPos) {
  if (!spec) return null;
  const st = typeof spec === 'function' ? spec(t) : spec;
  if (!st || st.visible === false) return null;
  if (st.from !== undefined && t < st.from) return null;
  if (st.to !== undefined && t >= st.to) return null;
  return {
    x: st.x === undefined ? defaultPos.x : st.x,
    y: st.y === undefined ? defaultPos.y : st.y,
    mood: st.mood || 'calm',
    blend: st.blend === undefined ? null : st.blend,
    palette: st.palette || 'coral',
    warmMix: st.warmMix || 0,
    pose: st.pose || 'stand',
  };
}

function drawClawdState(ctx, st, t) {
  drawClawd(ctx, st.x, st.y, t, st.mood, st.blend, { palette: st.palette, warmMix: st.warmMix });
}

// ---------------------------------------------------------------------------
// buildStory
// ---------------------------------------------------------------------------
function buildStory(cfg) {
  const scenes = cfg.scenes.map((sc, i) => ({
    ...sc,
    index: i,
    start: sc.start,
    end: sc.end,
    id: sc.id || `S${i + 1}`,
    lines: (sc.lines || []).map((ln) => normalizeLine(ln, sc.id || `S${i + 1}`)),
  }));

  // 剧本自检：每行时间必须落在所属场景区间内（防止把场景内相对时间写成绝对值）
  for (const sc of scenes) {
    for (const ln of sc.lines) {
      if (ln.start < sc.start - 1e-9 || ln.start >= sc.end) {
        throw new Error(`[${sc.id}] 行时间 ${ln.start}s 不在场景区间 [${sc.start}, ${sc.end}) 内："${ln.full}"`);
      }
    }
    for (const ov of sc.overlays || []) {
      const at = ov.at;
      if (ov.kind !== 'led' && (at < sc.start - 1e-9 || at >= sc.end)) {
        throw new Error(`[${sc.id}] 浮层 ${ov.kind} 出现时间 ${at}s 不在场景区间内`);
      }
    }
  }

  // 字幕
  const subLines = (cfg.subtitles || []).map((s) => s.text);
  const subWindows = (cfg.subtitles || []).map((s) => ({ start: s.start, end: s.end }));

  // 场景查找
  function sceneAt(t) {
    let cur = scenes[0];
    for (const sc of scenes) if (t >= sc.start) cur = sc;
    return cur;
  }

  // ---- 绘制 ----
  function drawScene(ctx, t, sc) {
    if (typeof sc.bg === 'function') sc.bg(ctx, t, sc);
    else drawBackground(ctx, t, sc.bg || {});

    if (sc.terminal) {
      drawTerminal(ctx, sc.terminal.title, sc.terminal.accent, sc.terminal.led || 'on');
      for (const ln of sc.lines) drawLineItem(ctx, ln, t);
      if (sc.status) {
        drawStatusDivider(ctx);
        drawStatusLine(ctx, sc.status, sc.statusColor || C.dim);
      }
    }

    const cs = resolveChar(sc.clawd, t, P.CLAWD_ROOM);
    if (cs) drawClawdState(ctx, cs, t);
    const hs = resolveChar(sc.her, t, P.HER_ROOM);
    if (hs) drawHer(ctx, hs.x, hs.y, t, hs.pose);

    for (const ov of sc.overlays || []) drawOverlayItem(ctx, ov, t);
    if (sc.extra) sc.extra(ctx, t, sc);

    // 字幕（全局窗口，可跨场景）
    if (!sc.hideSubtitleBar) drawSubtitle(ctx, subLines, subWindows, t);
  }

  // ---- 布局 ----
  function layoutAt(t) {
    const sc = sceneAt(t);
    const groups = {};

    const fg = [];
    if (sc.terminal) fg.push({ name: 'terminal', box: [TERM.x, TERM.y, TERM.w, TERM.h] });
    if (!sc.hideSubtitleBar) fg.push({ name: 'subtitleBar', box: [SUB.x, SUB.y, SUB.w, SUB.h] });

    const cs = resolveChar(sc.clawd, t, P.CLAWD_ROOM);
    if (cs) fg.push({ name: 'clawd', box: [cs.x, cs.y - 1, 40, 25] });
    const hs = resolveChar(sc.her, t, P.HER_ROOM);
    if (hs) fg.push({ name: 'her', box: [hs.x, hs.y - 1, 16, 29] });

    const fx = [];
    for (const ov of sc.overlays || []) {
      if (!overlayActive(ov, t)) continue;
      if (ov.kind === 'sparkles') {
        for (const p of sparkleList(t, ov.region, ov.count || 5, ov.at)) fx.push({ name: 'sparkle', box: [p.x, p.y, p.s, p.s] });
        continue;
      }
      fg.push({ name: `overlay_${ov.kind}`, box: overlayWorldBox(ov) });
    }
    groups.foreground = fg;
    if (fx.length) groups.fx = fx;

    if (sc.terminal) {
      groups.titleBar = [
        { name: 'btn_red', box: [TERM.x + 8, TERM.y + 7, 6, 6] },
        { name: 'btn_amber', box: [TERM.x + 18, TERM.y + 7, 6, 6] },
        { name: 'btn_green', box: [TERM.x + 28, TERM.y + 7, 6, 6] },
        { name: 'title_txt', box: textBox(TERM.x + TERM.w / 2, TERM.y + 5, sc.terminal.title, 10, 'center') },
        { name: 'led', box: P.ledBox() },
      ];

      const content = [];
      for (const ln of sc.lines) content.push(...lineBoxes(ln, t));
      if (sc.status) {
        content.push({ name: 'status_txt', box: textBox(TEXT_X, STATUS_Y, sc.status, 10) });
        content.push({ name: 'status_divider', box: [STATUS_DIVIDER.x, STATUS_DIVIDER.y, STATUS_DIVIDER.w, STATUS_DIVIDER.h] });
      }
      groups.content = content;
    }

    // 浮层内部
    for (const ov of sc.overlays || []) {
      if (ov.kind === 'sparkles') continue;
      const inner = overlayBoxes(ov, t);
      if (!inner.length) continue;
      groups[`overlayInner_${ov.kind}`] = inner;
    }

    // 字幕
    const subTxt = subtitleTextAt(subLines, subWindows, t);
    groups.subtitle = subTxt ? [{ name: 'subtitle_txt', box: textBox(BW / 2, SUB_TEXT_Y, subTxt, 12, 'center') }] : [];

    return { scene: sc.id, sceneIndex: sc.index, groups };
  }

  // ---- 点击时间轴 ----
  function getClickTimestamps() {
    const raw = [];
    for (const sc of scenes) {
      for (const ln of sc.lines) raw.push(...lineClickTimes(ln));
      for (const ev of sc.events || []) raw.push(ev.t);
      for (const ov of sc.overlays || []) {
        if (ov.click === false) continue;
        if (ov.clickAt !== undefined) raw.push(ov.clickAt);
        else if (ov.kind !== 'sparkles' && ov.kind !== 'led') raw.push(ov.at);
      }
    }
    for (const c of cfg.extraClicks || []) raw.push(c.t);

    const uniq = [];
    const sorted = raw.filter((c) => c >= 0 && c < DURATION - 0.05).sort((a, b) => a - b);
    for (const c of sorted) {
      const q = Math.round(c * FPS) / FPS;
      if (!uniq.length || q - uniq[uniq.length - 1] >= 0.035) uniq.push(Number(q.toFixed(6)));
    }
    return uniq;
  }

  // ---- 校验元数据 ----
  const typingSchedule = [];
  for (const sc of scenes) {
    for (const ln of sc.lines) {
      if (ln.kind === 'line') continue;
      const text = ln.kind === 'prompt' ? ln.parts[1].text : ln.full;
      const idx = sc.lines.indexOf(ln);
      const next = sc.lines[idx + 1];
      typingSchedule.push({
        text,
        start: ln.start,
        limit: sc.end - 0.2,
        strictBefore: next ? next.start : undefined,
        scene: sc.id,
      });
    }
  }
  for (const extra of cfg.extraTyping || []) typingSchedule.push(extra);

  const blackWindows = [];
  for (let i = 0; i < scenes.length - 1; i++) {
    const a = scenes[i];
    const b = scenes[i + 1];
    const fo = a.fadeOut === undefined ? P.FADE : a.fadeOut;
    const fi = b.fadeIn === undefined ? P.FADE : b.fadeIn;
    blackWindows.push({ start: a.end - fo, end: b.start + fi });
  }
  for (const w of cfg.blackWindows || []) blackWindows.push(w);

  const bounds = {
    content: TEXT_BOX,
    titleBar: { x: TERM.x, y: TERM.y, w: TERM.w, h: TERM.titleH },
  };

  // ---- 校验容器 ----
  function containerFor(groupName, t, sc) {
    if (groupName === 'foreground' || groupName === 'fx') return { x: 0, y: 0, w: BW, h: BH };
    if (groupName === 'titleBar') return bounds.titleBar;
    if (groupName === 'content') return bounds.content;
    if (groupName === 'subtitle') return { x: SUB.x, y: SUB.y, w: SUB.w, h: SUB.h };
    if (groupName.startsWith('overlayInner_')) {
      const kind = groupName.slice('overlayInner_'.length);
      const ov = (sc.overlays || []).find((o) => o.kind === kind);
      return ov ? overlayInnerBox(ov) : { x: 0, y: 0, w: BW, h: BH };
    }
    return { x: 0, y: 0, w: BW, h: BH };
  }

  const sceneRunners = scenes.map((sc) => ({
    start: sc.start,
    end: sc.end,
    fadeIn: sc.fadeIn,
    fadeOut: sc.fadeOut,
    draw: (ctx, t) => drawScene(ctx, t, sc),
  }));
  const renderer = createFrameRenderer(sceneRunners, cfg.outDir);

  const story = {
    id: cfg.id,
    BW, BH, SCALE, FW, FH, FPS, DURATION, NFRAMES,
    TYPE_CHAR_MS, SUB_CHAR_MS,
    pixel: P,
    C,
    TERM, TEXT_X, TEXT_BOX, STATUS_Y, SUB, SUB_TEXT_Y,
    CLAWD_ROOM: P.CLAWD_ROOM, HER_ROOM: P.HER_ROOM,
    scenes,
    SUB_LINES: subLines,
    SUB_WINDOWS: subWindows,
    BOUNDS: bounds,
    CHECK_TITLE: cfg.checkTitle,
    TYPING_SCHEDULE: typingSchedule,
    AA_SAMPLES: cfg.aaSamples || [],
    BLACK_WINDOWS: blackWindows,
    EVENTS: cfg.events || [],
    sceneAt,
    cardAt: sceneAt,
    drawSceneAt: (ctx, t) => drawScene(ctx, t, sceneAt(t)),
    layoutAt,
    containerFor,
    getClickTimestamps,
    overlayWorldBox,
    overlayInnerBox,
    renderFrameToCanvas: renderer.renderFrameToCanvas,
    renderAllFrames: renderer.renderAllFrames,
    renderer,
  };
  return story;
}

module.exports = {
  buildStory,
  normalizeLine,
  lineEndTime,
  lineClickTimes,
  lineVisibleText,
  lineBoxes,
  drawLineItem,
  overlayWorldBox,
  overlayInnerBox,
  overlaySymbol,
};
