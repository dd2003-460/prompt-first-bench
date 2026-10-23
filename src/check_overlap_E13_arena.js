#!/usr/bin/env node
'use strict';
// E13 思念 (longing) — 8-point layout/pixel gate + episode story/expression checks.
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E13_longing_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH8_REPORT_DIR
  ? path.join(process.env.BATCH8_REPORT_DIR, 'E13_overlap.json')
  : path.join('/tmp', 'batch8_reports', 'E13_overlap.json');

function checkExpressions() {
  const issues = [];
  const W = 160, H = 100, x = 40, y = 30, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const draw = (mood, opts = {}) => {
    ctx.fillStyle = BG;
    ctx.fillRect(0, 0, W, H);
    R.drawClawdEp(ctx, x, y, 1.4, mood, 0, opts);
    return readPixels(cv).data;
  };
  const at = (d, X, Y) => {
    const i = (Y * W + X) * 4;
    return `${d[i]},${d[i + 1]},${d[i + 2]}`;
  };
  const EYE = '20,20,19';
  const down = draw('look_down', { noBob: true });
  if (at(down, x + 10, y + 8) !== EYE || at(down, x + 10, y + 6) === EYE) {
    issues.push('look_down must lower eyes to y+8');
  }
  const win = draw('look_window', { noBob: true });
  if (at(win, x + 12, y + 4) !== EYE) {
    issues.push('look_window must raise/shift eyes toward window at (x+12, y+4)');
  }
  return { name: 'Clawd 低头 / 望向窗外像素表情校验', issues };
}

function checkStoryBeats() {
  const issues = [];
  if (R.SUB_LINES[0] !== '(less)') issues.push(`S1 subtitle "${R.SUB_LINES[0]}" !== "(less)"`);
  if (R.SUB_LINES[2] !== 'Still here.') issues.push(`S3 subtitle "${R.SUB_LINES[2]}" !== "Still here."`);
  const s1Text = R.S1_LINES.map(R.lineText).join('\n');
  if (!s1Text.includes('ls her_*') || !s1Text.includes('3 files (was 7)')) {
    issues.push('S1 must show ls her_* and 3 files (was 7)');
  }
  const s2Text = R.S2_LINES.map(R.lineText).join('\n');
  if (!s2Text.includes('cat her_notes.md')) {
    issues.push('S2 must show cat her_notes.md');
  }
  const l3 = R.layoutAt(25);
  if (l3.groups.content.length !== 1 || l3.groups.content[0].name !== 'empty_cursor') {
    issues.push('S3 terminal must be empty with just cursor');
  }
  return { name: 'E13 剧情节点 (ls her_* 3/7 → cat her_notes.md → 空终端仅光标)', issues };
}

const extra = [checkExpressions(), checkStoryBeats()];
const okBase = run(R, { reportPath: REPORT });
let issues = 0;
for (const r of extra) {
  issues += r.issues.length;
  console.log(`[${r.issues.length ? 'FAIL' : 'PASS'}] ${r.name}`);
  for (const msg of r.issues) console.log(`   - ${msg}`);
}
const report = JSON.parse(fs.readFileSync(REPORT, 'utf8'));
report.checks.push(...extra.map((r) => ({ name: r.name, status: r.issues.length ? 'FAILED' : 'PASSED', issues: r.issues })));
report.summary.checksTotal = report.checks.length;
report.summary.checksPassed = report.checks.filter((c) => c.status === 'PASSED').length;
report.summary.issues += issues;
report.status = report.summary.issues ? 'FAILED' : 'PASSED';
fs.writeFileSync(REPORT, JSON.stringify(report, null, 2) + '\n');
console.log(`=== E13 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
