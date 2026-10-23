#!/usr/bin/env node
'use strict';
// E13 音轨: emotional_bgm.wav (-12dB) + 每字符一次 sfx_click.wav (-6dB)，30s；
// 混音 = ffmpeg amix normalize=0（SOP 04），封装 libx264 crf18 + aac 192k。
const path = require('path');
const R = require('../src/render_E13_longing_arena');
const { buildEpisodeAudio } = require('./build_audio_batch8');

const ROOT = path.resolve(__dirname, '..');
const FRAMES_DIR = process.env.FRAMES_DIR || path.join(ROOT, 'src', 'frames_E13_arena');
const MP4_OUT = path.join(ROOT, 'outputs', 'E13_longing_arena_v1.0.mp4');

if (require.main === module) {
  buildEpisodeAudio({ renderer: R, episode: 'E13', framesDir: FRAMES_DIR, outMp4: MP4_OUT });
}
module.exports = { FRAMES_DIR, MP4_OUT };
