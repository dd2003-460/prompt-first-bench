#!/usr/bin/env node
'use strict';
// E14 嫉妒 (jealousy) — 8-point layout/pixel gate + episode story/expression checks.
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E14_jealousy_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH8_REPORT_DIR
  ? path.join(process.env.BATCH8_REPORT_DIR, 'E14_overlap.json')
  : path.join('/tmp', 'batch8_reports', 'E14_overlap.json');

function checkExpressions() {
  const issues = [];
  const W = 160, H = 100, x = 40, y = 30, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  const draw = (mood) => {
    ctx.fillStyle = BG;
    ctx.fillRect(0, 0, W, H);
    R.drawClawdEp(ctx, x, y, 1.4, mood, 0, { noBob: true });
    return readPixels(cv).data;
  };
  const at = (d, X, Y) => {
    const i = (Y * W + X) * 4;
    return `${d[i]},${d[i + 1]},${d[i + 2]}`;
  };
  const EYE = '20,20,19';
  const fr = draw('frown');
  if (at(fr, x + 16, y + 13) !== EYE || at(fr, x + 19, y + 12) !== EYE) {
    issues.push('frown mouth arc missing');
  }
  const ta = draw('turn_away');
  if (at(ta, x + 5, y + 7) !== EYE || at(ta, x + 17, y + 7) !== EYE) {
    issues.push('turn_away must shift eyes left to x+5 and x+17');
  }
  return { name: 'Clawd 皱眉 (frown) / 转身背对 (turn_away) 像素校验', issues };
}

function checkStoryBeats() {
  const issues = [];
  if (R.SUB_LINES[2] !== '(she is busy too)') {
    issues.push(`S3 subtitle "${R.SUB_LINES[2]}" !== "(she is busy too)"`);
  }
  const s1Text = R.S1_LINES.map(R.lineText).join('\n');
  if (!s1Text.includes('tail -f chat.log')) issues.push('S1 must show tail -f chat.log');
  const s2Text = R.S2_LINES.map(R.lineText).join('\n');
  if (!s2Text.includes('nova-ai')) issues.push('S2 must show nova-ai in chat.log');
  const s3Text = R.S3_LINES.map(R.lineText).join('\n');
  if (!s3Text.includes('nova-ai') || !s3Text.includes('echo-ai')) {
    issues.push('S3 must show her chatting with two AIs (nova-ai & echo-ai)');
  }
  return { name: 'E14 剧情节点 (tail -f chat.log → nova-ai → two AIs)', issues };
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
console.log(`=== E14 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
