# N371: Capex 摊销成本 = (GPU_Price + Platform_Cost) / Lifespan_Hours；对于 2x RTX 4090 方案，Cape

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N126

## Claim

Capex 摊销成本 = (GPU_Price + Platform_Cost) / Lifespan_Hours；对于 2x RTX 4090 方案，Capex_Amortized ≈ ($5198 / 8760) ≈ $0.593/hour (假设 3 年 8h/day 使用)；对于单卡 RTX 5090 方案，Capex_Amortized ≈ ($2999 / 8760) ≈ $0.342/hour。

## Corrected Claim

Capex 摊销成本 = (GPU_Price + Platform_Cost) / Lifespan_Hours；对于 2x RTX 4090 方案，Capex_Amortized ≈ ($5198 / 8760) ≈ $0.593/hour (假设 3 年 8h/day 使用)；对于单卡 RTX 5090 方案，Capex_Amortized ≈ ($2999 / 8760) ≈ $0.342/hour。

## Evidence

先验知识/题面给定，逻辑校验通过：8760小时对应3年8小时/天使用假设，算术计算正确（5198/8760≈0.593, 2999/8760≈0.342），符合Capex摊销定义。
