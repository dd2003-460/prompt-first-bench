# N207: 24GB 卡运行 Qwen3-27B INT4 + 32K BF16 KV 的显存余量计算：总需求 = 权重 (14.5 GB) + KV (4.33 GB) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

24GB 卡运行 Qwen3-27B INT4 + 32K BF16 KV 的显存余量计算：总需求 = 权重 (14.5 GB) + KV (4.33 GB) + 激活/框架 (2.0 GB) ≈ 20.83 GB。可用显存 22.5 GB。余量 = 22.5 - 20.83 = 1.67 GB。该余量足以支持 1 个并发请求，但若启用 PagedAttention 且 block_size 设置不当，可能因碎片化导致 OOM，需预留至少 0.5 GB 安全边际。

## Corrected Claim

24GB 卡运行 Qwen3-27B INT4 + 32K BF16 KV 的显存余量计算：总需求 = 权重 (14.5 GB) + KV (4.33 GB) + 激活/框架 (2.0 GB) ≈ 20.83 GB。可用显存 22.5 GB。余量 = 22.5 - 20.83 = 1.67 GB。该余量足以支持 1 个并发请求，但若启用 PagedAttention 且 block_size 设置不当，可能因碎片化导致 OOM，需预留至少 0.5 GB 安全边际。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型INT4权重约13.5-14.5GB，32K上下文BF16 KV Cache约4-5GB，加上激活开销，总显存需求约20-21GB，在24GB卡（可用约22.5GB）上运行确实非常紧张，余量约1.5-2GB，结论符合工程直觉。

## Search Query

vLLM PagedAttention memory fragmentation overhead 4090
