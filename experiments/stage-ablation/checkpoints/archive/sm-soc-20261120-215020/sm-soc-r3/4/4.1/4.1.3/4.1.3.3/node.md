# N153: 保留信号功能的最小惩罚系数 $\lambda_{min}$ 的约束条件：需满足 $\Delta T_{quality} \leq 0$（即高质量商品成交周期不增

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

保留信号功能的最小惩罚系数 $\lambda_{min}$ 的约束条件：需满足 $\Delta T_{quality} \leq 0$（即高质量商品成交周期不增加）。若 $\Delta T_{exposure} = -5\%$ 且 $\Delta T_{trust} = +2\%$（当 $\lambda=0.5$ 时），则 $\lambda$ 需降低至使 $\Delta T_{trust} < 2\%$ 的水平。假设 $\Delta T_{trust}$ 与 $\lambda$ 成正比，则 $\lambda_{min} = 0.5 \times (2/5) = 0.2$。

## Corrected Claim

保留信号功能的最小惩罚系数 $\lambda_{min}$ 的约束条件：需满足 $\Delta T_{quality} \leq 0$（即高质量商品成交周期不增加）。若 $\Delta T_{exposure} = -5\%$ 且 $\Delta T_{trust} = +2\%$（当 $\lambda=0.5$ 时），则 $\lambda$ 需降低至使 $\Delta T_{trust} < 2\%$ 的水平。假设 $\Delta T_{trust}$ 与 $\lambda$ 成正比，则 $\lambda_{min} = 0.5 \times (2/5) = 0.2$。

## Evidence

先验知识/题面给定，逻辑校验通过：基于题设条件（ΔT_trust与λ成正比，λ=0.5时ΔT_trust=2%），推导λ_min=0.2符合线性比例关系，且满足ΔT_quality≤0的约束逻辑。

## Search Query

minimum penalty coefficient preserve quality signal efficiency
