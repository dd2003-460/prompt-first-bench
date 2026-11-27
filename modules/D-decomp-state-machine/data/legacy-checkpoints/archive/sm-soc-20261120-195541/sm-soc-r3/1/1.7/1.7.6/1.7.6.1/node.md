# N131: 公允价 P_market 的基准定义：采用同类商品过去30天成交价格的加权中位数（权重=成交量），以消除极端值干扰，确保 μ_deviation 计算的稳健性。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

公允价 P_market 的基准定义：采用同类商品过去30天成交价格的加权中位数（权重=成交量），以消除极端值干扰，确保 μ_deviation 计算的稳健性。

## Corrected Claim

公允价 P_market 的基准定义：采用同类商品过去30天成交价格的加权中位数（权重=成交量），以消除极端值干扰，确保 μ_deviation 计算的稳健性。

## Evidence

先验知识/题面给定，逻辑校验通过：加权中位数在统计学上确实比均值更稳健，能有效消除极端值干扰，且以成交量为权重符合金融/商品定价中流动性加权的市场惯例，逻辑自洽且量级合理。
