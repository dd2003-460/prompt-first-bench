# N96: 若 S_total > 128GB（例如 s_min=10KB 时 S_total≈200GB），则 k_max < 100,000。此时需找到 k 使得 Σ_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

若 S_total > 128GB（例如 s_min=10KB 时 S_total≈200GB），则 k_max < 100,000。此时需找到 k 使得 Σ_{i=1}^{k} S_i = 128GB。由于热度-大小负相关，前 k 个最热对象的大小和小于随机 k 个对象的大小和，因此 k_max 会比无相关时更大。

## Corrected Claim

若 S_total > 128GB（例如 s_min=10KB 时 S_total≈200GB），则 k_max < 100,000。此时需找到 k 使得 Σ_{i=1}^{k} S_i = 128GB。由于热度-大小负相关，前 k 个最热对象的大小和小于随机 k 个对象的大小和，因此 k_max 会比无相关时更大。

## Evidence

先验知识/题面给定，逻辑校验通过：在总容量固定且对象按热度排序时，若热度与大小负相关（热对象小），则前k个热对象的总大小小于随机k个对象的总大小，因此需要更大的k才能达到相同的容量阈值128GB，推导自洽。
