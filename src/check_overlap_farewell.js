#!/usr/bin/env node
'use strict';
// src/check_overlap_farewell.js — 「Clawd 的告别」v1.0 重叠 + 截断 + 像素/规格检测
//
// 覆盖（0px 容差，逐帧 1800 帧）：
//   F1 决定：4 行 + 消息气泡 + 思考泡泡 + Clawd thinking
//   F2 等待：6 行（第 1/7/15 天）+ Her 离场 + 屏幕渐暗（时间流逝）
//   F3 回来：5 行（含 memory 删除）+ 便签「欢迎回来。」+ 星尘 + Clawd smile
//
// 用法: node src/check_overlap_farewell.js   (0 issues → exit 0)

const path = require('path');
const R = require('./render_farewell_arena');
const { run } = require('./check_overlap_v3_common');

const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'farewell-v1', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
