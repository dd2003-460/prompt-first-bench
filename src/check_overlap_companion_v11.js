#!/usr/bin/env node
'use strict';
// src/check_overlap_companion_v11.js — 「Clawd 的陪伴」v1.1 重叠 + 截断 + 像素/规格检测
//
// 覆盖（0px 容差，逐帧 1800 帧）：
//   D. 规格层：终端 440×200 @(100,140)、标题栏 20、内容区 180、7 行 ×20px、字幕条 20px 与终端 0 重叠
//   A. 几何层：房间前景层（终端 / Clawd / Her / 气泡 / 卡片 / 咖啡杯 / 便签 / 字幕条）
//   B. 文本层：标题栏圆点与标题、7 行终端文本与光标、状态行与分隔线、浮层内部文字、字幕
//   C. 像素层：2× 最近邻、文本无抗锯齿、Fusion Pixel 10px 点阵、Clawd 40×17 + 4×4 眼睛、Her 16×28
//
// 用法: node src/check_overlap_companion_v11.js   (0 issues → exit 0)

const path = require('path');
const R = require('./render_companion_arena_v11');
const { run } = require('./check_overlap_v3_common');

const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'companion-v11', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
