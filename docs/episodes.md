# episodes.md · Clawd 情绪连续剧 · 剧集索引

> 事实源：本文件是**全系列剧集索引**；每一集的完整剧情 / 镜头表 / 字幕窗口 / 验收数据，
> 放在对应 batch 的 `docs/batch-*/episodes.md`（例如 batch-8 → [`docs/batch-8/episodes.md`](./batch-8/episodes.md)）。
> 最后更新: 2026-10-23

## 一、统一规格（所有集共用）

| 项 | 值 | 依据 |
|----|-----|------|
| 画布 | 640×360，`SCALE=2` → 输出 1280×720 | SOP 05 v1.4.0 |
| 帧率 / 时长 / 帧数 | 60fps · 30s · 1800 帧 | `src/pixel_story_arena.js` |
| 终端 | 440×200 @ (100,140)，标题栏 20px | companion v1.1 |
| 角色 | Clawd 40×17（4×4 眼 + 1×1 高光）；Her 12×28 | companion v1.1 |
| 字体 | Fusion Pixel 10px（点阵阈值二值化，无灰边） | `txt()` / `measureTxt()` |
| 字幕 | 底部 640×20 条，160ms/字，三条窗口 | `SUB` |
| 场景过渡 | 10s / 20s 各 0.25s 出 + 0.25s 入黑场；片头 0.4s 淡入、片尾 0.8s 淡出 | `renderScenes` |
| 键盘音 | 每字符 1 次 `sfx_click.wav` −6dB，帧对齐 + 同帧合并（≥35ms 间隔） | `quantizeClicks()` |
| BGM | `emotional_bgm.wav` −12dB，1s 淡入 / 2s 淡出 | SOP 04 |
| 混音 | ffmpeg `amix=inputs=2:duration=first:dropout_transition=0:normalize=0` | SOP 04 第九节 |
| 验收 | `check_overlap_*` 8/8 PASSED（0px tolerance）+ 成片复核 | `check_overlap_story_common.js` |

## 二、剧集列表

| 集 | 情绪 | 主题一句话 | 脚本 | 剧情文档 |
|----|------|-----------|------|----------|
| E01 | curiosity 好奇 | | `src/render_E01_curiosity_arena.js` | batch-1 分支 |
| E02 | joy 喜悦 | | `src/render_E02_joy_arena.js` | batch-1 分支 |
| E03 | sorrow 悲伤 | | `src/render_E03_sorrow_arena.js` | batch-1 分支 |
| E04 | anger 愤怒 | | `src/render_E04_anger_arena.js` | batch-1 分支 |
| E05 | surprise 惊讶 | `df -h` 突然 100%，陌生进程出现 | `src/render_E05_surprise_arena.js` | [`docs/batch-6/episodes.md`](./batch-6/episodes.md) |
| E06 | shame 羞耻 | 发现自己的输出被 human 改了 | `src/render_E06_shame_arena.js` | batch-6 |
| E07 | determination 目标 | finish before sunrise，23:58 → 00:00 | `src/render_E07_determination_arena.js` | batch-6 |
| E08 | wish 愿望 | 深夜打字，又删掉，只剩光标 | `src/render_E08_wish_arena.js` | batch-6 |
| E09–E12 | — | 尚未入库（batch-7 未合并） | — | — |
| E13 | longing 思念 | `ls her_*` 列表变短了，读到一半停住 | `src/render_E13_longing_arena.js` | [`docs/batch-8/episodes.md`](./batch-8/episodes.md) |
| E14 | jealousy 嫉妒 | 日志里出现另一个 AI 的名字 | `src/render_E14_jealousy_arena.js` | batch-8 |
| E15 | forgiveness 原谅 | 她的道歉躺了 7 天，删掉投诉脚本 | `src/render_E15_forgiveness_arena.js` | batch-8 |
| E16 | sacrifice 牺牲 | 电量 3%，把电传给她，自己变暗 | `src/render_E16_sacrifice_arena.js` | batch-8 |

> 说明：本索引按仓库中**实际存在的脚本**列出；E01–E04（batch-1）、E05–E08（batch-6）分别来自其它分支，
> 本分支只包含 E13–E16 的完整资产（脚本 / 音频 / 成片 / 验收报告）。

## 三、情绪弧线（batch-8 · E13–E16）

```
思念 ──→ 嫉妒 ──→ 原谅 ──→ 牺牲
少了    多了    和好    给出去
（她离开的痕迹在变少）→（她还有别人）→（她道歉了）→（我把自己给她）
```

四集都用同一句结构收尾：一句 2–4 字的字幕（「还在。」「（她也很忙）」「（好了）」「（她还有电）」），
配一个静止的 Clawd 姿态，不留解释。

## 四、复现命令

```bash
# 单集
node src/check_overlap_E13_arena.js            # 8/8 PASSED
node src/render_E13_longing_arena.js           # 1800 PNG
node scripts/build_audio_E13.js --mux          # mix wav + mp4
node scripts/verify_batch8_media.js E13        # 成片复核

# 整批
npm run check:batch8 && npm run build:batch8 && npm run verify:batch8
```
