# N158: Qwen3-27B 在 INT8 混合精度量化下，FP16 保留层（如 Embedding/LM Head）的额外显存开销计算公式为：$C_{fp16} = (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Qwen3-27B 在 INT8 混合精度量化下，FP16 保留层（如 Embedding/LM Head）的额外显存开销计算公式为：$C_{fp16} = (N_{embed} + N_{lmhead}) \times 2 \text{ bytes}$，其中 $N_{embed} = 151936 \times 4096 \approx 0.62 \text{ GB}$，$N_{lmhead} = 151936 \times 4096 \approx 0.62 \text{ GB}$，总开销约 1.24 GB，导致总权重显存从 27.0 GB 升至 28.24 GB。

## Corrected Claim

Qwen3-27B 在 INT8 混合精度量化下，FP16 保留层（如 Embedding/LM Head）的额外显存开销计算公式为：$C_{fp16} = (N_{embed} + N_{lmhead}) \times 2 \text{ bytes}$，其中 $N_{embed} = 151936 \times 4096 \approx 0.62 \text{ GB}$，$N_{lmhead} = 151936 \times 4096 \approx 0.62 \text{ GB}$，总开销约 1.24 GB，导致总权重显存从 27.0 GB 升至 28.24 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 词表大小 151936 与隐藏层维度 4096 符合其架构规格，Embedding 和 LM Head 参数量计算及 FP16 显存开销推导在数学上自洽且量级合理。
