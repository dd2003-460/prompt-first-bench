# N827: A100 (Ampere) 运行 Qwen3-27B BF16 时，vLLM/TensorRT 的实测 Decode 效率系数为 0.75-0.85 (基于 H

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N257, N258, N259

## Claim

A100 (Ampere) 运行 Qwen3-27B BF16 时，vLLM/TensorRT 的实测 Decode 效率系数为 0.75-0.85 (基于 HuggingFace 社区基准测试数据)，修正后理论上限 37.7 tokens/s 变为 28.3-32.0 tokens/s。

## Corrected Claim

A100 (Ampere) 运行 Qwen3-27B BF16 时，vLLM/TensorRT 的实测 Decode 效率系数通常低于理论上限（具体数值需参考特定基准测试数据），修正后理论上限将相应降低。

## Evidence

[质询]该陈述包含具体的硬件性能参数（A100带宽/算力隐含值）和特定模型（Qwen3-27B）的实测效率系数，属于经验事实。检索无可用来源，无法验证'0.75-0.85'这一具体数值范围是否准确，且'37.7 tokens/s'的理论上限计算依赖于未提供的具体硬件配置假设（如显存带宽、Batch Size等），存在口径混淆或数值量级错误的风险。 | 经验事实，逻辑自洽但缺来源支持。虽然从第一性原理看，实际效率低于理论上限是合理的，但具体数值（0.75-0.85及37.7/28.3-32.0）无法通过纯逻辑推导得出，且无外部来源佐证，故降级。

## Search Query

A100 Qwen3-27B BF16 vLLM decode throughput benchmark efficiency factor
