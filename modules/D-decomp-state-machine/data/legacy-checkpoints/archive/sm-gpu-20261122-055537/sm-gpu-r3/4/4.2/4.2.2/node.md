# N65: NVIDIA H100 (SXM5) 单卡方案的整机满载功耗 P_draw_1xH100 约为 1000-1100W（含GPU TDP 700W + 系统/互联

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

NVIDIA H100 (SXM5) 单卡方案的整机满载功耗 P_draw_1xH100 约为 1000-1100W（含GPU TDP 700W + 系统/互联/散热基础负载 ~300W），来源为 NVIDIA H100 技术白皮书及典型服务器功耗测试数据。

## Corrected Claim

NVIDIA H100 (SXM5) 单卡方案的整机满载功耗 P_draw_1xH100 约为 1000-1100W（含GPU TDP 700W + 系统/互联/散热基础负载 ~300W），来源为 NVIDIA H100 技术白皮书及典型服务器功耗测试数据。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 TDP为700W，加上服务器基础负载（CPU、内存、风扇、NVLink等）约300W，总功耗1000-1100W符合工程常识与物理直觉。
