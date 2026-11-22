# N55: T_residence 的数值估算：基于 C=128GB 和总请求字节率 R_bytes=50,000,000 * E[size]，假设 E[size]=10K

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

T_residence 的数值估算：基于 C=128GB 和总请求字节率 R_bytes=50,000,000 * E[size]，假设 E[size]=10KB，则 R_bytes≈500GB/day，T_residence ≈ 128GB / (500GB/day * (1-H_LRU))，若 H_LRU=0.7，则 T_residence≈0.85天

## Corrected Claim

T_residence 的数值估算：基于 C=128GB 和总请求字节率 R_bytes=50,000,000 * E[size]，假设 E[size]=10KB，则 R_bytes≈500GB/day，T_residence ≈ 128GB / (500GB/day * (1-H_LRU))，若 H_LRU=0.7，则 T_residence≈0.85天

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 128 / (500 * 0.3) ≈ 0.853 与陈述一致，量纲与数值量级合理。
