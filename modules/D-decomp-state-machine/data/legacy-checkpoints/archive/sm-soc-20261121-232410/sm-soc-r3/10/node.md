# N88: 随机偏好噪声 σ_noise 的量化边界：在二手交易决策中，买家因非理性偏好（如品牌忠诚、颜色偏好）产生的价格容忍度噪声标准差 σ_noise 约为市场均值的 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声 σ_noise 的量化边界：在二手交易决策中，买家因非理性偏好（如品牌忠诚、颜色偏好）产生的价格容忍度噪声标准差 σ_noise 约为市场均值的 10%（即 σ_noise = 0.10 * P_market）。当卖家挂价溢价率 ΔP% 低于 2*σ_noise（即20%）时，信号效应被噪声掩盖，买家无法通过价格区分质量，导致高挂价无法有效筛选高质量商品，解释了为何部分高挂价商品成交周期并未显著缩短。

## Corrected Claim

在二手交易决策中，买家因非理性偏好产生的价格容忍度噪声（σ_noise）会掩盖价格信号。当卖家挂价溢价率低于噪声阈值（如2*σ_noise）时，买家难以通过价格区分质量，导致高挂价无法有效筛选高质量商品，这可能解释部分高挂价商品成交周期未显著缩短的现象。

## Evidence

[质询]该陈述将二手交易中的具体量化参数（σ_noise = 10% P_market）作为既定事实，但这是一个经验性假设，缺乏普遍适用的实证数据支持，且不同品类（如奢侈品 vs 日用品）的噪声差异巨大，无法一概而论。 | 参考来源[1][2][3]仅定性描述了噪声交易的存在及其对价格偏离的影响，未提供二手交易市场中噪声标准差为10%的具体数值支持，属于经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E5%99%AA%E5%A3%B0%E4%BA%A4%E6%98%93%E7%90%86%E8%AE%BA/326097&rut=e640bad7b6bbdecca27dfbd188475e547616db237b787600f23a984baf19bf45', 'type': 'ddg', 'title': '噪声交易理论 - 百度百科'}
- {'url': 'https://baike.baidu.com/item/DSSW%E6%A8%A1%E5%9E%8B/10704913&rut=af5acadbe63493cbda2963d901c7b1f8eedb88bc5e73daed28f1b496041b9dba', 'type': 'ddg', 'title': 'Dssw模型 - 百度百科'}
- {'url': 'https://zhuanlan.zhihu.com/p/1908049285011965828&rut=0a4e42b2577da50a44c1b20e31d44ffb8c1efdb5dd3a189e703d7185888934ca', 'type': 'ddg', 'title': '交易大百科 (N系列)——噪音交易 (Noise Trading) - 知乎'}
