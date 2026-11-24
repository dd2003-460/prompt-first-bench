# N671: RAID-5 重建高风险窗口时长 T_rebuild 的可计算表达式：T_rebuild = (V_usable / (N-1)) / T_rebuild_bw

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N232

## Claim

RAID-5 重建高风险窗口时长 T_rebuild 的可计算表达式：T_rebuild = (V_usable / (N-1)) / T_rebuild_bw，其中 V_usable=500TB*(N-1)/N, T_rebuild_bw 受限于最慢盘写入速度（典型企业级SSD ~1GB/s，HDD ~150MB/s），需区分SSD阵列与HDD阵列的具体带宽值。

## Corrected Claim

RAID-5 重建高风险窗口时长 T_rebuild 的可计算表达式：T_rebuild = (V_usable / (N-1)) / T_rebuild_bw，其中 V_usable=500TB*(N-1)/N, T_rebuild_bw 受限于最慢盘写入速度（典型企业级SSD ~1GB/s，HDD ~150MB/s），需区分SSD阵列与HDD阵列的具体带宽值。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-5重建需读取N-1个数据盘并写入1个校验盘，总数据量为可用容量，瓶颈通常在于最慢盘的写入带宽，公式推导符合存储系统基本原理。
