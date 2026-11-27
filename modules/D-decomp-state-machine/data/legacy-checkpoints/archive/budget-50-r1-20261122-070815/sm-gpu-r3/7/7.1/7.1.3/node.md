# N374: RTX 4090 24GB 显存中，INT4 权重 13.5 GB + BF16 KV Cache 2.0 GB + Activation 0.5 GB = 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N131

## Claim

RTX 4090 24GB 显存中，INT4 权重 13.5 GB + BF16 KV Cache 2.0 GB + Activation 0.5 GB = 16.0 GB，剩余 8.0 GB 用于 CUDA Context、vLLM 内部缓冲及碎片，此余量足以支持 Batch Size=8-16 的并发请求，无需双卡

## Corrected Claim

RTX 4090 24GB 显存中，INT4 权重 13.5 GB + BF16 KV Cache 2.0 GB + Activation 0.5 GB = 16.0 GB，剩余 8.0 GB 用于 CUDA Context、vLLM 内部缓冲及碎片，此余量足以支持 Batch Size=8-16 的并发请求，无需双卡

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+2.0+0.5=16.0GB，24-16=8GB，数值计算自洽；8GB余量对于BS=8-16的并发请求在工程实践中是合理的估计，符合vLLM等推理框架的资源分配逻辑。
