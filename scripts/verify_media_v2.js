#!/usr/bin/env node
'use strict';
// scripts/verify_media_v2.js — 对最终 MP4 做独立复核，并写出 docs/*-v2/media-report.json
//
// 复核项（全部来自成片本身，不复用渲染中间产物）：
//   1. 容器/编码：h264 High / yuv420p / 1280×720 / 60fps / 30.000s / 1800 帧 / aac 44.1kHz 单声道
//   2. 像素标准：解码帧按 2×2 采样，每个 2×2 块同色（最近邻 2× 放大特征）；
//      Clawd 眼睛暗块 8×8、窗棂 12px（均为基础像素 ×2）
//   3. 音频：解码 AAC → PCM，峰值 / 削波 / 时长 / 与 audio/*_mix.wav 的相关系数
//   4. 亮度：片头淡入、10s/20s 黑场、片尾淡出位置
//
// 用法: node scripts/verify_media_v2.js [learning|upgrade|all]

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');
const { loadImage, createCanvas } = require('@napi-rs/canvas');
const { readWav16, getFfmpegPath } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const FFMPEG = getFfmpegPath();

const JOBS = {
  learning: { mp4: 'outputs/learning_arena_v2.0.mp4', mix: 'audio/learning_arena_v2_mix.wav', doc: 'docs/learning-v2' },
  upgrade: { mp4: 'outputs/upgrade_arena_v2.0.mp4', mix: 'audio/upgrade_arena_v2_mix.wav', doc: 'docs/upgrade-v2' },
};

const CLAWD_BASE = { x: 52, y: 240 };

function ffprobe(file) {
  const local = path.join(ROOT, 'node_modules/@ffprobe-installer/linux-x64/ffprobe');
  const bin = fs.existsSync(local) ? local : 'ffprobe';
  const r = spawnSync(
    bin,
    ['-v', 'error', '-show_entries', 'format=duration,size,bit_rate',
      '-show_entries', 'stream=codec_name,profile,width,height,pix_fmt,r_frame_rate,nb_frames,sample_rate,channels,duration',
      '-of', 'json', file],
    { encoding: 'utf8' }
  );
  if (r.status !== 0) throw new Error(`ffprobe 失败: ${r.stderr}`);
  return JSON.parse(r.stdout);
}

function decodeFrame(mp4, n, out) {
  const r = spawnSync(FFMPEG, ['-y', '-v', 'error', '-i', mp4, '-vf', `select=eq(n\\,${n})`, '-vframes', '1', out], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`解码帧失败: ${r.stderr}`);
  return out;
}

async function framePixels(file) {
  const img = await loadImage(file);
  const cv = createCanvas(img.width, img.height);
  const ctx = cv.getContext('2d');
  ctx.drawImage(img, 0, 0);
  return { w: img.width, h: img.height, d: ctx.getImageData(0, 0, img.width, img.height).data };
}

function sameness2x(im, box) {
  const at = (X, Y) => {
    const i = (Y * im.w + X) * 4;
    return [im.d[i], im.d[i + 1], im.d[i + 2]];
  };
  const near = (a, b, tol) => Math.abs(a[0] - b[0]) <= tol && Math.abs(a[1] - b[1]) <= tol && Math.abs(a[2] - b[2]) <= tol;
  let same = 0;
  let tot = 0;
  for (let Y = box.y; Y < box.y + box.h - 1; Y += 2) {
    for (let X = box.x; X < box.x + box.w - 1; X += 2) {
      const a = at(X, Y);
      tot++;
      if (near(a, at(X + 1, Y), 14) && near(a, at(X, Y + 1), 14) && near(a, at(X + 1, Y + 1), 14)) same++;
    }
  }
  return { ratio: same / tot, samples: tot };
}

function darkBlockSize(im, box) {
  const at = (X, Y) => {
    const i = (Y * im.w + X) * 4;
    return [im.d[i], im.d[i + 1], im.d[i + 2]];
  };
  for (let Y = box.y; Y < box.y + box.h; Y++) {
    for (let X = box.x; X < box.x + box.w; X++) {
      const p = at(X, Y);
      if (p[0] < 70 && p[1] < 70 && p[2] < 70) {
        let w = 0;
        let h = 0;
        while (w < 40 && at(X + w, Y).every((v) => v < 90)) w++;
        while (h < 40 && at(X, Y + h).every((v) => v < 90)) h++;
        return { w, h, at: [X, Y] };
      }
    }
  }
  return null;
}

async function meanLuma(mp4, n) {
  const f = decodeFrame(mp4, n, `/tmp/vm_${n}.png`);
  const im = await framePixels(f);
  let s = 0;
  for (let i = 0; i < im.d.length; i += 4) s += 0.299 * im.d[i] + 0.587 * im.d[i + 1] + 0.114 * im.d[i + 2];
  return s / (im.d.length / 4);
}

