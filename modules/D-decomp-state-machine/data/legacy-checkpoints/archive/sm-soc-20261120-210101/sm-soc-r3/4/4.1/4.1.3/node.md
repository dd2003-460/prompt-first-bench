# N75: ‘近期均价’计算窗口的敏感性分析：N18 指定‘近7天’，但高波动品类（如潮玩）7天数据噪声大，应使用加权移动平均 P_ref = Σ(w_t * P_t)，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

‘近期均价’计算窗口的敏感性分析：N18 指定‘近7天’，但高波动品类（如潮玩）7天数据噪声大，应使用加权移动平均 P_ref = Σ(w_t * P_t)，其中 w_t 为时间衰减权重。若窗口从7天扩展至30天，P_ref 稳定性提升，但时效性下降，导致偏离度计算偏差 ΔD_window，需量化 ΔD_window 对 CTR' 预测误差的影响。

## Corrected Claim

‘近期均价’计算窗口的敏感性分析：N18 指定‘近7天’，但高波动品类（如潮玩）7天数据噪声大，应使用加权移动平均 P_ref = Σ(w_t * P_t)，其中 w_t 为时间衰减权重。若窗口从7天扩展至30天，P_ref 稳定性提升，但时效性下降，导致偏离度计算偏差 ΔD_window，需量化 ΔD_window 对 CTR' 预测误差的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：加权移动平均在时间序列分析中确实能平衡噪声与时效性，窗口扩展对稳定性与偏差的影响符合统计学直觉，无逻辑矛盾。

## Search Query

moving average window size impact on price reference stability e-commerce
