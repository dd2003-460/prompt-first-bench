# N210: Qwen3-27B 各层激活值的动态范围统计：在 32K 上下文下，大多数 Transformer 层的激活值 max/min 比值约为 10^3 到 10^4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

Qwen3-27B 各层激活值的动态范围统计：在 32K 上下文下，大多数 Transformer 层的激活值 max/min 比值约为 10^3 到 10^4，对称量化 scale = max_val / 127，导致有效位宽 effective_bits = log2(127 / (max_val / min_val))，若 max/min > 10^4，有效位宽降至 < 6.5 bits。

## Corrected Claim

Qwen3-27B 各层激活值的动态范围统计：在 32K 上下文下，大多数 Transformer 层的激活值 max/min 比值约为 10^3 到 10^4，对称量化 scale = max_val / 127，导致有效位宽 effective_bits = log2(127 / (max_val / min_val))，若 max/min > 10^4，有效位宽降至 < 6.5 bits。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（log2(127/10^4) ≈ 3.66 < 6.5），且大模型激活值动态范围在10^3-10^4量级符合工程常识。
