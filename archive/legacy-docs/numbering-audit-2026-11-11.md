# pfb 编号规范审计（2026-11-11）

## 结论

仓库有 **5 套并存的编号体系**，没有一套覆盖全仓。最乱的三处：根目录散落文件、`experiments/stage-ablation/runs-*` 前缀目录、任务 ID 双轨制。

---

## 现有编号体系盘点

### 1. 实验臂编号（runs/ 内 JSON）
格式：`{ARM}-{Qn}-r{k}.json`，如 `S5-Q3-r2.json`
- ARM: S0-S8M, T0-T2, D1, D1deep, S7F/S7T/S7V, S8C/S8E/S8L/S8M
- 问题：Q1-Q9（bench 题号），重复 r1-r3（n=3 median 口径）
- **状态：规范**。全 runs/ 目录一致，无例外。
- 例外：`S2-*-old.json` / `S3-*-old.json` / `S5-*-old.json`（旧 prompt 备份）、`S8-Q*-oldprompt.bak`（后缀不统一：`-old` vs `-oldprompt.bak`）

### 2. 运行批次目录（stage-ablation/ 下 runs-*）
格式：`runs-{label}/`
- 实际存在 30+ 个：`runs-s5-gpu-v3` ~ `v14`, `runs-s5-nat-v14`, `runs-s5-smoke`, `runs-s5-prod`, `runs-baseline`, `runs-d-face`, `runs-d1-c1`, `runs-d1-c1-scored`, `runs-d1score`, `runs-prod`, `runs-prod-s3`, `runs-prod-temp0`, `runs-r293`, `runs-s8b`, `runs-s8b-a3`, `runs-s8b-a4`, `runs-t53`, `runs-t53b`
- **问题**：
  - vN 版本号只用于 s5-gpu 系列（v3-v14），其他系列无版本
  - `runs-r293` — 不知道是什么（可能是某次 ralph round 293）
  - `runs-d1score` vs `runs-d1-c1-scored` — 同一批数据的两种命名
  - `runs-prod` / `runs-prod-s3` / `runs-prod-temp0` — prod 系列三个变体无统一规则
  - 与 runs/ 内的 ARM 编号无关（runs/ 是最终数据，runs-* 是过程批次）

### 3. 任务 ID（tasks/ + experiments/stage-ablation/tasks/）
- **主 tasks/**：T6, T7.1, T8, T23-T53C, R5, R5.1, R5.2audit, RV3G1, G1B, B1, C1C3, TASK-*（无前缀）
- **stage-ablation/tasks/**：D2, T26-T32, T38, T54, decomposition-*, goal-*, pipeline-checklist
- **问题**：
  - T 编号跨两个目录不连续（主 tasks 到 T53C，sub tasks 到 T54）
  - 前缀混乱：T*（主流）、R*（R5/R5.1/RV3G1）、TASK-*（早期）、G*/B*/C*（单字母）
  - 小数点：T7.1, R5.1, R5.2audit（audit 后缀不规范）
  - 日期前缀混入：`2026-11-07-nine-points.md`
  - 描述性文件名混入：`decomposition-pfb-paper-add-t17.md`、`current-goal.md`、`goal-queue.md`

### 4. 研究文档编号（research/）
- 无统一编号。混合了：
  - T 前缀：`T53C-RECEIPT.md`
  - sm- 前缀（state machine 系列）：`sm-leak-sop.md`, `sm-bench-sota-criteria.md`, `sm-error-paths.md`, `sm-modification-log.md`, `sm-thinking-sop.md`
  - 纯描述：`v17-hier-decomposition-blowup.md`, `self-judge-noise-penalty-survey.md`
  - 脚本混入：`build-sm-bench-sota-table.py`, `poll-tpr15.mjs`, `run-poll.mjs`
  - 子目录：`deepresearch-bench/`, `information-theory/`, `interpretability/`, `web-llm/`
- **问题**：research/ 同时放调研文档和工具脚本，职责不清。

### 5. 代码文件编号（stage-ablation/*.py）
- s 前缀：`s5_hierarchy.py`, `s5_pipeline.py`, `s5_state_machine.py`, `s7f_pilot.py`, `s8b_pilot.py`, `s8e_pilot.py`, `s8g_pilot.py`, `s10_runner.py`
- score 前缀：`score.py`, `score_arena_v33.py`, `score_e3_dual_track.py`, `score_m7.py`, `score_s10.py`, `score_s10_v2.py`, `score_single.py`
- 其他：`ablation_harness.py`, `baseline_gptr.py`, `bface_score.py`, `c1c3_paired_test.py`, `cross_judge.py`, `gates.py`, `jaccard_coverage.py`, `judge_v2_depth.py`, `m7_llm_judge.py`, `prod_run.py`, `rerun_local_aligned.py`, `research_hook.py`, `rule_hybrid_prototype.py`, `run_d1.py`, `run_d1_deep.py`, `s3_supplement.py`, `test_gates.py`
- **问题**：s 编号对应实验臂但只在文件名里，与 runs/ 的 ARM 编号语义一致但不显式；score_* 系列 7 个文件无统一后缀规则（有的带版本号 v33/v2，有的不带）。

