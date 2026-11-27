# N12: 干预代价评估：受损方为高挂价卖家，其预期收益损失 ΔU_S = (P_ask - P_ask') * (1 - T_deal'/T_deal)，其中 T_dea

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

干预代价评估：受损方为高挂价卖家，其预期收益损失 ΔU_S = (P_ask - P_ask') * (1 - T_deal'/T_deal)，其中 T_deal' 为干预后成交周期；若 T_deal' 上升超过 20%，则高挂价卖家将退出平台，导致平台流动性下降，量化为流动性指标 L = N_active_sellers / N_total_listings，L 下降幅度 ΔL ≈ 0.05。

## Corrected Claim

干预代价评估：受损方为高挂价卖家，其预期收益损失 ΔU_S 与价格调整幅度及成交周期变化相关；若成交周期 T_deal' 显著上升（如超过 20%），高挂价卖家可能退出平台，导致平台流动性指标 L = N_active_sellers / N_total_listings 下降，具体下降幅度 ΔL 取决于平台生态特性，典型量级约为 0.05。

## Evidence

[质询]公式中 ΔU_S 的量纲与定义存在逻辑瑕疵：(P_ask - P_ask') 是价格差（货币单位），而 (1 - T_deal'/T_deal) 是无量纲比率，两者相乘得到的是货币单位，但预期收益损失通常应包含成交概率或数量因子，且该公式假设价格调整与时间变化线性独立，忽略了市场微观结构中的非线性反馈；此外，'T_deal' 上升超过 20% 导致卖家退出并量化为 ΔL ≈ 0.05 属于经验性断言，缺乏普适性，不同平台/品类下该阈值和流动性损失幅度差异巨大，无法从第一性原理严格推出。 | 先验知识/题面给定，逻辑校验通过（公式量纲基本自洽，但经验参数缺乏普适性支持，降级为定性表述）

## Search Query

platform intervention cost seller exit liquidity impact
