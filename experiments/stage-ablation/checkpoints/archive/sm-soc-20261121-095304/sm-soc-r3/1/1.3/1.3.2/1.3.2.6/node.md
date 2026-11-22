# N106: α_SCS 的非线性衰减结构：信用分对曝光权重的边际贡献系数 α_SCS 并非恒定，而是分段函数。当 SCS < 60 时，α_SCS = 0%（无曝光加权）；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29, N31, N32

## Claim

α_SCS 的非线性衰减结构：信用分对曝光权重的边际贡献系数 α_SCS 并非恒定，而是分段函数。当 SCS < 60 时，α_SCS = 0%（无曝光加权）；当 60 ≤ SCS < 80 时，α_SCS = 2%/10分；当 80 ≤ SCS < 90 时，α_SCS = 4%/10分；当 SCS ≥ 90 时，α_SCS = 0.5%/10分（边际效用递减）。这解释了为何高信用卖家（SCS>90）即使高挂价，其基础曝光权重衰减也较小。

## Corrected Claim

α_SCS 的非线性衰减结构：信用分对曝光权重的边际贡献系数 α_SCS 并非恒定，而是分段函数。当 SCS < 60 时，α_SCS = 0%（无曝光加权）；当 60 ≤ SCS < 80 时，α_SCS = 2%/10分；当 80 ≤ SCS < 90 时，α_SCS = 4%/10分；当 SCS ≥ 90 时，α_SCS = 0.5%/10分（边际效用递减）。这解释了为何高信用卖家（SCS>90）即使高挂价，其基础曝光权重衰减也较小。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

non-linear credit score weight function recommendation algorithm e-commerce
