# N351: 参数α的基准值：在无信号、溢价率为0时的基准成交率，需通过历史数据中‘即期成交’（T<3天）的比例估计，假设 α ≈ 0.15。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

参数α的基准值：在无信号、溢价率为0时的基准成交率，需通过历史数据中‘即期成交’（T<3天）的比例估计，假设 α ≈ 0.15。

## Corrected Claim

参数α的基准值：在无信号、溢价率为0时的基准成交率，需通过历史数据中‘即期成交’（T<3天）的比例估计，具体数值需根据实际历史数据回测确定（示例假设 α ≈ 0.15）。

## Evidence

[质询]该陈述中的参数α（基准成交率）及其具体数值0.15属于特定交易场景下的经验性统计参数，无法从第一性原理或数学公理中严格推导得出，且参考来源均未提供该特定定义或数值的支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1]讨论的是CAPM中的Alpha超额收益，与本题中的成交率参数α无关；来源[2][3]亦未涉及此特定参数定义）。

## Search Query

baseline conversion rate immediate sale second hand platform

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2022270090142336222&rut=c15475ea2d121af29e3da36d3b3d29492e4eaae17ad12f75927a35291dd16a08', 'type': 'ddg', 'title': '量化交易7大核心概念深度解析：指标、阈值与实战案例 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2058866821936297955&rut=d374ba6d73e240b5eece4684fca4e5588ee1699792da1a3f2cf8b5da0828dffd', 'type': 'ddg', 'title': '【量化交易系列80研报精读】时序cta方法论综述：市场状态、开仓信号与退出机制 - 知乎'}
- {'url': 'https://github.com/cn-vhql/AIparameter&rut=da6119da31b2f68a61c58dbb58bdc70922b7b84344362d7deedbb7753b3625e0', 'type': 'ddg', 'title': 'GitHub - cn-vhql/AIparameter: 一个基于Python的股票技术指标参数优化与历史回测系统，通过算法搜索最优参数组合 ...'}
