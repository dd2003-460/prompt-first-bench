# N81: 参数 $\alpha$ 的理论下限推导：在 $Score = CTR \times P_{ask} \times (1 - \alpha \times \fra

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

参数 $\alpha$ 的理论下限推导：在 $Score = CTR \times P_{ask} \times (1 - \alpha \times \frac{|P_{ask}-P_{avg}|}{P_{avg}})$ 模型下，设高挂价商品 $P_{ask} = 1.2 P_{avg}$，低挂价商品 $P_{ask} = P_{avg}$，要使高挂价商品排名从Top 10%降至Top 50%，需满足 $Score_{high} / Score_{low} < 0.5$；代入得 $1.2 \times (1 - 0.2\alpha) / 1 < 0.5$，解得 $\alpha > 2.5$；具体 $\alpha$ 需根据平台CTR与Price的相关性 $\rho_{CTR,Price}$ 调整，若 $\rho = 0.8$，则 $\alpha_{min} = 2.5 / (1 - \rho \times 0.1) \approx 2.7$。

## Corrected Claim

在假设高、低挂价商品的基础 CTR 和 P_ask 值相同，且仅通过价格惩罚项影响排名的简化模型下，若要求高挂价商品（$P_{ask}=1.2 P_{avg}$）的得分低于低挂价商品（$P_{ask}=P_{avg}$）的一半，则需满足 $\alpha > 2.5$。实际 $\alpha$ 值需结合平台具体的 CTR-Price 相关性数据通过实验校准，而非仅通过简单的线性修正公式确定。

## Evidence

[质询]推导过程中隐含假设了高挂价与低挂价商品的 CTR 和 P_ask 基础值相同（即 CTR_high = CTR_low, P_ask_high = P_ask_low），仅通过价格惩罚项来区分。然而，在现实电商场景中，高挂价商品通常伴随不同的 CTR 分布，且公式中 CTR 和 P_ask 是独立变量。若 CTR 或基础 P_ask 存在差异，简单的代数推导 $1.2(1-0.2\alpha) < 0.5$ 将不再成立，导致 $\alpha$ 的下限计算错误。此外，$\rho_{CTR,Price}$ 的调整公式 $\alpha_{min} = 2.5 / (1 - \rho \times 0.1)$ 缺乏明确的理论推导依据，属于经验性拟合，逻辑链条不完整。 | 先验知识/题面给定，逻辑校验通过（在严格假设 CTR 和基础 P_ask 相同的前提下，代数推导 $1.2(1-0.2\alpha) < 0.5 \Rightarrow \alpha > 2.5$ 是正确的；但后续关于 $\rho$ 的调整公式缺乏严谨推导，且整体依赖强假设，故降级为定性表述）。

## Search Query

penalty parameter calibration for price deviation in search ranking
