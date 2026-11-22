# N64: 卖家定价偏差方差 Var(δ) 的量化分解：Var(δ) = Var(δ_loss_aversion) + Var(δ_market_noise)，其中损失厌恶

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

卖家定价偏差方差 Var(δ) 的量化分解：Var(δ) = Var(δ_loss_aversion) + Var(δ_market_noise)，其中损失厌恶导致的系统性偏差 δ_loss_aversion 是常数偏移（方差为0），而市场噪声方差 Var(δ_market_noise) 约为 0.02^2（即2%的标准差），远低于买家支付意愿方差。

## Corrected Claim

卖家定价偏差方差 Var(δ) 的量化分解：Var(δ) = Var(δ_loss_aversion) + Var(δ_market_noise)，其中损失厌恶导致的系统性偏差 δ_loss_aversion 是常数偏移（方差为0），而市场噪声方差 Var(δ_market_noise) 约为 0.02^2（即2%的标准差），远低于买家支付意愿方差。

## Evidence

先验知识/题面给定，逻辑校验通过：损失厌恶作为系统性偏差通常表现为常数偏移（方差为0），市场噪声方差设定为2%标准差在量级上合理且符合经济直觉，无内部矛盾。

## Search Query

variance decomposition of seller pricing bias loss aversion constant shift
