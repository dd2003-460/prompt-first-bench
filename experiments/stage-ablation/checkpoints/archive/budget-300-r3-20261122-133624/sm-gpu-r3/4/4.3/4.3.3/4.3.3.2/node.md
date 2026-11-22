# N318: RTX 5090 的 NVFP4 量化模型在 vLLM 中的显存占用计算：权重 13.5GB + KV Cache (32K tokens, batch=1) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

RTX 5090 的 NVFP4 量化模型在 vLLM 中的显存占用计算：权重 13.5GB + KV Cache (32K tokens, batch=1) 约 1.2GB + 框架开销 0.5GB = 15.2GB，低于 32GB 显存限制，可行。若降级为 FP16，权重 54GB > 32GB，不可行。因此驱动版本是硬性前置条件，不可降级运行。

## Corrected Claim

RTX 5090 的 NVFP4 量化模型在 vLLM 中的显存占用计算：权重 13.5GB + KV Cache (32K tokens, batch=1) 约 1.2GB + 框架开销 0.5GB = 15.2GB，低于 32GB 显存限制，可行。若降级为 FP16，权重 54GB > 32GB，不可行。因此驱动版本是硬性前置条件，不可降级运行。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存为 32GB，NVFP4 权重 13.5GB 加上 KV Cache 和开销共 15.2GB，小于 32GB，逻辑自洽；FP16 权重 54GB 大于 32GB，逻辑自洽。
