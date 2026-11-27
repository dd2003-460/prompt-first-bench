# N278: 激活值 INT8 量化引入的额外基准得分下降百分比 (ΔScore_act%) 的具体数值范围，需区分任务类型（如 MMLU-Pro 知识检索 vs Human

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

激活值 INT8 量化引入的额外基准得分下降百分比 (ΔScore_act%) 的具体数值范围，需区分任务类型（如 MMLU-Pro 知识检索 vs HumanEval 代码生成）对误差敏感度的不同影响，通常表现为 1-3% 区间内的具体值。

## Corrected Claim

激活值 INT8 量化引入的额外基准得分下降百分比 (ΔScore_act%) 的具体数值范围因模型架构、量化算法及任务类型而异，通常在 1-3% 区间内，但需根据具体实验数据确定。

## Evidence

[质询]该陈述包含具体的经验数值范围（1-3%），属于硬件/模型量化性能的经验事实，无法从第一性原理严格推导，且不同模型架构、量化算法（如GPTQ, AWQ, SmoothQuant）及具体任务下的实际下降幅度差异巨大，缺乏统一标准，'通常表现为1-3%'这一概括性结论缺乏普适性证据支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该数值范围属于特定实验结果，非通用物理/数学定律）

## Search Query

activation INT8 quantization benchmark score drop percentage MMLU HumanEval
