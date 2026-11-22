# N281: 计算 MI300X (FP8) 的最大并发 Batch Size：Max_Batch = (192GB - 28.6GB - 3GB) / 0.625GB ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

计算 MI300X (FP8) 的最大并发 Batch Size：Max_Batch = (192GB - 28.6GB - 3GB) / 0.625GB ≈ 160 / 0.625 = 256。即理论上可支持 256 并发 32K 上下文请求。

## Corrected Claim

计算 MI300X (FP8) 的最大并发 Batch Size：Max_Batch = (192GB - 28.6GB - 3GB) / 0.625GB ≈ 160 / 0.625 = 256。即理论上可支持 256 并发 32K 上下文请求。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X 显存 192GB 为已知规格，扣除模型权重(28.6GB)和系统开销(3GB)后剩余约 160.4GB，除以单请求 KV Cache 占用 0.625GB，计算结果 256 在数学上成立且量级合理。
