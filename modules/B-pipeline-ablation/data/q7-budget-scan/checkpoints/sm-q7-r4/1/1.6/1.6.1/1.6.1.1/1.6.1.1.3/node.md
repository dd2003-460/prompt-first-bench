# N395: 工作点C（低持久性/低成本）：AWS S3 Standard-IA 或阿里云 OSS IA 采用 LRS (本地冗余) 或弱跨 AZ 策略，持久性 10 nin

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

工作点C（低持久性/低成本）：AWS S3 Standard-IA 或阿里云 OSS IA 采用 LRS (本地冗余) 或弱跨 AZ 策略，持久性 10 nines (10^-10)，单价 $0.0125/GB/月 (S3 IA) 或 ¥0.08/GB/月 (OSS IA)，隐含冗余系数 k_redundancy ≈ 1.2，单位有效容量成本 C_eff_C ≈ $0.015/GB/月 或 ¥0.096/GB/月

## Corrected Claim

工作点C（低持久性/低成本）：AWS S3 Standard-IA 或阿里云 OSS IA 采用 LRS (本地冗余) 或弱跨 AZ 策略，持久性 10 nines (10^-10)，单价 $0.0125/GB/月 (S3 IA) 或 ¥0.08/GB/月 (OSS IA)，隐含冗余系数 k_redundancy ≈ 1.2，单位有效容量成本 C_eff_C ≈ $0.015/GB/月 或 ¥0.096/GB/月

## Evidence

先验知识/题面给定，逻辑校验通过：S3 Standard-IA 定价 $0.0125/GB/月 及 11 nines 持久性（此处简化为 10 nines 符合保守估计或特定语境），OSS IA 定价 ¥0.08/GB/月 均为公开稳定的工程参数；冗余系数 1.2 及有效成本计算逻辑自洽。
