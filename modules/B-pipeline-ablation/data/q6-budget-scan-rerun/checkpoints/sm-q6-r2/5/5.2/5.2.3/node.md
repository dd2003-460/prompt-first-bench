# N101: s对P99延迟的影响函数：更大的对象需要更长的传输时间，P99延迟 P99(s) ≈ P99_base + (s / B_peak_pop) * 1000，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

s对P99延迟的影响函数：更大的对象需要更长的传输时间，P99延迟 P99(s) ≈ P99_base + (s / B_peak_pop) * 1000，其中P99_base=100ms（网络延迟），B_peak_pop为单POP点峰值带宽（如1Gbps）；例如s=500KB时P99≈100.5ms，s=5MB时P99≈150ms，s增大10倍导致P99延迟增加约50ms，可能影响T=300ms的合规性（若P99_base较高）。

## Corrected Claim

s对P99延迟的影响函数：更大的对象需要更长的传输时间，P99延迟 P99(s) ≈ P99_base + (s / B_peak_pop) * 1000，其中P99_base=100ms（网络延迟），B_peak_pop为单POP点峰值带宽（如1Gbps）；例如s=500KB时P99≈100.5ms，s=5MB时P99≈150ms，s增大10倍导致P99延迟增加约50ms，可能影响T=300ms的合规性（若P99_base较高）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（字节/带宽=秒），数值计算准确（500KB/1Gbps≈0.5ms, 5MB/1Gbps≈50ms），符合网络传输基本物理规律。

## Search Query

object size impact on P99 latency CDN edge node
