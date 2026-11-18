# N89: 有效内存利用率 η_eff = 1 - (M_hash + M_lru + M_os) / C_total，代入上述估算值，η_eff ≈ 1 - (16 MB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

有效内存利用率 η_eff = 1 - (M_hash + M_lru + M_os) / C_total，代入上述估算值，η_eff ≈ 1 - (16 MB + 12.8 GB) / 128 GB ≈ 0.90，即 C_avail ≈ 115.2 GB。

## Corrected Claim

有效内存利用率 η_eff = 1 - (M_hash + M_lru + M_os) / C_total，代入上述估算值，η_eff ≈ 1 - (16 MB + 12.8 GB) / 128 GB ≈ 0.90，即 C_avail ≈ 115.2 GB。

## Evidence

先验知识/题面给定，逻辑校验通过
