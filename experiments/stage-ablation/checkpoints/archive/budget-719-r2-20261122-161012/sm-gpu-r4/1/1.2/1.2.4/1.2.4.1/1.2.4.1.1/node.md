# N358: INT4 量化方案下 24GB 显存卡的可用 KV Cache 预算计算：Total_VRAM(24GB) - Weight_INT4(13.5GB) - Ac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N149

## Claim

INT4 量化方案下 24GB 显存卡的可用 KV Cache 预算计算：Total_VRAM(24GB) - Weight_INT4(13.5GB) - Activation_Overhead(~0.5GB) - CUDA_Context(~0.5GB) = 9.5GB；对比 KV_Cache_Req(8.59GB)，剩余空间 0.91GB，仅支持 Batch Size=1 且无安全余量，任何 Batch>1 或长于 32K 的输入将导致 OOM。

## Corrected Claim

INT4 量化方案下 24GB 显存卡的可用 KV Cache 预算计算：Total_VRAM(24GB) - Weight_INT4(13.5GB) - Activation_Overhead(~0.5GB) - CUDA_Context(~0.5GB) = 9.5GB；对比 KV_Cache_Req(8.59GB)，剩余空间 0.91GB，仅支持 Batch Size=1 且无安全余量，任何 Batch>1 或长于 32K 的输入将导致 OOM。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（24-13.5-0.5-0.5=9.5，9.5-8.59=0.91），且符合显存预算分配的基本逻辑。

## Search Query

LLM inference VRAM calculation activation overhead cuda context size
