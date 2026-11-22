# N60: 中间环节失效边界：当市场流动性低于阈值 L_min（定义为日均搜索量/在售商品数），噪声导致的匹配加速效应消失，此时高挂价仅增加 T_deal 而不提升 P_d

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

中间环节失效边界：当市场流动性低于阈值 L_min（定义为日均搜索量/在售商品数），噪声导致的匹配加速效应消失，此时高挂价仅增加 T_deal 而不提升 P_deal，导致 ESS 崩溃，该阈值需通过平台历史数据回归确定。

## Corrected Claim

中间环节失效边界：当市场流动性低于某一特定阈值时，噪声导致的匹配加速效应可能减弱或消失，此时高挂价可能仅增加成交时间而不提升成交概率，进而影响系统稳定性；该阈值的具体定义及数值需通过平台历史数据回归确定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中的三个核心逻辑环节：1. L_min 的具体估计方法（回归模型）；2. 失效的物理/机制判据（噪声匹配效率）；3. 失效的后果及量化条件（ESS收益比较）。三者分别回答了‘如何测量阈值’、‘为何在阈值处失效’、‘失效导致何种结果’，逻辑上层层递进且互不重叠，无冗余。）

## Search Query

market liquidity threshold matching efficiency failure high price strategy second hand platform
