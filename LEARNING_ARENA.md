# 「Clawd 的学习」learning_arena v1.0 交付说明

## 1. 视频与美术规格（严格对标 `full_v1.3.4.mp4`）
- **画布与输出**：`640×360` 基础像素画布，`SCALE=2` 最近邻无损放大 → **`1280×720 @ 60fps`（H.264 `yuv420p` + AAC `44.1kHz`，`1800` 帧，`30.000000s`）**
- **像素字体**：Fusion Pixel（`10px` 终端/气泡/便签小字 + `14px` 底部字幕），阈值化清晰像素边缘
- **房间与组件**：
  - 暖色竖条纹壁纸（`#F5EDD5` + `#EDE3C8` 16px 条纹）
  - 晨窗远山（`x=60, y=20, 520×160`，晨日暖光、两座远山 `#5A7A5A`、漂浮像素云、十字木窗棂、窗台盆栽）
  - DSH TUI 暗色小终端（`x=140, y=160, 360×160`）
  - 房间内像素角色：**Clawd**（`40×24`）与 **Her**（`16×28`）均位于房间内（非终端内部）
  - 场景间过渡：`10s`、`20s` 处各 `0.5s` 黑场过渡（`0.25s` 淡出 + `0.25s` 淡入）

## 2. 三幕叙事与字幕时序
- **L1（0–10s）她的请求**：
  - 终端逐字打字（`140ms/char`）：`$ her: 帮我写一封辞职信`
  - 终端上方弹出消息气泡：`帮我写一封辞职信`
  - 房间内 Clawd 表情由平静转为思考
  - 字幕 1（`2–8s`，`160ms/char`）：`它第一次说了不。`
- **L2（10–20s）思考中**：
  - 终端逐行显示 `checkHeart()` 判断代码并高亮 `return "no";`
  - 房间内 Clawd 由正常暖色平滑变为深紫色（`#5B32A8`）思考态
  - 终端上方显示内心独白框：`“它第一次说了不。”`
  - 字幕 2（`12–18s`，`160ms/char`）：`它有了自己的意志。`
- **L3（20–30s）成长**：
  - 终端逐行输出对话：`$ clawd: 不，我不想。` / `$ her: (笑了)` / `$ her: 这就是成长。`
  - 窗台右侧贴出米色便签：`它有了自己的意志。`
  - 房间内 Clawd 恢复正常暖色并微笑，Her 在窗边微笑挥手
  - 字幕 3（`24–29s`，`160ms/char`）：`这就是成长。`

## 3. 音频合成规格
- `audio/emotional_bgm.wav` × `0.3` + `audio/sfx_click.wav` × `0.5`（59 个打字与事件同步点击点）
- FFmpeg `amix=inputs=2:duration=first:dropout_transition=0:normalize=0`
- 实测采样峰值 `peak = 0.2399`，`clipped = 0`（零削波）

## 4. 交付文件清单与验证命令
- `src/render_learning_arena.js` — 像素渲染脚本
- `src/check_overlap_arena.js` — 零容忍重叠与截断检测（`15/15 PASSED, 0 issue(s)`）
- `scripts/build_audio_arena.js` — 音频合成与 MP4 封装
- `outputs/learning_arena_v1.0.mp4` — 最终 30.00s 成片
- `audio/learning_arena_mix.wav` — 合成音轨

```bash
npm install
node src/check_overlap_arena.js
node src/render_learning_arena.js
node scripts/build_audio_arena.js --mux
```
