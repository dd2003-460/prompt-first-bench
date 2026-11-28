# N187: API 元数据查询的 P95 延迟阈值设定为 T_api_p95 = 1.5s，基于 HTTP REST 请求在局域网/内网环境下的标准响应时间分布（均值~20

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

API 元数据查询的 P95 延迟阈值设定为 T_api_p95 = 1.5s，基于 HTTP REST 请求在局域网/内网环境下的标准响应时间分布（均值~200ms，长尾由数据库索引缺失导致），若单次查询耗时 > 1.5s，视为超时并触发熔断机制

## Corrected Claim

API 元数据查询的 P95 延迟阈值设定为 T_api_p95 = 1.5s，基于 HTTP REST 请求在局域网/内网环境下的标准响应时间分布（均值~200ms，长尾由数据库索引缺失导致），若单次查询耗时 > 1.5s，视为超时并触发熔断机制

## Evidence

先验知识/题面给定，逻辑校验通过：局域网REST API均值200ms符合常规工程经验，P95设为1.5s（约7.5倍均值）作为熔断阈值在长尾场景下具备合理性，无内部矛盾。
