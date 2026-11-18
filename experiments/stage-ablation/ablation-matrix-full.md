# 完整消融矩阵（2026-11-18 夜）

> origin: ai · D 指令「我要求完整的消融矩阵」
> 一句话：现有 A0-A9 只能估 4 个主效应 + 2 个二阶交互，补 4 臂（A10-A13）后所有主效应 + 所有二阶交互都可估，14 臂 × 3 题 × 3 rep = 126 runs。

## 0. 两套矩阵的关系（别混）

| 矩阵 | 测什么 | 臂 | 状态 |
|------|--------|----|------|
| S0-S5 阶段消融 | 流程复杂度（每加一个阶段涨多少） | S0 裸答→S5 完整流程，累积式 | 已跑（T17 报告，n=90） |
| A0-A13 prompt 组件消融 | prompt 组件交互（质询/分析层/质检门/矛盾扫描） | 4 因子 14 臂 | 部分跑（仅 A0-nat） |

两套正交：S0-S5 回答「流程要不要这么长」，A0-A13 回答「流程里每个组件值不值」。本文件只规划 A0-A13（当前要跑的），S0-S5 作为背景。

## 1. 因子与水平

| 因子 | 变量 | 水平 | 说明 |
|------|------|------|------|
| D2 | 核验 prompt | baseline / no_challenge | 反方质询机制消融 |
| D3 | 综合 prompt | baseline / simple | 分析层消融 |
| D4 | 质检门 | none / Q2 / Q4 / Q2Q4 | 正交性 + 可压缩复杂度 |
| D5 | 矛盾扫描 | off / on | 全局矛盾扫描 |

全因子组合 = 2×2×4×2 = 32。现有 10 臂 + 补 4 臂 = 14 臂（覆盖所有主效应 + 所有二阶交互角点，不跑满 32 是因为三阶及以上交互在 n=3 下功效不足，记入 backlog）。

## 2. 完整矩阵（A0-A13）

| 臂 | D2 | D3 | D4 | D5 | 说明 | 状态 |
|----|----|----|----|----|------|------|
| A0 | baseline | baseline | none | off | 基线 | 已跑 nat |
| A1 | no_challenge | baseline | none | off | 去质询 | 待跑 |
| A2 | baseline | simple | none | off | 去分析层 | 待跑 |
| A3 | no_challenge | simple | none | off | 去质询+分析层 | 待跑 |
| A4 | baseline | baseline | Q2 | off | 加正交性 | 待跑 |
| A5 | baseline | baseline | Q4 | off | 加可压缩复杂度 | 待跑 |
| A6 | baseline | baseline | Q2Q4 | off | 加正交性+可压缩 | 待跑 |
| A7 | baseline | baseline | Q2Q4 | on | +矛盾扫描 | 待跑 |
| A8 | no_challenge | simple | Q2Q4 | on | 全消融+全质检 | 待跑 |
| A9 | baseline | baseline | none | on | 只加矛盾扫描 | 待跑 |
| **A10** | no_challenge | baseline | Q2Q4 | off | **补：D2×D4 角点** | 待跑 |
| **A11** | no_challenge | baseline | none | on | **补：D2×D5 角点** | 待跑 |
| **A12** | baseline | simple | Q2Q4 | off | **补：D3×D4 角点** | 待跑 |
| **A13** | baseline | simple | none | on | **补：D3×D5 角点** | 待跑 |

加粗 4 臂（A10-A13）是补全二阶交互角点必需的，缺了它们 D2×D4 / D2×D5 / D3×D4 / D3×D5 四个交互估不出来。

## 3. 统计可估计性

### 主效应（全部可估）

| 效应 | 角点 | 状态 |
|------|------|------|
| D2 | A0 vs A1 | ✓ |
| D3 | A0 vs A2 | ✓ |
| D4 | A0/A4/A5/A6（4 水平） | ✓ |
| D5 | A0 vs A9 | ✓ |

### 二阶交互（补 A10-A13 后全部可估）

