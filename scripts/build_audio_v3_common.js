#!/usr/bin/env node
'use strict';
// scripts/build_audio_v3_common.js — companion v1.1 / reboot / dialogue / farewell 共用音轨合成与封装
//
//   BGM : audio/emotional_bgm.wav  ×0.25  (-12 dB，1s 淡入 / 2s 淡出，截取 30s)
//   SFX : audio/sfx_click.wav      ×0.50  (-6 dB，每行/每字出现一次，时刻来自渲染脚本 same-frame 时间轴)
//         可选附加音效 audio/sfx_power_off.wav / sfx_power_on.wav（reboot 的关机/重启）
//   混合: JS 内确定性浮点混音（等价 amix=normalize=0），最后一次量化到 PCM16；
//         峰值超 -0.5 dBFS 时整体等比缩放并打印 [clip-guard]
//   封装: libx264 + aac 192k + yuv420p，-shortest
//
// 说明：仓库自带的 @ffmpeg-installer/ffmpeg 为旧构建，amix 不支持 normalize=0，
//       因此混音在 JS 内完成（结果确定、可逐样本审计），ffmpeg 只负责编码与封装。

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const { readWav16, writeWav16, inspectMixNoClipping, getFfmpegPath } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const AUDIO = path.join(ROOT, 'audio');
const BGM = path.join(AUDIO, 'emotional_bgm.wav');
const SFX_CLICK = path.join(AUDIO, 'sfx_click.wav');
const SAMPLE_RATE = 44100;

const BGM_GAIN = 0.25; // -12 dB
const CLICK_GAIN = 0.5; // -6 dB
const FADE_IN_S = 1.0;
const FADE_OUT_S = 2.0;

const _wavCache = new Map();
function loadWav(file) {
  if (!_wavCache.has(file)) _wavCache.set(file, readWav16(file));
  return _wavCache.get(file);
}

/**
 * 合成整条音轨
 * @param {object} o
 * @param {number[]} o.clickTimestamps  渲染脚本 getClickTimestamps()
 * @param {number} o.duration           秒
 * @param {string} o.clicksPath         中间点击轨输出
 * @param {string} o.mixPath            混音轨输出
 * @param {string} o.label              日志标签
 * @param {Array<{t:number,file:string,gain:number,label?:string}>} [o.sfxEvents] 附加音效
 */
