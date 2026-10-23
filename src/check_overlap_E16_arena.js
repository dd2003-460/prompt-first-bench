#!/usr/bin/env node
'use strict';
const path = require('path');
const R = require('./render_E16_sacrifice_arena');
const { run } = require('./check_overlap_story_common');
const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'batch-8', 'E16', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