function audioStats(mp4) {
  const wavPath = `/tmp/vm_audio_${path.basename(mp4, '.mp4')}.wav`;
  const r = spawnSync(FFMPEG, ['-y', '-v', 'error', '-i', mp4, '-vn', '-ac', '1', '-ar', '44100', '-c:a', 'pcm_s16le', wavPath], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`音轨解码失败: ${r.stderr}`);
  const wav = readWav16(wavPath);
  const arr = wav.ch[0];
  let peak = 0;
  let clipped = 0;
  let sumSq = 0;
  for (let i = 0; i < arr.length; i++) {
    const v = Math.abs(arr[i]);
    if (v > peak) peak = v;
    if (v >= 32760) clipped++;
    sumSq += (arr[i] / 32768) ** 2;
  }
  const rms = Math.sqrt(sumSq / arr.length);
  return {
    sampleRate: wav.sampleRate,
    channels: wav.channels,
    duration: arr.length / wav.sampleRate,
    peak: peak / 32768,
    peakDb: 20 * Math.log10(peak / 32768),
    rmsDb: 20 * Math.log10(rms),
    clipped,
    samples: arr,
  };
}

function correlate(a, b) {
  const n = Math.min(a.length, b.length);
  let sa = 0, sb = 0, saa = 0, sbb = 0, sab = 0;
  for (let i = 0; i < n; i++) {
    const x = a[i] / 32768;
    const y = b[i] / 32768;
    sa += x; sb += y; saa += x * x; sbb += y * y; sab += x * y;
  }
  const cov = sab / n - (sa / n) * (sb / n);
  return cov / Math.sqrt((saa / n - (sa / n) ** 2) * (sbb / n - (sb / n) ** 2));
}

