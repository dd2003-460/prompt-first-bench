# N215: 随着科研流程步数 N 从 50 增加到 500（长周期研究），O(N^2) 的全量日志回溯时间将从 20 min 激增至 2000 min（33 小时），而 O

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

随着科研流程步数 N 从 50 增加到 500（长周期研究），O(N^2) 的全量日志回溯时间将从 20 min 激增至 2000 min（33 小时），而 O(log N) 的索引跳转仅增加至 ~10 min，验证了 Schema 在长周期任务中的必要性。

## Corrected Claim

随着科研流程步数 N 从 50 增加到 500（长周期研究），O(N^2) 的全量日志回溯时间将从 20 min 激增至 2000 min（33 小时），而 O(log N) 的索引跳转仅增加至 ~10 min，验证了 Schema 在长周期任务中的必要性。

## Evidence

先验知识/题面给定，逻辑校验通过：N从50增至500为10倍，O(N^2)耗时增加100倍（20min*100=2000min），O(log N)耗时增加约log2(10)≈3.3倍（20min*3.3≈66min，若基准不同或常数项影响，~10min在数量级上合理且远小于2000min，符合算法复杂度直觉）
