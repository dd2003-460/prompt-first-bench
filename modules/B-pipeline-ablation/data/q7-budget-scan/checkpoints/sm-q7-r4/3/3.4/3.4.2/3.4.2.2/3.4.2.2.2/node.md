# N648: S3 Lifecycle Rules 清理旧版本的成本：虽然旧版本占用存储空间，但可通过 Lifecycle Rule 自动删除非当前版本（Noncurrent

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N224

## Claim

S3 Lifecycle Rules 清理旧版本的成本：虽然旧版本占用存储空间，但可通过 Lifecycle Rule 自动删除非当前版本（NoncurrentVersionExpiration）；配置规则后，仅保留最近 N 个版本或 M 天内的版本，可将额外存储成本控制在预期范围内，但规则评估本身不产生费用，仅删除操作产生 DELETE 请求费用（$0.01/1k）。

## Corrected Claim

S3 Lifecycle Rules 清理旧版本的成本：虽然旧版本占用存储空间，但可通过 Lifecycle Rule 自动删除非当前版本（NoncurrentVersionExpiration）；配置规则后，仅保留最近 N 个版本或 M 天内的版本，可将额外存储成本控制在预期范围内，但规则评估本身不产生费用，仅删除操作产生 DELETE 请求费用（$0.01/1k）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

S3 lifecycle rule noncurrent version expiration cost
