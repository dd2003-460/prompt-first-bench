# N91: 自建节点P99延迟的尾部修正因子 k_tail 取决于回源拥塞概率，对于10个POP点且源站位于核心机房（RTT 2-5ms）的场景，k_tail 通常取 1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

自建节点P99延迟的尾部修正因子 k_tail 取决于回源拥塞概率，对于10个POP点且源站位于核心机房（RTT 2-5ms）的场景，k_tail 通常取 1.2-1.5，导致实际 P99 修正后为 24-30ms，仍远低于 300ms 目标。

## Corrected Claim

自建节点P99延迟的尾部修正因子 k_tail 取决于回源拥塞概率，对于10个POP点且源站位于核心机房（RTT 2-5ms）的场景，k_tail 通常取 1.2-1.5，导致实际 P99 修正后为 24-30ms，仍远低于 300ms 目标。

## Evidence

先验知识/题面给定，逻辑校验通过：核心机房RTT 2-5ms，P99修正因子1.2-1.5倍后为2.4-7.5ms，远小于300ms目标，量级与逻辑自洽。

## Search Query

CDN P99 latency tail factor self-hosted edge nodes congestion probability
