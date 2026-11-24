# N493: PUE 与电价参数固化：N165 使用 PUE=1.4 和电价 0.8¥/kWh；对于自建机房，PUE 通常在 1.3-1.5 之间，电价因地区而异（中国东部约

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N165

## Claim

PUE 与电价参数固化：N165 使用 PUE=1.4 和电价 0.8¥/kWh；对于自建机房，PUE 通常在 1.3-1.5 之间，电价因地区而异（中国东部约 0.6-0.8¥/kWh）；若采用更高效的液冷设计，PUE 可降至 1.1；敏感性分析：PUE 从 1.4 降至 1.1 可使电力成本降低 21%。

## Corrected Claim

PUE 与电价参数固化：N165 使用 PUE=1.4 和电价 0.8¥/kWh；对于自建机房，PUE 通常在 1.3-1.5 之间，电价因地区而异（中国东部约 0.6-0.8¥/kWh）；若采用更高效的液冷设计，PUE 可降至 1.1；敏感性分析：PUE 从 1.4 降至 1.1 可使电力成本降低 21%。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE 1.3-1.5 符合行业常规，电价 0.6-0.8¥/kWh 符合中国东部工商业电价区间，液冷 PUE 1.1 符合技术极限，成本降低 21% 计算准确 ((1.4-1.1)/1.4 ≈ 21.4%)。

## Search Query

data center PUE standard efficiency electricity price China
