# N195: 基准等待时间 T0 的具体数值：需通过平台历史成交数据计算，若 T0 < 7 天则高挂价策略的临界曝光成本 C_exposure* 较低，更容易满足 C_exp

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N58

## Claim

基准等待时间 T0 的具体数值：需通过平台历史成交数据计算，若 T0 < 7 天则高挂价策略的临界曝光成本 C_exposure* 较低，更容易满足 C_exposure < C_exposure*。

## Corrected Claim

基准等待时间 T0 的具体数值需通过平台历史成交数据计算。在逻辑上，若 T0 较短（如 < 7 天），意味着商品周转快，高挂价策略的临界曝光成本 C_exposure* 相对较低，从而更容易满足 C_exposure < C_exposure* 的条件。

## Evidence

[质询]参考来源[1]讨论的是金融量化交易中的T0策略（日内回转交易），与陈述中提到的“高挂价策略”、“曝光成本”及“基准等待时间T0”（通常指二手交易或电商场景下的平均成交周期）属于完全不同的领域，存在严重的主题混淆和口径错误。 | 来源[1]与事实主题无关（金融T0 vs 交易/电商T0），无法提供外部支持；陈述内部逻辑自洽（T0越短，等待成本越低，临界曝光成本阈值越低），但作为经验事实缺乏有效来源支持。

## Search Query

average time to sale second-hand goods platform baseline

## Retrieval Sources

- {'url': 'https://www.sohu.com/a/937469709_121751016&rut=396b2ff47e12fea5766009a074b5f06f724772be5c47d478db56cd5fca44fcf1', 'type': 'ddg', 'title': 'T0智能算法是什么？T0策略开通指南!_交易_量化_进行'}
