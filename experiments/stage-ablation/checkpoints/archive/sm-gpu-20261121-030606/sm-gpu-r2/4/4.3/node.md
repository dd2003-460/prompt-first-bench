# N21: Qwen3-27B模型在BF16精度下的总显存需求（权重+激活值+KV Cache）在32K上下文长度下约为65GB，FP8/INT8精度下约为40GB，NVF

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下的总显存需求（权重+激活值+KV Cache）在32K上下文长度下约为65GB，FP8/INT8精度下约为40GB，NVFP4/W4精度下约为25GB

## Corrected Claim

Qwen3-27B模型在BF16精度下的总显存需求（权重+激活值+KV Cache）在32K上下文长度下约为65GB，FP8/INT8精度下约为40GB，NVFP4/W4精度下约为25GB

## Evidence

父节点级核验未通过：非正交（子节点1和子节点2存在严重逻辑矛盾。子节点1声称N21中BF16下的KV Cache为5.2GB，而子节点2通过精确计算指出在相同参数假设下KV Cache仅为3.98GB，并指出N21估算可能高估。这两个子节点对同一关键组件（KV Cache）的数值认定不一致，破坏了正交性。此外，子节点1试图用5.2GB去凑总显存65GB，而子节点2否定了5.2GB的合理性，导致子节点1的分解基础不成立。）
