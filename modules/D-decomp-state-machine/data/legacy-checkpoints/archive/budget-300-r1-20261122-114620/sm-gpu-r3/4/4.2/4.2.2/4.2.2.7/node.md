# N333: PCIe Gen4 x16 互连带宽下，双卡间权重加载时间 T_load 的计算需区分场景：若权重预加载至显存（常驻），T_load=0；若每次请求重新加载，T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106, N107, N108

## Claim

PCIe Gen4 x16 互连带宽下，双卡间权重加载时间 T_load 的计算需区分场景：若权重预加载至显存（常驻），T_load=0；若每次请求重新加载，T_load = 54GB / 32GB/s ≈ 1.69s；若采用权重分片（Tensor Parallelism），每卡仅加载 27GB，T_load = 27GB / 32GB/s ≈ 0.84s，但需增加 All-Reduce 通信开销

## Corrected Claim

PCIe Gen4 x16 互连带宽下，双卡间权重加载时间 T_load 的计算需区分场景：若权重预加载至显存（常驻），T_load=0；若每次请求重新加载，T_load = 54GB / 32GB/s ≈ 1.69s；若采用权重分片（Tensor Parallelism），每卡仅加载 27GB，T_load = 27GB / 32GB/s ≈ 0.84s，但需增加 All-Reduce 通信开销

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe Gen4 x16 理论带宽约 32GB/s，算术计算 54/32≈1.69 和 27/32≈0.84 正确，TP 分片逻辑自洽。
