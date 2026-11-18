# Prompt 组合消融矩阵

## 消融维度

| 维度 | 变量 | 取值 | 说明 |
|------|------|------|------|
| D1 | 分解 prompt | P1_decompose / P1H_index | 一次性分解 vs 逐层 INDEX 分解 |
| D2 | 核验 prompt | P3_verify（基线）/ P3_verify_no_challenge（去掉反方质询） | 质询机制消融 |
| D3 | 综合 prompt | P4_synthesize（基线）/ P4_synthesize_simple（去掉分析层） | 分析层消融 |
| D4 | 质检门 | none / Q2_only / Q4_only / Q2+Q4 | 正交性 + 可压缩复杂度 |
| D5 | 矛盾扫描 | off / on | D33 全局矛盾扫描 |

## 组合矩阵（2^4 = 16 组合，D1 固定 P1H_index 因为状态机只用这个）

| 臂 | D2 | D3 | D4 | D5 | 说明 |
|----|----|----|----|----|------|
| A0 | baseline | baseline | none | off | 基线（当前 s5_state_machine 行为） |
| A1 | no_challenge | baseline | none | off | 去掉质询 |
| A2 | baseline | simple | none | off | 去掉分析层 |
| A3 | no_challenge | simple | none | off | 去掉质询+分析层 |
| A4 | baseline | baseline | Q2_only | off | 加正交性 |
| A5 | baseline | baseline | Q4_only | off | 加可压缩复杂度 |
| A6 | baseline | baseline | Q2+Q4 | off | 加正交性+可压缩复杂度 |
| A7 | baseline | baseline | Q2+Q4 | on | 加正交性+可压缩复杂度+矛盾扫描 |
| A8 | no_challenge | simple | Q2+Q4 | on | 全消融+全质检 |
| A9 | baseline | baseline | none | on | 只加矛盾扫描 |

## 题目

s8b_pilot.py QUESTIONS 里的 3 道：
- nat: 自然语言处理
- soc: 社会/经济
- gpu: GPU 硬件

## 指标

| 指标 | 来源 | 说明 |
|------|------|------|
| coverage | s8b_pilot.judge | gold 要点覆盖率 |
| depth_score | judge_v2_depth.score_run | 深度连续分 |
| verified_rate | rounds_log | 核验通过率 |
| n_nodes | len(nodes) | 最终树大小 |
| wall_s | time | 总耗时 |
| n_orthogonal_dropped | rounds_log | Q2 丢弃数 |
| n_compression_dropped | rounds_log | Q4 丢弃数 |
| contradictions_found | rounds_log | Q5 检出数 |

## 产出

- `runs-qc-ablation/{arm}-{qid}-r1.json` — 每臂每题一个 JSON
- `runs-qc-ablation/step-log/{arm}-{qid}.jsonl` — 逐步日志（每步一行 JSON）
- `runs-qc-ablation/summary.md` — 汇总表格
