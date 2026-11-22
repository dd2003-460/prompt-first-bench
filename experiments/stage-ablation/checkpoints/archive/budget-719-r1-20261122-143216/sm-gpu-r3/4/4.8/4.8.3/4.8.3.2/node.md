# N357: 基于 Roofline 模型，64K 上下文 Decode 吞吐量 (tokens/s) 的理论上限计算公式为 Bandwidth / (Weight_Size

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

基于 Roofline 模型，64K 上下文 Decode 吞吐量 (tokens/s) 的理论上限计算公式为 Bandwidth / (Weight_Size + KV_Size_per_token)，其中 KV_Size_per_token 随上下文线性增长，导致分母增大，吞吐量下降比例约为 (KV_32K / (W + KV_32K))。

## Corrected Claim

基于 Roofline 模型，64K 上下文 Decode 吞吐量 (tokens/s) 的理论上限计算公式为 Bandwidth / (Weight_Size + KV_Size_per_token)，其中 KV_Size_per_token 随上下文线性增长，导致分母增大，吞吐量下降比例约为 (KV_32K / (W + KV_32K))。

## Evidence

先验知识/题面给定，逻辑校验通过：Roofline模型下Decode阶段为内存带宽受限，吞吐量上限确实由带宽除以每token需读取的数据量（权重+KV Cache）决定，KV Cache随上下文线性增长导致分母增大，推导逻辑自洽。
