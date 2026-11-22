# N276: 信任系数 (Trust_Coeff) 的量化定义与阈值：定义为买家对平台展示价格数据的采信概率，需通过问卷或行为实验（如展示价格与实际成交价的偏离容忍度）测定；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

信任系数 (Trust_Coeff) 的量化定义与阈值：定义为买家对平台展示价格数据的采信概率，需通过问卷或行为实验（如展示价格与实际成交价的偏离容忍度）测定；若 Trust_Coeff < 0.6，则有效方差压缩比需修正为 σ_eff = σ_old * (1 - (1 - σ_ratio) * Trust_Coeff)，导致VOI下降。

## Corrected Claim

信任系数 (Trust_Coeff) 的量化定义与阈值：定义为买家对平台展示价格数据的采信概率，需通过问卷或行为实验（如展示价格与实际成交价的偏离容忍度）测定；若 Trust_Coeff < 0.6，则有效方差压缩比需修正为 σ_eff = σ_old * (1 - (1 - σ_ratio) * Trust_Coeff)，导致VOI下降。

## Evidence

先验知识/题面给定，逻辑校验通过
