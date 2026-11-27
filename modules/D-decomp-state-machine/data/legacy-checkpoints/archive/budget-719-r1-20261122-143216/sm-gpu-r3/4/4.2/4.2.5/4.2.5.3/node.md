# N290: Qwen3-27B FP8 与 BF16 在指定测试集上的 KL 散度实测均值（Mean KL）及标准差（Std KL），需从社区量化评估报告或自行运行评估脚本

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

Qwen3-27B FP8 与 BF16 在指定测试集上的 KL 散度实测均值（Mean KL）及标准差（Std KL），需从社区量化评估报告或自行运行评估脚本获取，预期 Mean KL < 0.05 nats/token

## Corrected Claim

Qwen3-27B FP8 与 BF16 在指定测试集上的 KL 散度实测均值（Mean KL）及标准差（Std KL）需从社区量化评估报告或自行运行评估脚本获取，通常预期 Mean KL 处于较低水平（如 < 0.05 nats/token），具体数值取决于测试集分布。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（Mean KL < 0.05 nats/token），属于特定模型（Qwen3-27B）在特定量化方案（FP8）下的实测性能指标，无法从第一性原理或数学公理中严格推导得出，且缺乏具体的测试集定义和基准数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为具体模型的经验参数，不适用第一性原理推导条款）

## Search Query

Qwen3-27B FP8 vs BF16 KL divergence evaluation
