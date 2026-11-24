# N274: HDD 集群功耗 P_HDD_cluster 修正：基于 N131 的 4.675W/盘，若使用 16TB 盘，400TB 冷数据需 25 块盘（RAID6 冗

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

HDD 集群功耗 P_HDD_cluster 修正：基于 N131 的 4.675W/盘，若使用 16TB 盘，400TB 冷数据需 25 块盘（RAID6 冗余后），P_HDD_cluster = 25 * 4.675W ≈ 117W。注意：N130 原公式未考虑 RAID 冗余导致的物理盘数增加

## Corrected Claim

HDD 集群功耗 P_HDD_cluster 修正：基于 N131 的 4.675W/盘，若使用 16TB 盘，400TB 冷数据需 25 块盘（RAID6 冗余后），P_HDD_cluster = 25 * 4.675W ≈ 117W。注意：N130 原公式未考虑 RAID 冗余导致的物理盘数增加

## Evidence

先验知识/题面给定，逻辑校验通过：400TB/16TB=25块盘，25*4.675W≈116.875W≈117W，计算无误且符合HDD功耗常识。

## Search Query

hdd cluster power consumption raid6 redundancy overhead
