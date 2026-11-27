# N349: FP8 KV Cache 质量损失量化：采用 INT8 KV Cache 相比 BF16 会导致长上下文（>16K）的注意力分数误差增加约 2-5%，具体表现为

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

FP8 KV Cache 质量损失量化：采用 INT8 KV Cache 相比 BF16 会导致长上下文（>16K）的注意力分数误差增加约 2-5%，具体表现为 MMLU 下降 0.5-1.0%，该损失在 32K 上下文下累计效应需通过本地 Benchmark 验证，不可仅依赖理论估算。

## Corrected Claim

采用 INT8 KV Cache 相比 BF16 通常会导致长上下文（>16K）的注意力分数误差增加，具体表现为 MMLU 等基准测试出现轻微下降（量级通常在 0.5-1.0% 左右，视模型与量化策略而定），该损失在 32K 上下文下的累计效应需通过本地 Benchmark 验证，不可仅依赖理论估算。

## Evidence

[质询]数值量级与具体指标（MMLU下降0.5-1.0%）缺乏普适性，高度依赖具体模型架构、量化算法（如SmoothQuant/LLM.int8()）及数据集分布，将其作为通用量化结论存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值为经验事实，缺乏来源直接支持，故降级。

## Search Query

INT8 KV cache vs BF16 MMLU drop long context 32K
