# N664: H100 方案的隐性 TCO 修正项：根据 N306，若 Lead Time 为 3 个月，需计入 $30,000 机会成本；修正后 TCO = 26500 +

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N274

## Claim

H100 方案的隐性 TCO 修正项：根据 N306，若 Lead Time 为 3 个月，需计入 $30,000 机会成本；修正后 TCO = 26500 + 30000 = $56,500；修正后 Cost_Performance = 56500 / 100 = 565 $/tokens/s，此时 H100 性价比显著低于消费级双卡方案，仅在延迟极度敏感 (TTFT < 0.5s) 场景下才具优势。

## Corrected Claim

H100 方案的隐性 TCO 修正项：根据 N306，若 Lead Time 为 3 个月，需计入 $30,000 机会成本；修正后 TCO = 26500 + 30000 = $56,500；修正后 Cost_Performance = 56500 / 100 = 565 $/tokens/s，此时 H100 性价比显著低于消费级双卡方案，仅在延迟极度敏感 (TTFT < 0.5s) 场景下才具优势。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 26500+30000=56500 及 56500/100=565 正确，且符合 H100 高成本与消费级方案对比的常规经济直觉。
