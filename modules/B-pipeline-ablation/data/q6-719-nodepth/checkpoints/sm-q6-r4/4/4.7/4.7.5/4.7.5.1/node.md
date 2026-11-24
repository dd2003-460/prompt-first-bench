# N416: POP到源站的单链路带宽 B_pop_origin_link 规格设定：为确保回源不成为瓶颈，单链路带宽应满足 B_pop_origin_link >= B_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

POP到源站的单链路带宽 B_pop_origin_link 规格设定：为确保回源不成为瓶颈，单链路带宽应满足 B_pop_origin_link >= B_origin_peak / N_pop_active，若 N_pop_active=10, B_origin_peak=98.76Mbps，则单链路需 >= 10Mbps；实际采购通常选择 100Mbps 或 1Gbps 以预留余量。

## Corrected Claim

POP到源站的单链路带宽 B_pop_origin_link 规格设定：为确保回源不成为瓶颈，单链路带宽应满足 B_pop_origin_link >= B_origin_peak / N_pop_active，若 N_pop_active=10, B_origin_peak=98.76Mbps，则单链路需 >= 10Mbps；实际采购通常选择 100Mbps 或 1Gbps 以预留余量。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 98.76/10=9.876，向上取整或满足 >= 条件即为 10Mbps，逻辑自洽；采购建议符合工程惯例。
