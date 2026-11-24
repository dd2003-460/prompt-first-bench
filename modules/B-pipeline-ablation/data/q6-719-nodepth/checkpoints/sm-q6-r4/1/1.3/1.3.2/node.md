# N57: 自建 POP 用户到节点 RTT 的 P99 估算：10 个 POP 覆盖中国主要城市，假设 70% 用户距最近 POP <200km（RTT<30ms），30

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

自建 POP 用户到节点 RTT 的 P99 估算：10 个 POP 覆盖中国主要城市，假设 70% 用户距最近 POP <200km（RTT<30ms），30% 用户距 200-500km（RTT 30-60ms），则 P99(RTT_user_pop) ≈ 60ms。

## Corrected Claim

自建 POP 用户到节点 RTT 的 P99 估算：10 个 POP 覆盖中国主要城市，假设 70% 用户距最近 POP <200km（RTT<30ms），30% 用户距 200-500km（RTT 30-60ms），则 P99(RTT_user_pop) ≈ 60ms。

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 正交性冲突：父节点定义核心区域为 <200km，子节点将其收窄为 <100km，导致 100-200km 的用户区间未被明确归类（虽然可能归入长尾，但边界定义不一致）。2. 逻辑矛盾：父节点结论 P99≈60ms，而子节点给出的核心 P99=25ms 和长尾 P99=50ms，简单加权或取最大值均无法直接推导出 60ms（若 P99 落在长尾区间，其上限为 50ms，与父节点 60ms 矛盾）。3. 冗余：两个子节点本质上是同一参数模型（RTT=f(d)）在不同距离区间的取值，且都包含“跨网惩罚”这一相同变量，结构上高度重复，可合并为一个包含分段函数的节点或提取公共参数。）

## Search Query

Self-built POP geographic coverage RTT P99 latency estimate 60ms China
