# N445: 寻道时间对RAID6重建吞吐的影响公式：$T_{rebuild} = \frac{C_{data}}{B_{eff}}$，其中 $B_{eff} = \frac

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N198

## Claim

寻道时间对RAID6重建吞吐的影响公式：$T_{rebuild} = \frac{C_{data}}{B_{eff}}$，其中 $B_{eff} = \frac{B_{seq}}{1 + (T_{seek} \times IOPS_{rebuild})}$，对于400TB数据量，若 $T_{seek}=8ms$，$IOPS_{rebuild}$ 受限于控制器队列深度（通常QD=32），导致实际带宽较标称值下降约15%

## Corrected Claim

寻道时间对RAID6重建吞吐的影响公式：$T_{rebuild} = \frac{C_{data}}{B_{eff}}$，其中 $B_{eff} = \frac{B_{seq}}{1 + (T_{seek} \times IOPS_{rebuild})}$，对于400TB数据量，若 $T_{seek}=8ms$，$IOPS_{rebuild}$ 受限于控制器队列深度（通常QD=32），导致实际带宽较标称值下降约15%
