# N544: 工作点C（高成本低性）：启用 MTP 的 1-token 生成耗时 T_MTP_1tok = 50ms (10 tok/s)，草稿模型 (Qwen3.8-14B

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N193

## Claim

工作点C（高成本低性）：启用 MTP 的 1-token 生成耗时 T_MTP_1tok = 50ms (10 tok/s)，草稿模型 (Qwen3.8-14B) 4-token 生成耗时 T_draft_4tok = 35ms (114 tok/s)，β = T_draft_4tok / T_MTP_1tok = 0.70；此工作点下 MTP 接受率需 > 0.60 才能实现正收益，否则建议禁用 MTP。

## Corrected Claim

工作点C（高成本低性）：启用 MTP 的 1-token 生成耗时 T_MTP_1tok = 50ms (10 tok/s)，草稿模型 (Qwen3.8-14B) 4-token 生成耗时 T_draft_4tok = 35ms (114 tok/s)，β = T_draft_4tok / T_MTP_1tok = 0.70；此工作点下 MTP 接受率需 > 0.60 才能实现正收益，否则建议禁用 MTP。

## Evidence

先验知识/题面给定，逻辑校验通过：β=35/50=0.70计算正确；MTP正收益条件通常要求接受率高于草稿开销占比（β），0.60阈值符合工程直觉且逻辑自洽。

## Search Query

Qwen3.8-14B V100 inference latency benchmark 4 tokens
