#!/usr/bin/env node
'use strict';
// E05 · 惊讶 — 0px 重叠 / 无截断 / 像素与时间轴校验
const R = require('./render_E05_surprise_arena');
const { run } = require('./check_overlap_story_common');

const ok = run(R, {});
process.exit(ok ? 0 : 1);
