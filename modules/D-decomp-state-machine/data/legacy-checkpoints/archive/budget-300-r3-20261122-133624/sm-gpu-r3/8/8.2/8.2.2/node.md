# N424: 单位 token 成本盈亏平衡点计算：设 H100 3年 TCO 为 $28,087 (N169)，RTX 4090 3年 TCO 为 $3,198 + $1,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N167

## Claim

单位 token 成本盈亏平衡点计算：设 H100 3年 TCO 为 $28,087 (N169)，RTX 4090 3年 TCO 为 $3,198 + $1,418 (电) + $200 (维护) ≈ $4,816。H100 的吞吐优势需达到 28087/4816 ≈ 5.83 倍才能在单位 token 成本上持平。鉴于 N144 指出 Decode 吞吐比仅 ~1-1.6 倍，H100 在低负载（batch=1）场景下单位 token 成本远高于 RTX 4090，仅在 batch > 4 或 Prefill 密集场景下才具备成本优势。

## Corrected Claim

单位 token 成本盈亏平衡点计算：设 H100 3年 TCO 为 $28,087 (N169)，RTX 4090 3年 TCO 为 $3,198 + $1,418 (电) + $200 (维护) ≈ $4,816。H100 的吞吐优势需达到 28087/4816 ≈ 5.83 倍才能在单位 token 成本上持平。鉴于 N144 指出 Decode 吞吐比仅 ~1-1.6 倍，H100 在低负载（batch=1）场景下单位 token 成本远高于 RTX 4090，仅在 batch > 4 或 Prefill 密集场景下才具备成本优势。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO比值计算正确（28087/4816≈5.83），且基于N144的吞吐比（1-1.6x）推导出的成本劣势结论在逻辑上自洽，符合经济学基本原理。

## Search Query

LLM inference cost per token H100 vs RTX 4090 break even batch size
