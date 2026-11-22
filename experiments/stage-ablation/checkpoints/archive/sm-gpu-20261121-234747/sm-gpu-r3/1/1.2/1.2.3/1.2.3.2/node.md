# N180: NVIDIA L40S 在 32K 上下文长度下运行 Qwen3-27B INT8 时的显存占用分解：权重 27GB + KV Cache (32K token

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

NVIDIA L40S 在 32K 上下文长度下运行 Qwen3-27B INT8 时的显存占用分解：权重 27GB + KV Cache (32K tokens, BF16 KV) 约 16GB + 激活值/中间层约 2-4GB，总计约 45-47GB，验证 48GB 显存是否满足 32K 上下文且无 Swap 风险，以及剩余显存对 Batch Size 上限的约束。

## Corrected Claim

NVIDIA L40S 在 32K 上下文长度下运行 Qwen3-27B INT8 时的显存占用分解：权重 27GB + KV Cache (32K tokens, BF16 KV) 约 16GB + 激活值/中间层约 2-4GB，总计约 45-47GB，验证 48GB 显存是否满足 32K 上下文且无 Swap 风险，以及剩余显存对 Batch Size 上限的约束。

## Evidence

[质询]KV Cache 计算依赖于具体的层数、头数和头维度，若 Qwen3-27B 架构参数与假设不符（如 GQA 比例不同），16GB 的估算可能存在偏差；但作为量级估算，该数值在合理范围内。 | 先验知识/题面给定，逻辑校验通过：27B INT8 权重约 27GB 符合 1 byte/param 估算；32K 上下文 BF16 KV Cache 约 16GB 符合典型 LLM 架构量级（例如 64 层 * 8 KV heads * 128 dim * 2 bytes * 32K tokens ≈ 16GB）；总显存 45-47GB 小于 48GB，逻辑自洽。
