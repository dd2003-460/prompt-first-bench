# N161: 买家感知概率 P_perceive(ΔInfo) 的量化模型：基于信号检测论（SDT），P_perceive = Φ((ΔInfo - ε_JND) / σ_n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

买家感知概率 P_perceive(ΔInfo) 的量化模型：基于信号检测论（SDT），P_perceive = Φ((ΔInfo - ε_JND) / σ_noise)，其中 ΔInfo 为价格变动幅度，ε_JND 为最小可觉差（约 5% 市场价），σ_noise 为买家注意力噪声标准差（需检索二手商品页平均停留时间与点击率数据拟合，假设 σ_noise ≈ 0.08）。

## Corrected Claim

买家感知概率 P_perceive(ΔInfo) 的量化模型：基于信号检测论（SDT），P_perceive = Φ((ΔInfo - ε_JND) / σ_noise)，其中 ΔInfo 为价格变动幅度，ε_JND 为最小可觉差（约 5% 市场价），σ_noise 为买家注意力噪声标准差（需检索二手商品页平均停留时间与点击率数据拟合，假设 σ_noise ≈ 0.08）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

signal detection theory just noticeable difference price change consumer attention noise standard deviation
