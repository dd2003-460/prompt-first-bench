# N5: 演化定向压力参数：损失厌恶系数 (λ) 在二手交易定价中的量化值为 2.25（基于 Kahneman & Tversky 1979 及后续元分析），导致卖家心理

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

演化定向压力参数：损失厌恶系数 (λ) 在二手交易定价中的量化值为 2.25（基于 Kahneman & Tversky 1979 及后续元分析），导致卖家心理保留价 P_reserve = C_acq + λ*(C_acq - P_market)，其中 C_acq 为获客成本/沉没成本，P_market 为近期成交价。

## Corrected Claim

演化定向压力参数：损失厌恶系数 (λ) 在二手交易定价中通常被量化为大于 1 的数值（常见估计范围在 1.5 至 2.5 之间，具体值依情境而定），导致卖家心理保留价 P_reserve 高于市场公允价，其形式可近似表示为 P_reserve ≈ C_acq + λ*(C_acq - P_market)，其中 λ 反映卖家对潜在损失的敏感度。

## Evidence

[质询]数值量级与来源可靠性：Kahneman & Tversky (1979) 原始实验并未给出 λ=2.25 这一精确量化值，该数值通常来自后续特定情境下的元分析或特定模型拟合，直接归因于 1979 年原文存在事实错误；且将通用的损失厌恶系数直接线性应用于二手交易定价公式 P_reserve = C_acq + λ*(C_acq - P_market) 缺乏严格的经济学推导支持，属于过度简化的经验模型。 | 先验知识/题面给定，逻辑校验通过（公式量纲自洽，系数量级在行为经济学常见范围内），但具体数值 2.25 及其与 1979 年文献的直接对应关系缺乏权威来源直接支持，且无外部检索来源可用，故降级为定性表述。

## Search Query

loss aversion coefficient lambda 2.25 Kahneman Tversky meta-analysis
