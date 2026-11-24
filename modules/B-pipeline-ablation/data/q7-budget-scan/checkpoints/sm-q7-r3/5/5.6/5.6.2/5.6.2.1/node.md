# N302: 云对象存储请求费用计算中，LIST 请求单价为 $0.005/1,000 requests，该参数适用于 AWS S3 标准存储层，且 LIST 费用仅针对返回

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

云对象存储请求费用计算中，LIST 请求单价为 $0.005/1,000 requests，该参数适用于 AWS S3 标准存储层，且 LIST 费用仅针对返回的对象键数量计费，不随对象大小变化。

## Corrected Claim

云对象存储请求费用计算中，LIST 请求单价因存储层而异。例如，AWS S3 Standard-IA 存储层的 LIST 请求单价约为 $0.005/1,000 requests，而 Standard 存储层约为 $0.0004/1,000 requests。LIST 费用仅针对请求次数计费，不随对象大小变化。

## Evidence

[质询]数值量级与口径混淆：AWS S3 标准存储层（Standard）的 LIST 请求单价通常为 $0.0004/1,000 requests，而 $0.005/1,000 requests 是 S3 Standard-IA（低频访问）或 One Zone-IA 等存储层的典型价格。陈述将非标准存储层的价格错误地归因于标准存储层。 | 经验事实，逻辑自洽但缺来源支持；且该具体数值与 AWS S3 标准存储层的公开定价常识存在显著偏差（Standard 层 LIST 价格远低于 $0.005/1k），无法排除价格层级混淆的可能性。

## Search Query

AWS S3 LIST request pricing per 1000 requests 2024
