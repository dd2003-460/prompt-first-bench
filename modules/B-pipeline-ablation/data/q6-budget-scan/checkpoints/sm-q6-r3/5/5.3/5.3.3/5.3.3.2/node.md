# N316: 延迟惩罚高代价工作点（跨省/跨国回源）：Origin 位于核心枢纽（如北京/上海）而 POP 点在边缘（如新疆/西藏或海外），T_origin_RTT ≈ 80

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

延迟惩罚高代价工作点（跨省/跨国回源）：Origin 位于核心枢纽（如北京/上海）而 POP 点在边缘（如新疆/西藏或海外），T_origin_RTT ≈ 80-150ms，T_edge_RTT ≈ 20-30ms，延迟增加量 ΔLatency ≈ 60-120ms，若含跨国链路则可达 200ms+，P99 劣化显著，需依赖 Anycast 或智能调度缓解。

## Corrected Claim

延迟惩罚高代价工作点（跨省/跨国回源）：Origin 位于核心枢纽（如北京/上海）而 POP 点在边缘（如新疆/西藏或海外），T_origin_RTT ≈ 80-150ms，T_edge_RTT ≈ 20-30ms，延迟增加量 ΔLatency ≈ 60-120ms，若含跨国链路则可达 200ms+，P99 劣化显著，需依赖 Anycast 或智能调度缓解。

## Evidence

先验知识/题面给定，逻辑校验通过：跨省/跨国链路RTT量级（80-150ms）及边缘节点RTT（20-30ms）符合网络物理规律，延迟增量计算自洽。
