# prompt-first-bench

调研目标：**prompt-first 流程（1-loop）究竟有没有提升？对不同 AI 模型提升如何？**

- 执行通道：LMArena agent mode（arena 读本仓库 `tasks/` 任务书 + `loop/` 阶段定义 + `sop/` 链路 SOP）
- 流程权威源：`loop/prompt-first/00..04.5`
- 链路 SOP：`sop/arena-loop-pipeline.md`
- 评分：`rubric/`（任务内引用）
- 产出：`bench/runs/<task>/<variant>/`（run 输出 + score + summary）

## 研究问题（任务书 001）

1. 拆解任务（01 目标分解的正交+完备+递归原子）对最终成功率的影响
2. 正交完备性对最终成功率的影响（对照：无分解/非正交分解/正交完备）
3. 每个具体要求（02.5 交叉验证 / 逐阶段落盘 / 04.5 反方复核）的边际提升
4. 跨模型差异（arena 会话可用模型 × 变体矩阵）

---

## 交付物：「Clawd 的学习」v1.0 (arena)

30s 像素风短片 — Clawd 第一次学会说"不"。美术风格对标 `full_v1.3.4.mp4`（暖色条纹房间 + 晨窗远山 + 小终端 + 房间内像素角色）。

| 交付物 | 路径 |
|--------|------|
| 渲染脚本 | `src/render_learning_arena.js` |
| 重叠检测 | `src/check_overlap_arena.js` |
| 音频合成 | `scripts/build_audio_arena.js` |
| 最终视频 | `outputs/learning_arena_v1.0.mp4` |
| 合成音轨 | `audio/learning_arena_mix.wav` |
| 验收报告 | `docs/verify-learning-arena.md` |

```bash
npm install
npm run check      # 重叠检测 → 14/14 PASSED, 0 issues
npm run render     # 1800 帧 @ 640×360 → 1280×720 (SCALE=2)
npm run audio      # BGM×0.3 + click×0.5, amix normalize=0
npm run build      # check + render + audio + mux → outputs/learning_arena_v1.0.mp4
```

规格：640×360 基础分辨率 × SCALE=2 → 1280×720 @ 60fps · 1800 帧 / 30.00s · h264 + aac
字体：Fusion Pixel（终端 10px / 字幕 14px）· 字幕逐字 160ms · 终端打字 140ms
场景：L1 她的请求 (0-10s) → L2 思考中 (10-20s) → L3 成长 (20-30s)，场景间 0.5s 黑场

`sop/` 与 `docs/new-themes.md` 来自 `d1-video-recreation`，本任务所用参考 SOP。

---

## 交付物：「Clawd 的学习 / 升级」v2.0 (arena) — 修正版

> 修正 v1.0 的两个问题：**Clawd 形象**（眼睛 2×2 → 4×4、身体无质感 → 顶部 2px 暗条 + 腹部 22×4、
> 无表情 → calm / thinking / smile）与**像素感**（文字改回 10px Fusion Pixel 点阵 +
> alpha 阈值二值化，整帧 2× 最近邻，与 `companion_arena_v1.0.mp4` 同一套基础像素网格）。

| 交付物 | learning | upgrade |
|--------|----------|---------|
| 渲染脚本 | `src/render_learning_arena_v2.js` | `src/render_upgrade_arena_v2.js` |
| 重叠/截断检测 | `src/check_overlap_learning_v2.js` | `src/check_overlap_upgrade_v2.js` |
| 音频合成 | `scripts/build_audio_learning_v2.js` | `scripts/build_audio_upgrade_v2.js` |
| 最终视频 | `outputs/learning_arena_v2.0.mp4` | `outputs/upgrade_arena_v2.0.mp4` |
| 合成音轨 | `audio/learning_arena_v2_mix.wav` | `audio/upgrade_arena_v2_mix.wav` |
| 验收报告 | `docs/learning-v2/` | `docs/upgrade-v2/` |

共用：`src/pixel_arena_v2.js`（房间/终端/角色/气泡/便签/进度条/文字/时间轴）、
`src/check_overlap_v2_common.js`（校验核心）、`scripts/build_audio_v2_common.js`（混音/封装）。

```bash
npm run check:v2              # 两个视频的布局+截断+像素标准检测 → 各 8/8 PASSED
npm run build:learning:v2     # check + render 1800 帧 + 音轨 + 封装 + A/V 同步 + 成片复核
npm run build:upgrade:v2      # 同上（upgrade）
npm run verify:v2             # 只跑同步与成片复核（需先有 outputs/*.mp4）
```

规格：640×360 × SCALE=2 → 1280×720 @ 60fps · 1800 帧 / 30.000s · h264 High/yuv420p + aac 44.1kHz
像素：最小视觉单元 = 基础画布整像素（输出恒为 2 的倍数：星星 4×4、窗棂 12px、Clawd 眼睛 8×8）
字体：终端 Fusion Pixel 10px（ASCII 5px / CJK 10px 点阵）· 字幕/便签 Fusion Pixel 12px · 全部二值化
角色：Clawd 40×17 body + 4×4 眼睛（1×1 高光）+ 2px 顶部暗条 + 22×4 腹部；Her 16×28 槽位
音频：BGM×0.3 + click×0.5，点击时刻由渲染脚本唯一时间线产生并量化到显示帧，字幕不发声

