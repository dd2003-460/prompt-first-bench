# N36: 负相关系数 $\rho=-0.3$ 对命中率的影响修正项：由于大对象（高 $S$）倾向于低热度（低 $R$），LRU 驱逐的大对象中低热度占比更高，导致字节命中

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

负相关系数 $\rho=-0.3$ 对命中率的影响修正项：由于大对象（高 $S$）倾向于低热度（低 $R$），LRU 驱逐的大对象中低热度占比更高，导致字节命中率的实际值低于独立假设下的值。需引入修正因子 $F_{corr} = 1 - k \cdot \rho \cdot (Var(S)/E[S]^2)$，其中 $k$ 为耦合系数，需通过蒙特卡洛模拟确定 $k \approx 0.5-1.0$。

## Corrected Claim

负相关系数 $\rho=-0.3$ 会导致字节命中率低于独立假设下的值。具体的修正因子形式及耦合系数 $k$ 需通过蒙特卡洛模拟确定，目前缺乏确切的解析公式或标准系数范围。

## Evidence

[质询]修正因子公式 $F_{corr} = 1 - k \cdot \rho \cdot (Var(S)/E[S]^2)$ 缺乏严格的理论推导支持，且系数 $k$ 的范围（0.5-1.0）属于经验估计，未提供具体的蒙特卡洛模拟数据或文献佐证，存在将复杂统计关系简化为线性修正的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该公式非第一性原理可严格推导，属于需实证验证的经验模型参数）。

## Search Query

correlation effect on LRU cache byte hit rate pareto distribution simulation
