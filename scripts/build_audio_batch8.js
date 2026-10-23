#!/usr/bin/env node
'use strict';
// scripts/build_audio_batch8.js — batch-8 (E13–E16) 共用音轨合成 / 封装
//
//   BGM : audio/emotional_bgm.wav  → volume=0.251189 (-12dB) + 1s 淡入 / 2s 淡出
//   SFX : audio/sfx_click.wav      → volume=0.501187 (-6dB)，每字符 1 次 click
//   混音: ffmpeg `amix=inputs=2:duration=first:dropout_transition=0:normalize=0`
//         （SOP 04 指定；旧版 ffmpeg 不支持 normalize 选项时退化为
//           normalize=1 的等值补偿增益，输出逐样本一致，日志会注明）
//   封装: libx264 crf18 + aac 192k + yuv420p + faststart，-shortest
//
//   ffmpeg 解析顺序: FFMPEG_BIN → PATH 中的 ffmpeg → imageio-ffmpeg → 仓库内 @ffmpeg-installer
//   仓库自带的 2018 版 ffmpeg 没有 amix normalize，正常路径请提供 ≥4.4 的 ffmpeg。

const fs = require('fs');
const path = require('path');
const { spawnSync, execFileSync } = require('child_process');
const { readWav16, writeWav16, inspectMixNoClipping } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const AUDIO = path.join(ROOT, 'audio');
const BGM = path.join(AUDIO, 'emotional_bgm.wav');
const SFX = path.join(AUDIO, 'sfx_click.wav');
const SAMPLE_RATE = 44100;
const BGM_GAIN = Math.pow(10, -12 / 20); // -12 dB
const SFX_GAIN = Math.pow(10, -6 / 20);  // -6 dB