| 交互 | 2×2 角点 | 状态 |
|------|---------|------|
| D2×D3 | A0/A1/A2/A3 | ✓ 已有 |
| D2×D4 | A0/A1/A6/**A10** | 补 A10 |
| D2×D5 | A0/A1/A9/**A11** | 补 A11 |
| D3×D4 | A0/A2/A6/**A12** | 补 A12 |
| D3×D5 | A0/A2/A9/**A13** | 补 A13 |
| D4×D5 | A0/A6/A7/A9 | ✓ 已有 |

注：D4 有 4 水平，交互按 none vs Q2Q4 二水平近似估（Q2/Q4 单独效果由主效应覆盖）。完全估计 4 水平交互需 32 臂全跑，n=3 下三阶交互功效不足，不跑，记 backlog。

## 4. 题目集

s8b_pilot.py QUESTIONS 的 3 道：
- nat：自然语言处理（copula/相关结构）
- soc：社会/经济（二手交易演化心理学）
- gpu：GPU 硬件（H100 规格）

跨域覆盖：查表型（gpu）/ 观点型（soc）/ 结构型（nat）。

## 5. 指标

| 指标 | 来源 | 说明 |
|------|------|------|
| coverage | s8b_pilot.judge | gold 要点覆盖率 |
| depth_score | judge_v2_depth.score_run | 深度连续分 |
| verified_rate | rounds_log | 核验通过率 |
| n_nodes | len(nodes) | 最终树大小 |
| wall_s | time | 总耗时 |
| n_orthogonal_dropped | rounds_log | Q2 丢弃数 |
| n_compression_dropped | rounds_log | Q4 丢弃数 |
| contradictions_found | rounds_log | 矛盾扫描检出数 |

## 6. 执行计划

### 顺序（按 VRAM/8787 负载排）

1. **gptr 三题×3rep depth=6/breadth=6**（外部 baseline D1，独立 venv，不占 8787 推理）— 进行中
2. **langgraph nat**（S5 状态机，占 8787）— 进行中
3. **langgraph gpu**（S5 状态机，占 8787）— nat 完成后启动
4. **A0-A13 消融**（qc_ablation_sweep.py，占 8787）— 上面 3 个完成后启动

### 时间估计

| 任务 | runs | 单 run 耗时 | 总耗时 |
|------|------|------------|--------|
| gptr 3 题×3rep depth=6 | 9 | ~6-10 min | ~1-1.5 h（已跑 4/9） |
| langgraph nat max-nodes 12 | 1 | ~30-50 min | ~30-50 min |
| langgraph gpu max-nodes 12 | 1 | ~30-50 min | ~30-50 min |
| A0-A13 × 3 题 × 3 rep | 126 | ~5-8 min | ~10-17 h |

A0-A13 是大头，要跑一整夜 + 白天。断点续跑已实现（qc_ablation_sweep.py 每 run 落盘 step-log，重启跳过已完成的）。

### 断点续跑

- gptr：已 patch（每 run 完成立即写 summary.json，重启读回跳过已完成）
- langgraph：SqliteSaver checkpoint（控制流）+ _save_checkpoint（树形数据），crash 后从最后 checkpoint 恢复
- A0-A13：step-log/{arm}-{qid}.jsonl 每步落盘，重启跳过已完成 run

## 7. 判据

1. **主效应**：每个因子的 Δ = mean(高水平) − mean(低水平)，按总分和按维度分别看。Δ ≤ 0 的组件 = 砍掉或重做。
2. **交互**：D2×D5（质询×矛盾扫描）和 D3×D4（分析层×质检门）是重点——如果交互显著，说明组件不是独立叠加而是耦合的，论文主 claim 落在「X 组件在 Y 条件下才有价值」。
3. **发布判据**：S5（A7 或 A8）≥ GPT Researcher（D1，gptr 三题）。
4. **诚实条款**：n=3 只出方向性结论，「显著」措辞必须附 n=3 限定；judge 自判维度 conf 上限 0.7；D1 的 harness 差异（联网深度不等价）如实标注。

## 8. 不做的事（边界）

- 不跑满 32 臂（三阶交互 n=3 功效不足）
- 不提 n 到 ≥4（预算外，backlog）
- 不改 loop/prompt-first/ 阶段文件
- 不把 gold 泄漏进 prompt
- 不把 D1 的 pipeline 改动包装成公平对比
