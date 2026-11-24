# N540: s_weighted 的基准计算：在 P_img=0.7, P_video=0.3, s_img=1.0MB, s_video=10MB 的典型参数下，s_we

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N178

## Claim

s_weighted 的基准计算：在 P_img=0.7, P_video=0.3, s_img=1.0MB, s_video=10MB 的典型参数下，s_weighted = 0.7*1.0 + 0.3*10 = 3.7MB，该值超过 s_critical (3.2MB)，表明默认场景下自建策略在带宽成本上已具备优势。

## Corrected Claim

s_weighted 的基准计算：在 P_img=0.7, P_video=0.3, s_img=1.0MB, s_video=10MB 的典型参数下，s_weighted = 0.7*1.0 + 0.3*10 = 3.7MB，该值超过 s_critical (3.2MB)，表明默认场景下自建策略在带宽成本上已具备优势。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.7*1.0 + 0.3*10 = 3.7 正确，且 3.7 > 3.2 的比较逻辑自洽。
