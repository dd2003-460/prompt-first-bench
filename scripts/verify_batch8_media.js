#!/usr/bin/env node
'use strict';
// scripts/verify_batch8_media.js — 对 E13–E16 成片做独立复核（只看 MP4，不复用渲染中间产物）
//
//   1. 容器/编码：h264 High / yuv420p / 1280×720 / 60fps / 1800 帧 / aac 44.1kHz 单声道 / 30s
//   2. 像素标准：解码 3 帧，按 2×2 采样检查最近邻放大特征（每个 2×2 块同色，允许编码误差）
//   3. 音频：解码 AAC → PCM，峰值 / 削波 / 时长
//   4. 节奏：片头淡入(0s)、10.00s 与 20.00s 两处黑场、片尾淡出(29.9s) 的亮度轨迹
//
// 用法: node scripts/verify_batch8_media.js [E13|E14|E15|E16|all]

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const { loadImage, createCanvas } = require('@napi-rs/canvas');
const { readWav16 } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const TMP = path.join(ROOT, '.preview', 'batch8-verify');

const EPISODES = {
  E13: { mp4: 'outputs/E13_longing_arena_v1.0.mp4', mix: 'audio/E13_arena_mix.wav', clicks: 95 },
  E14: { mp4: 'outputs/E14_jealousy_arena_v1.0.mp4', mix: 'audio/E14_arena_mix.wav', clicks: 176 },
  E15: { mp4: 'outputs/E15_forgiveness_arena_v1.0.mp4', mix: 'audio/E15_arena_mix.wav', clicks: 169 },
  E16: { mp4: 'outputs/E16_sacrifice_arena_v1.0.mp4', mix: 'audio/E16_arena_mix.wav', clicks: 155 },
};

