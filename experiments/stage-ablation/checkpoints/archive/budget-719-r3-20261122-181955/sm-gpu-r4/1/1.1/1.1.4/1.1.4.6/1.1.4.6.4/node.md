# N439: 对比结论修正：RTX 3090 Ti (INT4) 的能效比 0.134 tokens/s/W 显著高于 RTX 4090 (FP8) 的 0.064 toke

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N147

## Claim

对比结论修正：RTX 3090 Ti (INT4) 的能效比 0.134 tokens/s/W 显著高于 RTX 4090 (FP8) 的 0.064 tokens/s/W，也高于 RTX 4090 (BF16) 的约 0.036-0.048 tokens/s/W (基于 N147 数据)。因此，在纯能效比维度上，3090 Ti 是更优选择，但其绝对吞吐量 (32.8 vs 20.2 tokens/s) 虽高，但需考虑其较高的功耗和较旧的架构特性（如不支持 FP8 原生加速）。

## Corrected Claim

对比结论修正：RTX 3090 Ti (INT4) 的能效比 0.134 tokens/s/W 显著高于 RTX 4090 (FP8) 的 0.064 tokens/s/W，也高于 RTX 4090 (BF16) 的约 0.036-0.048 tokens/s/W (基于 N147 数据)。因此，在纯能效比维度上，3090 Ti 是更优选择，但其绝对吞吐量 (32.8 vs 20.2 tokens/s) 虽高，但需考虑其较高的功耗和较旧的架构特性（如不支持 FP8 原生加速）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（0.134 > 0.064 > 0.036-0.048），且符合INT4量化通常比FP8/BF16能效比更高的工程常识。
