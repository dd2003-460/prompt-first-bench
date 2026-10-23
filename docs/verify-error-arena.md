# 验收报告 · 「Clawd 的错误」v1.0 (arena)

> 生成方式: `node src/render_error_arena.js` → `node scripts/build_audio_error.js --mux`
> 环境: Node 22 · @napi-rs/canvas 1.0.13 · Fusion Pixel (10px / 14px) · ffmpeg (n4.0 static)
> 故事: Clawd 犯了一个错，删掉了重要文件。它试图修复，但发现有些东西回不来。

## 一、验收清单

| # | 验收项 | 目标 | 实测 | 结果 |
|---|--------|------|------|------|
| 1 | `check_overlap_error.js` | 全部 PASSED, 0 issues | **16/16 checks PASSED, 0 issue(s)** (exit 0) | ✅ |
| 2 | 分辨率 | 1280×720 | 1280×720 (640×360 × SCALE=2, nearest-neighbor) | ✅ |
| 3 | 编码 | h264 | h264 / yuv420p / crf 18 | ✅ |
| 4 | 帧率 | 60fps | 60 / 1 fps | ✅ |
| 5 | 帧数 | 1800 | 1800 (`-map 0:v -f null -` → frame=1800) | ✅ |
| 6 | 时长 | 30.00s | video 30.000000 / audio 30.000000 / container 30.000000 | ✅ |
| 7 | 美术风格 | 对标 full_v1.3.4 | 暖色条纹墙 (#F5EDD5 / #EDE3C8 · 16px 周期) + 大窗 (60,20,520×160 · 8px 木框 · 十字窗棂) + 晨空 (#87CEEB→#E0F0FF) / 远山 / 云 + 小终端 (140,160,360×160 · #14161C · DSH TUI) | ✅ |
| 8 | 角色位置 | 角色在房间内 | Clawd (64,248) 终端左侧地板上；Her (560,194) 窗边；与终端 0px 重叠（check #1 断言） | ✅ |
| 9 | 键盘声音同步 | 与打字/事件对齐 | 终端 140ms/字 + 字幕 160ms/字，全部由 `getClickTimestamps()` 单源输出；音频脚本消费同一数组 → **86 clicks**；逐点检测瞬态 86/86 命中 | ✅ |
| 10 | 无削波 | clipping = 0 | 混音峰值 0.2621 (−11.63 dBFS)，`max_volume: -11.6 dB`（成品 mp4 复核一致），clipped samples = 0（脚本硬门禁） | ✅ |
| 11 | 字体 | Fusion Pixel 10px 终端 / 14px 字幕 | FONT_10=FusionPixel10(10px monospaced) · FONT_14=FusionPixel(12px 点阵渲染于 14px 行高)，threshold 二值化 | ✅ |
| 12 | 场景过渡 | 0.5s 黑场 | 10s / 20s 边界各 ±0.25s 全黑（合计 0.5s）；片头 0.4s 淡入、片尾 0.5s 渐暗 | ✅ |
| 13 | 字幕 | 逐字 160ms，3 条 | `它犯了一个错。` 2–8s · `有些东西回不来。` 12–18s · `但你还在。` 24–29s（帧级采样验证窗口边界与逐字节奏） | ✅ |
| 14 | 音轨 | BGM×0.3 + click×0.5, amix normalize=0 | `amix=inputs=2:duration=first:dropout_transition=0:normalize=0`，BGM 峰值 0.1251 / SFX 峰值 0.1878 | ✅ |

## 二、时间线（帧级）

| 区间 | 场景 | 内容 |
|------|------|------|
| 0.0–10.0s | **E1 删错了** | 0.7s 起逐字打 `$ rm -rf /important`（19 字 × 140ms → 3.36s 打完）→ 3.7s `> 确认删除 128 个文件？ [y/N]` → 4.9s `> y` → **5.2s 红色警告框弹出**（WARNING: 删除了重要文件 / 128 files permanently deleted）+ 终端边框闪红 + 房间红色脉冲 + Clawd 平静→惊恐（睁大眼 + 方嘴 + 冷汗 + 颤抖 ±2px）→ 6.3s `[DSH] irreversible · 128 files gone` |
| 10.0–20.0s | **E2 试图修复** | 10.6s 起逐字 `$ git restore /important`（→ 13.96s）→ 14.26s `> 错误: 文件已被永久删除` → 15.56s `$ ls /important`（逐字 → 17.38s）→ 16.76s `> 目录为空` → 17.76s `[DSH] nothing to restore · 0 files`；10.7–12.8s 房间灯光转冷变暗（窗面暮色 + 全屏冷色蒙版），Clawd 颜色 → 懊悔暗灰紫 #4A4757（低垂眼 + 泪光） |
| 20.0–30.0s | **E3 安慰** | 20.7s `$ her: 没关系，下次小心。`（逐字）→ 22.6s 窗台便签落位「有些东西，删了就回不来。但你还在。」→ 23.4s `$ clawd: 谢谢你还在。`（逐字 → 24.24s）→ 25.8s `[DSH] connection: still here` → 26.6s `# 有些东西回不来，但你还在。`；21.0–23.8s Clawd 颜色恢复暖珊瑚 + 微笑（23.4s 起 smile 表情）；Her 21.4–26.2s 在窗边轻轻点头；24.2s 起暖色星光 |

字幕（逐字 160ms）：`它犯了一个错。` 2–8s · `有些东西回不来。` 12–18s · `但你还在。` 24–29s。
E2 的内心独白「有些东西回不来。」同时以第 2 条字幕呈现（12–18s），与终端「永久删除 / 目录为空」节拍重合。

## 三、可复核命令

```bash
npm install

# 1) 布局检测 (必须 0 issues, exit 0)
node src/check_overlap_error.js

# 2) 渲染 1800 帧 (默认 /tmp/frames_error, 可用 FRAMES_DIR 覆盖)
FRAMES_DIR=/tmp/frames_error node src/render_error_arena.js

# 3) 音轨 + 封装 (amix=inputs=2:normalize=0, 内含削波/时长自检)
FRAMES_DIR=/tmp/frames_error node scripts/build_audio_error.js --mux

# 4) 复核封装结果
ffprobe -v error -select_streams v:0 -count_frames \
  -show_entries stream=width,height,codec_name,r_frame_rate,nb_read_frames,duration \
  -of default=noprint_wrappers=1 outputs/error_arena_v1.0.mp4
# → codec_name=h264 width=1280 height=720 r_frame_rate=60/1 nb_read_frames=1800 duration=30.000000

ffmpeg -hide_banner -i outputs/error_arena_v1.0.mp4 -map 0:a -af volumedetect -f null -
# → mean_volume: -34.2 dB / max_volume: -11.6 dB (无削波)
```

## 四、音轨构成

| 轨 | 源 | 处理 | 电平 |
|----|----|------|------|
| BGM | `audio/emotional_bgm.wav` | 截取前 30s × 0.3，0.8s 淡入 / 1.8s 淡出 | 峰值 0.1251 |
| SFX | `audio/sfx_click.wav` | 86 个时间戳 × 0.5（打字 140ms/字 + 字幕 160ms/字 + 事件点） | 峰值 0.1878 |
| 混合 | — | `amix=inputs=2:duration=first:dropout_transition=0:normalize=0` | 峰值 0.2621 (−11.63 dBFS)，clipped=0 |

> `normalize=0` 保证不做 1/n 衰减；音量已在各轨内标定（0.3 / 0.5），与规格一致。
> 音频脚本在混音后解析 PCM 做真峰值检测：`clipped >= 1` 或时长 ≠ 30.00s 直接抛错（硬门禁）。

## 五、布局检测覆盖范围（16 项，0px tolerance）

1. E1 Room — terminal / warningPanel / clawd_scared(含颤抖包络) / her / her_question_mark / subtitleBar
2. E2 Room — terminal / clawd_sad(含 2px 低落) / her / subtitleBar
3. E3 Room — terminal / stickyNote_sill(旋转 AABB) / clawd_smile / her_nod / 4× sparkle / subtitleBar
4. TitleBar × 3 场景 — 三色按钮 × 标题文字（边界 360×20）
5. E1 终端内容 — cmd / cursor / confirm / answer / warningPanel / footer（边界 360×140）
6. E2 终端内容 — cmd / error / ls / empty / footer
7. E3 终端内容 — her 行 / clawd 行 / status / cursor / footer
8. 警告框内部 — 三角图标 × 两行文字（边界 336×34）
9. 便签内部 — 图钉 × 三行文字（旋转后本地坐标）+ 文字宽度适配
10. 字幕栏 × 3 条 — 14px 字幕在 640×40 内
11. 安全边距 — 终端左右 ≥8px、终端底边 < 字幕栏、便签右边距 ≥4px

## 六、与「Clawd 的学习」v1.0 的差异

- 角色数不变（Clawd + Her），房间/终端/字体规格完全一致，保证系列观感连续。
- 新增可复用元素：`drawWarningPanel()`（终端内红色警告框，脉冲闪烁）、`mood='scared'`（惊恐表情：睁大眼/方嘴/冷汗）、`mood='sad'`（懊悔表情：低垂眼/泪光）、`drawBackground({cold})`（房间冷光变暗）、`drawHer(..., 'nod')`（轻轻点头）。
- E2 的房间冷光与 Clawd 去饱和是本片情绪主轴：暖 → 冷 → 回暖。
