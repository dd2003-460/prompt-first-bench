# N107: 对象更新率 1%/天 对应的失效时间 τ_obj=100 天是数学推导结果（Derived），基于指数分布假设；但实际 CDN 中对象更新的‘失效’定义（是 U

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 对应的失效时间 τ_obj=100 天是数学推导结果（Derived），基于指数分布假设；但实际 CDN 中对象更新的‘失效’定义（是 URL 变更还是 ETag 变更）属于需查证的业务逻辑（Business Logic），不同 CDN 提供商对‘更新’的定义不同，需查阅具体 API 文档确认是否会导致缓存 Key 变化。

## Corrected Claim

对象更新率 1%/天 对应的失效时间 τ_obj=100 天是数学推导结果（Derived），基于指数分布假设；但实际 CDN 中对象更新的‘失效’定义（是 URL 变更还是 ETag 变更）属于需查证的业务逻辑（Business Logic），不同 CDN 提供商对‘更新’的定义不同，需查阅具体 API 文档确认是否会导致缓存 Key 变化。

## Evidence

逻辑推导成立，来源未直接覆盖

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/682884720&rut=76e86a4a0b77a03fe28f35e37d161edb2d14cad3fa30e118d79626482f26b78f', 'type': 'ddg', 'title': '物理引擎的时间稳定性问题和实际工程中的解决方案 (顺便分析Unity的FixedUpdate机制) - 知乎'}