async function verify(name) {
  const job = JOBS[name];
  const mp4 = path.join(ROOT, job.mp4);
  if (!fs.existsSync(mp4)) throw new Error(`缺少成片 ${job.mp4}`);
  const issues = [];
  const checks = [];

  // 1. 容器/编码
  const probe = ffprobe(mp4);
  const v = probe.streams.find((s) => s.codec_name === 'h264') || {};
  const a = probe.streams.find((s) => s.codec_name === 'aac') || {};
  const spec = {
    codec: v.codec_name, profile: v.profile, width: v.width, height: v.height,
    pix_fmt: v.pix_fmt, fps: v.r_frame_rate, frames: Number(v.nb_frames),
    duration: Number(probe.format.duration),
    audio: { codec: a.codec_name, sampleRate: Number(a.sample_rate), channels: a.channels },
  };
  const c1 = [];
  if (spec.width !== 1280 || spec.height !== 720) c1.push(`分辨率 ${spec.width}×${spec.height} ≠ 1280×720`);
  if (spec.fps !== '60/1') c1.push(`帧率 ${spec.fps} ≠ 60/1`);
  if (spec.frames !== 1800) c1.push(`帧数 ${spec.frames} ≠ 1800`);
  if (Math.abs(spec.duration - 30) > 0.02) c1.push(`时长 ${spec.duration} ≠ 30.000s`);
  if (spec.codec !== 'h264' || spec.pix_fmt !== 'yuv420p') c1.push(`编码 ${spec.codec}/${spec.pix_fmt} 非 h264/yuv420p`);
  if (spec.audio.sampleRate !== 44100) c1.push(`音轨采样率 ${spec.audio.sampleRate} ≠ 44100`);
  if (spec.audio.channels !== 1) c1.push(`音轨声道 ${spec.audio.channels} ≠ 1`);
  issues.push(...c1);
  checks.push({ name: '容器/编码规格', ok: c1.length === 0, detail: spec });

  // 2. 像素标准
  const p2 = [];
  const im = await framePixels(decodeFrame(mp4, 120, `/tmp/vm_${name}_f120.png`));
  const room = sameness2x(im, { x: 0, y: 400, w: 260, h: 280 });
  const term = sameness2x(im, { x: 290, y: 340, w: 980, h: 290 });
  if (room.ratio < 0.995) p2.push(`房间区域 2×2 同色率 ${(room.ratio * 100).toFixed(2)}% < 99.5%`);
  if (term.ratio < 0.995) p2.push(`终端区域 2×2 同色率 ${(term.ratio * 100).toFixed(2)}% < 99.5%`);
  const eye = darkBlockSize(im, { x: CLAWD_BASE.x * 2, y: (CLAWD_BASE.y - 2) * 2, w: 90, h: 70 });
  if (!eye || eye.w !== 8 || eye.h !== 8) p2.push(`Clawd 眼睛暗块 ${eye ? eye.w + '×' + eye.h : '未找到'} ≠ 8×8 输出像素（4×4 基础像素）`);
  let mull = 0;
  for (let X = 620; X < 660; X++) {
    const i = (300 * im.w + X) * 4;
    const p = [im.d[i], im.d[i + 1], im.d[i + 2]];
    if (p[0] > 100 && p[0] < 200 && p[1] > 80 && p[2] > 55) mull++;
  }
  if (mull !== 12) p2.push(`窗棂宽度 ${mull}px ≠ 12px 输出（6px 基础像素）`);
  issues.push(...p2);
  checks.push({
    name: '像素标准（2× 最近邻 / Clawd 眼睛 8×8 / 窗棂 12px）',
    ok: p2.length === 0,
    detail: { room2xSameRatio: Number(room.ratio.toFixed(4)), term2xSameRatio: Number(term.ratio.toFixed(4)), eye, mullionPx: mull },
  });

  // 3. 音频
  const au = audioStats(mp4);
  const mixWav = readWav16(path.join(ROOT, job.mix));
  const corr = correlate(au.samples, mixWav.ch[0]);
  const c3 = [];
  if (au.peak >= 0.99) c3.push(`解码峰值 ${au.peak.toFixed(4)} 接近满刻度`);
  if (au.clipped > 0) c3.push(`削波样本 ${au.clipped} 个`);
  if (Math.abs(au.duration - 30) > 0.05) c3.push(`音轨时长 ${au.duration.toFixed(3)}s ≠ 30s`);
  if (corr < 0.995) c3.push(`与 mix.wav 相关系数 ${corr.toFixed(4)} < 0.995`);
  issues.push(...c3);
  checks.push({
    name: '音频（无削波 / 时长 / 与 mix.wav 一致）',
    ok: c3.length === 0,
    detail: {
      sampleRate: au.sampleRate, channels: au.channels, durationSeconds: Number(au.duration.toFixed(3)),
      peakLinear: Number(au.peak.toFixed(4)), peakDbFS: Number(au.peakDb.toFixed(2)),
      rmsDbFS: Number(au.rmsDb.toFixed(2)), clippedSamples: au.clipped,
      correlationWithMix: Number(corr.toFixed(5)),
    },
  });

  // 4. 亮度/黑场
  const lum = [];
  for (const n of [0, 12, 24, 585, 600, 615, 1190, 1200, 1210, 1750, 1780, 1799]) {
    lum.push({ frame: n, t: Number((n / 60).toFixed(3)), luma: Number((await meanLuma(mp4, n)).toFixed(2)) });
  }
  const L = (n) => lum.find((x) => x.frame === n).luma;
  const c4 = [];
  if (!(L(0) < 2)) c4.push(`片头首帧亮度 ${L(0)} 不为黑`);
  if (!(L(24) > 20)) c4.push(`0.4s 未完成淡入（亮度 ${L(24)}）`);
  if (!(L(600) < 2 && L(1200) < 2)) c4.push('10s/20s 转场黑场缺失');
  if (!(L(615) > 20 && L(1210) > 20)) c4.push('转场后未恢复');
  if (!(L(1799) < 2)) c4.push(`片尾末帧亮度 ${L(1799)} 不为黑`);
  issues.push(...c4);
  checks.push({ name: '淡入 / 10s·20s 黑场 / 淡出', ok: c4.length === 0, detail: lum });

  const pass = issues.length === 0;
  const report = {
    status: pass ? 'PASSED' : 'FAILED',
    generatedAt: new Date().toISOString(),
    file: job.mp4,
    sizeBytes: fs.statSync(mp4).size,
    video: spec,
    checks,
    issues,
  };
  console.log(`\n=== ${name} v2.0 成片复核: ${report.status} ===`);
  for (const c of checks) console.log(`[${c.ok ? 'PASS' : 'FAIL'}] ${c.name}`);
  for (const m of issues) console.log(`   - ${m}`);
  console.log(`   视频 ${spec.width}×${spec.height} ${spec.codec}/${spec.pix_fmt} ${spec.fps} ${spec.frames} 帧 ${spec.duration.toFixed(3)}s`);
  console.log(`   音频 ${au.sampleRate}Hz ${au.channels}ch peak=${au.peak.toFixed(4)} (${au.peakDb.toFixed(2)} dBFS) clipped=${au.clipped} corr(mix)=${corr.toFixed(5)}`);
  console.log(`   像素: 房间 2×2 同色率 ${(room.ratio * 100).toFixed(2)}% / 终端 ${(term.ratio * 100).toFixed(2)}% / 眼睛 ${eye ? eye.w + '×' + eye.h : 'n/a'} / 窗棂 ${mull}px`);

  fs.mkdirSync(path.join(ROOT, job.doc), { recursive: true });
  fs.writeFileSync(path.join(ROOT, job.doc, 'media-report.json'), JSON.stringify(report, null, 2) + '\n');
  return pass;
}

(async () => {
  const which = process.argv[2] || 'all';
  const names = which === 'all' ? ['learning', 'upgrade'] : [which];
  let ok = true;
  for (const n of names) ok = (await verify(n)) && ok;
  process.exit(ok ? 0 : 1);
})();
