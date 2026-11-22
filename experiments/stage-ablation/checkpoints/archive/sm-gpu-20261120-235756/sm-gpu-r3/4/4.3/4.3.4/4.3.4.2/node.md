# N256: 基于修正后的 KV Cache 占用 (12.88GB/req)，RTX 5090 (32GB) 在 FP8 权重 (~14GB) 和 2GB 开销下，可用显存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

基于修正后的 KV Cache 占用 (12.88GB/req)，RTX 5090 (32GB) 在 FP8 权重 (~14GB) 和 2GB 开销下，可用显存为 16GB，理论最大并发 Batch Size = floor(16 / 12.88) = 1，即仅支持单流推理，不支持 N90 中声称的 4 路并发。

## Corrected Claim

基于修正后的 KV Cache 占用 (12.88GB/req)，RTX 5090 (32GB) 在 FP8 权重 (~14GB) 和 2GB 开销下，可用显存为 16GB，理论最大并发 Batch Size = floor(16 / 12.88) = 1，即仅支持单流推理，不支持 N90 中声称的 4 路并发。

## Evidence

先验知识/题面给定，逻辑校验通过：32GB总显存减去14GB权重和2GB开销后剩余16GB，16GB除以12.88GB/req的KV Cache占用，向下取整确实为1，数学推导自洽。
