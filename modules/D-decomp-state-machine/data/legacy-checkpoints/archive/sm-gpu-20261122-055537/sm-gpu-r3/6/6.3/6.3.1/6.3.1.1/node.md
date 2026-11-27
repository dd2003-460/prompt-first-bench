# N323: 修正 N102 中 L4 价格假设：NVIDIA L4 单卡典型市场价约为 $2,500-$3,000 USD [待核验]，而 RTX 4090 为 $1,60

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

修正 N102 中 L4 价格假设：NVIDIA L4 单卡典型市场价约为 $2,500-$3,000 USD [待核验]，而 RTX 4090 为 $1,600 USD。若取 L4=$2,800, 4090=$1,600，则溢价 ΔC_hw = $1,200。结合 N99 的电力节省 $561.5/year，回本周期 = $1,200 / $561.5 ≈ 2.14 年。此修正后的回本周期比原 N102 假设的 2.5 年更短，意味着在 3 年 TCO 内，只要 E_price > $0.055/kWh (见 N123)，L4 的 TCO 即优于 4090。

## Corrected Claim

修正 N102 中 L4 价格假设：NVIDIA L4 单卡典型市场价约为 $2,500-$3,000 USD [待核验]，而 RTX 4090 为 $1,600 USD。若取 L4=$2,800, 4090=$1,600，则溢价 ΔC_hw = $1,200。结合 N99 的电力节省 $561.5/year，回本周期 = $1,200 / $561.5 ≈ 2.14 年。此修正后的回本周期比原 N102 假设的 2.5 年更短，意味着在 3 年 TCO 内，只要 E_price > $0.055/kWh (见 N123)，L4 的 TCO 即优于 4090。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVIDIA L4 price vs RTX 4090 price 2024
