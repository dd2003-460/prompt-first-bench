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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数 P_core 的不同取值（0.8, 0.6, 0.4），属于枚举而非正交维度分解，存在高度冗余；且未覆盖父节点中提到的‘用户地理分布’和‘业务热点区域’等决定 P_core 的关键前置因素，完备性不足。）

## Search Query

hybrid CDN strategy traffic distribution core vs tail region
