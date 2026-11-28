# N227: CSP 无解率 P_infeasible 的量化：在随机生成的实验约束中，若约束密度 (E/V) > 4.5，无解概率 P_infeasible > 50%；此

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

CSP 无解率 P_infeasible 的量化：在随机生成的实验约束中，若约束密度 (E/V) > 4.5，无解概率 P_infeasible > 50%；此时系统需回退到 LLM 重新生成松弛约束 (Relaxed Constraints) 的步骤，每次回退增加 1 轮 LLM 推理 (~5s)，若 P_infeasible > 0.1，则自动化模块的平均额外延迟 ΔT_auto = P_infeasible * 5s，需纳入端到端时间预算。

## Corrected Claim

在特定随机生成的实验约束场景中，若约束密度 (E/V) 超过特定阈值（如 4.5），无解概率 P_infeasible 可能显著升高（>50%）；此时系统需回退到 LLM 重新生成松弛约束，每次回退增加约 5s 延迟，平均额外延迟 ΔT_auto ≈ P_infeasible * 5s，需纳入端到端时间预算。

## Evidence

[质询]约束密度阈值 4.5 及对应的无解概率 >50% 属于特定实验设定下的经验数据，并非通用物理或数学定律，不同 CSP 问题域（如调度、图着色、SAT）的相变点差异巨大，该数值缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

constraint satisfaction problem infeasibility probability constraint density phase transition
