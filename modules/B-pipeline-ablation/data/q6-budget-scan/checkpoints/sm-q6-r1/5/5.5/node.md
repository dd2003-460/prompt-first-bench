# N31: 路由逻辑中的DNS解析延迟贡献：全公有云依赖Anycast DNS，解析延迟<10ms；自建+混合需智能DNS调度，解析延迟可能增加5-20ms，该延迟直接计入

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

路由逻辑中的DNS解析延迟贡献：全公有云依赖Anycast DNS，解析延迟<10ms；自建+混合需智能DNS调度，解析延迟可能增加5-20ms，该延迟直接计入每请求P99，需按策略分别计算

## Corrected Claim

路由逻辑中的DNS解析延迟贡献：全公有云依赖Anycast DNS，解析延迟<10ms；自建+混合需智能DNS调度，解析延迟可能增加5-20ms，该延迟直接计入每请求P99，需按策略分别计算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

DNS resolution latency impact CDN anycast vs smart DNS
