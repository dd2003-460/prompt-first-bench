#!/usr/bin/env node
'use strict';
// scripts/build_audio_dialogue.js — 「Clawd 的对话」v1.0 音轨合成 + MP4 封装
//
//   点击音时间轴 100% 来自 src/render_dialogue_arena.js#getClickTimestamps()：
//     · D1 早安：4 轮对话（每轮提示符 1 次 + 消息逐字 140ms）+ intent 行
//     · D2 理解：5 行（含 [clawd: 检测 → 情感] 行）+ 思考泡泡 ... → ? → !
//     · D3 陪伴：5 行 + 便签 + 星尘（无声）
//     全部量化到显示帧、同帧合并 → 与字形出现严格同步
//   BGM ×0.25（-12 dB，1s 淡入 / 2s 淡出）+ click ×0.5（-6 dB），含削波自检
//
// 用法: node scripts/build_audio_dialogue.js [--mux]

const path = require('path');
const R = require('../src/render_dialogue_arena');
const { buildAudio, muxVideo } = require('./build_audio_v3_common');

const ROOT = path.resolve(__dirname, '..');
const CLICKS_WAV = process.env.CLICKS_WAV || '/tmp/dialogue_clicks.wav';
const MIX_WAV = path.join(ROOT, 'audio', 'dialogue_arena_mix.wav');
const MP4_OUT = path.join(ROOT, 'outputs', 'dialogue_arena_v1.0.mp4');

if (require.main === module) {
  const clicks = R.getClickTimestamps();
  const { stats } = buildAudio({
    clickTimestamps: clicks,
    duration: R.DURATION,
    clicksPath: CLICKS_WAV,
    mixPath: MIX_WAV,
    label: 'dialogue-v1.0',
  });
  console.log(`点击统计: ${clicks.length} 次 / ${R.DURATION}s`);
  if (process.argv.includes('--mux')) {
    muxVideo({
      framesDir: process.env.FRAMES_DIR || path.join(ROOT, 'src', 'frames_dialogue'),
      mixPath: MIX_WAV,
      outMp4: MP4_OUT,
      fps: R.FPS,
    });
  }
  if (stats.peak > 0.95) process.exitCode = 2;
}

module.exports = { CLICKS_WAV, MIX_WAV, MP4_OUT };
