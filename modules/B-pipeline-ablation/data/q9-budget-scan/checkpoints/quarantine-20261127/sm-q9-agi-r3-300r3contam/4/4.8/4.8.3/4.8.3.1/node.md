# N229: Bootstrap 重抽样实现细节：从 100 个样本中有放回地随机抽取 100 个样本组成一个重抽样集，计算该集的 H_domain*，重复此过程 10,00

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

Bootstrap 重抽样实现细节：从 100 个样本中有放回地随机抽取 100 个样本组成一个重抽样集，计算该集的 H_domain*，重复此过程 10,000 次得到 H_domain* 的分布，CI_lower 为该分布的第 2.5 百分位数，CI_upper 为第 97.5 百分位数。

## Corrected Claim

Bootstrap 重抽样实现细节：从 100 个样本中有放回地随机抽取 100 个样本组成一个重抽样集，计算该集的 H_domain*，重复此过程 10,000 次得到 H_domain* 的分布，CI_lower 为该分布的第 2.5 百分位数，CI_upper 为第 97.5 百分位数。

## Evidence

先验知识/题面给定，逻辑校验通过：Bootstrap 重抽样的标准定义即为有放回抽样并重复多次以构建置信区间，通常取 2.5% 和 97.5% 分位数作为 95% CI 边界，描述符合统计学标准实践。
