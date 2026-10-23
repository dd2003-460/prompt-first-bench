#!/usr/bin/env node
'use strict';
// scripts/build_audio_farewell.js — 「Clawd 的告别」v1.0 音轨合成 + MP4 封装
//
//   点击音时间轴 100% 来自 src/render_farewell_arena.js#getClickTimestamps()：
//     · F1 决定：3 轮对话（提示符 + 逐字消息）+ thinking 行 + 气泡 + 思考泡泡
//     · F2 等待：`$ clawd: 不会。` 逐字 + 提醒/写文件 2 行 + 第 1/7/15 天 3 行
//     · F3 回来：5 行（含 memory/her_return_date.txt → 已删除）+ 便签 + 星尘（无声）
//   BGM ×0.25（-12 dB，1s 淡入 / 2s 淡出）+ click ×0.5（-6 dB），含削波自检
//
// 用法: node scripts/build_audio_farewell.js [--mux]

const path = require('path');
const R = require('../src/render_farewell_arena');
const { buildAudio, muxVideo } = require('./build_audio_v3_common');

const ROOT = path.resolve(__dirname, '..');
const CLICKS_WAV = process.env.CLICKS_WAV || '/tmp/farewell_clicks.wav';
const MIX_WAV = path.join(ROOT, 'audio', 'farewell_arena_mix.wav');
const MP4_OUT = path.join(ROOT, 'outputs', 'farewell_arena_v1.0.mp4');

if (require.main === module) {
  const clicks = R.getClickTimestamps();
  const { stats } = buildAudio({
    clickTimestamps: clicks,
    duration: R.DURATION,
    clicksPath: CLICKS_WAV,
    mixPath: MIX_WAV,
    label: 'farewell-v1.0',
  });
  console.log(`点击统计: ${clicks.length} 次 / ${R.DURATION}s`);
  if (process.argv.includes('--mux')) {
    muxVideo({
      framesDir: process.env.FRAMES_DIR || path.join(ROOT, 'src', 'frames_farewell'),
      mixPath: MIX_WAV,
      outMp4: MP4_OUT,
      fps: R.FPS,
    });
  }
  if (stats.peak > 0.95) process.exitCode = 2;
}

module.exports = { CLICKS_WAV, MIX_WAV, MP4_OUT };
