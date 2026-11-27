# N116: 在 LLM 推理负载下，GPU 的平均功耗利用率约为 60-80% 标称 TDP，因此 2x RTX 4090 的实际平均功率约为 540W-720W，导致实际

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

在 LLM 推理负载下，GPU 的平均功耗利用率约为 60-80% 标称 TDP，因此 2x RTX 4090 的实际平均功率约为 540W-720W，导致实际年电费低于基于满载 TDP 计算的 $1286。

## Corrected Claim

在 LLM 推理负载下，GPU 的平均功耗利用率约为 60-80% 标称 TDP，因此 2x RTX 4090 的实际平均功率约为 540W-720W，导致实际年电费低于基于满载 TDP 计算的 $1286。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP为450W，2x即900W；60-80%利用率对应540W-720W，计算无误；负载率低于100%必然导致电费低于满载计算值，逻辑自洽。

## Search Query

LLM inference GPU power utilization percentage
