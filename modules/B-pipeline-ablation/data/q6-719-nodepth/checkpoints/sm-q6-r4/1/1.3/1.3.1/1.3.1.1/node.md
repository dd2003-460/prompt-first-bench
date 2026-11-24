# N221: 在 T=200ms 阈值下，若 H_pop=0.95 且回源延迟 P99(T_origin_fetch_self)=80ms，则 (1-H_pop)*P99(T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

在 T=200ms 阈值下，若 H_pop=0.95 且回源延迟 P99(T_origin_fetch_self)=80ms，则 (1-H_pop)*P99(T_origin_fetch_self) = 4ms，该工作点下回源延迟贡献占比 < 3%，P99_self 主要受 RTT 主导

## Corrected Claim

在 T=200ms 阈值下，若 H_pop=0.95 且回源延迟 P99(T_origin_fetch_self)=80ms，则 (1-H_pop)*P99(T_origin_fetch_self) = 4ms，该工作点下回源延迟贡献占比 < 3%，P99_self 主要受 RTT 主导

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于命中率变化带来的成本与延迟预算敏感度（动态/边际分析），子节点2聚焦于回源延迟本身的物理构成验证（静态/结构性分析）。两者维度不同，无重复或矛盾。父节点的核心结论（回源贡献占比小，RTT主导）在子节点2中通过验证80ms的合理性间接支撑，在子节点1中通过量化4ms的具体数值体现，覆盖了父节点的关键逻辑链条（计算基础+敏感性/约束）。）
