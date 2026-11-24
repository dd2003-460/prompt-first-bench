# N441: 高码率工作点的缓存命中率 H_video=65% 的量化依据：对象大小 s=8.0MB，边缘节点 SSD 缓存（5TB/POP）可容纳 N_hot = 5000

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

高码率工作点的缓存命中率 H_video=65% 的量化依据：对象大小 s=8.0MB，边缘节点 SSD 缓存（5TB/POP）可容纳 N_hot = 5000GB / 8.0MB ≈ 625K 个对象；相比低码率（2.5M 个）覆盖度降至 1/4，导致命中率从 90% 降至 65%（基于 Zipf 分布中仅头部热门对象被覆盖）。

## Corrected Claim

高码率工作点的缓存命中率 H_video=65% 的量化依据：对象大小 s=8.0MB，边缘节点 SSD 缓存（5TB/POP）可容纳 N_hot = 5000GB / 8.0MB ≈ 625K 个对象；相比低码率（2.5M 个）覆盖度降至 1/4，导致命中率从 90% 降至 65%（基于 Zipf 分布中仅头部热门对象被覆盖）。

## Evidence

先验知识/题面给定，逻辑校验通过：5000GB/8MB=625K对象，625K/2.5M=1/4，符合Zipf分布头部覆盖逻辑
