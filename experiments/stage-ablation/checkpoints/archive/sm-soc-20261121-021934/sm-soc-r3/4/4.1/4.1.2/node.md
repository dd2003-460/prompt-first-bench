# N38: 后验概率 P(H|D) 的更新规则中，似然比 LR = P(D|H)/P(D|¬H) 需通过A/B测试数据计算；具体地，D 定义为‘高挂价且短周期’事件，H 为

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N15

## Claim

后验概率 P(H|D) 的更新规则中，似然比 LR = P(D|H)/P(D|¬H) 需通过A/B测试数据计算；具体地，D 定义为‘高挂价且短周期’事件，H 为‘损失厌恶驱动假设’，LR 的初始估计值为 2.5，需通过至少 n=1000 次交易的A/B测试数据验证。

## Corrected Claim

后验概率 P(H|D) 的更新规则中，似然比 LR = P(D|H)/P(D|¬H) 需通过A/B测试数据计算；具体地，D 定义为‘高挂价且短周期’事件，H 为‘损失厌恶驱动假设’，LR 的初始估计值需通过A/B测试数据验证，样本量需满足统计功效要求。

## Evidence

[质询]LR=2.5 和 n=1000 是具体的经验参数/统计功效设定，无法从贝叶斯定理的第一性原理中推导出来，属于特定实验设计的选择而非通用数学事实。 | 来源[1]和[2]仅提供了贝叶斯推断的通用框架和公式，未包含针对‘损失厌恶’假设的具体似然比数值（2.5）或样本量要求（1000），属于经验事实缺来源支持。

## Search Query

Bayesian posterior update likelihood ratio high price short cycle A/B test secondhand

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/27398304&rut=a7af9b8f7f3ba5daff29910e4bddad7e37f7a34a80ba7f4b193174a32bc267ec', 'type': 'ddg', 'title': '贝叶斯推断如何更新后验概率？ - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/31882798076&rut=0ec16e72dcbebb2f417b5390b461fbc7c8fadc6b282678fc3bc7d2f74fe5a124', 'type': 'ddg', 'title': '第20章 概率模型学习 - 知乎 - 知乎专栏'}
