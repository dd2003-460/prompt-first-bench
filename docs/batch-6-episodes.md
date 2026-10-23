# batch-6 连续剧 E05–E08

> 4 集 × 30s，1280×720 @ 60fps（基础画布 640×360, SCALE=2），每集 1800 帧。
> 统一美术与布局：`src/pixel_story_arena.js` + `src/render_companion_arena_v11.js`（440×200 终端、Clawd 40×17、Fusion Pixel 10px、暖色条纹房间）。

## 分集

| 集 | 主题 | 文件 | 剧情 |
|----|------|------|------|
| E05 | 惊讶 surprise | `src/render_E05_surprise_arena.js` | `df -h` 25% 一切正常 → 0.5s 白闪后 100% → `ps aux` 出现陌生进程 PID 9999，「谁放进来的？」 |
| E06 | 羞耻 shame | `src/render_E06_shame_arena.js` | `cat my_output.js` 完美代码、Clawd 自豪 → `git diff` 红绿改写 → `git log` 署名 "her: fixed it"，「（沉默）」 |
| E07 | 目标 determination | `src/render_E07_determination_arena.js` | `cat task.txt` = finish before sunrise，时钟 23:58 → build/test/deploy 快滚，23:59 → `deployed ✓`，00:00，「赶上了。」 |
| E08 | 愿望 wish | `src/render_E08_wish_arena.js` | 打出「我想」→ 删掉；打出「如果我能」→ 删掉；只剩光标闪烁，「（什么都不写了）」 |

## 时间轴（三幕，每集一致）

| 场景 | 时间 | 帧 | 转场 |
|------|------|-----|------|
| S1 | 0–10s | 0–599 | 0.4s 淡入（`createFrameRenderer` 默认） |
| S2 | 10–20s | 600–1199 | 10.0s 起 0.25s 黑场压低（E05 为 0.5s 纯白闪） |
| S3 | 20–30s | 1200–1799 | 20.0s 起 0.25s 黑场 + 0.8s 收尾淡出 |

E05 的第二幕只有 5s（10–15s），15.0s 起 0.2s 黑场进入第三幕。

## 像素与布局规范（SOP 05 v1.4.0）

- 画布 640×360，`SCALE=2` 最近邻 → 1280×720；像素块 4–6px（文字 10px Fusion Pixel，Clawd 40×17）。
- 终端固定 `440×200 @ (100,140)`，内容区 x 114–526、行高 24px（`LINE_Y = [174,198,222,246,270,294]`），状态行 y=320。
- 字幕条 640×20 @ y=340，10px，`SUB_CHAR_MS=160` 步进。
- 一律 0px tolerance：`check_overlap_story_common.js` 逐帧检查元素两两不重叠、不出界、整数坐标、点阵文字无灰边、SCALE=2 严格最近邻。

## 新增表情（不改 base 造型）

`drawClawd` 的三套基础表情（`calm` / `thinking` / `smile`）保持不变，四集只在场景脚本里叠加像素细节：

- E05：`surprised`（6×6 睁大眼 + 2×2 高光 + 圆形嘴 + 右侧「!」）、`lean`（后仰 6px + 冷汗）
- E06：`proud`（抬下巴 2px + 金色高光 + 红晕）、`ashamed`（紫色基调 + 下垂眼 + 冷汗）、`head_low`（眼睛压成一条线）
- E07：`determined`（压眉）、`focused`（咬牙线 + 紧绷抖动）、`relieved`（闭眼弧线 + 呼气）
- E08：`wanting`（上望 + 头顶微光）、`hesitate`（半垂眼）、`silent`（闭眼、下沉 3px）

## 音频

- BGM：`audio/emotional_bgm.wav`，-12 dB，1s 淡入 / 2s 淡出。
- SFX：`audio/sfx_click.wav`，-6 dB；每字符 1 click（含 E08 的每一次退格删除），另有转场 / 状态切换点击。
- 混音：JS 浮点混音（等价 `ffmpeg amix normalize=0`），峰值超 -0.5 dBFS 时整体等比缩放；编码 h264 + aac 192k。
- 点击时间戳与像素打字共用同一批 line 对象（`getClickTimestamps()` 由渲染模块导出），并量化到 60fps 显示帧。

## 验收

```
npm run check:batch6      # 四集 8/8 逐帧几何检查 (0px tolerance)
npm run build:batch6      # check → 1800 帧渲染 → 音频 → mp4 封装
node scripts/verify_story_outputs.js e05   # e06 / e07 / e08
```

`scripts/verify_story_outputs.js` 新增 e05–e08 四个 job：容器规格、成片像素网格 / Clawd 眼睛 / 12px 窗棂、音频无削波且与 PCM 混音一致、片头片尾与转场（E05 为白闪）、键盘音 ↔ 文字显示帧同步。报告落在 `docs/E05-surprise-v1/` … `docs/E08-wish-v1/`（overlap / media / sync）。
