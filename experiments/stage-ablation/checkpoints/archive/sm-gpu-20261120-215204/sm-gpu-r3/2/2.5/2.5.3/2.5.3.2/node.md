# N234: 在 LLM 解码阶段 (Memory-Bound)，显存带宽利用率修正因子 η 对于 W4 精度，η 通常在 0.75-0.90 之间，因为 4-bit 权重需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

在 LLM 解码阶段 (Memory-Bound)，显存带宽利用率修正因子 η 对于 W4 精度，η 通常在 0.75-0.90 之间，因为 4-bit 权重需要更复杂的反量化逻辑 (如 GPTQ/AWQ 的查找表或算术运算)，且内存访问模式可能因非对齐访问而效率降低。

## Corrected Claim

在 LLM 解码阶段 (Memory-Bound)，显存带宽利用率修正因子 η 对于 W4 精度，η 通常在 0.75-0.90 之间，因为 4-bit 权重需要更复杂的反量化逻辑 (如 GPTQ/AWQ 的查找表或算术运算)，且内存访问模式可能因非对齐访问而效率降低。

## Evidence

先验知识/题面给定，逻辑校验通过
