# N548: 低价情景的边界条件：¥2,000/TB 的单价通常对应消费级或入门级企业 NVMe（如 Intel D3-S4520 级别），其 MTBF 可能从 2M 小时降

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N236

## Claim

低价情景的边界条件：¥2,000/TB 的单价通常对应消费级或入门级企业 NVMe（如 Intel D3-S4520 级别），其 MTBF 可能从 2M 小时降至 1M 小时，导致年故障率 P_failure_yearly 翻倍（从 0.043 升至 0.087）。这将使 RTO 代价 C_RTO_annual 翻倍，且需增加备件预算。若计入此风险，低价情景的有效成本需上浮约 5-8% 以覆盖额外的备件与潜在停机损失，削弱其相对基准的 33% 成本优势。

## Corrected Claim

低价情景的边界条件：¥2,000/TB 的单价通常对应消费级或入门级企业 NVMe（如 Intel D3-S4520 级别），其 MTBF 可能从 2M 小时降至 1M 小时，导致年故障率 P_failure_yearly 翻倍（从 0.043 升至 0.087）。这将使 RTO 代价 C_RTO_annual 翻倍，且需增加备件预算。若计入此风险，低价情景的有效成本需上浮约 5-8% 以覆盖额外的备件与潜在停机损失，削弱其相对基准的 33% 成本优势。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF减半导致年故障率翻倍符合数学定义（1/MTBF），成本上浮比例与故障率变化及备件需求在量级上合理自洽。
