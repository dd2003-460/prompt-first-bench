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

## 交付物：「Clawd 的错误」v1.0 (arena) ⭐ 最新

30s 像素风短片 — Clawd 犯了一个错，删掉了重要文件。它试图修复，但发现有些东西回不来。
美术风格严格对标 `full_v1.3.4.mp4`（暖色条纹房间 + 晨窗远山 + 小终端 DSH TUI + 房间内像素角色）。

| 交付物 | 路径 |
|--------|------|
| 渲染脚本 | `src/render_error_arena.js` |
| 重叠检测 | `src/check_overlap_error.js` |
| 音频合成 | `scripts/build_audio_error.js` |
| 最终视频 | `outputs/error_arena_v1.0.mp4` |
| 合成音轨 | `audio/error_arena_mix.wav` |
| 验收报告 | `docs/verify-error-arena.md` |

```bash
npm install
npm run check:error      # 重叠检测 → 16/16 PASSED, 0 issues
npm run render:error     # 1800 帧 @ 640×360 → 1280×720 (SCALE=2)
npm run audio:error      # BGM×0.3 + click×0.5, amix normalize=0
npm run build:error      # check + render + audio + mux → outputs/error_arena_v1.0.mp4
```

规格：640×360 基础分辨率 × SCALE=2 → 1280×720 @ 60fps · 1800 帧 / 30.00s · h264 + aac
字体：Fusion Pixel（终端 10px / 字幕 14px）· 字幕逐字 160ms · 终端打字 140ms
场景：E1 删错了 (0-10s) → E2 试图修复 (10-20s) → E3 安慰 (20-30s)，场景间 0.5s 黑场
情绪：暖 → 冷（房间转冷 + Clawd 去饱和）→ 回暖

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
