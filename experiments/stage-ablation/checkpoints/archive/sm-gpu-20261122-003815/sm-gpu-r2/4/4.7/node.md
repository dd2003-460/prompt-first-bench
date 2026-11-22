# N28: 批处理大小 (Batch Size) 对吞吐的非线性影响：在显存受限下，最大 batch size B_max = (available_vram - weig

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

批处理大小 (Batch Size) 对吞吐的非线性影响：在显存受限下，最大 batch size B_max = (available_vram - weights - fixed_kv) / kv_per_token。吞吐提升因子 ≈ min(B_max, compute_saturation_point)。通常 B=1 到 B=4 时吞吐接近线性增长，B>8 后受计算瓶颈限制增长放缓。

## Corrected Claim

批处理大小 (Batch Size) 对吞吐的非线性影响：在显存受限下，最大 batch size B_max = (available_vram - weights - fixed_kv) / kv_per_token。吞吐提升因子 ≈ min(B_max, compute_saturation_point)。通常 B=1 到 B=4 时吞吐接近线性增长，B>8 后受计算瓶颈限制增长放缓。

## Evidence

先验知识/题面给定，逻辑校验通过
