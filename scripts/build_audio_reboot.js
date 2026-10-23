#!/usr/bin/env node
'use strict';
// scripts/build_audio_reboot.js — 「Clawd 的重启」v1.0 音轨合成 + MP4 封装
//
//   点击音时间轴 100% 来自 src/render_reboot_arena.js#getClickTimestamps()：
//     · R1 关机：`$ her: clawd, 关机`（逐字 140ms）+ `$ clawd: 好的...`（逐字）+ 4 条整行
//     · R2 黑暗：无点击（只有电源灯亮起的电源音效）
//     · R3 重启：4 条启动日志行 + `✓ 欢迎回来。上次聊到哪里了？` 逐字 + memory 行
//   电源音效（audio/sfx_power_off.wav / sfx_power_on.wav）：
//     · 6.20s 关机（电源灯熄灭，×0.35）
//     · 13.00s 电源灯亮起（×0.40）
//     · 24.60s Clawd 亮起 smile（×0.22）
//   BGM ×0.25（-12 dB，1s 淡入 / 2s 淡出）+ click ×0.5（-6 dB），含削波自检
//
// 用法: node scripts/build_audio_reboot.js [--mux]
//       FRAMES_DIR=/tmp/frames_reboot node scripts/build_audio_reboot.js --mux

const path = require('path');
const R = require('../src/render_reboot_arena');
const { buildAudio, muxVideo } = require('./build_audio_v3_common');

const ROOT = path.resolve(__dirname, '..');
const CLICKS_WAV = process.env.CLICKS_WAV || '/tmp/reboot_clicks.wav';
const MIX_WAV = path.join(ROOT, 'audio', 'reboot_arena_mix.wav');
const MP4_OUT = path.join(ROOT, 'outputs', 'reboot_arena_v1.0.mp4');

const SFX_FILES = {
  off: path.join(ROOT, 'audio', 'sfx_power_off.wav'),
  on: path.join(ROOT, 'audio', 'sfx_power_on.wav'),
};

if (require.main === module) {
  const clicks = R.getClickTimestamps();
  const sfxEvents = R.SFX_EVENTS.map((e) => ({ t: e.t, file: SFX_FILES[e.key], gain: e.gain, label: e.key }));
  const { stats } = buildAudio({
    clickTimestamps: clicks,
    duration: R.DURATION,
    clicksPath: CLICKS_WAV,
    mixPath: MIX_WAV,
    label: 'reboot-v1.0',
    sfxEvents,
  });
  console.log(`点击统计: ${clicks.length} 次 / ${R.DURATION}s · 电源音效 ${sfxEvents.length} 次`);
  if (process.argv.includes('--mux')) {
    muxVideo({
      framesDir: process.env.FRAMES_DIR || path.join(ROOT, 'src', 'frames_reboot'),
      mixPath: MIX_WAV,
      outMp4: MP4_OUT,
      fps: R.FPS,
    });
  }
  if (stats.peak > 0.95) process.exitCode = 2;
}

module.exports = { CLICKS_WAV, MIX_WAV, MP4_OUT };
