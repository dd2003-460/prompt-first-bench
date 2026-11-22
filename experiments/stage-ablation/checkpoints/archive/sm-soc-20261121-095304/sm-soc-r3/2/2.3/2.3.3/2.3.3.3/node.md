# N125: 触发风控的单价降幅阈值 θ_drop 通常设定为 10% 或 15%；当单次降价幅度 ΔP > θ_drop 时，即使次数未超 N_max，也可能因‘异常低价’

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

触发风控的单价降幅阈值 θ_drop 通常设定为 10% 或 15%；当单次降价幅度 ΔP > θ_drop 时，即使次数未超 N_max，也可能因‘异常低价’触发搜索降权或人工审核。

## Corrected Claim

在电商搜索风控中，触发风控的单价降幅阈值 θ_drop 通常设定在 10% 至 15% 区间；当单次降价幅度 ΔP 超过该阈值时，可能因‘异常低价’触发搜索降权或人工审核。

## Evidence

[质询]来源主题不匹配：参考来源[1]讨论的是金融合约交易（Mark Price等）的风控，而事实节点讨论的是电商/搜索场景下的价格风控（搜索降权、人工审核），两者领域完全不同，无法提供有效支持。 | 逻辑自洽，但参考来源[1]与电商搜索风控主题无关，属于经验事实且缺乏直接来源支持。

## Search Query

platform price drop threshold 10% OR 15% search weight penalty risk control

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1889825170887262711&rut=ecd186629449f36b13923cec56241bacc553f5fef8f5f4791ec246eebd03692d', 'type': 'ddg', 'title': '合约交易的风控规则 - 知乎 - 知乎专栏'}
