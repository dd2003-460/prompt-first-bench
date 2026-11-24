# N726: 小文件场景下RAID-6元数据开销量化：当块大小<4KB时，每次I/O需读取/更新额外的P/Q块元数据，假设元数据占比为10%，则有效吞吐量 T_eff = T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N254

## Claim

小文件场景下RAID-6元数据开销量化：当块大小<4KB时，每次I/O需读取/更新额外的P/Q块元数据，假设元数据占比为10%，则有效吞吐量 T_eff = T_raw / 1.1，导致I/O时间增加约11%，叠加随机寻址延迟。

## Corrected Claim

小文件场景下RAID-6元数据开销量化：当块大小<4KB时，每次I/O需读取/更新额外的P/Q块元数据，假设元数据占比为10%，则有效吞吐量 T_eff = T_raw / 1.1，导致I/O时间增加约11%，叠加随机寻址延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：T_eff = T_raw / (1 + overhead) 的数学关系正确，10% 开销对应 1/1.1 ≈ 0.909 的吞吐率，即时间增加约 11%，符合 RAID-6 双校验（P/Q）在小块 I/O 下的元数据开销量化逻辑。

## Search Query

RAID-6 metadata overhead small file random I/O throughput penalty
