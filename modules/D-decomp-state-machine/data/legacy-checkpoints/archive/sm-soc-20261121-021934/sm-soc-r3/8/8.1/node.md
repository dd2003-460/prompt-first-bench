# N134: 买家感知噪声阈值 σ_perception 的计算公式为 σ_perception = k_vis * (ΔP / P_rec)，其中 k_vis 为视觉显著性

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

买家感知噪声阈值 σ_perception 的计算公式为 σ_perception = k_vis * (ΔP / P_rec)，其中 k_vis 为视觉显著性系数，需通过眼动追踪实验中的‘注视时长变化率’或点击热图的‘价格区域点击率变化’进行校准，若 k_vis < 0.5 则阈值判定为低敏感。

## Corrected Claim

买家感知噪声阈值 σ_perception 的一种可能计算模型为 σ_perception = k_vis * (ΔP / P_rec)，其中 k_vis 需通过眼动追踪或点击热图数据校准，具体阈值判定标准（如 k_vis < 0.5 为低敏感）取决于特定实验设定或模型假设。

## Evidence

[质询]该公式及具体阈值（k_vis < 0.5）属于特定模型或假设，缺乏通用学术共识支持，且参考来源未涵盖此具体量化定义，存在将特定实验参数泛化为通用公式的风险。 | 参考来源[1]仅定义感知价值概念，未涉及具体计算公式或眼动追踪校准参数，属于经验事实且缺乏直接来源支持。

## Search Query

consumer price perception threshold eye tracking experiment k_vis coefficient

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%B6%88%E8%B4%B9%E8%80%85%E6%84%9F%E7%9F%A5%E4%BB%B7%E5%80%BC/56354576&rut=c53e77a4ff2777ab8dc252f412bf6f32ff17feee89a8a9e2ef61c5c23403ebee', 'type': 'ddg', 'title': '感知价值_百度百科'}
