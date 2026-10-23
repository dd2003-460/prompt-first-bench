#!/usr/bin/env node
'use strict';
// E15 原谅 (forgiveness) — 8-point layout/pixel gate + episode story/expression checks.
const fs = require('fs');
const path = require('path');
const { createCanvas } = require('@napi-rs/canvas');
const R = require('./render_E15_forgiveness_arena');
const { run, readPixels } = require('./check_overlap_story_common');

const REPORT = process.env.BATCH8_REPORT_DIR
  ? path.join(process.env.BATCH8_REPORT_DIR, 'E15_overlap.json')
  : path.join('/tmp', 'batch8_reports', 'E15_overlap.json');

function checkExpressions() {
  const issues = [];
  const W = 160, H = 100, x = 40, y = 30, BG = '#F5EDD5';
  const cv = createCanvas(W, H);
  const ctx = cv.getContext('2d');
  ctx.fillStyle = BG;
  ctx.fillRect(0, 0, W, H);
  R.drawClawdEp(ctx, x, y, 1.4, 'hesitate', 0, { noBob: true, staticGaze: true });
  const d = readPixels(cv).data;
  const at = (X, Y) => {
    const i = (Y * W + X) * 4;
    return `${d[i]},${d[i + 1]},${d[i + 2]}`;
  };
  const EYE = '20,20,19';
  if (at(x + 11, y + 7) !== EYE && at(x + 12, y + 8) !== EYE) {
    issues.push('hesitate shifted eyes missing');
  }
  return { name: 'Clawd 犹豫 (hesitate) → 平静 (calm) 像素表情校验', issues };
}

function checkStoryBeats() {
  const issues = [];
  if (R.SUB_LINES[2] !== '(ok)') {
    issues.push(`S3 subtitle "${R.SUB_LINES[2]}" !== "(ok)"`);
  }
  const s1Text = R.S1_LINES.map(R.lineText).join('\n');
  if (!s1Text.includes('ls inbox/') || !s1Text.includes('apology.md') || !s1Text.includes('7d unread')) {
    issues.push('S1 must show ls inbox/ and apology.md (7d unread)');
  }
  const s2Text = R.S2_LINES.map(R.lineText).join('\n');
  if (!s2Text.includes('apology.md')) {
    issues.push('S2 must show cat apology.md');
  }
  const s3Text = R.S3_LINES.map(R.lineText).join('\n');
  if (!s3Text.includes('rm complaint.sh') || !s3Text.includes('clean')) {
    issues.push('S3 must show rm complaint.sh success and clean terminal');
  }
  return { name: 'E15 剧情节点 (ls inbox/ apology.md 7d unread → cat apology.md → rm complaint.sh)', issues };
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
console.log(`=== E15 summary: ${report.summary.checksPassed}/${report.summary.checksTotal} checks PASSED, ${report.summary.issues} issue(s) ===`);
process.exit(okBase && issues === 0 ? 0 : 1);
