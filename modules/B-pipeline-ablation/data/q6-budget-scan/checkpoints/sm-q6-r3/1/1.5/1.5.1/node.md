# N63: 请求到达率λ的计算：λ = (DAU * req_per_user_per_day) / 86400 * Burst_Factor，其中DAU=5,000,00

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

请求到达率λ的计算：λ = (DAU * req_per_user_per_day) / 86400 * Burst_Factor，其中DAU=5,000,000，req_per_user_per_day为每用户日均请求数（图片+短视频平台典型值20-50次），Burst_Factor为峰值突发系数（典型1.5-3.0，反映早晚高峰），计算得λ ≈ 17-87 req/s（全量）或按POP分摊。

## Corrected Claim

请求到达率λ的计算：λ = (DAU * req_per_user_per_day) / 86400 * Burst_Factor，其中DAU=5,000,000，req_per_user_per_day为每用户日均请求数（图片+短视频平台典型值20-50次），Burst_Factor为峰值突发系数（典型1.5-3.0，反映早晚高峰），计算得λ ≈ 17-87 req/s（全量）或按POP分摊。

## Evidence

父节点级核验未通过：不完备（子节点分别推导了公式中的两个关键变量（req_per_user_per_day 和 Burst_Factor），二者正交且无冗余。但父节点中明确提到的 DAU=5,000,000 这一基础参数在子节点中仅作为计算输入被引用，缺乏对其来源或合理性的独立分解节点；此外，父节点提及“按POP分摊”这一维度，子节点未覆盖多节点/区域分摊对λ计算的影响逻辑，导致完备性不足。）