function buildAudio(o) {
  const { clickTimestamps, duration, clicksPath, mixPath, label } = o;
  const sfxEvents = o.sfxEvents || [];
  if (!fs.existsSync(AUDIO)) fs.mkdirSync(AUDIO, { recursive: true });

  const click = loadWav(SFX_CLICK).ch[0];
  const totalSamples = Math.round(duration * SAMPLE_RATE);

  // 1) 点击轨（先按满幅叠加，评估是否需要缩放）
  const clickSum = new Int32Array(totalSamples);
  for (const t of clickTimestamps) {
    const off = Math.round(t * SAMPLE_RATE);
    for (let i = 0; i < click.length; i++) {
      const idx = off + i;
      if (idx >= 0 && idx < totalSamples) clickSum[idx] += click[i];
    }
  }
  let rawPeak = 0;
  for (let i = 0; i < totalSamples; i++) rawPeak = Math.max(rawPeak, Math.abs(clickSum[i]));
  const guard = rawPeak > 32767 * 0.85 ? (32767 * 0.85) / rawPeak : 1;
  if (guard < 1) console.log(`[clip-guard] click 轨理论峰值 ${(rawPeak / 32768).toFixed(3)}，整体缩放 x${guard.toFixed(3)}`);
  const clicks = new Int16Array(totalSamples);
  for (let i = 0; i < totalSamples; i++) clicks[i] = Math.max(-32768, Math.min(32767, Math.round(clickSum[i] * guard)));
  writeWav16(clicksPath, SAMPLE_RATE, 1, [clicks]);
  console.log(`[${label}] 点击轨: ${clicksPath} (${clickTimestamps.length} clicks, ${duration}s)`);

  // 2) 附加音效轨（电源开关等）
  const extra = new Float64Array(totalSamples);
  for (const ev of sfxEvents) {
    const wav = loadWav(ev.file);
    const mono = wav.ch[0];
    const off = Math.round(ev.t * SAMPLE_RATE);
    for (let i = 0; i < mono.length; i++) {
      const idx = off + i;
      if (idx >= 0 && idx < totalSamples) extra[idx] += (mono[i] / 32768) * ev.gain;
    }
  }

  // 3) 确定性混音 BGM×0.25（含淡入淡出） + click×0.5 + extra
  const bgm = loadWav(BGM);
  if (bgm.sampleRate !== SAMPLE_RATE || bgm.bits !== 16) throw new Error(`BGM 规格不符: ${bgm.sampleRate}Hz/${bgm.bits}bit`);
  const bgmMono = bgm.ch[0];
  const mix = new Float64Array(totalSamples);
  for (let i = 0; i < totalSamples; i++) {
    const t = i / SAMPLE_RATE;
    let g = o.bgmGain === undefined ? BGM_GAIN : o.bgmGain;
    if (t < FADE_IN_S) g *= t / FADE_IN_S;
    if (t > duration - FADE_OUT_S) g *= Math.max(0, (duration - t) / FADE_OUT_S);
    const b = i < bgmMono.length ? bgmMono[i] : 0;
    mix[i] = (b / 32768) * g + (clicks[i] / 32768) * (o.clickGain === undefined ? CLICK_GAIN : o.clickGain) + extra[i];
  }

  // 4) 峰值保护（-0.5 dBFS）
  let peak = 0;
  for (let i = 0; i < totalSamples; i++) peak = Math.max(peak, Math.abs(mix[i]));
  const LIMIT = 0.944;
  if (peak > LIMIT) {
    const k = LIMIT / peak;
    console.log(`[clip-guard] 混音峰值 ${peak.toFixed(4)} 超限，整体缩放 x${k.toFixed(3)}`);
    for (let i = 0; i < totalSamples; i++) mix[i] *= k;
    peak = LIMIT;
  }

  const out = new Int16Array(totalSamples);
  let clipped = 0;
  for (let i = 0; i < totalSamples; i++) {
    let v = Math.round(mix[i] * 32767);
    if (v > 32767) { v = 32767; clipped++; }
    if (v < -32768) { v = -32768; clipped++; }
    out[i] = v;
  }
  writeWav16(mixPath, SAMPLE_RATE, 1, [out]);

  const stats = inspectMixNoClipping(mixPath);
  if (stats.clipped > 0) throw new Error(`检测到削波：${stats.clipped} samples`);
  console.log(
    `[${label}] 混音: ${mixPath} | peak=${stats.peak.toFixed(4)} (${stats.peakDb.toFixed(2)} dBFS) | clipped=0 | ${stats.duration.toFixed(2)}s | click=${clickTimestamps.length}` +
      (sfxEvents.length ? ` | 附加音效=${sfxEvents.length}` : '')
  );
  return { mixPath, clicksCount: clickTimestamps.length, stats };
}

function muxVideo(o) {
  const { framesDir, mixPath, outMp4, fps } = o;
  const ffmpeg = getFfmpegPath();
  fs.mkdirSync(path.dirname(outMp4), { recursive: true });
  const ff = spawnSync(
    ffmpeg,
    [
      '-y',
      '-framerate', String(fps),
      '-i', path.join(framesDir, 'f_%05d.png'),
      '-i', mixPath,
      '-c:v', 'libx264',
      '-pix_fmt', 'yuv420p',
      '-preset', 'medium',
      '-crf', '18',
      '-r', String(fps),
      '-c:a', 'aac',
      '-b:a', '192k',
      '-shortest',
      '-movflags', '+faststart',
      outMp4,
    ],
    { encoding: 'utf8' }
  );
  if (ff.error) throw ff.error;
  if (ff.status !== 0) {
    console.error(ff.stderr);
    throw new Error(`ffmpeg mux failed with status ${ff.status}`);
  }
  console.log(`封装完成: ${outMp4}`);
  return outMp4;
}

module.exports = { buildAudio, muxVideo, BGM_GAIN, CLICK_GAIN, SAMPLE_RATE, ROOT, AUDIO, BGM, SFX_CLICK };
