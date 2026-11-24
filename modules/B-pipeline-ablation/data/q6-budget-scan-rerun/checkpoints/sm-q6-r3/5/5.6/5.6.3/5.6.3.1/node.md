# N298: 自建系统切换时间 $T_{self\_switch}$ 由BGP收敛主导，基于N121计算，典型值为30-150秒（取决于DNS TTL配置），取中值60秒（假

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

自建系统切换时间 $T_{self\_switch}$ 由BGP收敛主导，基于N121计算，典型值为30-150秒（取决于DNS TTL配置），取中值60秒（假设TTL=60s优化后）。

## Corrected Claim

自建系统切换时间 $T_{self\_switch}$ 由BGP收敛主导，基于N121计算，典型值为30-150秒（取决于DNS TTL配置），取中值60秒（假设TTL=60s优化后）。

## Evidence

先验知识/题面给定，逻辑校验通过：BGP收敛时间通常在秒级至分钟级，结合DNS TTL=60s的假设，30-150秒的范围及60秒的中值在工程上合理且自洽。
