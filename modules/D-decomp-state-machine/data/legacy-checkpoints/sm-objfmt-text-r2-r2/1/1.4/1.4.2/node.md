# N48: 工作点2（高吞吐/高Batch）：batch_size=4, seq_len=32768, BF16精度下，激活值显存占用随batch线性增长至约16.0 GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

工作点2（高吞吐/高Batch）：batch_size=4, seq_len=32768, BF16精度下，激活值显存占用随batch线性增长至约16.0 GB，加上15%碎片开销后总计约18.4 GB，此时激活值显存需求(18.4GB)已超过KV Cache(13.7GB)，成为显存分配的主要瓶颈，限制了单卡可承载的最大并发数。

## Corrected Claim

工作点2（高吞吐/高Batch）：batch_size=4, seq_len=32768, BF16精度下，激活值显存占用随batch线性增长至约16.0 GB，加上15%碎片开销后总计约18.4 GB，此时激活值显存需求(18.4GB)已超过KV Cache(13.7GB)，成为显存分配的主要瓶颈，限制了单卡可承载的最大并发数。

## Evidence

先验知识/题面给定，逻辑校验通过：16.0 * 1.15 = 18.4，数值计算准确；18.4 > 13.7，比较逻辑正确；激活值随batch线性增长符合Transformer推理显存占用的一般规律。
