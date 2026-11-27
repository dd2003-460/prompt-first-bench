# N45: 心理账户最低溢价阈值 δ_min = λ * σ_W / μ_W，其中 λ=2.25 (损失厌恶系数)，σ_W/μ_W 为买家支付意愿变异系数，需计算具体数值以

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

心理账户最低溢价阈值 δ_min = λ * σ_W / μ_W，其中 λ=2.25 (损失厌恶系数)，σ_W/μ_W 为买家支付意愿变异系数，需计算具体数值以验证是否落在 [0.15, 0.25] 区间

## Corrected Claim

在特定心理账户模型假设下，最低溢价阈值 δ_min 可表示为 λ * σ_W / μ_W，其中 λ=2.25 为损失厌恶系数，σ_W/μ_W 为买家支付意愿变异系数；需结合具体数据计算以验证其是否落在 [0.15, 0.25] 区间。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1提供了参数 σ_W/μ_W 的实证/先验区间（输入端），子节点2提供了基于该参数推导出的 δ_min 理论区间及其与观测值的对比分析（输出端）。两者逻辑层层递进，分别覆盖了'参数估计'和'模型验证'两个不同维度，不存在重复或矛盾，且共同完成了父节点要求的'计算数值以验证区间'的任务。）

## Search Query

loss aversion coefficient lambda 2.25 pricing bias threshold second hand market
