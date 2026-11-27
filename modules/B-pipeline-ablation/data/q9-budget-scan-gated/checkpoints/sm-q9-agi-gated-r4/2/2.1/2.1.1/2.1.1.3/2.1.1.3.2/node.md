# N117: 在 TP=4 配置下，15k tokens Prefill 的实际瓶颈从纯计算转向 KV Cache 写入带宽与 HBM 访问模式：每层 Attention 计

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

在 TP=4 配置下，15k tokens Prefill 的实际瓶颈从纯计算转向 KV Cache 写入带宽与 HBM 访问模式：每层 Attention 计算后需将 Key/Value 写入 HBM，15k tokens * 32 layers * 2(K+V) * 8 heads * 128 dim * 1 byte = 960 MB 数据量，以 900 GB/s HBM 带宽计算，纯写入时间约 1.07 ms，但受 Kernel Launch 和同步影响，实际 Prefill 延迟主要由 2.025e14 FLOPs 的计算时间决定，约为 4-5 秒。

## Corrected Claim

在 TP=4 配置下，15k tokens Prefill 的主要瓶颈仍为计算（约 4-5 秒），KV Cache 写入带宽（约 1.07 ms）并非主要瓶颈；尽管写入操作存在，但其耗时相对于计算时间可忽略不计，因此整体延迟由 FLOPs 决定的计算时间主导。

## Evidence

[质询]陈述内部存在逻辑矛盾：前半部分声称瓶颈从计算转向KV Cache写入带宽（暗示内存受限），后半部分却断言实际延迟主要由计算时间决定（暗示计算受限），两者互斥。此外，基于TP=4和900GB/s带宽推算出的1.07ms写入时间与4-5秒的计算时间相比微不足道，无法支撑‘瓶颈转向’的结论，除非计算时间被严重高估或带宽被严重低估，但这与给定的FLOPs和带宽参数不符。 | 先验知识/题面给定，逻辑校验发现内部矛盾：瓶颈归因前后不一致（内存 vs 计算），且数值量级对比显示写入时间远小于计算时间，不支持‘瓶颈转向’的定性描述。
