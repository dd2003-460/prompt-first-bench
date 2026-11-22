# N69: AMD MI250X (128GB HBM2, 3.2 TB/s) 虽显存带宽高，但缺乏主流推理框架（如 vLLM/TensorRT-LLM）的完整支持，需依赖

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

AMD MI250X (128GB HBM2, 3.2 TB/s) 虽显存带宽高，但缺乏主流推理框架（如 vLLM/TensorRT-LLM）的完整支持，需依赖 ROCm 生态，部署复杂度导致额外工程成本约 $5,000-$10,000/年（人力），使其在 TCO 对比中通常劣于 NVIDIA 同级产品，除非存在极高的显存需求且无法通过量化解决。

## Corrected Claim

AMD MI250X (128GB HBM2, 3.2 TB/s) 虽显存带宽高，但缺乏主流推理框架（如 vLLM/TensorRT-LLM）的完整支持，需依赖 ROCm 生态，部署复杂度导致额外工程成本，使其在 TCO 对比中通常劣于 NVIDIA 同级产品，除非存在极高的显存需求且无法通过量化解决。

## Evidence

[质询]具体的人力成本数值（$5,000-$10,000/年）缺乏普遍适用的标准，属于高度依赖具体团队技能水平和市场行情的经验性估算，且不同规模项目差异巨大，该具体数值区间可能不准确或具有误导性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。AMD MI250X 确实依赖 ROCm 且生态成熟度低于 CUDA，导致部署复杂度增加，但具体成本数值无法从第一性原理推出，且无外部来源佐证该特定金额区间。

## Search Query

AMD MI250X inference software support cost vLLM ROCm Qwen3-27B
