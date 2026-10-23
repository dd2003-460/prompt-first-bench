#!/usr/bin/env node
'use strict';
// scripts/gen_sfx_power_v3.js — 生成 reboot 用的电源音效（确定性合成，无外部依赖）
//
//   audio/sfx_power_off.wav  — 关机：320→70 Hz 下滑正弦 + 指数衰减 + 首帧轻点击，0.80s
//   audio/sfx_power_on.wav   — 开机：180→520 Hz 上滑正弦 + 2 次泛音 + 轻微颤音，0.70s
//
// 规格：44.1kHz / 16-bit / 单声道 / 峰值 ≈ 0.5 FS（混音时再乘 -12 dB 左右的增益）
//
// 用法: node scripts/gen_sfx_power_v3.js

const fs = require('fs');
const path = require('path');
const { writeWav16 } = require('./build_audio_v2_common');

const ROOT = path.resolve(__dirname, '..');
const AUDIO = path.join(ROOT, 'audio');
const SR = 44100;

function synthPowerOff(dur = 0.8) {
  const n = Math.round(dur * SR);
  const out = new Float64Array(n);
  let phase = 0;
  for (let i = 0; i < n; i++) {
    const t = i / SR;
    const k = t / dur;
    const f = 320 * Math.pow(70 / 320, k); // 指数下滑
    phase += (2 * Math.PI * f) / SR;
    const env = Math.pow(1 - k, 1.6);
    out[i] = 0.42 * Math.sin(phase) * env;
    // 关机瞬间的机械点击（前 12ms）
    if (t < 0.012) out[i] += 0.5 * Math.sin(2 * Math.PI * 1400 * t) * (1 - t / 0.012);
  }
  return out;
}

function synthPowerOn(dur = 0.7) {
  const n = Math.round(dur * SR);
  const out = new Float64Array(n);
  let phase = 0;
  for (let i = 0; i < n; i++) {
    const t = i / SR;
    const k = t / dur;
    const f = 180 + (520 - 180) * Math.pow(k, 0.7);
    phase += (2 * Math.PI * f) / SR;
    const env = Math.min(1, t / 0.02) * Math.pow(1 - k, 0.9);
    const vib = 1 + 0.004 * Math.sin(2 * Math.PI * 6 * t);
    out[i] =
      0.34 * Math.sin(phase * vib) * env +
      0.14 * Math.sin(2 * phase) * env +
      0.06 * Math.sin(3 * phase) * env;
  }
  return out;
}

function normalize(x, peak = 0.5) {
  let m = 0;
  for (let i = 0; i < x.length; i++) m = Math.max(m, Math.abs(x[i]));
  const k = m > 0 ? peak / m : 1;
  const out = new Int16Array(x.length);
  for (let i = 0; i < x.length; i++) out[i] = Math.round(x[i] * k * 32767);
  return out;
}

if (require.main === module) {
  if (!fs.existsSync(AUDIO)) fs.mkdirSync(AUDIO, { recursive: true });
  const off = normalize(synthPowerOff());
  const on = normalize(synthPowerOn());
  writeWav16(path.join(AUDIO, 'sfx_power_off.wav'), SR, 1, [off]);
  writeWav16(path.join(AUDIO, 'sfx_power_on.wav'), SR, 1, [on]);
  console.log(`audio/sfx_power_off.wav  ${(off.length / SR).toFixed(3)}s  ${off.length} samples`);
  console.log(`audio/sfx_power_on.wav   ${(on.length / SR).toFixed(3)}s  ${on.length} samples`);
}

module.exports = { synthPowerOff, synthPowerOn, normalize };
