# N515: 冷数据扫描的HDD机械瓶颈量化：400TB冷数据分布在不连续的HDD扇区，寻道时间占主导。假设平均寻道时间5ms，每次读取块大小1MB，IOPS上限 = 1/0

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N170, N171, N172

## Claim

冷数据扫描的HDD机械瓶颈量化：400TB冷数据分布在不连续的HDD扇区，寻道时间占主导。假设平均寻道时间5ms，每次读取块大小1MB，IOPS上限 = 1/0.005 = 200 IOPS/盘；25块盘聚合IOPS = 5000；若数据随机分布，实际吞吐 = 5000 * 1MB = 5GB/s，但受限于机械旋转延迟，有效吞吐降至2.5GB/s（50%效率因子）。

## Corrected Claim

冷数据扫描的HDD机械瓶颈量化：400TB冷数据分布在不连续的HDD扇区，寻道时间占主导。假设平均寻道时间5ms，每次读取块大小1MB，IOPS上限 = 1/0.005 = 200 IOPS/盘；25块盘聚合IOPS = 5000；若数据随机分布，实际吞吐 = 5000 * 1MB = 5GB/s，但受限于机械旋转延迟，有效吞吐降至2.5GB/s（50%效率因子）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术推导正确（1/0.005=200, 200*25=5000, 5000*1MB=5GB/s, 5GB/s*50%=2.5GB/s），量级符合HDD机械瓶颈常识。

## Search Query

enterprise HDD random read IOPS seek time 5ms throughput calculation
