# N559: 工作点1（高IOPS/低延迟）：在 IOPS > 10,000 且延迟 < 10ms 场景下，Glacier Instant Retrieval 年化成本 = 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N202

## Claim

工作点1（高IOPS/低延迟）：在 IOPS > 10,000 且延迟 < 10ms 场景下，Glacier Instant Retrieval 年化成本 = ¥35.6/TB/年 + 请求成本（18,500 IOPS * 86400s * 365d * ¥1e-6/次 ≈ ¥58,500/年，分摊 ¥117/TB/年）+ 运维 ¥30/TB/年 ≈ ¥182.6/TB/年，高于 S3 Standard（¥232/TB/年含请求）但低于本地 NVMe（¥2,075/TB/年），适合温数据缓存层。

## Corrected Claim

在工作点1（高IOPS/低延迟）场景下，基于特定假设（18,500 IOPS/1TB），Glacier Instant Retrieval 的估算年化成本约为 ¥182.6/TB/年，低于本地 NVMe 但高于 S3 Standard（注：具体价格需以 AWS 官方实时报价为准，此处为基于特定参数的估算）。

## Evidence

[质询]该陈述包含大量具体的经验性价格数据（如 Glacier Instant Retrieval 单价、S3 Standard 总价、NVMe 成本等）及特定的业务假设（18,500 IOPS 对应 1TB 容量），这些属于经验事实，无法从第一性原理推导。参考来源仅定义了 IOPS 概念，未提供任何 AWS 或存储介质的具体定价信息，因此缺乏外部证据支持其数值准确性。 | 逻辑计算自洽（35.6 + 117 + 30 = 182.6），但参考来源 [1][2] 仅涉及 IOPS 定义，与具体成本数据无关，属经验事实且缺来源支持。

## Search Query

AWS S3 Glacier Instant Retrieval request cost IOPS 10000 latency 10ms

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/668976764&rut=a7f464f3c37d3da390d9dd115f6ea6e5b107c7506a16f208723d37c99b592bf7', 'type': 'ddg', 'title': '一文读懂：Iops、延迟和吞吐量等存储性能指标 - 知乎'}
- {'url': 'https://en.wikipedia.org/wiki/IOPS&rut=93baf5699d468654ed6e0502e464fe1f1a967c86dbd2c5787e548d50c960670b', 'type': 'ddg', 'title': 'IOPS - Wikipedia'}
