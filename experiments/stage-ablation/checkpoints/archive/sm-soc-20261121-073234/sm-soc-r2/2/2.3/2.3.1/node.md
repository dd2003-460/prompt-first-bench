# N59: 平台GMV最大化目标函数中，'成交速度'代理变量定义为 TimeToSale (TTS)，算法优化目标为 Max Σ (GMV_i / TTS_i)，需验证该目

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

平台GMV最大化目标函数中，'成交速度'代理变量定义为 TimeToSale (TTS)，算法优化目标为 Max Σ (GMV_i / TTS_i)，需验证该目标函数是否隐含对高价低周转商品的惩罚或对高价高周转商品的奖励。

## Corrected Claim

平台GMV最大化目标函数中，'成交速度'代理变量定义为 TimeToSale (TTS)，算法优化目标为 Max Σ (GMV_i / TTS_i)，需验证该目标函数是否隐含对高价低周转商品的惩罚或对高价高周转商品的奖励。

## Evidence

先验知识/题面给定，逻辑校验通过：目标函数 Max Σ (GMV_i / TTS_i) 等价于 Max Σ (Price_i * Quantity_i / TTS_i)，即最大化单位时间的销售额（Revenue Rate）。对于高价低周转商品，TTS 大导致分母大，从而降低单项贡献，隐含惩罚；对于高价高周转商品，TTS 小且 Price 高，导致单项贡献大，隐含奖励。逻辑自洽。
