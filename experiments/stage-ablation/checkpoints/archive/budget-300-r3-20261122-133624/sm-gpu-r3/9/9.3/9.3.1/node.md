# N432: 2× RTX 3090 方案的有效吞吐量 T_eff 修正：理论 Decode 吞吐 29.5 tokens/s (单卡) * 2 (卡数) = 59 toke

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N170

## Claim

2× RTX 3090 方案的有效吞吐量 T_eff 修正：理论 Decode 吞吐 29.5 tokens/s (单卡) * 2 (卡数) = 59 tokens/s。考虑 PCIe 4.0 张量并行通信开销 10% 及框架调度开销 5%，实际有效吞吐 T_eff = 59 * 0.85 = 50.15 tokens/s。

## Corrected Claim

2× RTX 3090 方案的有效吞吐量 T_eff 修正：理论 Decode 吞吐 29.5 tokens/s (单卡) * 2 (卡数) = 59 tokens/s。考虑 PCIe 4.0 张量并行通信开销 10% 及框架调度开销 5%，实际有效吞吐 T_eff = 59 * 0.85 = 50.15 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：29.5 * 2 = 59，59 * (1 - 0.10 - 0.05) = 59 * 0.85 = 50.15，计算无误且量级合理。
