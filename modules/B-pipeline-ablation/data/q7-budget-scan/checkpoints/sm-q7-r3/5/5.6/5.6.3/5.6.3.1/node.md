# N307: 云对象存储带宽出口费用计算中，公网出口单价为 $0.09/GB，该参数适用于 AWS S3 公网下行流量，若使用 VPC 内网或 PrivateLink，单价可

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

云对象存储带宽出口费用计算中，公网出口单价为 $0.09/GB，该参数适用于 AWS S3 公网下行流量，若使用 VPC 内网或 PrivateLink，单价可降低至 $0.01/GB 或 $0.005/GB。

## Corrected Claim

云对象存储（如AWS S3）公网出口流量通常按GB计费（例如us-east-1区域约为$0.09/GB），而通过VPC内网或PrivateLink访问时，数据传输费用通常显著降低或免除（具体取决于网络架构和计费项），但具体单价需参考最新官方定价表。

## Evidence

[质询]具体数值（$0.09/GB, $0.01/GB, $0.005/GB）属于经验事实，且AWS S3标准存储的公网出口单价通常约为$0.09/GB（us-east-1），但VPC内网流量通常免费或极低，PrivateLink费用结构复杂（包含端点费用和数据传输费），直接断言降低至特定固定值可能混淆了不同计费项或地域差异，且缺乏来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

AWS S3 data transfer out pricing per GB public internet 2024
