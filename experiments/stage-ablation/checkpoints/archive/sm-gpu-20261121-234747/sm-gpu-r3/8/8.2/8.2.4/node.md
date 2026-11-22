# N468: DeepSpeed-Inference 在 2 卡 PCIe 4.0 互联下，Decode 阶段的扩展效率：通常为 1.5-1.7 [待核验]，与 vLLM 相

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N148

## Claim

DeepSpeed-Inference 在 2 卡 PCIe 4.0 互联下，Decode 阶段的扩展效率：通常为 1.5-1.7 [待核验]，与 vLLM 相当，但可能在某些 batch size 下表现更优或更差

## Corrected Claim

DeepSpeed-Inference 在 2 卡 PCIe 4.0 互联下，Decode 阶段的扩展效率通常较高，与 vLLM 表现相当，具体数值随 batch size 和模型架构波动。

## Evidence

[质询]该陈述包含具体的经验性数值范围（1.5-1.7）和特定硬件配置下的性能对比结论，属于硬件/软件性能经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

DeepSpeed-Inference tensor parallelism decode speedup 2 GPU
