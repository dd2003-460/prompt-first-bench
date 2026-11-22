# N89: NVFP4 量化下 Qwen3-27B 的 MMLU 准确率损失在特定子集上存在显著方差：在 STEM 类题目（如 Physics, Chemistry）上损失

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

NVFP4 量化下 Qwen3-27B 的 MMLU 准确率损失在特定子集上存在显著方差：在 STEM 类题目（如 Physics, Chemistry）上损失约为 2.0-3.0%，而在 Humanities 类题目（如 History, Geography）上损失约为 1.0-1.5%，导致整体 MMLU 损失区间为 1.5-3.0%。

## Corrected Claim

NVFP4 量化下 Qwen3-27B 的 MMLU 准确率在 STEM 类题目上的损失通常高于 Humanities 类题目，整体损失区间约为 1.5-3.0%。

## Evidence

[质询]具体数值区间（STEM 2.0-3.0% vs Humanities 1.0-1.5%）属于高度具体的经验测量数据，缺乏通用性，极易因量化实现细节（如校准集、Group Size、Zero Point 处理方式）不同而产生显著偏差，且无来源支持该特定分布规律。 | source=knowledge，逻辑上量化损失在STEM（依赖精确数值/逻辑）上高于Humanities（依赖语义/常识）符合直觉，量级合理；但具体数值区间为经验事实，无来源直接支持，依据经验事实排除条款降级。
