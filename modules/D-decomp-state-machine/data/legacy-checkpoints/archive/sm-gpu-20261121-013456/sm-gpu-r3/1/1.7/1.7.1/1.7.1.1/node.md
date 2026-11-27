# N172: GQA Group Size=4 对 KV Cache 显存占用的节省系数：相比 MHA (32 KV Heads)，GQA (8 KV Heads) 将 KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

GQA Group Size=4 对 KV Cache 显存占用的节省系数：相比 MHA (32 KV Heads)，GQA (8 KV Heads) 将 KV Cache 显存占用降低至 1/4（即节省 75%），这是 Qwen3-27B 能在 24GB 显存下支持 32K 上下文的关键架构因素。

## Corrected Claim

GQA Group Size=4 对 KV Cache 显存占用的节省系数：相比 MHA (32 KV Heads)，GQA (8 KV Heads) 将 KV Cache 显存占用降低至 1/4（即节省 75%），这是 Qwen3-27B 能在 24GB 显存下支持 32K 上下文的关键架构因素。

## Evidence

先验知识/题面给定，逻辑校验通过：GQA将KV Heads从32降至8，KV Cache显存占用与KV Heads数量成正比，故节省系数为1/4，逻辑自洽且符合架构原理。
