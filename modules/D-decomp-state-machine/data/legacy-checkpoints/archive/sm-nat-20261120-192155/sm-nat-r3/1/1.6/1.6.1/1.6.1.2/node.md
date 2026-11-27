# N99: 工作点3（局部热点漂移）：当负载存在局部热点且热点位置随时间缓慢漂移时，LRU因驱逐滞后（eviction lag）导致命中率波动；滞后时间T_lag ≈ 1/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

工作点3（局部热点漂移）：当负载存在局部热点且热点位置随时间缓慢漂移时，LRU因驱逐滞后（eviction lag）导致命中率波动；滞后时间T_lag ≈ 1/r_{k+1}，在Pareto(β=0.9)下，T_lag与k的-0.9次方成正比，漂移速度越快，ΔH越大。

## Corrected Claim

工作点3（局部热点漂移）：当负载存在局部热点且热点位置随时间缓慢漂移时，LRU因驱逐滞后（eviction lag）导致命中率波动；滞后时间T_lag ≈ 1/r_{k+1}，在Pareto(β=0.9)下，T_lag与k的-0.9次方成正比，漂移速度越快，ΔH越大。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驱逐滞后与访问频率倒数成正比符合缓存理论，Pareto分布下频率与排名呈幂律关系，推导出的时间复杂度与漂移影响逻辑自洽。

## Search Query

LRU eviction lag dynamic workload hotspot drift
