# N298: 2x RTX 4090 在 BF16 精度下的总显存需求计算：权重 54GB + KV Cache 10.7GB + 框架开销 4GB = 68.7GB，远超 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

2x RTX 4090 在 BF16 精度下的总显存需求计算：权重 54GB + KV Cache 10.7GB + 框架开销 4GB = 68.7GB，远超 48GB 物理显存，导致 BF16 方案不可行，必须降级至 INT8 或 W4。

## Corrected Claim

2x RTX 4090 在 BF16 精度下的总显存需求计算：权重 54GB + KV Cache 10.7GB + 框架开销 4GB = 68.7GB，远超 48GB 物理显存，导致 BF16 方案不可行，必须降级至 INT8 或 W4。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 物理显存为 48GB，计算出的 68.7GB 需求确实超出物理限制，结论符合硬件约束逻辑。
