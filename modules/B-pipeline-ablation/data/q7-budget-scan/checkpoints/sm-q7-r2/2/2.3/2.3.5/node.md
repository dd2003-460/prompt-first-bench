# N70: S3 Intelligent-Tiering 的监控费（Monitoring Fee）：$0.0025/GB/月，需从总存储成本中扣除或单独列出；对于 500T

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

S3 Intelligent-Tiering 的监控费（Monitoring Fee）：$0.0025/GB/月，需从总存储成本中扣除或单独列出；对于 500TB 数据，监控费 ≈ $0.0025 * 500,000 * 12 * 7.2 ≈ ¥10,800/年，占 Intelligent-Tiering 存储费的 ~6%。

## Corrected Claim

S3 Intelligent-Tiering 的监控费为 $0.0025/GB/月。对于 500TB 数据，年监控费约为 $15,000（$0.0025 * 500,000 GB * 12 个月）。

## Evidence

[质询]计算逻辑存在严重错误：公式中同时乘以 12（月）和 7.2（疑似汇率或系数），导致量级错误。若 7.2 为汇率，则不应再乘以 12 后直接得出人民币年费而不明确单位转换逻辑；若 7.2 为其他系数，则缺乏依据。此外，$0.0025/GB/月 是 AWS 官方标准监控费，但 500TB 的监控费计算应为 $0.0025 * 500,000 GB * 12 个月 = $15,000/年，而非通过乘以 7.2 得到 ¥10,800。 | 来源 [1] 确认存在监控费，但未提供具体数值；来源 [2] 和 [3] 未涉及费用细节。计算逻辑自相矛盾（同时使用月费、年费和汇率系数），且与 AWS 标准定价逻辑不符。

## Search Query

AWS S3 Intelligent-Tiering monitoring fee per GB month

## Retrieval Sources

- {'url': 'https://aws.amazon.com/s3/storage-classes/intelligent-tiering/&rut=b1facab1d2a9de1c1bcf75b28167229732a9eb70ef441587f8d64eba00acaf24', 'type': 'ddg', 'title': 'Amazon S3 Intelligent-Tiering Storage Class | AWS'}
- {'url': 'https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/intelligent-tiering.html&rut=3e22e3c828a6fbbe3ccd298a3b6fd5702bc5d8089fee2b4f331841796a878e81', 'type': 'ddg', 'title': '使用 Amazon S3 Intelligent-Tiering 管理存储成本'}
- {'url': 'https://aws.amazon.com/cn/s3/storage-classes/intelligent-tiering/&rut=805def3f547221ff81315cf8da5561fff630d864eb9f0198cd25280a39a725d6', 'type': 'ddg', 'title': 'Amazon S3 Intelligent-Tiering 存储类 | AWS'}
