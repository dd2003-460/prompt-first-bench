#!/usr/bin/env node
'use strict';
// src/check_overlap_dialogue.js — 「Clawd 的对话」v1.0 重叠 + 截断 + 像素/规格检测
//
// 覆盖（0px 容差，逐帧 1800 帧）：
//   D1 早安：4 轮对话行 + intent 行 + 消息气泡 + Clawd calm
//   D2 理解：5 行（含 [clawd: 检测 → 情感] 行）+ 思考泡泡 ... → ? → ! + Clawd thinking
//   D3 陪伴：5 行 + 便签「陪伴。」+ 温暖星尘 + Clawd smile
//
// 用法: node src/check_overlap_dialogue.js   (0 issues → exit 0)

const path = require('path');
const R = require('./render_dialogue_arena');
const { run } = require('./check_overlap_v3_common');

const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'dialogue-v1', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
