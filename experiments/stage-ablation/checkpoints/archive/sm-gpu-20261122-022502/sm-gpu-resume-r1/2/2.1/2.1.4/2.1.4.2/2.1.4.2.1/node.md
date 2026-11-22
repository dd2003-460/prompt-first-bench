# N570: RTX 4090 32K FP8 双卡方案的通信开销量化：2x 4090 通过 PCIe 4.0 x16 互联，带宽 ~32 GB/s，KV Cache 同步开

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N174

## Claim

RTX 4090 32K FP8 双卡方案的通信开销量化：2x 4090 通过 PCIe 4.0 x16 互联，带宽 ~32 GB/s，KV Cache 同步开销 = (32K tokens * 2 * 128 layers * 128 dims * 1 byte) / 32 GB/s ≈ 2.1s/step，导致有效吞吐从理论 37.4 tokens/s 降至 18.7 tokens/s，效率损失 50%

## Corrected Claim

RTX 4090 32K FP8 双卡方案的通信开销量化：2x 4090 通过 PCIe 4.0 x16 互联，带宽 ~32 GB/s。KV Cache 同步开销需根据实际 KV Cache 大小（取决于模型架构、batch size 等）计算，原陈述中 2.1s/step 的延迟与 32K tokens 的 KV 数据量级不匹配，需重新核算数据量与带宽关系。

## Evidence

[质询]数值量级与硬件规格严重不符：RTX 4090 显存带宽高达 1008 GB/s，而 PCIe 4.0 x16 带宽仅约 32 GB/s。若 KV Cache 同步发生在 GPU 显存之间（通常通过 NVLink 或 PCIe），2.1s 的延迟意味着传输了约 67 GB 数据，这与 32K tokens 的 KV Cache 大小（约 1-2 GB）严重不匹配；若指 PCIe 传输，2.1s 对应 67 GB 数据，远超 32K tokens 的 KV 大小。此外，'32K tokens * 2 * 128 layers * 128 dims' 的计算逻辑存疑，通常 KV Cache 大小取决于 batch size 和 head dim，而非简单的 token 数乘以层数和维度，且 128 dims 对于 LLM 的 head dim 或 hidden dim 均偏小或需明确上下文。 | 经验事实，逻辑自洽但缺来源支持；且数值计算与硬件带宽/数据量级存在明显矛盾，无法验证其合理性。