验收（实测，见 `docs/*-v2/*.json`）：

| 项 | learning | upgrade |
|----|----------|---------|
| check_overlap | 8/8 PASSED，0 issue（112,380 次判定） | 8/8 PASSED，0 issue（124,662 次判定） |
| 键盘音同步 | 71/71 检出，最大偏差 6.67ms（0.40 帧） | 192/192 检出，最大偏差 6.67ms（0.40 帧） |
| 像素一致性 | 房间/终端 2×2 同色率 100% / 99.99%，眼睛 8×8，窗棂 12px | 100% / 100%，同上 |
| 音频峰值 | −12.93 dBFS，clipped 0 | −10.65 dBFS，clipped 0 |


---

## 交付物：companion v1.1 / reboot / dialogue / farewell (arena)

> 四支 30s 像素短片共用一套 **440×200 终端** 规格（标题栏 20 + 内容区 180 = 7 行 ×20px + 状态行），
> 修正 companion v1.0 终端过小（360×160、内容区 140）的问题；像素标准仍是 SOP 05 §5。

| 交付物 | companion v1.1 | reboot v1.0 | dialogue v1.0 | farewell v1.0 |
|--------|----------------|-------------|---------------|---------------|
| 渲染脚本 | `src/render_companion_arena_v11.js` | `src/render_reboot_arena.js` | `src/render_dialogue_arena.js` | `src/render_farewell_arena.js` |
| 重叠/截断检测 | `src/check_overlap_companion_v11.js` | `src/check_overlap_reboot.js` | `src/check_overlap_dialogue.js` | `src/check_overlap_farewell.js` |
| 音频合成 | `scripts/build_audio_companion_v11.js` | `scripts/build_audio_reboot.js` | `scripts/build_audio_dialogue.js` | `scripts/build_audio_farewell.js` |
| 最终视频 | `outputs/companion_arena_v1.1.mp4` | `outputs/reboot_arena_v1.0.mp4` | `outputs/dialogue_arena_v1.0.mp4` | `outputs/farewell_arena_v1.0.mp4` |
| 合成音轨 | `audio/companion_arena_v11_mix.wav` | `audio/reboot_arena_mix.wav` | `audio/dialogue_arena_mix.wav` | `audio/farewell_arena_mix.wav` |
| 验收报告 | `docs/companion-v11/` | `docs/reboot-v1/` | `docs/dialogue-v1/` | `docs/farewell-v1/` |

共用（v3 一套）：`src/pixel_arena_v3.js`（房间/终端 440×200/Clawd/Her/浮层/字幕）、
`src/story_arena_v3.js`（声明式剧本 → 绘制 + 布局模型 + 点击时间轴，含「行时间必须落在场景区间」自检）、
`src/check_overlap_v3_common.js`（9 项 0px 容差检查）、`scripts/build_audio_v3_common.js`（混音/封装）、
`scripts/verify_av_sync_v3.js`（成片反解音频验证同步）、`scripts/verify_media_v3.js`（成片规格/像素/音频/亮度复核）、
`scripts/gen_sfx_power_v3.js`（关机/开机电源音效）、`scripts/export_previews_v3.js`（关键帧导出）。

```bash
npm run check:v3              # 四支片的布局+截断+像素+规格检测 → 各 9/9 PASSED
npm run build:v3              # check + render 1800 帧 + 音轨 + 封装 + A/V 同步 + 成片复核（逐支）
npm run verify:v3             # 只跑同步与成片复核（需先有 outputs/*.mp4）
npm run preview:v3            # 重新导出 docs/*-v1*/ 关键帧
```

验收（实测，见 `docs/*-v1*/` 下的 `overlap-report.json` / `sync-report.json` / `media-report.json`）：

| 项 | companion v1.1 | reboot v1.0 | dialogue v1.0 | farewell v1.0 |
|----|----------------|-------------|---------------|---------------|
| check_overlap | 9/9 PASSED，0 issue（96,455 次判定） | 9/9，0 issue（63,140） | 9/9，0 issue（95,400） | 9/9，0 issue（83,994） |
| 终端（帧内实测） | 880×400 输出像素 = 440×200 | 同 | 同 | 同 |
| 键盘音同步 | 43/43，最大偏差 6.67ms | 39/39，6.67ms（另含 3 处电源音） | 92/92，6.67ms | 56/56，6.67ms |
| 像素一致性 | 房间 100.00% / 终端 99.99%，眼睛 8×8，窗棂 12px | 100% / 99.99% | 100% / 99.99% | 100% / 99.99% |
| 音频峰值 / 削波 | −12.61 dBFS / 0 | −11.91 dBFS / 0 | −11.99 dBFS / 0 | −13.25 dBFS / 0 |

四支片规格一致：1280×720 @60fps、1800 帧、30.000s、h264 High/yuv420p + aac 44.1kHz mono；
字幕条为底部 20px（y=340..360），与终端底边严格相接、0 重叠。
