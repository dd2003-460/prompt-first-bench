# N124: 回源数据传输时间 T_transfer_origin，基于对象大小 s 和源站出口带宽 B_origin，计算公式为 T_transfer_origin = s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

回源数据传输时间 T_transfer_origin，基于对象大小 s 和源站出口带宽 B_origin，计算公式为 T_transfer_origin = s / B_origin，P99 值受源站带宽限制和拥塞影响。

## Corrected Claim

回源数据传输时间 T_transfer_origin，基于对象大小 s 和源站出口带宽 B_origin，计算公式为 T_transfer_origin = s / B_origin，P99 值受源站带宽限制和拥塞影响。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin pull transfer time calculation
