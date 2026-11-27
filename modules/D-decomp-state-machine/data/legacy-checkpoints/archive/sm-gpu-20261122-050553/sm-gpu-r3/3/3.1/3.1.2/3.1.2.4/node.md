# N198: AMD Radeon PRO W7900 (48GB HBM3) 在 BF16 精度下不可行，显存缺口为 38.0 GB (86.0 GB 需求 - 48.0 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

AMD Radeon PRO W7900 (48GB HBM3) 在 BF16 精度下不可行，显存缺口为 38.0 GB (86.0 GB 需求 - 48.0 GB 容量)；需采用 FP8 权重 (27GB) + BF16 KV (32GB) = 59GB 仍超容，或 FP8 权重 + INT8 KV (16GB) = 43GB 可行。

## Corrected Claim

AMD Radeon PRO W7900 (48GB HBM3) 在 BF16 精度下不可行，显存缺口为 38.0 GB (86.0 GB 需求 - 48.0 GB 容量)；需采用 FP8 权重 (27GB) + BF16 KV (32GB) = 59GB 仍超容，或 FP8 权重 + INT8 KV (16GB) = 43GB 可行。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（86-48=38, 27+32=59, 27+16=43），且符合大模型显存估算的基本逻辑（权重+KV Cache）。
