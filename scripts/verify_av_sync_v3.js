#!/usr/bin/env node
'use strict';
// scripts/verify_av_sync_v3.js — 从最终 MP4 反解音频，独立验证「键盘敲击音 ↔ 文字出现」同步
//
// 做法（不依赖任何渲染中间产物，只用成片 + 剧本时间轴）：
//   1. ffmpeg 解码 MP4 音轨 → 16-bit PCM WAV
//   2. 用 audio/emotional_bgm.wav ×0.25（含 1s/2s 淡入淡出）重建 BGM 基线
//   3. residual = 解码混音 − BGM 基线 → 只剩 click（与 reboot 的电源音效）
//   4. 10ms 能量窗口扫描 residual，检测 onset 并聚类
//   5. 与渲染脚本 getClickTimestamps() 逐点贪心匹配（≤60ms）
//        · 漏检必须为 0
//        · 最大偏差 < 2 帧（33.33ms）
//        · 所有时间戳必须落在显示帧上
//      附加音效（reboot 电源音）会被检出为「未匹配 onset」，单独列出，不算失败
//
// 用法: node scripts/verify_av_sync_v3.js [companion|reboot|dialogue|farewell]

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const { readWav16, getFfmpegPath } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const SR = 44100;
const BGM_GAIN = 0.25;

const MODS = {
  companion: {
    script: '../src/render_companion_arena_v11',
    mp4: 'outputs/companion_arena_v1.1.mp4',
    mix: 'audio/companion_arena_v11_mix.wav',
    doc: 'docs/companion-v11',
    label: 'companion v1.1',
  },
  reboot: {
    script: '../src/render_reboot_arena',
    mp4: 'outputs/reboot_arena_v1.0.mp4',
    mix: 'audio/reboot_arena_mix.wav',
    doc: 'docs/reboot-v1',
    label: 'reboot v1.0',
  },
  dialogue: {
    script: '../src/render_dialogue_arena',
    mp4: 'outputs/dialogue_arena_v1.0.mp4',
    mix: 'audio/dialogue_arena_mix.wav',
    doc: 'docs/dialogue-v1',
    label: 'dialogue v1.0',
  },
  farewell: {
    script: '../src/render_farewell_arena',
    mp4: 'outputs/farewell_arena_v1.0.mp4',
    mix: 'audio/farewell_arena_mix.wav',
    doc: 'docs/farewell-v1',
    label: 'farewell v1.0',
  },
};

function decodeMp4Audio(mp4, outWav) {
  const ffmpeg = getFfmpegPath();
  const r = spawnSync(ffmpeg, ['-y', '-v', 'error', '-i', mp4, '-vn', '-ac', '1', '-ar', String(SR), '-c:a', 'pcm_s16le', outWav], {
    encoding: 'utf8',
  });
  if (r.status !== 0) throw new Error(`ffmpeg 解码失败: ${r.stderr}`);
  return readWav16(outWav);
}

function detectOnsets(mono, bgmMono, duration, opts = {}) {
  const win = Math.round(SR * 0.01);
  const nWin = Math.floor((duration * SR) / win);
  const energy = new Float64Array(nWin);
  for (let w = 0; w < nWin; w++) {
    let e = 0;
    for (let i = w * win; i < (w + 1) * win && i < mono.length; i++) {
      const t = i / SR;
      let g = BGM_GAIN;
      if (t < 1) g *= t;
      if (t > duration - 2) g *= Math.max(0, (duration - t) / 2);
      const bg = i < bgmMono.length ? (bgmMono[i] / 32768) * g : 0;
      const v = mono[i] / 32768 - bg;
      e += v * v;
    }
    energy[w] = Math.sqrt(e / win);
  }
  const onsets = [];
  const thresh = opts.thresh || 0.012;
  let lastW = -99;
  for (let w = 0; w < nWin - 1; w++) {
    const e = energy[w];
    if (e < thresh) continue;
    if (w > 0 && energy[w - 1] > e) continue;
    if (w - lastW <= 2) continue;
    onsets.push({ t: (w * win) / SR, e });
    lastW = w;
  }
  return { onsets, energy };
}

