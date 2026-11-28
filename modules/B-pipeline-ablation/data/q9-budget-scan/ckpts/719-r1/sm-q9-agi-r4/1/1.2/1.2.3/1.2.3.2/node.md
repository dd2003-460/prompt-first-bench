# N130: FP8 量化对 Attention Score 分布的扰动量 δ_S，定义为 FP8 与 FP16 计算出的 Attention Weights 之间的 L2 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

FP8 量化对 Attention Score 分布的扰动量 δ_S，定义为 FP8 与 FP16 计算出的 Attention Weights 之间的 L2 范数距离 ||S_fp8 - S_fp16||_2，在长上下文中该值随序列长度 L 呈线性增长，系数需通过 vLLM profiling 实测获取

## Corrected Claim

FP8 量化对 Attention Score 分布的扰动量 δ_S 在长上下文中通常随序列长度 L 显著增长，其具体增长趋势（如线性或其他形式）及量化系数需结合具体硬件和框架（如 vLLM）进行 profiling 实测获取。

## Evidence

[质询]将FP8量化误差随序列长度的增长严格断言为“线性”缺乏普适的理论必然性，实际增长曲线可能受softmax归一化效应影响呈现非线性（如对数或饱和），且“系数需通过vLLM profiling实测”属于特定实现的经验性操作建议，而非通用数学性质。 | 先验知识/题面给定，逻辑校验通过：虽然量化误差累积通常随长度增加，但严格线性关系并非第一性原理可严格推导的普适结论，且缺乏外部来源支持具体的线性系数及vLLM特定行为，故降级为定性表述。