function getFfmpeg() {
  if (process.env.FFMPEG_BIN && fs.existsSync(process.env.FFMPEG_BIN)) return process.env.FFMPEG_BIN;
  try {
    const exe = require('child_process').execFileSync('python3', ['-c', 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())'], {
      encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    if (exe && fs.existsSync(exe)) return exe;
  } catch (_) {}
  return path.join(ROOT, 'node_modules/@ffmpeg-installer/linux-x64/ffmpeg');
}

function getFfprobe() {
  const local = path.join(ROOT, 'node_modules/@ffprobe-installer/linux-x64/ffprobe');
  return fs.existsSync(local) ? local : 'ffprobe';
}

const FFMPEG = getFfmpeg();
const FFPROBE = getFfprobe();

function probe(file) {
  const r = spawnSync(FFPROBE, [
    '-v', 'error', '-count_frames',
    '-show_entries', 'format=duration,size,bit_rate',
    '-show_entries', 'stream=codec_type,codec_name,profile,width,height,pix_fmt,r_frame_rate,nb_read_frames,sample_rate,channels,duration',
    '-of', 'json', file,
  ], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`ffprobe: ${r.stderr}`);
  return JSON.parse(r.stdout);
}

function extractFrame(mp4, n, out) {
  const r = spawnSync(FFMPEG, ['-y', '-v', 'error', '-i', mp4, '-vf', `select=eq(n\\,${n})`, '-frames:v', '1', out], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`decode frame ${n}: ${r.stderr}`);
  return out;
}

function extractAudio(mp4, out) {
  const r = spawnSync(FFMPEG, ['-y', '-v', 'error', '-i', mp4, '-vn', '-ac', '1', '-ar', '44100', '-c:a', 'pcm_s16le', out], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`decode audio: ${r.stderr}`);
  return out;
}

function luminanceAt(mp4, sec) {
  // 取该时刻 1 帧，返回平均亮度（0..1）
  const out = path.join(TMP, `lum_${sec.toFixed(2)}.png`);
  const r = spawnSync(FFMPEG, ['-y', '-v', 'error', '-ss', String(sec), '-i', mp4, '-frames:v', '1', out], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`luma frame ${sec}: ${r.stderr}`);
  return readPng(out).then((im) => {
    let sum = 0;
    const n = im.w * im.h;
    for (let i = 0; i < n; i++) {
      const k = i * 4;
      sum += 0.2126 * im.d[k] + 0.7152 * im.d[k + 1] + 0.0722 * im.d[k + 2];
    }
    return sum / n / 255;
  });
}

async function readPng(file) {
  const img = await loadImage(file);
  const cv = createCanvas(img.width, img.height);
  const ctx = cv.getContext('2d');
  ctx.drawImage(img, 0, 0);
  return { w: img.width, h: img.height, d: ctx.getImageData(0, 0, img.width, img.height).data };
}

function nearest2xRatio(im) {
  // 每个 2×2 块是否近似同色（编码噪声容差 ±6）
  let blocks = 0;
  let same = 0;
  for (let y = 0; y + 1 < im.h; y += 2) {
    for (let x = 0; x + 1 < im.w; x += 2) {
      const a = (y * im.w + x) * 4;
      const b = (y * im.w + x + 1) * 4;
      const c = ((y + 1) * im.w + x) * 4;
      const d = ((y + 1) * im.w + x + 1) * 4;
      blocks++;
      const ok = [0, 1, 2].every((k) =>
        Math.abs(im.d[a + k] - im.d[b + k]) <= 6 &&
        Math.abs(im.d[a + k] - im.d[c + k]) <= 6 &&
        Math.abs(im.d[a + k] - im.d[d + k]) <= 6);
      if (ok) same++;
    }
  }
  return { ratio: same / blocks, blocks };
}

async function verifyEpisode(id) {
  const cfg = EPISODES[id];
  const mp4 = path.join(ROOT, cfg.mp4);
  const issues = [];
  const info = probe(mp4);
  const v = (info.streams || []).find((s) => s.codec_type === 'video');
  const a = (info.streams || []).find((s) => s.codec_type === 'audio');
  const duration = Number(info.format.duration);

  if (!v) issues.push('missing video stream');
  else {
    if (v.codec_name !== 'h264') issues.push(`video codec ${v.codec_name} ≠ h264`);
    if (v.pix_fmt !== 'yuv420p') issues.push(`pix_fmt ${v.pix_fmt} ≠ yuv420p`);
    if (v.width !== 1280 || v.height !== 720) issues.push(`size ${v.width}×${v.height} ≠ 1280×720`);
    if (v.r_frame_rate !== '60/1') issues.push(`fps ${v.r_frame_rate} ≠ 60/1`);
    if (Number(v.nb_read_frames) !== 1800) issues.push(`frames ${v.nb_read_frames} ≠ 1800`);
  }
  if (!a) issues.push('missing audio stream');
  else {
    if (a.codec_name !== 'aac') issues.push(`audio codec ${a.codec_name} ≠ aac`);
    if (Number(a.sample_rate) !== 44100) issues.push(`sample rate ${a.sample_rate} ≠ 44100`);
    if (Number(a.channels) !== 1) issues.push(`channels ${a.channels} ≠ 1`);
  }
  if (!(Math.abs(duration - 30) <= 0.06)) issues.push(`duration ${duration.toFixed(3)}s ≠ 30s ±0.06`);

  // 像素：3 帧最近邻特征
  const pixelSamples = [];
  for (const n of [240, 900, 1560]) {
    const png = extractFrame(mp4, n, path.join(TMP, `${id}_f${n}.png`));
    const im = await readPng(png);
    const { ratio } = nearest2xRatio(im);
    pixelSamples.push({ frame: n, ratio: Number(ratio.toFixed(4)) });
    if (ratio < 0.995) issues.push(`frame ${n}: only ${(ratio * 100).toFixed(2)}% of 2×2 blocks are uniform`);
  }

  // 音频
  const wavPath = extractAudio(mp4, path.join(TMP, `${id}_a.wav`));
  const wav = readWav16(wavPath);
  let peak = 0;
  let clipped = 0;
  for (const v2 of wav.ch[0]) {
    const abs = Math.abs(v2);
    if (abs > peak) peak = abs;
    if (abs >= 32760) clipped++;
  }
  const audio = {
    peakDb: Number((20 * Math.log10(peak / 32768)).toFixed(2)),
    clipped,
    duration: Number((wav.samples / wav.sampleRate).toFixed(3)),
  };
  if (clipped > 0) issues.push(`audio clipping: ${clipped} samples`);
  if (audio.duration < 29.9 || audio.duration > 30.1) issues.push(`audio duration ${audio.duration}s out of range`);

  // 混音轨一致性（成片音频 vs audio/*_mix.wav）
  const mix = readWav16(path.join(ROOT, cfg.mix));
  const n = Math.min(mix.samples, wav.samples);
  let dot = 0, na = 0, nb = 0;
  for (let i = 0; i < n; i++) {
    const x = mix.ch[0][i];
    const y = wav.ch[0][i];
    dot += x * y; na += x * x; nb += y * y;
  }
  const correlation = na && nb ? Number((dot / Math.sqrt(na * nb)).toFixed(4)) : 0;
  if (correlation < 0.98) issues.push(`mix/encode correlation ${correlation} < 0.98`);

  // 亮度节奏
  const luma = {
    fadeIn0: Number((await luminanceAt(mp4, 0)).toFixed(3)),
    midScene5: Number((await luminanceAt(mp4, 5)).toFixed(3)),
    at10: Number((await luminanceAt(mp4, 10.0)).toFixed(3)),
    at20: Number((await luminanceAt(mp4, 20.0)).toFixed(3)),
    end29_9: Number((await luminanceAt(mp4, 29.9)).toFixed(3)),
  };
  if (luma.fadeIn0 > 0.02) issues.push(`first frame not black (${luma.fadeIn0})`);
  if (luma.at10 > 0.08) issues.push(`10s transition frame is not dark (${luma.at10})`);
  if (luma.at20 > 0.08) issues.push(`20s transition frame is not dark (${luma.at20})`);
  // 片尾 0.8s 淡出：29.9s 应只剩片中的 ~1/8 亮度
  if (luma.end29_9 > 0.06 || luma.end29_9 > 0.2 * luma.midScene5) {
    issues.push(`tail not faded out (${luma.end29_9} vs mid ${luma.midScene5})`);
  }
  if (luma.midScene5 < 0.05) issues.push(`scene 1 looks blank (${luma.midScene5})`);

  const report = {
    status: issues.length ? 'FAILED' : 'PASSED',
    generatedAt: new Date().toISOString(),
    episode: id,
    file: cfg.mp4,
    sizeBytes: fs.statSync(mp4).size,
    container: {
      video: v ? { codec: v.codec_name, profile: v.profile, width: v.width, height: v.height, pixFmt: v.pix_fmt, fps: v.r_frame_rate, frames: Number(v.nb_read_frames) } : null,
      audio: a ? { codec: a.codec_name, sampleRate: Number(a.sample_rate), channels: Number(a.channels) } : null,
      duration,
    },
    pixels: { method: '2×2 block uniformity on decoded frames', samples: pixelSamples },
    audio: { ...audio, correlationToMixWav: correlation, clicks: cfg.clicks },
    luma,
    issues,
  };
  fs.mkdirSync(path.join(ROOT, 'docs', 'batch-8', id), { recursive: true });
  fs.writeFileSync(path.join(ROOT, 'docs', 'batch-8', id, 'media-report.json'), JSON.stringify(report, null, 2) + '\n');
  return report;
}

(async () => {
  fs.mkdirSync(TMP, { recursive: true });
  const arg = process.argv[2] || 'all';
  const ids = arg === 'all' ? Object.keys(EPISODES) : [arg];
  let failed = 0;
  for (const id of ids) {
    const r = await verifyEpisode(id);
    failed += r.issues.length ? 1 : 0;
    console.log(`[${r.issues.length ? 'FAIL' : 'PASS'}] ${id} ${r.container.video.width}×${r.container.video.height} ${r.container.duration.toFixed(2)}s ` +
      `${r.container.video.frames}f · audio peak ${r.audio.peakDb} dBFS · corr ${r.audio.correlationToMixWav} · luma ${JSON.stringify(r.luma)}`);
    for (const msg of r.issues) console.log(`   - ${msg}`);
  }
  console.log(failed ? `${failed} episode(s) FAILED` : 'All episodes PASSED');
  process.exit(failed ? 1 : 0);
})().catch((err) => {
  console.error(err);
  process.exit(1);
});