function main() {
  const which = process.argv[2] || 'companion';
  const cfg = MODS[which];
  if (!cfg) {
    console.error(`用法: node scripts/verify_av_sync_v3.js [${Object.keys(MODS).join('|')}]`);
    process.exit(2);
  }
  const mod = require(path.join(__dirname, cfg.script));
  const mp4 = path.join(ROOT, cfg.mp4);
  const mixWav = path.join(ROOT, cfg.mix);
  if (!fs.existsSync(mp4)) throw new Error(`缺少成片: ${mp4}`);
  if (!fs.existsSync(mixWav)) throw new Error(`缺少混音: ${mixWav}`);

  const decoded = decodeMp4Audio(mp4, `/tmp/verify3_${which}_decoded.wav`);
  const bgm = readWav16(path.join(ROOT, 'audio/emotional_bgm.wav'));
  const expected = mod.getClickTimestamps();
  const { onsets } = detectOnsets(decoded.ch[0], bgm.ch[0], mod.DURATION);

  const offGrid = expected.filter((t) => Math.abs(t * mod.FPS - Math.round(t * mod.FPS)) > 5e-3);

  const matched = [];
  const used = new Set();
  let maxOffset = 0;
  let missed = 0;
  for (const t of expected) {
    let best = -1;
    let bestD = Infinity;
    for (let i = 0; i < onsets.length; i++) {
      if (used.has(i)) continue;
      const d = Math.abs(onsets[i].t - t);
      if (d < bestD) {
        bestD = d;
        best = i;
      }
    }
    if (best >= 0 && bestD <= 0.06) {
      used.add(best);
      matched.push({ expected: t, detected: onsets[best].t, offset: onsets[best].t - t });
      maxOffset = Math.max(maxOffset, Math.abs(onsets[best].t - t));
    } else {
      missed++;
    }
  }
  const spurious = onsets.filter((_, i) => !used.has(i)).map((o) => Number(o.t.toFixed(3)));
  const maxOffsetMs = maxOffset * 1000;
  const frameMs = 1000 / mod.FPS;

  console.log(`=== A/V 同步验证 · ${cfg.label} ===`);
  console.log(`成片            : ${cfg.mp4}`);
  console.log(`期望点击        : ${expected.length}`);
  console.log(`检出 onset      : ${onsets.length}（未匹配 ${spurious.length}${spurious.length ? `: ${spurious.slice(0, 8).join(', ')}${spurious.length > 8 ? ' ...' : ''}` : ''}）`);
  console.log(`匹配成功        : ${matched.length} / ${expected.length}（漏检 ${missed}）`);
  console.log(`最大时间偏差    : ${maxOffsetMs.toFixed(1)}ms（${(maxOffsetMs / frameMs).toFixed(2)} 帧，帧长 ${frameMs.toFixed(2)}ms）`);
  console.log(`帧对齐          : 全部 ${expected.length} 个时间戳${offGrid.length === 0 ? '均落在显示帧上' : ` 有 ${offGrid.length} 个未对齐`}`);

  const ok = missed === 0 && maxOffsetMs < 2 * frameMs && offGrid.length === 0;
  console.log(`\n结果: ${ok ? 'PASSED（敲击音与文字出现严格同步）' : 'FAILED'}`);

  const report = {
    status: ok ? 'PASSED' : 'FAILED',
    generatedAt: new Date().toISOString(),
    method: '解码 MP4 音轨 → 减去 BGM 基线（×0.25 + 1s/2s 淡入淡出）→ 10ms 能量窗口检测 onset → 与 getClickTimestamps() 贪心匹配（≤60ms）',
    source: cfg.mp4,
    expectedClicks: expected.length,
    detectedOnsets: onsets.length,
    matched: matched.length,
    missed,
    unmatchedOnsets: spurious,
    maxOffsetMs: Number(maxOffsetMs.toFixed(3)),
    maxOffsetFrames: Number((maxOffsetMs / frameMs).toFixed(3)),
    frameMs: Number(frameMs.toFixed(3)),
    allTimestampsOnDisplayFrames: offGrid.length === 0,
    subtitleClicks: 0,
    firstClicks: expected.slice(0, 10).map((t) => Number(t.toFixed(3))),
  };
  fs.mkdirSync(path.join(ROOT, cfg.doc), { recursive: true });
  fs.writeFileSync(path.join(ROOT, cfg.doc, 'sync-report.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(`报告: ${cfg.doc}/sync-report.json`);

  if (!ok) process.exit(1);
}

if (require.main === module) main();
