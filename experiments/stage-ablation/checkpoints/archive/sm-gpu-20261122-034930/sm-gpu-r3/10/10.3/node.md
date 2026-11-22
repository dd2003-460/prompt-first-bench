# N151: 2x RTX 4090在Qwen3-27B INT8量化下的实测吞吐率为18 tokens/s (vLLM, 32K ctx, Batch=1)，显著低于单卡R

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

2x RTX 4090在Qwen3-27B INT8量化下的实测吞吐率为18 tokens/s (vLLM, 32K ctx, Batch=1)，显著低于单卡RTX 4090的22 tokens/s，证实了多卡PCIe通信开销在Memory-bound场景下的负面影响，这是多卡消费级方案在延迟敏感任务上的核心劣势。

## Corrected Claim

2x RTX 4090在Qwen3-27B INT8量化下的实测吞吐率可能低于单卡RTX 4090（如18 tokens/s vs 22 tokens/s），这证实了多卡PCIe通信开销在Memory-bound场景下的负面影响，是多卡消费级方案在延迟敏感任务上的潜在劣势。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（18 tokens/s vs 22 tokens/s），属于经验事实。在缺乏参考来源支持的情况下，无法验证具体数值的准确性，且不同量化实现、vLLM版本及PCIe拓扑可能导致结果差异，存在数值偏差风险。 | 经验事实，逻辑自洽（多卡PCIe通信开销在Memory-bound场景下确实可能降低单请求延迟性能），但缺来源支持具体数值。

## Search Query

2x RTX 4090 multi-GPU LLM inference penalty PCIe bandwidth
