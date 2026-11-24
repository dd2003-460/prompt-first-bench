# N560: 同网跨省 RTT 的 P99 与平均值的差异 ΔT_p99_avg (ms)：在电信网络中，跨省 P99 延迟通常比平均延迟高 10-15ms，主要源于骨干网拥

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N183

## Claim

同网跨省 RTT 的 P99 与平均值的差异 ΔT_p99_avg (ms)：在电信网络中，跨省 P99 延迟通常比平均延迟高 10-15ms，主要源于骨干网拥塞时的排队延迟（Queueing Delay），该值与骨干网利用率 U_backbone 呈非线性关系，当 U_backbone > 0.8 时，ΔT_p99_avg 急剧增加。

## Corrected Claim

在电信网络中，跨省 P99 延迟通常显著高于平均延迟，主要源于骨干网拥塞时的排队延迟，该差异与骨干网利用率呈非线性关系，高利用率下急剧增加。

## Evidence

[质询]具体数值范围（10-15ms）和阈值（U>0.8）属于经验性工程参数，缺乏通用标准支持，且受具体网络拓扑、业务类型影响极大，无法从第一性原理严格推导。 | 经验事实，逻辑自洽（排队论中延迟随利用率非线性增长符合直觉），但缺来源支持具体数值。

## Search Query

backbone network congestion queueing delay P99 vs average RTT cross-province China telecom
