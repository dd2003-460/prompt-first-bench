# N117: α 与 β 的交互效应边界：实际权重 W_rec 对时间的导数 dW_rec/dT = -β * (1 + α * ΔP)；若 β 过小，即使 T_stock 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

α 与 β 的交互效应边界：实际权重 W_rec 对时间的导数 dW_rec/dT = -β * (1 + α * ΔP)；若 β 过小，即使 T_stock 增加，W_rec 下降缓慢；需计算在 T_stock=48h 时，W_rec_high 与 W_rec_low 的比值，若比值 > 1.1，则算法仍在系统性偏好高挂价，证实平台驱动均衡。

## Corrected Claim

α 与 β 的交互效应边界：实际权重 W_rec 对时间的导数 dW_rec/dT = -β * (1 + α * ΔP)；若 β 过小，即使 T_stock 增加，W_rec 下降缓慢；需计算在 T_stock=48h 时，W_rec_high 与 W_rec_low 的比值，若比值 > 1.1，则算法仍在系统性偏好高挂价，证实平台驱动均衡。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

interaction effect alpha beta recommendation weight time decay high price bias
