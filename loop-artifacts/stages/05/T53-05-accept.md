# T53 阶段 05：验收核验（Lead 逐项检查，2026-11-16）

> 对照 `tasks/D-decomp-state-machine/TASK-D01-t53-decomp-state-machine-main.md` §AC 逐条核验。
> 结论：**不达标（4/7 过）**，3 条未达，其中 2 条可本地解、1 条被 8787 基础设施阻塞。

## 1. AC 逐条裁决

| AC | 结果 | 证据 |
|---|---|---|
| AC1 节点效率 | ✅ | gpu 树 163 节点 ≤200（v17 是 1930）；gap_check 正交维度 7 ≥6（`runs-s5-sm-gpu-mc.log` gap_check A 行）。nat 278 / soc 283 超 200，但 AC1 口径写的是"GPU 单题" |
| AC2 防泄漏 | ✅ | 全程无 LeakError（`s5_state_machine.py` line 467/470/1063 每轮 decompose/rework 输出后执行 leak_check，命中即 ABORT）；q6-nev 日志无 LEAK 行。checkpoint 中"新能源汽车"出现 61 次属 SOP 白名单（题目给定实体，`sm-leak-sop.md` §泄漏判定口径 r4 审计先例） |
| AC3 核验覆盖 ≥90% | ⚠️ 部分 | soc 55/56=0.982 ✅、gpu 61/64=0.953 ✅、**nat 24/37=0.649 ❌**。nat 树有 70 个 pending 节点——是 8787 proxy 502 中断导致未跑完，非状态机逻辑缺陷。解除条件：8787 稳定后 `--resume` 续跑 nat 树完成节点核验 |
| AC4 打赢 SOTA | ❌ 未跑 | q6-nev 停在 24 节点（9 verified / 11 degraded / 4 pending，502 中断，checkpoint 可续）；q7-rd / q8-nvda 未启动；SOTA 基线分数未取（`modules/E-sota-benchmark/research/sm-bench-sota-criteria.md` 有对标清单，基线数值 [待核验]）。需 ≥5 题，当前 0 题完成 |
| AC5 返工生效 | ✅ | gpu 40 次 rework，其中 N29/N45/N31/N18 返工后终态 verified；nat 1 个（N28）；soc 5 次（未翻回，但 AC5 只要求 ≥1 题） |
| AC6 SOP 落盘 | ✅ | 5 文件全存在非空：sm-leak-sop 57 行 / sm-error-paths 73 行 / sm-modification-log 119 行 / sm-thinking-sop 641 行 / sm-bench-sota-criteria 64 行 |
| AC7 可复现 | ❌ | `s5_state_machine.py` line 346 `random.sample` 无 seed；`t53_synth.py` temperature=0.7 无 seed。结果不可重放。另注：8787 推理引擎侧采样是否可复现 [待核验]（取决于 ninfer 后端） |

## 2. 未达标项的处置

| 项 | 性质 | 处置 |
|---|---|---|
| AC3 nat 0.649 | 基础设施阻塞（502） | 8787 已恢复，nat synth 补跑占用中；跑完后 `--resume` 续跑 nat 状态机树补完 70 pending 节点，重测覆盖率 |
| AC4 SOTA bench | 未启动 + 需串行 | q6 resume → q7 → q8 → 再选 2 题，每题状态机+综合+judge 约 1-2h，8787 单路串行。SOTA 基线分数需先经 ego-browser 取公开结果 [待核验] |
| AC7 seed | 本地代码缺口 | 状态机 random 部分加 SEED 环境变量（向后兼容）；LLM 采样侧可复现性受 8787 后端限制，如实标注 |

## 3. 对 goal 的裁决

**不 complete**。按 05-accept SOP「不达标 → 回 03 发补充任务书」，补充任务书内容 = 上表 3 项。
其中 AC7 是小改动，Lead 本地直接做（不外包）；AC3/AC4 是长 run，排 8787 串行队列：
nat synth 补跑（进行中）→ nat 状态机 resume → q6 resume → q7 → q8 → SOTA 基线核验。