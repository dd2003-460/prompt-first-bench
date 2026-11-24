# N29: 延迟需求：温数据扫描为顺序读，延迟不敏感（P99<100ms即可）；冷数据无交互查询，延迟无约束；若存在偶发点查（<1%流量），P99延迟需<10ms

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

延迟需求：温数据扫描为顺序读，延迟不敏感（P99<100ms即可）；冷数据无交互查询，延迟无约束；若存在偶发点查（<1%流量），P99延迟需<10ms

## Corrected Claim

延迟需求：温数据扫描为顺序读，延迟不敏感（P99<100ms即可）；冷数据无交互查询，延迟无约束；若存在偶发点查（<1%流量），P99延迟需<10ms

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对父节点中提到的三个不同数据层级/场景（温数据顺序读、冷数据点查、温数据延迟敏感度与吞吐可行性）进行了独立且具体的量化分析。三者关注点不同（IOPS计算、延迟边界、吞吐与限流），无逻辑重叠或矛盾，且完整覆盖了父节点定义的所有约束条件。）

## Search Query

sequential scan latency requirement point query P99
