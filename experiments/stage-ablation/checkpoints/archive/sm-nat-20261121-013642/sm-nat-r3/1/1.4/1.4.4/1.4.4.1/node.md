# N125: 工作点2（近似最优/低代价）：使用 LRU-K (K=2) 或 ARC 算法作为 MIN 的在线近似，其命中率 H_ARC 通常落在 H_LRU 和 H_MIN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点2（近似最优/低代价）：使用 LRU-K (K=2) 或 ARC 算法作为 MIN 的在线近似，其命中率 H_ARC 通常落在 H_LRU 和 H_MIN 之间，且计算复杂度 O(log N)，是工程上可落地的上界参照，预期 H_ARC ≈ H_MIN - 2-3%。

## Corrected Claim

工作点2（近似最优/低代价）：使用 LRU-K (K=2) 或 ARC 算法作为 MIN 的在线近似，其命中率 H_ARC 通常落在 H_LRU 和 H_MIN 之间，且计算复杂度 O(log N)，是工程上可落地的上界参照，预期 H_ARC ≈ H_MIN - 2-3%。

## Evidence

先验知识/题面给定，逻辑校验通过
