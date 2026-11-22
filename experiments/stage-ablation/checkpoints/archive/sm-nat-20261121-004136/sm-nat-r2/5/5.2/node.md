# N20: 需查证部分：具体参数如 Pareto 分布的截断值 s_min/s_max、对象大小与热度的联合分布协方差结构（ρ=-0.3 的精确含义）、实际 CDN 节点中

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

需查证部分：具体参数如 Pareto 分布的截断值 s_min/s_max、对象大小与热度的联合分布协方差结构（ρ=-0.3 的精确含义）、实际 CDN 节点中 LRU/LFU 的实测命中率差异数据，这些需查阅特定文献或实验数据。

## Corrected Claim

Pareto分布截断值、对象大小与热度的协方差结构（如ρ值）以及LRU/LFU命中率差异均为特定实验环境下的经验参数，无通用固定值，需依据具体数据集和文献单独查证。

## Evidence

[质询]该陈述本身是一个关于“需查证”的元陈述，而非具体事实断言。其潜在错误在于暗示这些参数（如ρ=-0.3）是普遍存在的固定值，而实际上它们高度依赖于具体的数据集、时间窗口和CDN架构，不存在通用的“精确含义”或“实测差异数据”标准值。 | 无可用外部证据。该节点为经验事实相关的查证需求描述，逻辑自洽（指出需要查阅特定文献），但缺乏来源支持其具体参数（如ρ=-0.3）的普遍有效性，故降级。

## Search Query

CDN LRU LFU hit rate Pareto distribution object size update rate measurement study
