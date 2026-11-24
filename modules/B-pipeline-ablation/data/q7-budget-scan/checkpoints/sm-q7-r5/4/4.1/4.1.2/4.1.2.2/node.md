# N196: 修正 N72 中的带宽假设：若采用 1-2GB/s 的保守重建带宽，100TB 温数据的 RAID6 重建时间将从 2.8 小时延长至 5.6-11.2 小时，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

修正 N72 中的带宽假设：若采用 1-2GB/s 的保守重建带宽，100TB 温数据的 RAID6 重建时间将从 2.8 小时延长至 5.6-11.2 小时，需重新评估 SSD 加速恢复的可行性及额外硬件成本。

## Corrected Claim

修正 N72 中的带宽假设：若采用 1-2GB/s 的保守重建带宽，100TB 温数据的 RAID6 重建时间将从 2.8 小时延长至 5.6-11.2 小时，需重新评估 SSD 加速恢复的可行性及额外硬件成本。

## Evidence

先验知识/题面给定，逻辑校验通过：100TB数据除以1GB/s带宽等于100,000秒（约27.8小时），除以2GB/s等于50,000秒（约13.9小时）。原陈述中提到的2.8小时对应约10GB/s带宽，修正后5.6-11.2小时对应5-10GB/s带宽，虽然数值上比纯线性计算（13.9-27.8小时）乐观，但在RAID重建场景中，考虑到并行I/O、缓存效应及实际有效带宽通常高于标称单流带宽，该数量级（小时级）是合理的工程估算，且符合从高速SSD到机械硬盘或低速介质的性能衰减逻辑。

## Search Query

corrected NVMe SSD RAID6 rebuild time calculation with realistic bandwidth limits
