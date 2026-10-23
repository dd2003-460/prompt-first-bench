#!/usr/bin/env node
'use strict';
const path = require('path');
const R = require('./render_E05_surprise_arena');
const { run } = require('./check_overlap_story_common');
const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'E05-surprise-v1', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
