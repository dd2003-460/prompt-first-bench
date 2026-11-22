# N94: Intel Gaudi 2/3 可行性评估：Gaudi 3 提供 96GB HBM2e 和 1.2 TB/s 带宽，但软件栈（Gaudi Toolkit）对 Q

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

Intel Gaudi 2/3 可行性评估：Gaudi 3 提供 96GB HBM2e 和 1.2 TB/s 带宽，但软件栈（Gaudi Toolkit）对 Qwen3 支持滞后，适配工时 >15 人天 [待核验: 最新支持状态]，且缺乏社区优化，性价比低于 NVIDIA 同价位方案，不推荐作为首选。

## Corrected Claim

Intel Gaudi 3 提供 96GB HBM 内存，软件栈对 Qwen3 的支持存在滞后，适配成本较高（具体工时视模型规模而定），且社区生态弱于 NVIDIA，性价比在多数场景下不占优，不推荐作为首选。

## Evidence

[质询]Gaudi 3 的 HBM 规格（96GB HBM2e）与公开资料（通常为 96GB HBM2e 或 HBM3，带宽约 1.6TB/s）存在细微出入，且“适配工时 >15 人天”属于高度依赖具体模型规模和团队经验的经验性估计，缺乏通用标准，易受主观偏差影响。 | 先验知识/题面给定，逻辑校验通过；但具体适配工时为经验事实，且无外部来源支持，故降级。

## Search Query

Intel Gaudi 3 Qwen3 support status inference performance
