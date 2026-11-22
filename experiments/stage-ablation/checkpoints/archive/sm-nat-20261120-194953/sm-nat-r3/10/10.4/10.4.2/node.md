# N179: H_base = 1.0 的边界条件：该结论仅在缓存内容完全匹配请求目标集合时成立；若存在请求指向已失效（更新后）的对象，H_base 需修正为 H_base'

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83, N84

## Claim

H_base = 1.0 的边界条件：该结论仅在缓存内容完全匹配请求目标集合时成立；若存在请求指向已失效（更新后）的对象，H_base 需修正为 H_base' = 1 - P_stale，其中 P_stale 为请求命中失效对象的概率，在全量驻留且无更新场景下 P_stale = 0，故 H_base = 1.0 是理想上界

## Corrected Claim

H_base = 1.0 的边界条件：该结论仅在缓存内容完全匹配请求目标集合时成立；若存在请求指向已失效（更新后）的对象，H_base 需修正为 H_base' = 1 - P_stale，其中 P_stale 为请求命中失效对象的概率，在全量驻留且无更新场景下 P_stale = 0，故 H_base = 1.0 是理想上界

## Evidence

先验知识/题面给定，逻辑校验通过：H_base 定义为理想命中率，当缓存内容完全匹配且无失效（P_stale=0）时，命中率确为 1.0，公式推导自洽。
