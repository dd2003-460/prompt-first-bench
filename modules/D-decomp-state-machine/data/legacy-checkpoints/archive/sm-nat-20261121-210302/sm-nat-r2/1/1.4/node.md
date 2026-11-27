# N8: 对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均驻留时间（由 LRU 替换策略和请求频率决定）

## Corrected Claim

对象更新率 1%/天 导致 LRU 有效命中率折损系数 D = 1 - (1 - 0.01)^(T_resident)，其中 T_resident 是对象的平均驻留时间（由 LRU 替换策略和请求频率决定）

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点1和子节点4均旨在估算 T_resident，存在概念重叠（冗余）；子节点1使用宏观稳态近似（C/R_evict），而子节点4使用微观排名近似（Pareto逆CDF），两者在逻辑上可能不一致（矛盾风险）；此外，父节点公式中的 T_resident 被分解为两个不同来源的估算方法，且子节点3中的折损机制描述（H_eff = H_original * (1 - P_stale * H_original)）在数学上存疑（通常有效命中率应直接减去因过期导致的无效命中部分，即 H_eff ≈ H_original - P_stale * H_original 或类似形式，当前公式可能导致命中率非线性下降过度或逻辑不清），且未明确说明 H_original 是 LRU 命中率还是其他基准。）
