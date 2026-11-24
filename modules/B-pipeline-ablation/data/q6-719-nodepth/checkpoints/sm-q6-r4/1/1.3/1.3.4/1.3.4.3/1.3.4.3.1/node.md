# N688: 跨大区公网BGP接入下，P99回源延迟中的网络传输时间 T_transfer_origin 估算为 30-50ms，基于典型对象大小 s=1MB 和 BGP 路

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N229

## Claim

跨大区公网BGP接入下，P99回源延迟中的网络传输时间 T_transfer_origin 估算为 30-50ms，基于典型对象大小 s=1MB 和 BGP 路由拥塞导致的平均吞吐量 20-30Mbps 计算 (T = s / Throughput)。

## Corrected Claim

跨大区公网BGP接入下，基于典型对象大小 s=1MB 和平均吞吐量 20-30Mbps 计算，纯网络传输时间 T_transfer_origin 估算为 267-400ms。若 P99 回源延迟中的网络传输时间仅为 30-50ms，则对应的平均吞吐量需达到 160-213Mbps，或对象大小需缩小至约 75-150KB。

## Evidence

先验知识/题面给定，逻辑校验通过：1MB数据在20-30Mbps吞吐量下的传输时间计算为 8Mbit / (20-30Mbit/s) ≈ 267-400ms，但题目中给出的30-50ms与计算结果存在数量级差异。然而，考虑到source为knowledge，且通常BGP回源延迟包含RTT和传输时间，若仅指纯传输时间，30-50ms对应的是约200-300Mbps的吞吐量，这与'20-30Mbps'矛盾。但重新审视：1MB = 8Mbit。8Mbit / 20Mbps = 0.4s = 400ms。8Mbit / 30Mbps ≈ 0.26s = 267ms。题目声称估算为30-50ms，这与基于20-30Mbps吞吐量的计算严重不符（差了一个数量级）。但是，如果这里的'回源延迟'指的是RTT（往返时延）而非纯传输时间，或者对象大小并非1MB而是更小（如100KB），则可能合理。但题目明确说'基于典型对象大小 s=1MB 和 ... 20-30Mbps 计算'。这是一个明显的逻辑/计算错误。1MB在20-30Mbps下传输需要267-400ms，绝非30-50ms。因此，该陈述存在硬逻辑错误（数值计算错误）。

## Search Query

public BGP inter-region latency 1MB transfer time congestion
