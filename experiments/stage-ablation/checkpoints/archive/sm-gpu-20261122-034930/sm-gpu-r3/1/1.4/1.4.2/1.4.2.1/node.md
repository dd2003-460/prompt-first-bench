# N182: 在vLLM中启用INT8 KV Cache时，由于量化误差累积，32K长上下文下的Perplexity增加幅度相比FP16 KV Cache额外增加0.2-0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

在vLLM中启用INT8 KV Cache时，由于量化误差累积，32K长上下文下的Perplexity增加幅度相比FP16 KV Cache额外增加0.2-0.5%，导致整体MMLU准确率损失从1-2%（INT8权重+FP16 KV）上升至1.5-2.5%（INT8权重+INT8 KV），需权衡显存节省与质量损失。

## Corrected Claim

在vLLM中启用INT8 KV Cache时，由于量化误差累积，长上下文下的Perplexity相比FP16 KV Cache会有所增加，导致整体MMLU准确率损失相比仅INT8权重量化进一步上升，需权衡显存节省与质量损失。

## Evidence

[质询]具体数值（Perplexity增加0.2-0.5%，MMLU损失从1-2%升至1.5-2.5%）缺乏通用基准支持，不同模型、数据集及量化实现（如SmoothQuant, GPTQ等）下误差累积表现差异显著，该具体区间可能仅适用于特定实验条件，存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过：INT8 KV Cache确实会引入额外量化误差，导致长上下文下精度损失高于仅权重量化，定性趋势符合物理/工程直觉；但具体数值为经验事实，无来源直接支持，故降级。

## Search Query

INT8 KV cache quantization perplexity loss long context 32k vLLM
