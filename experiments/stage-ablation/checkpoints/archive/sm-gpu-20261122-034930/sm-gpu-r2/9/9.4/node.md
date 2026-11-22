# N148: 在32K长上下文场景下，KV Cache读取占比随seq_len线性增加，使得实际吞吐率偏离理论带宽上限的比例从短文本(1K ctx)的~5%增加到长文本(32

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N43

## Claim

在32K长上下文场景下，KV Cache读取占比随seq_len线性增加，使得实际吞吐率偏离理论带宽上限的比例从短文本(1K ctx)的~5%增加到长文本(32K ctx)的~15-20% [待核验：需实测vLLM在不同ctx长度下的带宽利用率曲线]，这是导致N44中实际值(20-30)低于理论值(26.7)的主要机制之一。

## Corrected Claim

在32K长上下文场景下，KV Cache读取占比随seq_len增加，导致实际吞吐率偏离理论带宽上限的比例较短文本显著增加，这是导致实际值低于理论值的主要机制之一。

## Evidence

[质询]该陈述包含具体的经验性数值（5%、15-20%）和线性关系假设，属于硬件/系统性能的经验事实，无法从第一性原理严格推导，且缺乏实测数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM memory bandwidth utilization 32k context length overhead
