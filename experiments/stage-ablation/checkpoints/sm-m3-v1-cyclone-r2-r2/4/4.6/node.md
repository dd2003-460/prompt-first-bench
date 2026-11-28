# N22: 模型参数化争议：不同数值模式（如HWRF、HMON）对摩擦系数和潜热参数化的处理差异，导致预测衰减速率偏差达30%-50%。

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

模型参数化争议：不同数值模式（如HWRF、HMON）对摩擦系数和潜热参数化的处理差异，导致预测衰减速率偏差达30%-50%。

## Corrected Claim

不同数值模式（如HWRF、HMON）对摩擦系数和潜热参数化的处理差异，会导致预测衰减速率出现显著偏差（具体幅度依模型配置和研究场景而异）。

## Evidence

[质询]具体数值范围（30%-50%）缺乏通用性，不同研究、不同气候区域及不同模型版本间的偏差幅度差异极大，该特定区间可能仅适用于特定文献或特定实验设置，存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过；但作为经验事实，具体偏差幅度（30%-50%）缺乏普适性来源支持，故降级为定性表述。

## Search Query

tropical cyclone model parameterization friction coefficient latent heat HWRF HMON decay rate uncertainty
