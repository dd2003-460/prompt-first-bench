# N119: 紧迫系数 $\gamma_{urgency}$ 的量化定义：$\gamma_{urgency} = \frac{\sigma_{FOMO} - \sigma_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

紧迫系数 $\gamma_{urgency}$ 的量化定义：$\gamma_{urgency} = \frac{\sigma_{FOMO} - \sigma_{calm}}{\sigma_{calm}}$，其中 $\sigma_{FOMO}$ 为高紧迫场景（如限时秒杀、库存仅剩 1 件）下买家估值偏差的标准差，$\sigma_{calm}$ 为常态场景下的标准差；若 FOMO 场景下偏差标准差放大 50%，则 $\gamma_{urgency} = 0.5$。

## Corrected Claim

紧迫系数 $\gamma_{urgency}$ 的量化定义：$\gamma_{urgency} = \frac{\sigma_{FOMO} - \sigma_{calm}}{\sigma_{calm}}$，其中 $\sigma_{FOMO}$ 为高紧迫场景（如限时秒杀、库存仅剩 1 件）下买家估值偏差的标准差，$\sigma_{calm}$ 为常态场景下的标准差；若 FOMO 场景下偏差标准差放大 50%，则 $\gamma_{urgency} = 0.5$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，数值推导（(1.5-1)/1=0.5）正确，量纲一致（无量纲比值）。
