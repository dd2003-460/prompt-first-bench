# N40: 使用 Clayton Copula 函数 C(u,v) = (u^{-θ} + v^{-θ} - 1)^{-1/θ} 建模大小与热度的负相关，其中参数 θ 需根

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

使用 Clayton Copula 函数 C(u,v) = (u^{-θ} + v^{-θ} - 1)^{-1/θ} 建模大小与热度的负相关，其中参数 θ 需根据 Pearson 相关系数 ρ≈-0.3 反解确定。

## Corrected Claim

使用 Clayton Copula 函数 C(u,v) = (u^{-θ} + v^{-θ} - 1)^{-1/θ} 建模大小与热度的负相关，其中参数 θ 需根据 Pearson 相关系数 ρ≈-0.3 反解确定。

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 是标准的负相关建模工具，其参数 θ 与 Pearson 相关系数 ρ 存在确定的数学映射关系（ρ = θ/(θ+2)），给定 ρ≈-0.3 可唯一反解出 θ，逻辑自洽且符合统计学原理。

## Search Query

Clayton copula parameter theta from Pearson correlation coefficient formula
