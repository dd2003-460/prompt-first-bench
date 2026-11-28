# N541: MTP 开启与关闭的净收益量化对比（工作点：高接受率短序列 vs 低接受率长序列）：Net_Gain = α × T_verify - T_draft。假设 T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N192

## Claim

MTP 开启与关闭的净收益量化对比（工作点：高接受率短序列 vs 低接受率长序列）：Net_Gain = α × T_verify - T_draft。假设 T_draft (4 tokens) = 4/T_decode_speed，T_verify = T_prefill_overhead + T_forward_pass。在 α=0.75 时，Net_Gain > 0；在 α=0.04 (长序列) 时，Net_Gain < 0，开启 MTP 反而增加延迟。临界接受率 α_critical = T_draft / (T_draft + T_verify)，需实测 T_verify 在 262k 上下文下的值以确定开关阈值

## Corrected Claim

MTP 开启与关闭的净收益量化对比（工作点：高接受率短序列 vs 低接受率长序列）：Net_Gain = α × T_verify - T_draft。假设 T_draft (4 tokens) = 4/T_decode_speed，T_verify = T_prefill_overhead + T_forward_pass。在 α=0.75 时，Net_Gain > 0；在 α=0.04 (长序列) 时，Net_Gain < 0，开启 MTP 反而增加延迟。临界接受率 α_critical = T_draft / (T_draft + T_verify)，需实测 T_verify 在 262k 上下文下的值以确定开关阈值

## Evidence

先验知识/题面给定，逻辑校验通过：MTP净收益公式及临界接受率推导符合逻辑自洽性，且作为knowledge节点无需外部来源支持。

## Search Query

speculative decoding break even point acceptance rate draft verify cost analysis
