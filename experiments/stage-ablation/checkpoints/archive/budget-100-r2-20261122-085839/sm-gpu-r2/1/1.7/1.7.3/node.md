# N50: 量化方法差异导致的性能方差：在相同 INT8 位宽下，GPTQ 与 SmoothQuant 的 MMLU 得分差异约为 0.3 个百分点 (GPTQ 通常略低或

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

量化方法差异导致的性能方差：在相同 INT8 位宽下，GPTQ 与 SmoothQuant 的 MMLU 得分差异约为 0.3 个百分点 (GPTQ 通常略低或持平，取决于校准集分布)，HumanEval 差异约为 0.3-0.5 个百分点，主要源于激活值分布处理策略不同 [待核验: 需具体对比数据]

## Corrected Claim

在相同 INT8 位宽下，GPTQ 与 SmoothQuant 的性能差异通常较小（通常在 1 个百分点以内），具体数值取决于模型架构、校准集分布及任务类型，主要源于激活值分布处理策略不同。

## Evidence

[质询]具体数值（0.3个百分点、0.3-0.5个百分点）属于经验事实，且高度依赖于具体的模型规模、校准集大小及数据集版本，缺乏通用性；在无来源支持的情况下，断言具体的数值差异存在过度精确化的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

GPTQ vs SmoothQuant INT8 performance difference LLM 27B MMLU
