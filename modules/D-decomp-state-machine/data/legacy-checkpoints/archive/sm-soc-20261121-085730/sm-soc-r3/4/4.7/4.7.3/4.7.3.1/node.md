# N299: CTR衰减系数 γ 与降价幅度 ΔP 的非线性关系：γ = γ_base * (1 + β_γ * |ΔP|/P_ref)^δ，其中 γ_base 为基线衰减率

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

CTR衰减系数 γ 与降价幅度 ΔP 的非线性关系：γ = γ_base * (1 + β_γ * |ΔP|/P_ref)^δ，其中 γ_base 为基线衰减率，β_γ 为价格敏感度对点击率的交叉弹性，δ 为凸性指数，需通过A/B测试中不同降价档位（5%, 10%, 20%）的CTR变化拟合确定。

## Corrected Claim

CTR衰减系数 γ 与降价幅度 ΔP 可能存在非线性关系，一种常见的拟合形式为 γ = γ_base * (1 + β_γ * |ΔP|/P_ref)^δ，其中参数需通过A/B测试中不同降价档位（如5%, 10%, 20%）的CTR变化数据拟合确定，具体参数值及模型适用性依赖于特定业务场景。

## Evidence

[质询]该公式为特定业务场景下的经验拟合模型，并非普适的物理或数学定律。不同行业、不同商品类别的CTR对价格变化的响应机制差异巨大，直接断言存在统一的非线性关系且参数需通过特定档位拟合，缺乏普适性证据支持，属于未经证实的经验假设。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该模型非第一性原理可推导的普适规律）

## Search Query

price change impact on click-through rate non-linear elasticity e-commerce A/B testing
