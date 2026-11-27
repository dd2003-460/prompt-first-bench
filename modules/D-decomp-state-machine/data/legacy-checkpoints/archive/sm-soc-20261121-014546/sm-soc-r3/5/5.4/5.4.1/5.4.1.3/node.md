# N336: 控制点击率(CTR)和转化率(CVR)后，高溢价商品的曝光权重偏差 ΔW_exp_adj 可通过回归模型 W = β0 + β1*Price_Premium +

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N108

## Claim

控制点击率(CTR)和转化率(CVR)后，高溢价商品的曝光权重偏差 ΔW_exp_adj 可通过回归模型 W = β0 + β1*Price_Premium + β2*CTR + ε 中的 β1 系数量化，β1 > 0.3 表明存在独立于用户偏好的算法偏向。

## Corrected Claim

控制点击率(CTR)和转化率(CVR)后，高溢价商品的曝光权重偏差可通过回归模型 W = β0 + β1*Price_Premium + β2*CTR + ε 中的 β1 系数量化，若 β1 统计显著且为正，则表明存在独立于用户偏好的算法偏向。

## Evidence

[质询]β1 > 0.3 作为判定“算法偏向”的阈值缺乏普适性标准，其显著性高度依赖于 Price_Premium 和 CTR 的归一化方式及量纲，未标准化前该数值无绝对物理或统计意义。 | 先验知识/题面给定，逻辑校验通过：回归模型控制变量后系数确实反映独立影响，但具体阈值 0.3 为经验性设定，缺乏通用标准支持，故降级为定性表述。
