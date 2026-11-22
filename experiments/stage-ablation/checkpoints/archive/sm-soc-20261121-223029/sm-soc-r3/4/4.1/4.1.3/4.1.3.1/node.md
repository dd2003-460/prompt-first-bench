# N236: 透明化机制下的买家信息不对称成本基线 C_info_base 的量化构成：C_info_base = C_search_time * W_buyer + C_v

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79, N80, N81

## Claim

透明化机制下的买家信息不对称成本基线 C_info_base 的量化构成：C_info_base = C_search_time * W_buyer + C_verification_cost，其中 C_search_time 为平均比价耗时（小时），W_buyer 为买家时薪（元/小时），C_verification_cost 为验证商品真伪/成色的直接成本（如鉴定费或运费险）；需估计二手平台典型买家的 W_buyer ≈ 50-100元/小时，C_search_time ≈ 0.5-2小时，从而得出 C_info_base 的典型区间。

## Corrected Claim

透明化机制下的买家信息不对称成本基线 C_info_base 的量化构成：C_info_base = C_search_time * W_buyer + C_verification_cost，其中 C_search_time 为平均比价耗时（小时），W_buyer 为买家时薪（元/小时），C_verification_cost 为验证商品真伪/成色的直接成本（如鉴定费或运费险）；需估计二手平台典型买家的 W_buyer ≈ 50-100元/小时，C_search_time ≈ 0.5-2小时，从而得出 C_info_base 的典型区间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second-hand platform buyer search time cost hourly wage average
