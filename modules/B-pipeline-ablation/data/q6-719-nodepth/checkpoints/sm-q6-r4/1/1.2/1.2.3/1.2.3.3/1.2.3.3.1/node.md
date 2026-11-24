# N479: 核心区域跳数 Hops_core 量化：在 80% 用户集中 5 个核心区域且自建 POP 全覆盖的场景下，用户请求通常经过 1 跳（用户->POP）或 2 跳

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N161

## Claim

核心区域跳数 Hops_core 量化：在 80% 用户集中 5 个核心区域且自建 POP 全覆盖的场景下，用户请求通常经过 1 跳（用户->POP）或 2 跳（用户->本地汇聚->POP）。若采用 Anycast 直接路由，Hops_core ≈ 1-2 跳。取均值 1.5 跳，则 Hops_core = 1.5。

## Corrected Claim

核心区域跳数 Hops_core 量化：在 80% 用户集中 5 个核心区域且自建 POP 全覆盖的场景下，用户请求通常经过 1 跳（用户->POP）或 2 跳（用户->本地汇聚->POP）。若采用 Anycast 直接路由，Hops_core ≈ 1-2 跳。取均值 1.5 跳，则 Hops_core = 1.5。

## Evidence

先验知识/题面给定，逻辑校验通过：在用户高度集中且POP全覆盖的假设下，1-2跳的路由结构符合网络拓扑常识，取均值1.5在数学上自洽。
