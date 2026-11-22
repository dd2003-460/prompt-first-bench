# N137: 在 W4 量化方案下，Batch=4 时的总显存需求 = 权重(13.55GB) + KV Cache(B=4) + 激活值(B=4) + 基础开销(1.02G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

在 W4 量化方案下，Batch=4 时的总显存需求 = 权重(13.55GB) + KV Cache(B=4) + 激活值(B=4) + 基础开销(1.02GB)，需计算该值是否超过 24GB (单卡 4090/3090) 或 48GB (双卡 3090/A6000) 的容量阈值，以判断单卡/双卡可行性边界

## Corrected Claim

在 W4 量化方案下，Batch=4 时的总显存需求 = 权重(13.55GB) + KV Cache(B=4) + 激活值(B=4) + 基础开销(1.02GB)，需计算该值是否超过 24GB (单卡 4090/3090) 或 48GB (双卡 3090/A6000) 的容量阈值，以判断单卡/双卡可行性边界

## Evidence

先验知识/题面给定，逻辑校验通过
