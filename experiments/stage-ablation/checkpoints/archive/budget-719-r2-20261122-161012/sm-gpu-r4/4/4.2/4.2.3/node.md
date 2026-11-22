# N101: RTX 4090 (1008 GB/s) 在 BF16 下 Decode 理论最大吞吐为 1008 / 55 ≈ 18.3 tokens/s；H100 SXM 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

RTX 4090 (1008 GB/s) 在 BF16 下 Decode 理论最大吞吐为 1008 / 55 ≈ 18.3 tokens/s；H100 SXM (3350 GB/s) 理论最大吞吐为 3350 / 55 ≈ 60.9 tokens/s。实际吞吐受内存控制器效率影响，通常打 6-8 折。

## Corrected Claim

RTX 4090 (1008 GB/s) 在 BF16 下 Decode 理论最大吞吐为 1008 / 55 ≈ 18.3 tokens/s；H100 SXM (3350 GB/s) 理论最大吞吐为 3350 / 55 ≈ 60.9 tokens/s。实际吞吐受内存控制器效率影响，通常打 6-8 折。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余性高：三个子节点本质上都是同一公式（带宽/模型大小*效率系数）在不同硬件参数下的实例化，属于‘同构’数据，而非正交的概念维度。2. 完备性不足：父节点仅对比了 RTX 4090 和 H100，子节点引入了父节点未提及的 RTX 5090 和 Apple M3 Ultra，导致信息范围不一致；且未覆盖父节点中隐含的‘55GB模型大小’这一关键前提变量。）

## Search Query

RTX 4090 H100 decode throughput theoretical limit 55GB