function ffmpegCandidates() {
  const list = [];
  if (process.env.FFMPEG_BIN) list.push(process.env.FFMPEG_BIN);
  try {
    const exe = execFileSync('python3', ['-c', 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())'], {
      encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    if (exe) list.push(exe);
  } catch (_) {}
  list.push('ffmpeg', '/usr/local/bin/ffmpeg', '/usr/bin/ffmpeg');
  // 仓库自带的 2018 版 ffmpeg 没有 amix normalize；放在最后，只做兜底（等值补偿增益）。
  list.push(path.join(ROOT, 'node_modules/@ffmpeg-installer/linux-x64/ffmpeg'));
  return list;
}

function runFfmpeg(bin, args, opts = {}) {
  const res = spawnSync(bin, args, { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024, ...opts });
  if (res.error) throw res.error;
  if (res.status !== 0) throw new Error(`ffmpeg failed (${res.status}): ${res.stderr}`);
  return res;
}

let _ffmpeg = null;
function getFfmpeg() {
  if (_ffmpeg) return _ffmpeg;
  const tried = [];
  for (const bin of ffmpegCandidates()) {
    if (!bin) continue;
    try {
      const help = spawnSync(bin, ['-hide_banner', '-h', 'filter=amix'], { encoding: 'utf8' });
      if (help.error || help.status !== 0) { tried.push(bin); continue; }
      _ffmpeg = { bin, hasNormalize: /\bnormalize\b/.test(help.stdout || '') };
      return _ffmpeg;
    } catch (_) {
      tried.push(bin);
    }
  }
  throw new Error(`no usable ffmpeg found (tried: ${tried.join(', ') || 'none'})`);
}

/** 生成点击轨：每个时间戳放一次 sfx_click.wav，1.0 幅度，增益在 ffmpeg 里做。 */
function buildClickTrack(clickTimestamps, duration, outPath) {
  const sfx = readWav16(SFX);
  if (sfx.sampleRate !== SAMPLE_RATE) throw new Error(`sfx_click.wav: ${sfx.sampleRate}Hz ≠ ${SAMPLE_RATE}Hz`);
  const src = sfx.ch[0];
  const total = Math.round(duration * SAMPLE_RATE);
  const track = new Float64Array(total);
  for (const t of clickTimestamps) {
    const off = Math.round(t * SAMPLE_RATE);
    for (let i = 0; i < src.length; i++) {
      const idx = off + i;
      if (idx >= 0 && idx < total) track[idx] += src[i] / 32768;
    }
  }
  let peak = 0;
  for (let i = 0; i < total; i++) peak = Math.max(peak, Math.abs(track[i]));
  const guard = peak > 0.98 ? 0.98 / peak : 1;
  const pcm = new Int16Array(total);
  for (let i = 0; i < total; i++) pcm[i] = Math.max(-32768, Math.min(32767, Math.round(track[i] * guard * 32767)));
  writeWav16(outPath, SAMPLE_RATE, 1, [pcm]);
  return { count: clickTimestamps.length, peak, guard };
}

function mixTracks({ clicksPath, mixPath, duration, bgmGain = BGM_GAIN, sfxGain = SFX_GAIN, fadeIn = 1, fadeOut = 2, label = 'batch-8' }) {
  const { bin, hasNormalize } = getFfmpeg();
  const fadeOutStart = Math.max(0, duration - fadeOut);
  // 旧 ffmpeg 的 amix 固定按输入数归一（÷2）；把两个增益都 ×2 即可得到 normalize=0 的等值输出。
  const k = hasNormalize ? 1 : 2;
  const filter = [
    `[0:a]volume=${(sfxGain * k).toFixed(6)}[click]`,
    `[1:a]volume=${(bgmGain * k).toFixed(6)},afade=t=in:st=0:d=${fadeIn},afade=t=out:st=${fadeOutStart}:d=${fadeOut}[bgm]`,
    `[click][bgm]amix=inputs=2:duration=first:dropout_transition=0${hasNormalize ? ':normalize=0' : ''}[mix]`,
  ].join(';');
  fs.mkdirSync(path.dirname(mixPath), { recursive: true });
  runFfmpeg(bin, [
    '-y', '-hide_banner', '-loglevel', 'error',
    '-i', clicksPath, '-i', BGM,
    '-filter_complex', filter,
    '-map', '[mix]', '-t', String(duration),
    '-ar', String(SAMPLE_RATE), '-ac', '1', '-c:a', 'pcm_s16le', mixPath,
  ]);
  const stats = inspectMixNoClipping(mixPath);
  console.log(
    `[${label}] ffmpeg=${bin} amix=${hasNormalize ? 'normalize=0' : 'default-normalize (compensated ×2)'} | ` +
    `BGM=${(20 * Math.log10(bgmGain)).toFixed(1)}dB SFX=${(20 * Math.log10(sfxGain)).toFixed(1)}dB | ` +
    `peak=${stats.peakDb.toFixed(2)} dBFS | clipped=${stats.clipped} | ${stats.duration.toFixed(2)}s`
  );
  if (stats.clipped > 0) throw new Error(`削波: ${stats.clipped} samples`);
  if (Math.abs(stats.duration - duration) > 0.05) throw new Error(`混音时长 ${stats.duration}s ≠ ${duration}s`);
  return stats;
}

function muxVideo({ framesDir, mixPath, outMp4, fps = 60, label = 'batch-8' }) {
  const { bin } = getFfmpeg();
  fs.mkdirSync(path.dirname(outMp4), { recursive: true });
  runFfmpeg(bin, [
    '-y', '-hide_banner', '-loglevel', 'error',
    '-framerate', String(fps), '-i', path.join(framesDir, 'f_%05d.png'),
    '-i', mixPath,
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '18',
    '-r', String(fps), '-c:a', 'aac', '-b:a', '192k',
    '-shortest', '-movflags', '+faststart',
    outMp4,
  ]);
  const size = fs.statSync(outMp4).size;
  console.log(`[${label}] 封装完成: ${outMp4} (${(size / 1024 / 1024).toFixed(2)} MB)`);
  return outMp4;
}

function buildEpisodeAudio(opts) {
  const { renderer, episode, framesDir, outMp4 } = opts;
  const label = `${episode} ${renderer.CHECK_TITLE.split(' ')[1] || ''} v1.0`.trim();
  const clicksPath = process.env.CLICKS_WAV || `/tmp/${episode}_arena_clicks.wav`;
  const mixPath = path.join(AUDIO, `${episode}_arena_mix.wav`);
  const clicks = renderer.getClickTimestamps();
  const track = buildClickTrack(clicks, renderer.DURATION, clicksPath);
  console.log(`[${label}] click 轨: ${clicksPath} · ${track.count} clicks (每字符 1 次) · ${renderer.DURATION}s`);
  const stats = mixTracks({ clicksPath, mixPath, duration: renderer.DURATION, label });
  if (process.argv.includes('--mux')) {
    muxVideo({ framesDir, mixPath, outMp4, fps: renderer.FPS, label });
  }
  return { clicks: track.count, mixPath, stats };
}

module.exports = {
  ROOT, AUDIO, BGM, SFX, SAMPLE_RATE, BGM_GAIN, SFX_GAIN,
  getFfmpeg, buildClickTrack, mixTracks, muxVideo, buildEpisodeAudio,
};
