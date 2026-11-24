# N147: 在区域中心用户（如武汉用户访问武汉POP）场景下，物理距离 d ≈ 50-100 km，RTT 理论下限 ≈ 0.5-1ms，代表中等延迟/中等成本工作点，常用

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在区域中心用户（如武汉用户访问武汉POP）场景下，物理距离 d ≈ 50-100 km，RTT 理论下限 ≈ 0.5-1ms，代表中等延迟/中等成本工作点，常用于验证 POP 覆盖密度对 P99 的影响。

## Corrected Claim

在区域中心用户（如武汉用户访问武汉POP）场景下，物理距离 d ≈ 50-100 km，RTT 理论下限 ≈ 0.5-1ms，代表中等延迟/中等成本工作点，常用于验证 POP 覆盖密度对 P99 的影响。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点1和子节点2存在严重冗余和逻辑重叠：子节点1中的 T_rtt_regional 与子节点2中的 T_rtt_actual 指代同一物理量，且数值范围（0.5-1ms vs 0.85-1.15ms）存在轻微矛盾（子节点2计算值下限高于子节点1引用值下限）；子节点3关于P99影响的公式推导过于简化，未区分P99与RTT的直接线性关系，且与子节点1的延迟构成模型缺乏明确关联。）

## Search Query

regional center user to local POP distance 50-100km RTT
