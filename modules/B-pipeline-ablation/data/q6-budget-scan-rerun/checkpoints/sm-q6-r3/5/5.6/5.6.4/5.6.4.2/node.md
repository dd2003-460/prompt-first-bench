# N303: 自建POP最小灰度粒度取决于DNS权重或L4 LB配置，通常最小粒度为5%（因DNS解析缓存及权重整数限制），即500万日活中25万用户；若使用Anycast+

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

自建POP最小灰度粒度取决于DNS权重或L4 LB配置，通常最小粒度为5%（因DNS解析缓存及权重整数限制），即500万日活中25万用户；若使用Anycast+本地DNS，可细化至1-2%，但工程复杂度激增。

## Corrected Claim

自建POP最小灰度粒度取决于DNS权重或L4 LB配置，通常最小粒度为5%（因DNS解析缓存及权重整数限制），即500万日活中25万用户；若使用Anycast+本地DNS，可细化至1-2%，但工程复杂度激增。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

DNS weighted round robin minimum granularity
