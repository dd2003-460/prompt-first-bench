# N467: DeepSpeed-Inference 在 2 卡 PCIe 4.0 互联下，Prefill 阶段的扩展效率：与 vLLM 类似，通常为 1.8-1.9 [待核

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N148

## Claim

DeepSpeed-Inference 在 2 卡 PCIe 4.0 互联下，Prefill 阶段的扩展效率：与 vLLM 类似，通常为 1.8-1.9 [待核验]，但具体数值取决于 DeepSpeed 的 kernel 优化和通信原语选择

## Corrected Claim

DeepSpeed-Inference 在 2 卡 PCIe 4.0 互联下，Prefill 阶段的扩展效率通常接近线性（约 1.8-1.9），但具体数值高度依赖于 DeepSpeed 的 kernel 优化、通信原语选择及具体模型架构。

## Evidence

[质询]具体数值（1.8-1.9）属于经验事实，且缺乏来源支持，无法排除因硬件配置、模型大小或DeepSpeed版本不同导致的显著差异。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

DeepSpeed-Inference tensor parallelism prefill speedup 2 GPU
