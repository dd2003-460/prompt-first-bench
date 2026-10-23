# 「Clawd 的升级」Arena v1.0

## 交付
- `src/render_upgrade_arena.js`：640×360 → nearest-neighbor 2×，60fps，1800 帧。
- `src/upgrade_room.js`：独立可复用房间组件，沿用参考房间的配色、木窗、远山、云、盆栽。
- `src/check_overlap_arena.js`：逐帧语义区域、文字宽度/行间、边界、全文完成、黑场像素检测。
- `scripts/build_audio_arena.js`：BGM × 0.3（1s 淡入/2s 淡出）+ click × 0.5，`amix=inputs=2:normalize=0`。
- `outputs/upgrade_arena_v1.0.mp4`、`audio/upgrade_arena_mix.wav`：最终成片及独立音轨。
- `scripts/validate_upgrade.js`：实际解码视频数帧、检查规格、检查 WAV 和解码 AAC 峰值。

## 规格冲突及处理
1. 全部终端文本若按单一串行流逐字符 140ms 打印，无法容纳在三个 10s 场景中。因此每行保持 140ms/字符，但采用错峰并行行打字；没有删减任何指定终端文本。字幕独立使用 160ms/字。
2. “终端全屏”与“暖色房间 + 小终端 + 房间内角色”互相冲突。本版优先后者：DSH TUI 占满小终端内容区，而不覆盖整个视频。终端 376×128，位置 (132,186)，为完整日志和窗台便签留出空间。
3. 参考仓库未提供名为 `full_v1.3.4.mp4` 的视频（提供的是 `full_v1.3.mp4`）；本版依据用户指定的 full 渲染脚本、goodmorning 布局及 SOP 的 v1.3.4 描述制作，不宣称与缺失文件逐像素比对。
4. 两次黑场分别为 [9.75,10.25)、[19.75,20.25)，各 30 帧，不额外延长视频。
5. 保留 full 的橙色四足、黑眼、浅色腹部、无天线角色；U2 连续褪灰，U3 恢复，23.4s 出现便签和微笑。

## 可复现
```sh
npm ci
python -m venv .venv
.venv/bin/pip install -r scripts/requirements-video.txt
npm test
npm run render
FRAMES_DIR=outputs/frames_upgrade npm run build:video
node scripts/validate_upgrade.js
```
支持 `FFMPEG_BIN` 指定现代 ffmpeg；默认使用本地 `.venv` 中 imageio-ffmpeg。帧 PNG 属于可再生中间产物，不进入 Git。

## 复用 / 字体 / 音轨 SOP
- 参考来源：`dd2003-460/d1-video-recreation` commit `1ab903f35429d9f0b63ff8bdf7a5d9939f89b728`。已阅读 SOP 00、02、05，full / goodmorning_arena / memory 脚本以及 new-themes。
- 房间组件从参考 `render_goodmorning_arena.js` 提取；Clawd 依据 `render_full_pixel.js`，不采用 memory 的绿色终端内角色。
- `emotional_bgm.wav`、`sfx_click.wav` 原样取自参考仓库；点击时刻从渲染脚本唯一时间线产生，向上量化到实际显示帧，黑场内不触发；同帧点击合并，避免并行行造成不必要叠峰。
- 字体 Fusion Pixel：终端使用原生 10px Latin 字形（Fontsource 5.3.0，导出 TTF），中文用 Fusion Pixel 12px 字形最近邻缩放到 14px，避免直接栅格化 14px 造成笔画断裂。统一 alpha threshold 150。OFL 在 `assets/fonts/OFL.txt`，中文字体通过 npm 锁定依赖提供。
- `glyph()` 缓存栅格字形，`drawClawd()` / `drawTerminal()` / `drawNote()` / `drawSubtitle()` 可复用；所有坐标在基础画布上取整。
- 自动重叠检测对房间背景、窗台支撑关系、终端容器与其子文本允许有意包含；对终端、便签（含阴影和胶带）、角色（含抖动和表情标记）、字幕区做严格互斥检查。报告列出实际检查数量，不把背景包含关系误报为冲突。

## 验证记录
见 `overlap-report.json` 和 `media-report.json`。另检查 U1 完整日志、U2 灰色角色、U3 完整备份命令/便签/微笑关键帧。自动峰值检查不代替最终人工试听。
