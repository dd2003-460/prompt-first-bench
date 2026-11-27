# N292: GMV_0 的基准期选择存在 trade-off：若选择 T_30d（近30天），受季节性波动影响大，GMV_0 方差高；若选择 T_365d_avg（近365

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

GMV_0 的基准期选择存在 trade-off：若选择 T_30d（近30天），受季节性波动影响大，GMV_0 方差高；若选择 T_365d_avg（近365天日均*30），平滑了短期噪声但可能滞后于市场结构变化。前沿工作点1：T_30d，适用于高流动性品类（如数码），GMV_0 反映当前热度，但需引入季节调整因子 S_season ∈ [0.8, 1.2]。

## Corrected Claim

GMV_0 的基准期选择存在 trade-off：若选择 T_30d（近30天），受季节性波动影响大，GMV_0 方差高；若选择 T_365d_avg（近365天日均*30），平滑了短期噪声但可能滞后于市场结构变化。前沿工作点1：T_30d，适用于高流动性品类（如数码），GMV_0 反映当前热度，但需引入季节调整因子 S_season ∈ [0.8, 1.2]。

## Evidence

先验知识/题面给定，逻辑校验通过：基准期选择确实存在平滑度与时效性的权衡，T_30d 方差大且需季节调整符合统计学直觉，T_365d 平滑但滞后符合经济学常识，数值范围 [0.8, 1.2] 合理。

## Search Query

e-commerce baseline GMV calculation seasonality adjustment 30-day vs 365-day average
