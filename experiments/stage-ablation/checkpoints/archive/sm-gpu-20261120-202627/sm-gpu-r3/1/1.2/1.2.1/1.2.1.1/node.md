# N171: GQA 机制对 KV Cache 带宽压力的修正效应：相比 MHA (32 heads)，GQA (8 heads) 将每 token 解码阶段需读取的 KV 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

GQA 机制对 KV Cache 带宽压力的修正效应：相比 MHA (32 heads)，GQA (8 heads) 将每 token 解码阶段需读取的 KV 数据量减少至 1/4，从而将带宽瓶颈阈值降低 75%，使得 RTX 4090 (1008 GB/s) 等消费级显卡在 32K 上下文下的理论延迟可行性显著提升。

## Corrected Claim

GQA 机制对 KV Cache 带宽压力的修正效应：相比 MHA (32 heads)，GQA (8 heads) 将每 token 解码阶段需读取的 KV 数据量减少至 1/4，从而将带宽瓶颈阈值降低 75%，使得 RTX 4090 (1008 GB/s) 等消费级显卡在 32K 上下文下的理论延迟可行性显著提升。

## Evidence

先验知识/题面给定，逻辑校验通过：GQA将KV头数从32降至8，KV Cache大小及读取带宽需求线性减少至1/4，带宽瓶颈阈值降低75%的推导符合线性缩放原理，数值量级合理。
