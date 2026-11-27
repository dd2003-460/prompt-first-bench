# N91: NVFP4量化在长上下文（>32k）下导致logit分布偏差的量化指标：需计算在seq_len=32k, 64k, 128k时，主模型与NVFP4量化模型在To

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

NVFP4量化在长上下文（>32k）下导致logit分布偏差的量化指标：需计算在seq_len=32k, 64k, 128k时，主模型与NVFP4量化模型在Top-10 token概率分布上的KL散度或JS散度，以验证接受率α下降至45%的具体数值依据

## Corrected Claim

NVFP4量化在长上下文（>32k）下可能导致logit分布偏差，进而影响接受率α。需通过计算seq_len=32k, 64k, 128k时主模型与NVFP4量化模型在Top-10 token概率分布上的KL散度或JS散度来量化此偏差，并验证其对接受率α（如降至45%）的具体影响。

## Evidence

[质询]该陈述描述的是一个需要特定实验数据支撑的经验性观察（具体序列长度下的KL/JS散度数值及对应的接受率α=45%），而非可从第一性原理推导的数学或物理定律。由于缺乏具体的实验报告或论文数据作为直接证据，无法确认这些具体数值（如32k/64k/128k下的具体散度值）的真实性，存在将假设性目标误述为已验证事实的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实属于具体实验参数与观测结果，非第一性原理可推导范畴）

## Search Query

NVFP4 quantization logit distribution divergence long context acceptance rate
