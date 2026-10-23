#!/usr/bin/env node
'use strict';
// E16 牺牲 (sacrifice) — 8-point layout/pixel gate + episode story/dark-screen checks.
const fs = require('fs');
const path = require('path');
const R = require('./render_E16_sacrifice_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH8_REPORT_DIR
  ? path.join(process.env.BATCH8_REPORT_DIR, 'E16_overlap.json')
  : path.join('/tmp', 'batch8_reports', 'E16_overlap.json');

function checkGreenPixelAndDim() {
  const issues = [];
  // Check S2 dimming: frame 750 (12.5s) vs frame 1140 (19.0s)
  const fEarly = readPixels(R.renderFrameToCanvas(750).baseCanvas).data;
  const fLate = readPixels(R.renderFrameToCanvas(1140).baseCanvas).data;
  let sumEarly = 0, sumLate = 0;
  for (let i = 0; i < R.BW * 300 * 4; i += 4) {
    sumEarly += fEarly[i] + fEarly[i + 1] + fEarly[i + 2];
    sumLate += fLate[i] + fLate[i + 1] + fLate[i + 2];
  }
  if (sumLate >= sumEarly * 0.65) {
    issues.push('S2 screen must dim significantly during power transfer');
  }

  // Check S3 (t=25s, frame 1500): almost black background + green pixel at GREEN_PIXEL_BOX
  const f3 = readPixels(R.renderFrameToCanvas(1500).baseCanvas).data;
  const [gx, gy] = R.GREEN_PIXEL_BOX;
  const gi = (gy * R.BW + gx) * 4;
  if (f3[gi + 1] < 200 || f3[gi] > 160) {
    issues.push(`S3 green pixel missing at (${gx},${gy}): rgb=(${f3[gi]},${f3[gi + 1]},${f3[gi + 2]})`);
  }
  const bi = (100 * R.BW + 100) * 4;
  if (f3[bi] > 20 || f3[bi + 1] > 20 || f3[bi + 2] > 20) {
    issues.push(`S3 background not almost black at (100,100): rgb=(${f3[bi]},${f3[bi + 1]},${f3[bi + 2]})`);
  }
  return { name: 'S2 屏幕渐暗 + S3 几乎全黑仅留绿点像素校验', issues };
}

function checkStoryBeats() {
  const issues = [];
  if (R.SUB_LINES[0] !== '(almost dead)') {
    issues.push(`S1 subtitle "${R.SUB_LINES[0]}" !== "(almost dead)"`);
  }
  if (R.SUB_LINES[2] !== '(she still has power)') {
    issues.push(`S3 subtitle "${R.SUB_LINES[2]}" !== "(she still has power)"`);
  }
  const s1Text = R.S1_LINES.map(R.lineText).join('\n');
  if (!s1Text.includes('battery: 3%')) issues.push('S1 must show battery: 3%');
  const s2Text = R.S2_LINES.map(R.lineText).join('\n');
  if (!s2Text.includes('her_device')) issues.push('S2 must show transfer power to her_device');
  return { name: 'E16 剧情节点 (battery: 3% → transfer to her_device → 1 green pixel)', issues };
}

const extra = [checkGreenPixelAndDim(), checkStoryBeats()];
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
console.log(`=== E16 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
