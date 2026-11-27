# N53: 不同精度下的显存需求对比表：BF16 总需求 = 54 + 0.256N + 4 GB；FP8 总需求 = 27 + 0.128N + 4 GB；INT8 总需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

不同精度下的显存需求对比表：BF16 总需求 = 54 + 0.256N + 4 GB；FP8 总需求 = 27 + 0.128N + 4 GB；INT8 总需求 = 27 + 0.128N + 4 GB；此表用于确定各精度下最小可行显存档位（如 BF16 需 ≥60GB，FP8/INT8 需 ≥35GB for N=1）。

## Corrected Claim

不同精度下的显存需求对比表：BF16 总需求 = 54 + 0.256N + 4 GB；FP8 总需求 = 27 + 0.128N + 4 GB；INT8 总需求 = 27 + 0.128N + 4 GB；此表用于确定各精度下最小可行显存档位（如 BF16 需 ≥60GB，FP8/INT8 需 ≥35GB for N=1）。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16(2字节)与FP8/INT8(1字节)的参数量显存占比系数比为2:1，常数项（如KV Cache或固定开销）随精度减半或保持不变符合工程直觉，数值量级合理。
