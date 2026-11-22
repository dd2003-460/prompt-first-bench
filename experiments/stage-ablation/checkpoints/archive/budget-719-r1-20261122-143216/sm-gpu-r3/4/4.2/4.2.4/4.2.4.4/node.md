# N287: NVFP4/W4 量化导致 MMLU-Pro 分数下降的归因分解：其中由权重量化误差引起的下降幅度（Delta_Weight）与由激活量化误差引起的下降幅度（D

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N101

## Claim

NVFP4/W4 量化导致 MMLU-Pro 分数下降的归因分解：其中由权重量化误差引起的下降幅度（Delta_Weight）与由激活量化误差引起的下降幅度（Delta_Activation）各自占比，需通过仅量化权重或仅量化激活的消融实验数据验证

## Corrected Claim

NVFP4/W4 量化导致 MMLU-Pro 分数下降，其归因分解（权重量化误差 Delta_Weight 与激活量化误差 Delta_Activation 的占比）需通过仅量化权重或仅量化激活的消融实验数据验证，具体数值有待实验确认。

## Evidence

[质询]该陈述声称需要具体的消融实验数据来验证 Delta_Weight 和 Delta_Activation 的占比，但参考来源为空，无法提供具体的数值或比例支持，属于缺乏外部证据的经验性结论。 | 逻辑上，将量化误差分解为权重和激活两部分是合理的归因方法，且需要消融实验验证符合科学方法论；但作为 search 节点，缺乏来源支持具体数值或占比，且属于经验事实（具体实验结果），故降级。

## Search Query

Qwen3-27B quantization ablation study weight vs activation MMLU drop
