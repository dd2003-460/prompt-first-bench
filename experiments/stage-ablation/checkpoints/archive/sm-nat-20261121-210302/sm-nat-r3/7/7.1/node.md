# N75: LFU 保留的热点对象平均大小 S_LFU_hot 的计算公式：S_LFU_hot = E[S | P > P_95%]，其中 P_95% 是热度 Pareto

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LFU 保留的热点对象平均大小 S_LFU_hot 的计算公式：S_LFU_hot = E[S | P > P_95%]，其中 P_95% 是热度 Pareto(β=0.9) 的 95 分位数，对应头部 5% 最热门对象。

## Corrected Claim

LFU 保留的热点对象平均大小 S_LFU_hot 的计算公式：S_LFU_hot = E[S | P > P_95%]，其中 P_95% 是热度 Pareto(β=0.9) 的 95 分位数，对应头部 5% 最热门对象。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pareto distribution percentile conditional expectation
