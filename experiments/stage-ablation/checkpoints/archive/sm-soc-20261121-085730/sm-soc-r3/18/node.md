# N432: 假设链中‘损失规避导致高挂价’断言的贝叶斯置信度计算：$C_{loss} = P(Hypothesis_{Loss} | Data) = \frac{P(Dat

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

假设链中‘损失规避导致高挂价’断言的贝叶斯置信度计算：$C_{loss} = P(Hypothesis_{Loss} | Data) = \frac{P(Data | H_{Loss}) P(H_{Loss})}{P(Data)}$。其中似然函数 $P(Data | H_{Loss})$ 基于卖家在价格偏离 $C_{ref}$ 15%以上时的成交概率衰减曲线拟合，先验 $P(H_{Loss})$ 设定为 0.6（基于Kahneman & Tversky元分析），需输出后验概率区间 [0.5, 0.7] 以支持高置信度结论。

## Corrected Claim

假设链中‘损失规避导致高挂价’断言的贝叶斯置信度计算：$C_{loss} = P(Hypothesis_{Loss} | Data) = \frac{P(Data | H_{Loss}) P(H_{Loss})}{P(Data)}$。其中似然函数 $P(Data | H_{Loss})$ 基于卖家在价格偏离 $C_{ref}$ 15%以上时的成交概率衰减曲线拟合，先验 $P(H_{Loss})$ 设定为 0.6（基于Kahneman & Tversky元分析），需输出后验概率区间 [0.5, 0.7] 以支持高置信度结论。

## Evidence

检索失败: no sources from any channel (all 5 failed)
