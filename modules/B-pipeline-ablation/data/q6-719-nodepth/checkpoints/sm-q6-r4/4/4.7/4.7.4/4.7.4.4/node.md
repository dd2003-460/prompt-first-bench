# N415: 跨网惩罚项 ΔT_cross 的具体量化：当 POP 接入运营商与源站出口运营商不一致时，ΔT_cross = 15ms (基础跨网延迟) + 5ms (路由抖

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

跨网惩罚项 ΔT_cross 的具体量化：当 POP 接入运营商与源站出口运营商不一致时，ΔT_cross = 15ms (基础跨网延迟) + 5ms (路由抖动 P99 增量) = 20ms；若部署 BGP 多线，ΔT_cross 降至 5ms，但带宽成本增加 30%。

## Corrected Claim

跨网惩罚项 ΔT_cross 通常由基础跨网延迟和路由抖动组成，具体数值取决于运营商间互联质量；部署 BGP 多线可显著降低跨网延迟（通常降至个位数毫秒级），但会增加带宽采购成本。

## Evidence

[质询]具体数值（15ms, 5ms, 20ms, 30%）属于高度依赖具体网络拓扑、运营商策略及BGP配置的经验参数，缺乏通用性，不同场景下差异巨大，无法作为固定常量。 | source=knowledge，逻辑自洽（加法运算正确，BGP多线降低延迟但增加成本的逻辑符合网络工程常识），但具体数值为经验事实，无来源支持，依据经验事实排除条款降级。
