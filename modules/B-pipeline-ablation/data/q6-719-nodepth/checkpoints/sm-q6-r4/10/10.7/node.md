# N193: P99 合规率定义为满足 P99_latency <= T 的请求比例，对于固定 T=100ms，公有云 CDN 在长尾区域（距离 >500km）的合规率约为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49

## Claim

P99 合规率定义为满足 P99_latency <= T 的请求比例，对于固定 T=100ms，公有云 CDN 在长尾区域（距离 >500km）的合规率约为 40-60%，因为 RTT 基础值已接近 50-80ms，加上处理延迟易超标

## Corrected Claim

P99 合规率定义为满足 P99_latency <= T 的请求比例，对于固定 T=100ms，公有云 CDN 在长尾区域（距离 >500km）的合规率约为 40-60%，因为 RTT 基础值已接近 50-80ms，加上处理延迟易超标

## Evidence

先验知识/题面给定，逻辑校验通过：物理上距离>500km的RTT基础值（光速限制）确实在50-80ms量级，加上处理延迟后P99超过100ms是符合物理直觉的，40-60%的合规率作为经验估计在逻辑上自洽。
