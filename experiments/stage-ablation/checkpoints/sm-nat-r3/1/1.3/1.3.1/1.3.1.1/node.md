# N86: 哈希表内存开销 M_hash = N_cached * (k_bucket * sizeof(pointer) + sizeof(object_header))

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

哈希表内存开销 M_hash = N_cached * (k_bucket * sizeof(pointer) + sizeof(object_header))，在 N_cached=100,000, k_bucket=8, pointer=8B, header=64B 时，M_hash ≈ 100,000 * (64+64) = 12.8 MB。

## Corrected Claim

哈希表内存开销 M_hash = N_cached * (k_bucket * sizeof(pointer) + sizeof(object_header))，在 N_cached=100,000, k_bucket=8, pointer=8B, header=64B 时，M_hash ≈ 100,000 * (64+64) = 12.8 MB。

## Evidence

先验知识/题面给定，逻辑校验通过
