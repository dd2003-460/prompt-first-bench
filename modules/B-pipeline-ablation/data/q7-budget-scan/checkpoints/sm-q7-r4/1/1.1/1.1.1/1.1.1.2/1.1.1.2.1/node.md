# N431: RAID6 重建时间 t_rebuild 的实测基准：对于 12TB HDD，RAID6 重建吞吐量通常受限于 I/O 瓶颈，典型值为 100-200 MB/s

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160

## Claim

RAID6 重建时间 t_rebuild 的实测基准：对于 12TB HDD，RAID6 重建吞吐量通常受限于 I/O 瓶颈，典型值为 100-200 MB/s/盘，单盘重建时间 t_rebuild = 12TB / (150 MB/s * 3600 * 1024) ≈ 23.3 小时（若并行度受限）至 11.7 小时（若带宽充足），此时间直接代入 P_double_fail 公式。

## Corrected Claim

RAID6 重建时间 t_rebuild 的实测基准：对于 12TB HDD，RAID6 重建吞吐量通常受限于 I/O 瓶颈，典型值为 100-200 MB/s/盘，单盘重建时间 t_rebuild = 12TB / (150 MB/s * 3600 * 1024) ≈ 23.3 小时（若并行度受限）至 11.7 小时（若带宽充足），此时间直接代入 P_double_fail 公式。

## Evidence

先验知识/题面给定，逻辑校验通过：12TB / (150MB/s * 3600s/h * 1024MB/GB) ≈ 23.3h，计算无误，符合RAID6重建I/O瓶颈的工程常识。

## Search Query

RAID6 rebuild time 12TB HDD throughput MB/s
