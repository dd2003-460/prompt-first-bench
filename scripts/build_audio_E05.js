#!/usr/bin/env node
'use strict';
// E05 惊讶: BGM emotional_bgm.wav -12dB + 逐字符 sfx_click.wav -6dB, JS 浮点混音 (等价 amix normalize=0)
const path = require('path');
const R = require('../src/render_E05_surprise_arena');
const { buildAudio, muxVideo } = require('./build_audio_v2_common');
const ROOT = path.resolve(__dirname, '..');
const BGM_GAIN = Math.pow(10, -12 / 20);
const SFX_GAIN = Math.pow(10, -6 / 20);
const CLICKS_WAV = process.env.CLICKS_WAV || '/tmp/E05_arena_clicks.wav';
const MIX_WAV = path.join(ROOT, 'audio', 'E05_surprise_arena_mix.wav');
const MP4_OUT = path.join(ROOT, 'outputs', 'E05_surprise_arena_v1.0.mp4');
const FADE_IN = 1;
const FADE_OUT = 2;

if (require.main === module) {
  const clicks = R.getClickTimestamps();
  const { stats } = buildAudio({
    clickTimestamps: clicks, duration: R.DURATION, clicksPath: CLICKS_WAV, mixPath: MIX_WAV,
    label: 'E05-surprise-v1.0', bgmGain: BGM_GAIN, sfxGain: SFX_GAIN, fadeIn: FADE_IN, fadeOut: FADE_OUT,
  });
  console.log(`Clicks: ${clicks.length}; BGM=-12dB SFX=-6dB; peak=${stats.peakDb.toFixed(2)} dBFS; clipped=${stats.clipped}`);
  if (process.argv.includes('--mux')) muxVideo({
    framesDir: R.OUT_DIR, mixPath: MIX_WAV, outMp4: MP4_OUT, fps: R.FPS,
  });
}
module.exports = { CLICKS_WAV, MIX_WAV, MP4_OUT, BGM_GAIN, SFX_GAIN, FADE_IN, FADE_OUT };
