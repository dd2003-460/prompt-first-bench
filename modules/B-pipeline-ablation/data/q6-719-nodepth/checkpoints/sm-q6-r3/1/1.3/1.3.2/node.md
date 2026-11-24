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

父节点级核验未通过：非正交, 不完备, 有冗余（1. 非正交且矛盾：父节点定义70%用户RTT<30ms，子节点却计算核心区域P99为25ms（虽在范围内但逻辑上若P99是25ms，则大部分应更低，且与父节点整体P99=60ms的推导逻辑割裂，父节点直接取最大值60ms忽略了加权分布或更精确的P99定义）。2. 不完备：父节点提到30%用户距离200-500km，子节点仅覆盖300-500km，遗漏了200-300km区间，导致P99估算依据不全。3. 冗余：两个子节点本质上是同一公式 RTT = 0.05*d + 5 + ΔT 在不同距离和惩罚参数下的计算，属于同一模型的不同参数代入，可合并为一个参数化节点。）

## Search Query

Self-built POP geographic coverage RTT P99 latency estimate 60ms China
