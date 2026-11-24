# N251: NVMe RAID-6重建速率的实测工作点3（高成本低性）：使用Micron 9300 PRO NVMe SSD（顺序写6.0GB/s），RAID控制器为Ada

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

NVMe RAID-6重建速率的实测工作点3（高成本低性）：使用Micron 9300 PRO NVMe SSD（顺序写6.0GB/s），RAID控制器为Adaptec 7265-16i（5.0GB/s），实测Rebuild_Rate=4.8GB/s=172.8GB/h；重建1.92TB耗时=1.92TB/172.8GB/h≈11.1小时，但SSD单价高出40%，CapEx增加¥38,400/TB，仅适用于对RTO有严格要求的场景

## Corrected Claim

基于Micron 9300 PRO NVMe SSD（顺序写6.0GB/s）与Adaptec 7265-16i控制器（5.0GB/s）的配置，理论重建速率上限约为5.0GB/s，实测可能略低（如4.8GB/s），重建1.92TB耗时约11小时以上；由于缺乏具体价格来源，CapEx增加¥38,400/TB及单价高出40%的具体数值需进一步核实，但高成本高性能SSD用于严格RTO场景的逻辑成立。

## Evidence

[质询]参考来源仅提供了测试报告的标题和引言，未包含具体的实测数据（如Micron 9300 PRO的具体重建速率、Adaptec 7265-16i的瓶颈数据、具体的CapEx成本计算及价格差异），无法验证这些具体数值是否真实存在于该报告中或符合行业常识。 | 逻辑上重建速率受限于控制器带宽（5.0GB/s）略低于SSD写入速度（6.0GB/s）是合理的，耗时计算（1.92TB/172.8GB/h ≈ 11.1h）数学正确；但来源[1]仅显示报告标题，未提供具体数据支持，属于经验事实且缺乏直接来源佐证。

## Search Query

Micron 9300 PRO NVMe RAID-6 rebuild rate Adaptec 7265-16i high performance

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/721396458&rut=6840234b243512f61ddcb52b3751f0a66d74941fd85aacfd80a9e371781e3e0d', 'type': 'ddg', 'title': 'ODCC NVMe SSD RAID 性能测试技术报告 (附批注) - 知乎'}
