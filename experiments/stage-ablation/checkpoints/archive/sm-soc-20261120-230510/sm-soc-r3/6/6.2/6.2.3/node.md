# N278: T_shorten 在典型参数下的数值解：代入 T_base = 10 天、μ = 1.0、(P_ask - V)/σ = 0.2，得 T_shorten = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

T_shorten 在典型参数下的数值解：代入 T_base = 10 天、μ = 1.0、(P_ask - V)/σ = 0.2，得 T_shorten = 10 × exp(-1.0 × 0.2) ≈ 8.2 天，即高挂价商品成交周期缩短约 18%

## Corrected Claim

T_shorten 在典型参数下的数值解：代入 T_base = 10 天、μ = 1.0、(P_ask - V)/σ = 0.2，得 T_shorten = 10 × exp(-1.0 × 0.2) ≈ 8.2 天，即高挂价商品成交周期缩短约 18%

## Evidence

先验知识/题面给定，逻辑校验通过：计算 exp(-0.2) ≈ 0.8187，10 * 0.8187 ≈ 8.19 天，缩短比例 1 - 0.8187 ≈ 18.13%，数值与结论一致。
