#!/usr/bin/env node
'use strict';
const path = require('path');
const R = require('./render_E08_wish_arena');
const { run } = require('./check_overlap_story_common');
const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'batch-6', 'E08', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
