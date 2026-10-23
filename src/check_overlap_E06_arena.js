#!/usr/bin/env node
'use strict';
// E06 · 羞耻 — 0px 重叠 / 无截断 / 像素与时间轴校验
const R = require('./render_E06_shame_arena');
const { run } = require('./check_overlap_story_common');

const ok = run(R, {});
process.exit(ok ? 0 : 1);
