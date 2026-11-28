# N209: 在资源受限的本地推理环境下，若单次实验生成高质量数据点的成本高（如每次运行耗时 >10 分钟），应采用序贯检验（Sequential Testing）或贝叶斯 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

在资源受限的本地推理环境下，若单次实验生成高质量数据点的成本高（如每次运行耗时 >10 分钟），应采用序贯检验（Sequential Testing）或贝叶斯 A/B 测试方法，其平均所需样本量 ASN 可比固定样本量设计减少 20%-40%，同时保持相同的 Type I/II 错误率。

## Corrected Claim

在资源受限的本地推理环境下，若单次实验生成高质量数据点的成本高（如每次运行耗时 >10 分钟），应采用序贯检验（Sequential Testing）或贝叶斯 A/B 测试方法，其平均所需样本量 ASN 可比固定样本量设计减少 20%-40%，同时保持相同的 Type I/II 错误率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sequential testing sample size reduction Bayesian A/B test average sample number
