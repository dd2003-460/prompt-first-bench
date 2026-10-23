#!/usr/bin/env node
'use strict';
// scripts/build_audio_companion_v11.js — 「Clawd 的陪伴」v1.1 音轨合成 + MP4 封装
//
//   点击音时间轴 100% 来自 src/render_companion_arena_v11.js#getClickTimestamps()：
//     · 终端行：提示符/整行出现 1 次 click，消息逐字 140ms/字 每字 1 次
//     · 浮层（气泡 / 独白卡 / 咖啡杯 / 便签）出现各 1 次
//     · 字幕切换不发声（SOP 04）
//     全部量化到显示帧，同帧合并 → 与画面严格同步
//   BGM ×0.25（-12 dB，1s 淡入 / 2s 淡出）+ click ×0.5（-6 dB），含削波自检
//
// 用法: node scripts/build_audio_companion_v11.js           → audio/companion_arena_v11_mix.wav
//       node scripts/build_audio_companion_v11.js --mux     → 同时封装 outputs/companion_arena_v1.1.mp4
//       FRAMES_DIR=/tmp/frames_companion_v11 node ... --mux

const path = require('path');
const R = require('../src/render_companion_arena_v11');
const { buildAudio, muxVideo } = require('./build_audio_v3_common');

const ROOT = path.resolve(__dirname, '..');
const CLICKS_WAV = process.env.CLICKS_WAV || '/tmp/companion_v11_clicks.wav';
const MIX_WAV = path.join(ROOT, 'audio', 'companion_arena_v11_mix.wav');
const MP4_OUT = path.join(ROOT, 'outputs', 'companion_arena_v1.1.mp4');

if (require.main === module) {
  const clicks = R.getClickTimestamps();
  const { stats } = buildAudio({
    clickTimestamps: clicks,
    duration: R.DURATION,
    clicksPath: CLICKS_WAV,
    mixPath: MIX_WAV,
    label: 'companion-v1.1',
  });
  console.log(`点击统计: ${clicks.length} 次 / ${R.DURATION}s`);
  if (process.argv.includes('--mux')) {
    muxVideo({
      framesDir: process.env.FRAMES_DIR || path.join(ROOT, 'src', 'frames_companion_v11'),
      mixPath: MIX_WAV,
      outMp4: MP4_OUT,
      fps: R.FPS,
    });
  }
  if (stats.peak > 0.95) process.exitCode = 2;
}

module.exports = { CLICKS_WAV, MIX_WAV, MP4_OUT };
