# N12: AMD ROCm 平台对 Qwen3-27B 的推理支持成熟度低于 CUDA，截至 2024 年 Q3，ROCm 对 GQA 架构和 FlashAttentio

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

AMD ROCm 平台对 Qwen3-27B 的推理支持成熟度低于 CUDA，截至 2024 年 Q3，ROCm 对 GQA 架构和 FlashAttention-2 的优化程度导致推理速度比同代 NVIDIA 卡低 15-30% [待核验]。

## Corrected Claim

AMD ROCm 平台已支持 Qwen3-27B 的推理部署（如通过 vLLM），但截至 2024 年 Q3，其在 GQA 架构和 FlashAttention-2 等关键算子上的优化成熟度通常低于 CUDA 生态，导致在同等硬件规格下推理性能可能存在一定差距，具体数值需视具体硬件和配置而定。

## Evidence

[质询]陈述中引用的具体性能差距数值（15-30%）缺乏权威基准测试支持，且将特定模型（Qwen3-27B）的特定架构特性（GQA/FlashAttention-2）优化程度直接等同于整体推理速度差距，存在以偏概全和数值臆测的风险。 | 来源[1]证实了Qwen3系列模型在ROCm平台上的部署可行性，但未提供与CUDA平台对比的具体性能损耗数据（15-30%），属于经验事实且缺乏直接来源支持。

## Search Query

ROCm vs CUDA inference performance Qwen 27B GQA FlashAttention

## Retrieval Sources

- {'url': 'https://github.com/zhangsongyang/Qwen3.8-27B-ROCm&rut=fa7eb0f5f71338c11b5280426f2b8b04b86cf96e4c28aa35e43b64ee7d368c1e', 'type': 'ddg', 'title': 'GitHub - zhangsongyang/Qwen3.8-27B-ROCm'}
