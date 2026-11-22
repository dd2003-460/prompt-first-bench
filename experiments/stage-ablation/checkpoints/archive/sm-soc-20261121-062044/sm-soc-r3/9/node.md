# N97: 演化心理学假设链起点：随机偏好噪声（Random Preference Noise）量化为买家对商品非价格属性（如成色描述、卖家信誉）的感知方差 (σ²_per

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

演化心理学假设链起点：随机偏好噪声（Random Preference Noise）量化为买家对商品非价格属性（如成色描述、卖家信誉）的感知方差 (σ²_perception)，通过A/B测试中同一商品不同展示文案下的点击率标准差估计，若 σ²_perception > 0.1，则表明噪声足以掩盖价格差异，支持‘高挂价被合理化’的假设。

## Corrected Claim

演化心理学假设链起点：随机偏好噪声（Random Preference Noise）量化为买家对商品非价格属性（如成色描述、卖家信誉）的感知方差 (σ²_perception)，通过A/B测试中同一商品不同展示文案下的点击率标准差估计，若 σ²_perception > 0.1，则表明噪声足以掩盖价格差异，支持‘高挂价被合理化’的假设。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于σ²_perception的估计方法（计算与实验设计），子节点2聚焦于判断阈值S_p的定义与临界条件，两者在逻辑上是‘测量’与‘判定’的关系，互不重叠且无矛盾，正交性良好。但父节点中提到的具体阈值‘σ²_perception > 0.1’未在子节点中体现，子节点2引入了新变量σ²_price_diff并定义了相对阈值S_p>1，导致父节点的绝对阈值条件缺失，且未说明S_p与σ²_perception绝对值阈值的对应关系，完备性不足。）
