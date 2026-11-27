# N185: 工作点1（高惩罚/高GMV敏感）：当推荐权重函数 W_rec 对 GMV 敏感度高且价格惩罚项 P_penalty 高（如 P_penalty > 0.8）时，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

工作点1（高惩罚/高GMV敏感）：当推荐权重函数 W_rec 对 GMV 敏感度高且价格惩罚项 P_penalty 高（如 P_penalty > 0.8）时，高溢价商品曝光量下降比例 ΔE_seller_high ≈ 0.6-0.8，此时平台短期收入损失 L_short 最大，但长期成交效率增益 G_long 也最大，适用于高流动性市场。

## Corrected Claim

工作点1（高惩罚/高GMV敏感）：当推荐权重函数 W_rec 对 GMV 敏感度高且价格惩罚项 P_penalty 高时，高溢价商品曝光量显著下降，此时平台短期收入损失较大，但长期成交效率增益也较大，适用于高流动性市场。

## Evidence

[质询]该陈述包含具体的经验性数值区间（ΔE_seller_high ≈ 0.6-0.8）和定性结论（L_short最大、G_long最大），属于经验事实而非第一性原理可推导的数学/逻辑恒等式。在缺乏具体市场数据、模型参数或实证研究支持的情况下，这些具体数值和因果关系的强度无法仅凭逻辑自洽性得到验证，存在过度具体化或拟合偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值区间无法从第一性原理严格推出）

## Search Query

high price penalty impact on exposure GMV sensitive recommendation algorithm A/B test
