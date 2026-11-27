# N293: ΔM（干预后平均客单价增量）的量化计算：ΔM = P_ref × (1 - 0.125) - P_ref = -0.125 × P_ref。假设 P_ref=1

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

ΔM（干预后平均客单价增量）的量化计算：ΔM = P_ref × (1 - 0.125) - P_ref = -0.125 × P_ref。假设 P_ref=100元，则 ΔM = -12.5元。此负值代表客单价损失，Revenue_service 需覆盖此部分。

## Corrected Claim

ΔM（干预后平均客单价增量）的量化计算：ΔM = P_ref × (1 - 0.125) - P_ref = -0.125 × P_ref。假设 P_ref=100元，则 ΔM = -12.5元。此负值代表客单价损失，Revenue_service 需覆盖此部分。

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导 ΔM = P_ref(1-0.125) - P_ref = -0.125P_ref 正确，数值代入 P_ref=100 得 -12.5 元，量纲与符号逻辑自洽。
