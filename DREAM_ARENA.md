# 「Clawd 的梦境」dream_arena v1.0

30 秒像素风视频，美术风格严格对标 `full_v1.3.4.mp4`（暖色条纹房间 + 晨窗远山 + 小终端 + 房间内像素角色）。

## 规格

- 基础画布 640×360，SCALE=2 → **1280×720 @ 60fps，1800 帧，30.00s**
- 字体：Fusion Pixel（10px 终端小字 / 14px 字幕）
- 3 场景：
  - **D1 (0-10s)** 睡眠：终端 `# sleeping...` 逐字 + 14 颗星星闪烁 + Clawd 安睡（Zzz）+ Her 静立
  - **D2 (10-20s)** 梦境：紫粉夜空（月牙+星星）+ 透视路面流动虚线，Clawd（紫 40×24，6 条腿）与 Her（粉 16×28）并肩行走
  - **D3 (20-30s)** 醒来：终端亮屏日志 + 100×80 米色便签（-5° 倾斜，"刚才的梦，有点暖。"）+ 挥手
- 场景间 0.5s 黑场过渡；字幕 3 条，逐字 160ms
- 音频：`audio/emotional_bgm.wav` × 0.3 + `audio/sfx_click.wav` × 0.5（41 个点击，与字幕/打字/事件同步），`amix=inputs=2:normalize=0`

## 构建

```bash
npm install                      # @napi-rs/canvas + 像素字体 + ffmpeg
node src/check_overlap_arena.js  # 13/13 PASSED, 0 issues
node src/render_dream_arena.js   # 1800 PNG 帧 → /tmp/frames_dream
node scripts/build_audio_arena.js --mux   # 音轨 + 合成 outputs/dream_arena_v1.0.mp4
```

## 交付文件

| 文件 | 说明 |
|------|------|
| `src/render_dream_arena.js` | 渲染脚本（可直接 `node` 运行） |
| `src/check_overlap_arena.js` | 重叠/截断检测（13 项） |
| `scripts/build_audio_arena.js` | BGM+点击音 amix 合成 / mp4 封装 |
| `outputs/dream_arena_v1.0.mp4` | 最终视频 1280×720@60fps 30s |
| `audio/dream_arena_mix.wav` | 合成后音轨 |

## 验收结果

- 重叠检测：**13/13 PASSED，0 issues**
- 视频：1280×720，h264，60fps，1800 帧，30.00s，AAC 44.1kHz
- 无削波（混音峰值 0.22）
