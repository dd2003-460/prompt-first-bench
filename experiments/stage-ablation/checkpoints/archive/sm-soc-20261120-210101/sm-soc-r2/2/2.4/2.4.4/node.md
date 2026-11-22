# N58: 平台偏离均衡的边际收益：dU_platform/dW = ΔGMV * Commission_Rate - C_computation(W)。在均衡权重 W* 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N13

## Claim

平台偏离均衡的边际收益：dU_platform/dW = ΔGMV * Commission_Rate - C_computation(W)。在均衡权重 W* 处，若 dU_platform/dW < 0，则平台单方面调整曝光权重（如过度抑制高挂价）会导致效用下降，因为 GMV 的损失超过了算法优化带来的边际收益。

## Corrected Claim

平台偏离均衡的边际收益：dU_platform/dW = ΔGMV * Commission_Rate - C_computation(W)。在均衡权重 W* 处，若 dU_platform/dW < 0，则平台单方面调整曝光权重（如过度抑制高挂价）会导致效用下降，因为 GMV 的损失超过了算法优化带来的边际收益。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述基于平台效用函数的标准定义（GMV收益减去计算成本），在均衡点处若边际收益为负，则偏离均衡确实会导致效用下降，符合经济学基本原理。
