# N298: 直连源站的P99延迟增加量 ΔP99_limit 与源站地理位置及网络RTT相关：若源站位于上海，长尾地区（如新疆）RTT≈80ms，加上源站处理时间 50ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

直连源站的P99延迟增加量 ΔP99_limit 与源站地理位置及网络RTT相关：若源站位于上海，长尾地区（如新疆）RTT≈80ms，加上源站处理时间 50ms，总延迟≈130ms；相比边缘节点延迟 50ms，增加量 ΔP99_limit ≈ 80ms，符合 50-100ms 区间

## Corrected Claim

直连源站的P99延迟增加量 ΔP99_limit 与源站地理位置及网络RTT相关：若源站位于上海，长尾地区（如新疆）RTT≈80ms，加上源站处理时间 50ms，总延迟≈130ms；相比边缘节点延迟 50ms，增加量 ΔP99_limit ≈ 80ms，符合 50-100ms 区间

## Evidence

先验知识/题面给定，逻辑校验通过：上海至新疆RTT约80ms符合网络物理常识，总延迟130ms减去边缘50ms得增量80ms，计算自洽且符合50-100ms区间。
