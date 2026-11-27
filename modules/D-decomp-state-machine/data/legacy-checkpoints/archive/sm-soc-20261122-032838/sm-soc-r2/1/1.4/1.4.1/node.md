# N45: 买家心理阈值 $P_{threshold}$ 的构成公式：$P_{threshold} = P_{ref} - \gamma \cdot C_{search}$

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

买家心理阈值 $P_{threshold}$ 的构成公式：$P_{threshold} = P_{ref} - \gamma \cdot C_{search}$，其中 $\gamma$ 为搜索成本敏感度系数。根据二手市场行为数据，平均搜索成本 $C_{search} \approx 5\% P_{ref}$，且 $\gamma \in [0.5, 1.5]$，因此 $P_{threshold} \approx 0.925 P_{ref}$ 至 $0.875 P_{ref}$，验证了 N8 中 $0.9 P_{ref}$ 的近似值。

## Corrected Claim

在特定模型假设下，若搜索成本约为参考价的5%且敏感度系数在0.5-1.5之间，则心理阈值约为参考价的87.5%-92.5%，支持0.9倍参考价的近似估计。

## Evidence

[质询]该公式及参数（γ范围、C_search比例）属于特定模型假设或经验拟合值，并非普适的物理定律或数学公理。虽然逻辑推导自洽，但缺乏外部数据支持其作为通用'二手市场行为数据'的准确性，存在将特定模型参数误标为普遍事实的风险。 | source=knowledge，逻辑校验通过：0.925=1-0.5*0.05, 0.875=1-1.5*0.05，计算无误且区间覆盖0.9；但作为经验性参数组合，缺乏外部来源直接支持其普适性，故降级。
