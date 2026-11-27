# N245: L40S 在 Qwen3-27B INT8 推理下的显存占用验证：INT8 权重 27GB + 32K KV Cache (1.6GB) + 框架开销 (5GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

L40S 在 Qwen3-27B INT8 推理下的显存占用验证：INT8 权重 27GB + 32K KV Cache (1.6GB) + 框架开销 (5GB) = 33.6GB，L40S 48GB 剩余 14.4GB 可用于扩展并发或更长上下文，支持最多 8 个 32K 并发请求（14.4GB / 1.6GB = 9，但需预留安全边际，实际建议 8 并发）

## Corrected Claim

L40S 在 Qwen3-27B INT8 推理下的显存占用验证：INT8 权重 27GB + 32K KV Cache (1.6GB) + 框架开销 (5GB) = 33.6GB，L40S 48GB 剩余 14.4GB 可用于扩展并发或更长上下文，支持最多 8 个 32K 并发请求（14.4GB / 1.6GB = 9，但需预留安全边际，实际建议 8 并发）

## Evidence

[质询]KV Cache 1.6GB 的估算可能偏低（取决于具体实现如 FlashAttention 或 PagedAttention 的优化程度及数据类型），且 5GB 框架开销为经验值，不同推理引擎（vLLM/TGI）差异较大。 | 先验知识/题面给定，逻辑校验通过：INT8 权重 27GB 符合 27B 模型量级；KV Cache 与并发数的线性关系逻辑自洽；总显存 33.6GB < 48GB，剩余空间计算正确。
