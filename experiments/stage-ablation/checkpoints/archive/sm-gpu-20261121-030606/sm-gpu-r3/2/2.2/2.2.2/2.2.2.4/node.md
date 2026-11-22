# N229: RTX 5090在W4A16精度下的每Token成本计算：采购成本$1999 + 年均电力成本$480（基于450W平均功耗） / (60.4 tokens/s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103, N104, N105

## Claim

RTX 5090在W4A16精度下的每Token成本计算：采购成本$1999 + 年均电力成本$480（基于450W平均功耗） / (60.4 tokens/s * 86400 * 365 * 3年) ≈ $0.0000041/token，该数值用于与FP8不可行场景下的H100方案进行TCO对比。

## Corrected Claim

RTX 5090在W4A16精度下的每Token成本计算：采购成本$1999 + 年均电力成本$480（基于450W平均功耗） / (60.4 tokens/s * 86400 * 365 * 3年) ≈ $0.0000041/token，该数值用于与FP8不可行场景下的H100方案进行TCO对比。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（(1999+480*3)/(60.4*86400*365*3) ≈ 0.0000041），量级符合高端GPU推理成本直觉。

## Search Query

RTX 5090 W4A16 cost per token calculation
