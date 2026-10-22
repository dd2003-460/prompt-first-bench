# 验收报告 · 「Clawd 的学习」v1.0 (arena)

> 生成方式: `node src/render_learning_arena.js` → `node scripts/build_audio_arena.js --mux`
> 环境: Node 22 · @napi-rs/canvas 1.0.13 · @fontpkg/fusion-pixel (Fusion Pixel 12px) · ffmpeg 7.0.2

## 一、验收清单

| # | 验收项 | 目标 | 实测 | 结果 |
|---|--------|------|------|------|
| 1 | `check_overlap_arena.js` | 全部 PASSED, 0 issues | **14/14 checks PASSED, 0 issue(s)** (exit 0) | ✅ |
| 2 | 分辨率 | 1280×720 | 1280×720 (640×360 × SCALE=2, nearest-neighbor) | ✅ |
| 3 | 编码 | h264 | h264 (High) / yuv420p | ✅ |
| 4 | 帧率 | 60fps | 60 fps | ✅ |
| 5 | 帧数 | 1800 | 1800 (`-map 0:v -f null -` → frame=1800) | ✅ |
| 6 | 时长 | 30.00s | 00:00:30.00 (视频/音频等长) | ✅ |
| 7 | 美术风格 | 对标 full_v1.3.4 | 暖色条纹墙 (#F5EDD5/#EDE3C8 · 16px 周期) + 大窗 (60,20,520×160, 8px 木框, 十字窗棂) + 晨空/远山/云 + 小终端 #0d1117 + 奶油色字幕条 (#CDC6B4) | ✅ |
| 8 | 角色位置 | 角色在房间内 (不在终端里) | Clawd (552,286) / Her (56,280 · L3 34,280)，与终端 0px 重叠 | ✅ |
| 9 | 键盘声音同步 | 与打字 140ms/字 对齐 | 终端字 140ms、字幕字 160ms 全部由渲染脚本 `getClickTimestamps()` 输出，音频脚本消费同一数组 (82 clicks) | ✅ |
| 10 | 无削波 | 无 clipping | 峰值 0.2399 (−12.40 dBFS)，clipped samples = 0 (脚本内 selftest 硬门禁) | ✅ |
| 11 | 字体 | Fusion Pixel 10px 终端 / 14px 字幕 | F_TERM=10, F_SUB=14, F_TITLE=12, F_NOTE=10 (Fusion Pixel 点阵, threshold 二值化) | ✅ |
| 12 | 场景过渡 | 0.5s 黑场 | 10s / 20s 边界各 ±0.25s 全黑 → 合计 0.5s；片头 0.4s 淡入、片尾 0.4s 淡出 | ✅ |

## 二、时间线（帧级）

| 区间 | 场景 | 内容 |
|------|------|------|
| 0.0–10.0s | L1 她的请求 | `$ her: 帮我写一封辞职信` 逐字 140ms (0.8s 起, 3.29s 打完) → 3.5s 消息气泡 → 4.6s `> awaiting reply` → 5.2s Clawd 表情 平静→思考(身体渐变为深紫) |
| 10.0–20.0s | L2 思考中 | 6 行代码逐行出现 (10.6s→16.2s)，`return "no";` 逐字 140ms (13.2s→14.5s)，17.2s `// 它没有撒谎。`；11.0–14.0s Clawd 颜色 → 深紫 #4B2E83 |
| 20.0–30.0s | L3 成长 | 20.8s `$ clawd: 不，我不想。` / 23.4s `$ her: (笑了)` / 25.2s `$ her: 这就是成长。`；22.0s 窗台便签弹出；21.6s 起 Clawd 恢复原色 + 微笑；23.0s 起 Her 微笑 (挥手 → 微笑，粉色爱心) |

字幕（逐字 160ms）：`它第一次说了不。` 2–8s · `它有了自己的意志。` 12–18s · `这就是成长。` 24–29s。

## 三、可复核命令

```bash
# 1) 布局检测 (必须 0 issues, exit 0)
node src/check_overlap_arena.js

# 2) 渲染 1800 帧 (默认输出 src/frames_learning_arena/, 可用 FRAMES_DIR 覆盖)
FRAMES_DIR=/tmp/frames_learning node src/render_learning_arena.js

# 3) 音轨 + 封装 (amix=inputs=2:normalize=0, 内含削波自检)
FRAMES_DIR=/tmp/frames_learning node scripts/build_audio_arena.js --mux

# 4) 复核封装结果
ffmpeg -i outputs/learning_arena_v1.0.mp4          # 1280x720 / 60fps / 30.00s / h264 + aac
ffmpeg -i outputs/learning_arena_v1.0.mp4 -map 0:v -f null -   # frame= 1800
ffmpeg -i outputs/learning_arena_v1.0.mp4 -map 0:a -af volumedetect -f null -  # max_volume: -12.4 dB
```

## 四、音轨构成

| 轨 | 源 | 处理 | 电平 |
|----|----|------|------|
| BGM | `audio/emotional_bgm.wav` | 截取前 30s, ×0.3, 1s 淡入 / 2s 淡出 | 峰值 0.1251 |
| SFX | `audio/sfx_click.wav` | 82 次点击 ×0.5，时间戳与打字/事件同步 | 峰值 0.1878 |
| 混合 | — | `amix=inputs=2:duration=first:dropout_transition=0:normalize=0` | 峰值 0.2399 / 平均 −34.3 dB |

> 说明：`normalize=0` 保证不做 1/n 衰减；音量已在各自轨内标定（0.3 / 0.5）。脚本在混音后解析 PCM 做真峰值与 ±1.0 夹取检测，若超限则整体等比缩放并打印 `[clip-guard]`。

## 五、重叠检测覆盖范围（0px tolerance）

1. 房间前景层：终端、消息气泡、Clawd（含 ±1px 呼吸包络）、Her、思考点、便签、爱心粒子、字幕栏
2. 终端标题栏：3 个窗口按钮 × 标题文字（380×20）
3. 终端内容区：L1/L2/L3 全部文本行、光标、底部状态栏（380×144）
4. 便签内部：图钉 × 标题 × 副标题（118×70）
5. 消息气泡内部：文本 × 气泡框（132×26）
6. 字幕栏内部：3 条字幕（640×44）

内容区文本行坐标单一来源 `TLAYOUT`（渲染与检测共用），避免"检测通过但实际漂移"。
