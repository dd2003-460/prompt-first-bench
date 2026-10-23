#!/usr/bin/env node
'use strict';
// E05 惊讶 (surprise) — BGM -12dB + 键盘音 -6dB，click 时间戳来自渲染脚本（每字符 1 次，白屏期间静音）。
// 混音口径与 batch-5 一致：amix normalize=0 等价（scripts/build_audio_v2_common.js 内的确定性 JS 混音，
// 仓库自带的 2018 版 ffmpeg 不支持 amix normalize=0，故混音在 JS 内做，ffmpeg 只负责编码与封装）。
const path = require('path');
const R = require('../src/render_E05_surprise_arena');
const { buildAudio, muxVideo } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const BGM_GAIN = Math.pow(10, -12 / 20);
const SFX_GAIN = Math.pow(10, -6 / 20);
const CLICKS_WAV = process.env.CLICKS_WAV || '/tmp/E05_clicks.wav';
const MIX_WAV = path.join(ROOT, 'audio', 'E05_mix.wav');
const MP4_OUT = path.join(ROOT, 'outputs', 'E05_surprise_arena_v1.0.mp4');

if (require.main === module) {
  const clicks = R.getClickTimestamps();
  const { stats } = buildAudio({
    clickTimestamps: clicks,
    duration: R.DURATION,
    clicksPath: CLICKS_WAV,
    mixPath: MIX_WAV,
    label: 'E05-surprise',
    bgmGain: BGM_GAIN,
    sfxGain: SFX_GAIN,
    fadeIn: 1,
    fadeOut: 2,
  });
  const silent = clicks.filter((t) => t >= R.FLASH_START && t < R.FLASH_END).length;
  console.log(`Clicks: ${clicks.length} (白屏期间 ${silent}); BGM=-12dB SFX=-6dB; peak=${stats.peakDb.toFixed(2)} dBFS; clipped=${stats.clipped}`);
  if (process.argv.includes('--mux')) {
    muxVideo({
      framesDir: process.env.FRAMES_DIR || path.join(ROOT, 'src', 'frames_E05_surprise_arena'),
      mixPath: MIX_WAV,
      outMp4: MP4_OUT,
      fps: R.FPS,
    });
  }
}

module.exports = { CLICKS_WAV, MIX_WAV, MP4_OUT, BGM_GAIN, SFX_GAIN, FADE_IN: 1, FADE_OUT: 2 };
