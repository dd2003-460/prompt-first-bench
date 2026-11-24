# N242: 公有云 CDN 的基础设施成本 C_infra_public 主要不包含硬件折旧，而是体现为按需计费的资源预留费（如函数计算、边缘脚本执行）及基础请求费，对于纯

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62, N63, N68

## Claim

公有云 CDN 的基础设施成本 C_infra_public 主要不包含硬件折旧，而是体现为按需计费的资源预留费（如函数计算、边缘脚本执行）及基础请求费，对于纯静态资源分发，C_infra_public ≈ 0 或仅为极低的请求处理费。

## Corrected Claim

公有云 CDN 的基础设施成本 C_infra_public 主要不包含硬件折旧，而是体现为按需计费的资源预留费（如函数计算、边缘脚本执行）及基础请求费，对于纯静态资源分发，C_infra_public ≈ 0 或仅为极低的请求处理费。

## Evidence

先验知识/题面给定，逻辑校验通过：公有云CDN采用按量付费模式，无固定硬件折旧成本，静态资源分发主要产生极低的请求处理费，符合云计算经济学原理。
