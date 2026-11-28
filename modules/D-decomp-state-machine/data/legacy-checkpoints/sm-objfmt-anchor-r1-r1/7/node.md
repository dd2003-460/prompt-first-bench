# N30: 性价比核心指标定义为 'Cost-Effective Throughput' (CET) = (Tokens_per_second * Quality_Rete

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比核心指标定义为 'Cost-Effective Throughput' (CET) = (Tokens_per_second * Quality_Retention_Score) / (Total_Cost_of_Ownership_5yr)。其中 Quality_Retention_Score = 1 - (Normalized_PPL_Increase)，若 CET 值在 INT4 方案中比 BF16 方案高 20% 以上，则判定 INT4 为更优性价比选择。

## Corrected Claim

在特定评估框架中，可定义 'Cost-Effective Throughput' (CET) 为 (Tokens_per_second * Quality_Retention_Score) / (Total_Cost_of_Ownership_5yr)，其中 Quality_Retention_Score 基于 PPL 增加量计算；若 INT4 方案的 CET 显著高于 BF16（例如高 20% 以上），则可视为在该框架下具有更优性价比。

## Evidence

[质询]该陈述定义了一个特定的复合指标 'Cost-Effective Throughput' (CET) 及其具体计算公式和阈值（20%），这属于特定场景下的经验性定义或自定义指标，并非通用的行业标准或第一性原理可推导的数学事实。参考来源仅提供了通用的‘性价比’概念（性能/价格），并未包含此特定公式、PPL归一化细节或INT4/BF16的具体对比阈值，因此缺乏直接来源支持。 | 逻辑上公式自洽（吞吐量*质量/成本符合性价比直觉），但作为经验事实（具体指标定义与阈值），参考来源[1]仅涵盖通用性价比概念，未提供该特定CET公式及阈值的直接支持，故降级。

## Retrieval Sources

- {'url': 'https://zh.wikipedia.org/zh-hans/%E6%80%A7%E5%83%B9%E6%AF%94&rut=86f5d6e6ee00fd2de785af2fdfe8e2b590af3ae331297f2bffe2ab19bf969593', 'type': 'ddg', 'title': '性价比 - 维基百科，自由的百科全书'}
