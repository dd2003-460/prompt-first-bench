# N140: 量化热门对象更新带来的带宽节省：若更新概率与热度正相关（ρ_update_heat > 0），则被更新对象的条件期望大小 E[Size | Updated, H

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

量化热门对象更新带来的带宽节省：若更新概率与热度正相关（ρ_update_heat > 0），则被更新对象的条件期望大小 E[Size | Updated, Hot] = E[Size] * (1 - ρ_update_heat * σ_lnS * z_hot)，其中 z_hot 为热门对象的标准化热度 Z-score。量化节省比例 Saving_pct = (E[Size] - E[Size|Updated,Hot]) / E[Size]。

## Corrected Claim

在假设对象大小与热度存在对数线性负相关且更新概率与热度正相关的特定模型下，可近似量化热门对象更新带来的带宽节省，其节省比例 Saving_pct 正比于 ρ_update_heat * σ_lnS * z_hot。

## Evidence

[质询]公式中直接引入 ρ_update_heat * σ_lnS * z_hot 作为大小缩减比例缺乏严格的统计推导支持，通常需假设大小与热度存在特定的对数线性关系且更新机制与大小变化严格耦合，该线性近似在一般情形下可能不成立或量纲/系数定义模糊。 | 先验知识/题面给定，逻辑校验通过（公式结构自洽，量纲合理，但具体系数关系为经验性近似模型，非第一性原理严格推导，且无外部来源支持，故降级为定性/模型假设表述）
