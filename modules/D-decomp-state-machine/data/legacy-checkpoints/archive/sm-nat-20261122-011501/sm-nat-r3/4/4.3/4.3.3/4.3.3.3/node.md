# N138: 非命中率维度的代价量化：更新导致的 ETag 校验开销。每次命中需比对 ETag，若更新率高，ETag 不匹配率 P_mismatch ≈ λ_update *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

非命中率维度的代价量化：更新导致的 ETag 校验开销。每次命中需比对 ETag，若更新率高，ETag 不匹配率 P_mismatch ≈ λ_update * T_res。虽然字节命中率不变，但 CPU 开销增加 ΔCPU = P_mismatch * Cost_Validate。此代价在 1%/天 更新率下可忽略，但在 100%/天 更新率下成为瓶颈。

## Corrected Claim

非命中率维度的代价量化：更新导致的 ETag 校验开销。每次命中需比对 ETag，若更新率高，ETag 不匹配率 P_mismatch ≈ λ_update * T_res。虽然字节命中率不变，但 CPU 开销增加 ΔCPU = P_mismatch * Cost_Validate。此代价在 1%/天 更新率下可忽略，但在 100%/天 更新率下成为瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过
