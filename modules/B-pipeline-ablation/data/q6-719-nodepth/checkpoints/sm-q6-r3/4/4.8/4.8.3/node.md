# N132: 混合策略中核心区域的流量占比 P_core，通常为 60-80%，取决于用户地理分布和业务热点区域，影响 P99_mix 的加权计算。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

混合策略中核心区域的流量占比 P_core，通常为 60-80%，取决于用户地理分布和业务热点区域，影响 P99_mix 的加权计算。

## Corrected Claim

混合策略中核心区域的流量占比 P_core，通常为 60-80%，取决于用户地理分布和业务热点区域，影响 P99_mix 的加权计算。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是参数 P_core 在不同取值（0.8, 0.6, 0.4）下的实例化，属于同一维度的离散采样，存在高度冗余；且父节点明确指出 P_core 范围为 60-80%，子节点中 P_core=0.4 超出该范围，导致逻辑不一致且未覆盖完整定义域。）

## Search Query

hybrid CDN strategy traffic distribution core vs tail region
