#!/usr/bin/env node
'use strict';
// src/check_overlap_reboot.js — 「Clawd 的重启」v1.0 重叠 + 截断 + 像素/规格检测
//
// 覆盖（0px 容差，逐帧 1800 帧）：
//   R1 关机：终端 440×200 / 6 行文本 / 状态行 / Clawd calm / Her / 字幕
//   R2 黑暗：全黑场景（无终端、无角色）+ 光标 + 电源灯（允许黑场窗口 10-20s）
//   R3 重启：终端 / 6 行启动日志 / ✓ 逐字行 / 便签 / 电源灯 / Clawd thinking→smile
//
// 用法: node src/check_overlap_reboot.js   (0 issues → exit 0)

const path = require('path');
const R = require('./render_reboot_arena');
const { run } = require('./check_overlap_v3_common');

const ok = run(R, { reportPath: path.join(__dirname, '..', 'docs', 'reboot-v1', 'overlap-report.json') });
process.exit(ok ? 0 : 1);
