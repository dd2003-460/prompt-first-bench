# N332: RTX 5090 运行 Qwen3-27B FP8 时的最大并发 Batch Size (B_max) 计算：可用显存 = 32GB - 13.5GB (Wei

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107, N108, N109

## Claim

RTX 5090 运行 Qwen3-27B FP8 时的最大并发 Batch Size (B_max) 计算：可用显存 = 32GB - 13.5GB (Weights) - 2GB (Activations/Buffer) = 16.5GB；单请求 KV Cache (FP8) = 2GB；B_max = 16.5GB / 2GB ≈ 8；即理论上支持 8 路并发 32K 上下文请求

## Corrected Claim

RTX 5090 运行 Qwen3-27B FP8 时的最大并发 Batch Size (B_max) 计算：可用显存 = 32GB - 13.5GB (Weights) - 2GB (Activations/Buffer) = 16.5GB；单请求 KV Cache (FP8) = 2GB；B_max = 16.5GB / 2GB ≈ 8；即理论上支持 8 路并发 32K 上下文请求

## Evidence

先验知识/题面给定，逻辑校验通过：显存计算（32-13.5-2=16.5GB）及并发数推导（16.5/2≈8）在算术和逻辑上自洽，符合大模型推理显存估算的基本原理。
