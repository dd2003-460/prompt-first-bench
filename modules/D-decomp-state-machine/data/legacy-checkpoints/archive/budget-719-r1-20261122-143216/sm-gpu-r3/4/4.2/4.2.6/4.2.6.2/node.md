# N293: Qwen3-27B NVFP4/W4 与 BF16 在指定测试集上的 KL 散度实测均值（Mean KL）及 95 分位数（P95 KL），需从社区量化评估报告

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103

## Claim

Qwen3-27B NVFP4/W4 与 BF16 在指定测试集上的 KL 散度实测均值（Mean KL）及 95 分位数（P95 KL），需从社区量化评估报告获取，预期 Mean KL 在 0.05-0.15 nats/token 之间，P95 KL 可能显著更高

## Corrected Claim

Qwen3-27B NVFP4/W4 与 BF16 在指定测试集上的 KL 散度实测均值（Mean KL）及 95 分位数（P95 KL）需从社区量化评估报告获取，具体数值范围待验证。

## Evidence

[质询]该陈述包含具体的经验数值范围（Mean KL 0.05-0.15 nats/token），属于特定模型在特定量化方案下的实测数据，无法从第一性原理推导，且当前无可用来源支持该具体数值区间。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据验证具体数值范围）

## Search Query

Qwen3-27B NVFP4 W4 KL divergence evaluation
