#!/usr/bin/env node
'use strict';
// scripts/export_previews_v3.js — 从渲染脚本导出验收用关键帧（PNG，1280×720）
//
// 每部片 3 帧（三场景各一帧），写入 docs/<doc>/ 目录，作为 README 的视觉证据。
//
// 用法: node scripts/export_previews_v3.js [companion|reboot|dialogue|farewell|all]

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const JOBS = {
  companion: {
    script: '../src/render_companion_arena_v11',
    doc: 'docs/companion-v11',
    frames: [
      { n: 360, name: 'C1_6.0s.png' },
      { n: 870, name: 'C2_14.5s.png' },
      { n: 1680, name: 'C3_28.0s.png' },
    ],
  },
  reboot: {
    script: '../src/render_reboot_arena',
    doc: 'docs/reboot-v1',
    frames: [
      { n: 330, name: 'R1_5.5s.png' },
      { n: 1020, name: 'R2_17.0s.png' },
      { n: 1750, name: 'R3_29.2s.png' },
    ],
  },
  dialogue: {
    script: '../src/render_dialogue_arena',
    doc: 'docs/dialogue-v1',
    frames: [
      { n: 540, name: 'D1_9.0s.png' },
      { n: 1140, name: 'D2_19.0s.png' },
      { n: 1680, name: 'D3_28.0s.png' },
    ],
  },
  farewell: {
    script: '../src/render_farewell_arena',
    doc: 'docs/farewell-v1',
    frames: [
      { n: 510, name: 'F1_8.5s.png' },
      { n: 1140, name: 'F2_19.0s.png' },
      { n: 1740, name: 'F3_29.0s.png' },
    ],
  },
};

function exportOne(name) {
  const job = JOBS[name];
  const mod = require(path.join(__dirname, job.script));
  const dir = path.join(ROOT, job.doc);
  fs.mkdirSync(dir, { recursive: true });
  for (const f of job.frames) {
    const { outCanvas } = mod.renderFrameToCanvas(f.n);
    fs.writeFileSync(path.join(dir, f.name), outCanvas.toBuffer('image/png'));
    console.log(`${job.doc}/${f.name}  (frame ${f.n}, ${(f.n / mod.FPS).toFixed(2)}s)`);
  }
}

if (require.main === module) {
  const which = process.argv[2] || 'all';
  const names = which === 'all' ? Object.keys(JOBS) : [which];
  for (const n of names) exportOne(n);
}

module.exports = { JOBS };
