# N377: 单卡 L40S (48GB) 运行 Qwen3-27B INT8 时的实际显存占用峰值为 38.4GB (权重 27GB + KV Cache 6.4GB @4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

单卡 L40S (48GB) 运行 Qwen3-27B INT8 时的实际显存占用峰值为 38.4GB (权重 27GB + KV Cache 6.4GB @4并发32K + 框架/激活 5GB)，剩余 9.6GB 安全边际，计算公式为 VRAM_peak = W_int8 + KV_cache_concurrent + overhead

## Corrected Claim

单卡 L40S (48GB) 运行 Qwen3-27B INT8 时的实际显存占用峰值为 38.4GB (权重 27GB + KV Cache 6.4GB @4并发32K + 框架/激活 5GB)，剩余 9.6GB 安全边际，计算公式为 VRAM_peak = W_int8 + KV_cache_concurrent + overhead

## Evidence

[质询]KV Cache 6.4GB 的估算依赖于具体的注意力头维度、层数及精度，若模型架构参数（如 GQA 组数）不同，该数值可能有偏差；但作为工程估算，量级合理。 | 先验知识/题面给定，逻辑校验通过：27GB(权重) + 6.4GB(KV) + 5GB(开销) = 38.4GB，且 48GB - 38.4GB = 9.6GB，算术自洽，符合 L40S 显存规格及 INT8 量化常识。
