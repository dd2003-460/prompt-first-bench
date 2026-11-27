# N169: W4 量化误差的主要来源分解：权重量化误差（Quantization Error）与激活值动态范围溢出（Activation Outlier）的贡献比例，需通过

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

W4 量化误差的主要来源分解：权重量化误差（Quantization Error）与激活值动态范围溢出（Activation Outlier）的贡献比例，需通过误差分析实验确定哪部分是导致 MMLU 下降 2.5% 的主导因素，以指导是否采用 SmoothQuant 等缓解技术。

## Corrected Claim

W4 量化误差主要来源于权重量化误差与激活值动态范围溢出（Activation Outlier）。需通过误差分析实验确定哪部分是导致模型性能（如 MMLU）下降的主导因素，以指导是否采用 SmoothQuant 等缓解技术。

## Evidence

[质询]该陈述将‘误差来源分解’和‘主导因素确定’描述为需要实验确定的未知事实，但缺乏具体的实验数据或文献支持来证明哪部分是主导因素，且‘MMLU下降2.5%’这一具体数值缺乏来源佐证，属于未经验证的经验性断言。 | 逻辑自洽（量化误差确实包含权重和激活值两部分，且SmoothQuant是已知缓解技术），但作为source=search节点，缺乏外部来源支持具体的误差比例或MMLU下降数值，属于经验事实且缺来源支持。

## Search Query

LLM 4bit quantization error analysis weight vs activation outlier MMLU impact
