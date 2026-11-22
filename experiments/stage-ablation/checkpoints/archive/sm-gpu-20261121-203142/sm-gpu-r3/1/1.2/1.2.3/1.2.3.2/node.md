# N142: 在RTX 4090 (24GB) 上运行Qwen3-27B INT8权重 + BF16 KV Cache的显存预算分配：权重~13.6GB (INT8) + K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

在RTX 4090 (24GB) 上运行Qwen3-27B INT8权重 + BF16 KV Cache的显存预算分配：权重~13.6GB (INT8) + KV Cache 4.29GB (32K) + 激活值/缓冲~2GB = ~19.89GB，剩余~4.1GB用于Batch扩展，计算B_max ≈ (24-19.89) / (4.29/32768) ≈ 3116 tokens (理论上限，受激活值动态分配限制)

## Corrected Claim

在RTX 4090 (24GB) 上运行Qwen3-27B INT8权重 + BF16 KV Cache的显存预算分配：权重~13.6GB (INT8) + KV Cache 4.29GB (32K) + 激活值/缓冲~2GB = ~19.89GB，剩余~4.1GB用于Batch扩展，计算B_max ≈ (24-19.89) / (4.29/32768) ≈ 3116 tokens (理论上限，受激活值动态分配限制)

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，INT8量化后权重约13.5-14GB，与13.6GB吻合；KV Cache计算基于32K上下文及BF16精度，数值量级合理；总显存占用19.89GB小于24GB，剩余空间计算逻辑自洽。
