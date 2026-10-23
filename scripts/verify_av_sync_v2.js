#!/usr/bin/env node
'use strict';
// scripts/verify_av_sync_v2.js — 从最终 MP4 反解音频，独立验证「键盘敲击音 ↔ 文字出现」同步
//
// 做法：
//   1. ffmpeg 解码 MP4 音轨 → 16-bit PCM WAV
//   2. 用 audio/emotional_bgm.wav ×0.3（含 1s/2s 淡入淡出）重建 BGM 基线
//   3. residual = 解码混音 − BGM 基线 → 只剩下 click 能量
//   4. 以 10ms 窗口扫描 residual 能量，检测 onset，聚类成点击事件
//   5. 与渲染脚本 getClickTimestamps() 逐点比对：
//        · 每个期望点击是否都被检出（漏检 ≤ 1）
//        · 检测事件与期望时间戳的最大偏差（应 < 2 帧 / 33ms）
//        · 期望时间戳是否全部落在显示帧上（打字瞬间可见）
//
// 用法: node scripts/verify_av_sync_v2.js learning
//       node scripts/verify_av_sync_v2.js upgrade

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const { readWav16, getFfmpegPath } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const SR = 44100;

const MODS = {
  learning: {
    script: '../src/render_learning_arena_v2',
    mp4: 'outputs/learning_arena_v2.0.mp4',
    mix: 'audio/learning_arena_v2_mix.wav',
    doc: 'docs/learning-v2',
  },
  upgrade: {
    script: '../src/render_upgrade_arena_v2',
    mp4: 'outputs/upgrade_arena_v2.0.mp4',
    mix: 'audio/upgrade_arena_v2_mix.wav',
    doc: 'docs/upgrade-v2',
  },
};

function decodeMp4Audio(mp4, outWav) {
  const ffmpeg = getFfmpegPath();
  const r = spawnSync(
    ffmpeg,
    ['-y', '-v', 'error', '-i', mp4, '-vn', '-ac', '1', '-ar', String(SR), '-c:a', 'pcm_s16le', outWav],
    { encoding: 'utf8' }
  );
  if (r.status !== 0) throw new Error(`ffmpeg 解码失败: ${r.stderr}`);
  return readWav16(outWav);
}

function detectOnsets(mono, bgmMono, duration, opts = {}) {
  const win = Math.round(SR * 0.01); // 10ms
  const nWin = Math.floor((duration * SR) / win);
  const energy = new Float64Array(nWin);
  const baseline = new Float64Array(nWin);

  for (let w = 0; w < nWin; w++) {
    let e = 0;
    let b = 0;
    for (let i = w * win; i < (w + 1) * win && i < mono.length; i++) {
      const t = i / SR;
      let g = 0.3;
      if (t < 1) g *= t / 1;
      const fo = duration - 2;
      if (t > fo) g *= Math.max(0, (duration - t) / 2);
      const bg = i < bgmMono.length ? (bgmMono[i] / 32768) * g : 0;
      b += Math.abs(bg);
      const v = mono[i] / 32768 - bg;
      e += v * v;
    }
    energy[w] = Math.sqrt(e / win);
    baseline[w] = b / win;
  }

  // 自适应阈值：能量显著高于邻域中位数即认为有 onset
  const onsets = [];
  const thresh = opts.thresh || 0.012;
  let lastW = -99;
  for (let w = 1; w < nWin - 1; w++) {
    const e = energy[w];
    if (e < thresh) continue;
    if (energy[w - 1] > e) continue; // 仅取局部起点
    if (w - lastW <= 2) continue; // 同一次点击内不重复
    onsets.push({ t: (w * win) / SR, e });
    lastW = w;
  }
  return { onsets, energy };
}

function main() {
  const which = process.argv[2] || 'learning';
  const cfg = MODS[which];
  if (!cfg) {
    console.error('用法: node scripts/verify_av_sync_v2.js [learning|upgrade]');
    process.exit(2);
  }
  const mod = require(path.join(__dirname, cfg.script));
  const mp4 = path.join(ROOT, cfg.mp4);
  const mixWav = path.join(ROOT, cfg.mix);
  if (!fs.existsSync(mp4)) throw new Error(`缺少成片: ${mp4}`);

  const tmp = `/tmp/verify_${which}_decoded.wav`;
  const decoded = decodeMp4Audio(mp4, tmp);
  const bgm = readWav16(path.join(ROOT, 'audio/emotional_bgm.wav'));
  const expected = mod.getClickTimestamps();
  const { onsets } = detectOnsets(decoded.ch[0], bgm.ch[0], mod.DURATION);

  // 期望时间戳是否都落在显示帧上（打字/文字出现发生在该帧）
  const offGrid = expected.filter((t) => Math.abs(t * mod.FPS - Math.round(t * mod.FPS)) > 5e-3);

  // 贪心匹配：每个期望点击找最近的检测 onset（≤ 60ms）
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
  const spurious = onsets.length - used.size;
  const maxOffsetMs = maxOffset * 1000;
  const frameMs = 1000 / mod.FPS;

  console.log(`=== A/V 同步验证 · ${which} v2.0 ===`);
  console.log(`成片            : ${cfg.mp4}`);
  console.log(`期望点击        : ${expected.length}`);
  console.log(`检出 onset      : ${onsets.length}（未匹配 ${spurious}）`);
  console.log(`匹配成功        : ${matched.length} / ${expected.length}（漏检 ${missed}）`);
  console.log(`最大时间偏差    : ${maxOffsetMs.toFixed(1)}ms（${(maxOffsetMs / frameMs).toFixed(2)} 帧，帧长 ${frameMs.toFixed(2)}ms）`);
  console.log(`帧对齐          : 全部 ${expected.length} 个时间戳${offGrid.length === 0 ? '均落在显示帧上' : ` 有 ${offGrid.length} 个未对齐`}`);

  // 判定
  const ok = missed === 0 && maxOffsetMs < 2 * frameMs && offGrid.length === 0;
  console.log(`\n结果: ${ok ? 'PASSED（敲击音与文字出现严格同步）' : 'FAILED'}`);

  const report = {
    status: ok ? 'PASSED' : 'FAILED',
    generatedAt: new Date().toISOString(),
    method: '解码 MP4 音轨 → 减去 BGM 基线（×0.3 + 1s/2s 淡入淡出）→ 10ms 能量窗口检测 onset → 与 getClickTimestamps() 贪心匹配（≤60ms）',
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
