# N115: 自建 POP 单级缓存命中率 H_self_single = 1 - (W / C_pop)^(1/α)，其中 W 为内容工作集大小，C_pop 为 POP 总

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

自建 POP 单级缓存命中率 H_self_single = 1 - (W / C_pop)^(1/α)，其中 W 为内容工作集大小，C_pop 为 POP 总存储容量，α 为 Zipf 分布参数（通常 α=0.8-1.2），当 W > C_pop 时 H_self_single < 0.5，当 W < C_pop/2 时 H_self_single > 0.8。

## Corrected Claim

自建 POP 单级缓存命中率 H_self_single = 1 - (W / C_pop)^(1/α)，其中 W 为内容工作集大小，C_pop 为 POP 总存储容量，α 为 Zipf 分布参数（通常 α=0.8-1.2），当 W > C_pop 时 H_self_single < 0.5，当 W < C_pop/2 时 H_self_single > 0.8。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Zipf distribution cache hit rate formula
