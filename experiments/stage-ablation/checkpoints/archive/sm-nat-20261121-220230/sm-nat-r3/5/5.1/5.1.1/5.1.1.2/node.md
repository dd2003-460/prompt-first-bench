# N216: 在 ρ=-0.3 负相关约束下，LRU 流体模型命中率公式的解析误差扩大至 4.8%，主要源于联合分布尾部密度在驱逐边界处的积分偏差，该值接近 5% 阈值上限

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75, N76, N77

## Claim

在 ρ=-0.3 负相关约束下，LRU 流体模型命中率公式的解析误差扩大至 4.8%，主要源于联合分布尾部密度在驱逐边界处的积分偏差，该值接近 5% 阈值上限

## Corrected Claim

在 ρ=-0.3 负相关约束下，LRU 流体模型命中率公式的解析误差显著扩大（接近 5% 阈值），主要源于联合分布尾部密度在驱逐边界处的积分偏差。

## Evidence

[质询]具体数值（4.8%）及归因（联合分布尾部密度积分偏差）属于特定模型下的经验/模拟结果，无法从第一性原理直接推导，且缺乏来源支持该精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LRU fluid model error negative correlation size popularity Pareto
