# N51: 性价比排序核心算法定义：Cost-Performance Ratio (CPR) = (Normalized Throughput * Quality Scor

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比排序核心算法定义：Cost-Performance Ratio (CPR) = (Normalized Throughput * Quality Score) / (TCO_3yr * 0.8 + TCO_3yr * 0.2 * Risk_Factor)。其中Normalized Throughput = tokens/s / max(tokens/s)；Quality Score为归一化后的基准测试得分（0-1）；Risk_Factor反映驱动稳定性与软件生态支持度（NVIDIA=0.5, AMD=0.8, Apple=0.6）。该算法旨在平衡吞吐量、质量、长期成本及部署风险。

## Corrected Claim

存在一种定义性价比排序的算法，其核心逻辑为平衡吞吐量、质量、长期成本及部署风险，具体公式及参数（如Risk_Factor数值）需依据特定研究或行业标准确定，当前缺乏通用标准来源支持。

## Evidence

[质询]该陈述定义了一个具体的工程算法（CPR公式）及特定的经验参数（如Risk_Factor的具体数值、TCO权重0.8/0.2），这些属于经验事实或特定项目/论文的定义，无法从第一性原理推导。参考来源[1]关于CPR（心肺复苏）中的心律分类，与GPU/硬件性价比评估完全无关，属于主题不匹配。因此，该陈述缺乏外部来源支持，且作为经验事实不能仅凭逻辑自洽判定为verified。 | 参考来源[1]主题为医学心律分类，与硬件性价比算法无关，无可用外部证据；该陈述为经验事实（具体参数值），逻辑自洽但缺来源支持，依据经验事实排除条款降级。

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2611.26393&rut=ff168055c0e70b070c2c94719afce3ac3dfc4e8c3c6aa21e5f897830494a457b', 'type': 'ddg', 'title': '[2611.26393] Sensor-Free Shockable Rhythm Classification During CPR ...'}
