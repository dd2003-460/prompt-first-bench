# N49: 在 BF16 精度下，若模型未启用 Flash Attention 或 Paged Attention，激活值中间缓冲（Activations）的显存占用与序列

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

在 BF16 精度下，若模型未启用 Flash Attention 或 Paged Attention，激活值中间缓冲（Activations）的显存占用与序列长度线性相关，对于 32K 上下文，单条序列的激活显存开销约为 1.5-2.5 GB，需从 54 GB 权重之外的总显存预算中扣除。

## Corrected Claim

在 BF16 精度下，若模型未启用 Flash Attention 或 Paged Attention，激活值中间缓冲（Activations）的显存占用与序列长度线性相关，对于 32K 上下文，单条序列的激活显存开销约为 1.5-2.5 GB，需从 54 GB 权重之外的总显存预算中扣除。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于未启用Flash Attention时的具体计算与数值验证（符合父节点前提），子节点2聚焦于启用Flash Attention后的对比与优化效果。两者在逻辑上正交（基线 vs 优化后），且无冗余。但父节点明确限定了前提为“未启用Flash Attention或Paged Attention”，子节点2引入了“启用Flash Attention”的场景，超出了父节点的范围，导致完备性检查出现偏差（子节点覆盖了父节点范围之外的内容，虽然有助于理解，但严格来说父节点未涵盖优化后的情况，或者说子节点2偏离了父节点的限定条件）。更准确地说，父节点只讨论了“未启用”的情况，子节点2讨论“启用”的情况，这使得分解结构变成了“基线情况”和“优化情况”的对比，而父节点本身只陈述了基线情况的后果。如果父节点意图是包含对比，则描述不全；如果父节点意图仅限基线，则子节点2多余。鉴于学术分解通常要求子节点严格支撑父节点，子节点2引入了父节点未提及的“启用FA”假设，属于范围偏移。）