---

## 根目录散落文件（最乱）

| 文件 | 性质 | 建议 |
|------|------|------|
| `runs-s5-sm-gpu-r3.pid` / `r4.pid` | 进程锁文件 | 删除（已 tracked，git rm） |
| `runs-s5-sm-gpu-r3-console.log` / `r4-console.log` | 控制台日志 | 移入 `experiments/stage-ablation/runs-s5-gpu/` 或删除 |
| `runs-guard-test-console.log` | 测试日志 | 同上 |
| `runs-s5-v16.3-smoke/` (5 files) | 运行数据 | 移入 `experiments/stage-ablation/runs-s5-v16.3-smoke/`（已有同名空目录） |
| `runs-s8n3/` (1 file) | 运行日志 | 移入 `experiments/stage-ablation/runs-s8b/` 或新建 `runs-s8n3/` |
| `loop-state.json.bak` | 备份 | 删除（loop-state.json 本身才是正式文件） |
| `BRIDGE-REPORT.md` | 一次性报告 | 移入 `docs/` 或 `research/` |
| `CONTINUE_MSG.md` | 一次性消息 | 删除或移入 `docs/` |
| `ralph-loop.md` | 配置文档 | 移入 `sop/` |
| `loop-events.md` | 事件日志 | 移入 `loop-artifacts/` 或删除 |
| `notes` (空文件) | 垃圾 | 删除 |
| `knowledge-base/lattice-explained.md` | 单文件目录 | 移入 `research/` 或直接放根 |
| `outputs/full_v1.3.4.mp4` | 视频残留 | 删除（.gitignore 有 *.mp4 但仍被 tracked） |
| `src/check_overlap_E16_arena.js` 等 3 个 JS | arena 渲染脚本 | 移入 `arena-prompts/` 或 `scripts/` |

---

## 推荐统一方案（最小改动）

### 原则
1. **runs/ 不动** — 它是最终数据，ARM-Qn-rk 格式已经稳定且被 scorer 引用。
2. **runs-* 批次目录加版本归一** — 全部改为 `runs/{batch-label}/`（移入 runs/ 子目录），消灭 stage-ablation/ 下的 30 个平级 runs-* 目录。
3. **任务 ID 收口到 tasks/** — 所有任务卡（无论哪个阶段）统一放 `tasks/`，用 `T{n}-{slug}.md` 格式；废弃 stage-ablation/tasks/ 作为任务卡存放地（保留 decomposition 类文件）。
4. **research/ 只放 .md 调研文档** — 脚本移入 `scripts/` 或对应实验目录。
5. **根目录只留 5 个文件** — README.md, CLAUDE.md, APPROVALS.md, loop-state.json, .gitignore。其余全部归位。

### 具体迁移清单（可执行）

```bash
# 1. 根目录清理
git rm runs-s5-sm-gpu-r3.pid runs-s5-sm-gpu-r4.pid
git rm runs-s5-sm-gpu-r3-console.log runs-s5-sm-gpu-r4-console.log runs-guard-test-console.log
git rm loop-state.json.bak notes outputs/full_v1.3.4.mp4
git mv BRIDGE-REPORT.md docs/
git mv CONTINUE_MSG.md docs/
git mv ralph-loop.md sop/
git mv loop-events.md loop-artifacts/
git mv runs-s5-v16.3-smoke/ experiments/stage-ablation/runs-s5-v16.3-smoke/
mkdir -p experiments/stage-ablation/runs-s8n3 && git mv runs-s8n3/s8n3.log experiments/stage-ablation/runs-s8n3/
git mv knowledge-base/lattice-explained.md research/
git mv src/check_overlap_E16_arena.js arena-prompts/
git mv src/render_E01_curious_arena.js arena-prompts/
git mv src/render_E16_sacrifice_arena.js arena-prompts/
rmdir knowledge-base src

# 2. research/ 脚本外迁
git mv research/build-sm-bench-sota-table.py scripts/
git mv research/poll-tpr15.mjs scripts/
git mv research/run-poll.mjs scripts/

# 3. runs-* 批次目录归入 runs/（大动作，需确认 scorer 不引用路径）
# 暂缓 — 先跑通当前 bench 再做
```

### 不做的事
- 不改 runs/ 内的 ARM-Qn-rk 命名（scorer 硬编码引用）
- 不改 tasks/ 内已有 T 编号（历史 commit 里大量引用）
- 不合并 runs-t53 和 runs-t53b（不同实验设计，应保留区分）

---

## 风险

- runs-* 目录迁移可能破坏 `prod_run.py` / `score.py` 里的硬编码路径 → 迁移前 grep 确认
- 任务 ID 收口需要更新 `loop-state.json` 里的 task 引用
- 本审计本身是 L0 可逆操作（只读分析 + 落盘），迁移执行是 L1（git mv 可 revert）