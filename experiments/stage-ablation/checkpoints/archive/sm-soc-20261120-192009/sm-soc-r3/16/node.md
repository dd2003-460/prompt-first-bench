# N360: 随机偏好噪声导致的'僵尸挂单'比例量化：定义僵尸挂单为 Price > 1.15 * P_market 且 T_wait > 7天。基于 Beta 分布噪声假设

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声导致的'僵尸挂单'比例量化：定义僵尸挂单为 Price > 1.15 * P_market 且 T_wait > 7天。基于 Beta 分布噪声假设，若 σ_noise/μ = 0.1，则 P(Zombie) ≈ 0.15。平台算法若未剔除僵尸挂单，会导致 P_market 估计偏差，进而使新卖家锚定偏差 β_anchor 系统性上移 0.05-0.10。

## Corrected Claim

随机偏好噪声导致的'僵尸挂单'（Price > 1.15 * P_market 且 T_wait > 7天）若未被剔除，会导致 P_market 估计偏差，进而使新卖家锚定偏差 β_anchor 系统性上移。具体量化比例（如 P(Zombie) ≈ 0.15 或偏差幅度 0.05-0.10）需基于特定市场数据实证得出，此处仅为基于 Beta 分布噪声假设的估算值。

## Evidence

[质询]该陈述包含具体的经验性数值结论（P(Zombie) ≈ 0.15, β_anchor 上移 0.05-0.10），这些数值依赖于特定的市场微观结构假设和噪声分布参数，无法仅从第一性原理或题面条件严格推导得出，属于经验事实。 | 逻辑上，高价格且长期未成交的挂单确实可能扭曲市场参考价，导致锚定偏差，方向合理；但参考来源[1][2][3]仅涉及A股盘口结构、撮合逻辑及订单簿失衡策略，未提供关于'僵尸挂单'比例量化或特定噪声参数下锚定偏差幅度的直接数据支持，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33139275/article/details/169583048&rut=8da8e01c5c19c14ad18e1ce325a85cfdcf86a00c30379a33510b6e0b3d306f95', 'type': 'ddg', 'title': '五档盘口与集合竞价：A股高频数据解析与量化实战-csdn博客'}
- {'url': 'https://www.cnblogs.com/mm12/p/19734255&rut=2938676db3b0ededb3669b38b30d0c3a938be4de8affa598d78c370ec8b35d56', 'type': 'ddg', 'title': '量化交易实盘成交难题解析：从订单簿撮合逻辑到落地实践'}
- {'url': 'https://www.quant58.com/learn/order-book-imbalance&rut=8cbc5511bdc4a28ddf0e9ff9f19f4668f733486d891889ba264546d785eaba68', 'type': 'ddg', 'title': '订单簿失衡高频交易策略详解：盘口挂单量的量化实战 - Quant58 AI智能量化交易平台'}
