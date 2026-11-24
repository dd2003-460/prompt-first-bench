# N129: 自建 POP 回源数据传输时间 T_transfer_origin_self，基于对象大小 s 和 POP 到源站的带宽 B_pop_origin，计算公式为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

自建 POP 回源数据传输时间 T_transfer_origin_self，基于对象大小 s 和 POP 到源站的带宽 B_pop_origin，计算公式为 T_transfer_origin_self = s / B_pop_origin，P99 值受 POP 出口带宽限制。

## Corrected Claim

自建 POP 回源数据传输时间 T_transfer_origin_self，基于对象大小 s 和 POP 到源站的带宽 B_pop_origin，计算公式为 T_transfer_origin_self = s / B_pop_origin，P99 值受 POP 出口带宽限制。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别涵盖了带宽规格设定（基础设施）、基础传输时间计算（核心公式应用）以及并发导致的队列延迟（边界条件/扩展因素），三者维度不同，无逻辑重叠或矛盾。父节点中提到的'P99值受POP出口带宽限制'在子节点2和3中通过具体数值计算和队列效应得到了体现和解释，覆盖了关键方面。）

## Search Query

self-built POP origin pull transfer time calculation
