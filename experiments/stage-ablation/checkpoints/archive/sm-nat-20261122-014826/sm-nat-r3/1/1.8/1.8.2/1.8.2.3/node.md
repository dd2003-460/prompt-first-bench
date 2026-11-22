# N123: H_revalidate 的边界条件量化：若对象更新导致内容变更（而非仅版本戳更新），H_revalidate = P[content_unchanged]。在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

H_revalidate 的边界条件量化：若对象更新导致内容变更（而非仅版本戳更新），H_revalidate = P[content_unchanged]。在 CDN 场景中，若 90% 的更新仅为元数据刷新（如 ETag 不变），则 H_revalidate = 0.9；若 100% 更新导致内容变更，H_revalidate = 0。此参数决定了公式中第二项 u * P_in_LRU * H_revalidate 的权重，当 H_revalidate=1 时该项抵消了第一项的损失，净损失为 0；当 H_revalidate=0 时净损失为 u * P_in_LRU。

## Corrected Claim

H_revalidate 的边界条件量化：若对象更新导致内容变更（而非仅版本戳更新），H_revalidate = P[content_unchanged]。在 CDN 场景中，若 90% 的更新仅为元数据刷新（如 ETag 不变），则 H_revalidate = 0.9；若 100% 更新导致内容变更，H_revalidate = 0。此参数决定了公式中第二项 u * P_in_LRU * H_revalidate 的权重，当 H_revalidate=1 时该项抵消了第一项的损失，净损失为 0；当 H_revalidate=0 时净损失为 u * P_in_LRU。

## Evidence

先验知识/题面给定，逻辑校验通过
