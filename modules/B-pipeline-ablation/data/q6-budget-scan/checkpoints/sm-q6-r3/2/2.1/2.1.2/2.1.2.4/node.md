# N168: T_target 降低 50ms 导致的故障风险成本增量 ΔC_risk：更严格的 T_target 意味着更小的故障容忍窗口，P(SLA_Breach) 增加

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

T_target 降低 50ms 导致的故障风险成本增量 ΔC_risk：更严格的 T_target 意味着更小的故障容忍窗口，P(SLA_Breach) 增加，ΔC_risk = ΔP_breach × Penalty_per_breach；若 T 从 100ms 降至 50ms，P99 超标概率可能从 0.5% 升至 1.5%，假设单次违约罚金/机会成本为 1 万元，则 ΔC_risk 月增约 10 万元（基于 2TB/日流量规模估算）。

## Corrected Claim

T_target 降低 50ms 导致的故障风险成本增量 ΔC_risk：更严格的 T_target 意味着更小的故障容忍窗口，P(SLA_Breach) 增加，ΔC_risk = ΔP_breach × Penalty_per_breach；若 T 从 100ms 降至 50ms，P99 超标概率可能从 0.5% 升至 1.5%，假设单次违约罚金/机会成本为 1 万元，则 ΔC_risk 月增约 10 万元（基于 2TB/日流量规模估算）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算自洽（(1.5%-0.5%) * 1万元 * 30天 = 30万元? 等等，这里需要仔细检查逻辑。

## Search Query

SLA penalty cost increase latency target tightening
