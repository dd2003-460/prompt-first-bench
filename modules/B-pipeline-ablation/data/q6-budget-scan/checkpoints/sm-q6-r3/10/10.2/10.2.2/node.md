# N338: 共因故障相关系数 k_correlation 量化：k_correlation = 1 + (N_shared_components / N_total_com

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

共因故障相关系数 k_correlation 量化：k_correlation = 1 + (N_shared_components / N_total_components) * k_shared_failure_prob，其中骨干网中断影响所有POP，概率约0.1-0.2次/年，导致k_correlation在1.0-1.2区间

## Corrected Claim

共因故障相关系数 k_correlation 量化：k_correlation = 1 + (N_shared_components / N_total_components) * k_shared_failure_prob，其中骨干网中断影响所有POP，概率约0.1-0.2次/年，导致k_correlation在1.0-1.2区间

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data center correlated failure probability backbone network outage
