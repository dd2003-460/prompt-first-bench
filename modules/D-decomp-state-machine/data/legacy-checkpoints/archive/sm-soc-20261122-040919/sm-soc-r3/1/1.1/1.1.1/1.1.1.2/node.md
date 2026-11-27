# N127: 卖家定价噪声投影系数 β_seller：ε_seller = β_seller * ε_t + η_seller，其中 β_seller 为卖家定价对流动性冲击

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N31

## Claim

卖家定价噪声投影系数 β_seller：ε_seller = β_seller * ε_t + η_seller，其中 β_seller 为卖家定价对流动性冲击的敏感度，可通过回归分析卖家挂价偏差率与流动性指数的月度数据估计，预期 β_seller > 0。

## Corrected Claim

卖家定价噪声投影系数 β_seller 定义为卖家定价对流动性冲击的敏感度，理论上预期 β_seller > 0，具体数值需通过回归分析卖家挂价偏差率与流动性指数的月度数据估计。

## Evidence

[质询]该陈述属于特定市场微观结构模型中的经验性参数定义，无法从第一性原理或数学公理中严格推导得出其具体形式（线性投影）及符号（β>0），且参考来源中无任何内容支持这一特定的金融/计量经济学模型设定。 | 逻辑上自洽（流动性冲击通常影响卖家定价行为，正相关符合直觉），但参考来源[1]为希腊电气公司，[2]为eBay定价工具，[3]为5G通信信号处理，均与该金融计量模型无关，无外部证据支持。

## Search Query

regression coefficient seller pricing sensitivity to market liquidity index

## Retrieval Sources

- {'url': 'https://www.fundamenta.gr/companies/083973002000&rut=56151babb77c479a8a7569d8d6e6c8bf90e1354bff25ab108e7212bba126eb2d', 'type': 'ddg', 'title': 'Seller Ελλασ Ανωνυμη Βιομηχανικη Και Εμπορικη Εταιρια Ηλεκτρικων Ειδων ...'}
- {'url': 'https://dataede.com/zh/ebay-pricing-calculator&rut=22dcd180907cd320b880e48aeda64e2925e130d7b5bd000f63e33a0d826e749a', 'type': 'ddg', 'title': 'eBay 定价计算器 2026 - 全市场覆盖 | SellerLab'}
- {'url': 'https://blog.csdn.net/b405516801/article/details/160239968&rut=a954c0b8fdfb63d6e0aec89c37f9311ecac97b9f9e605bc0ecb394cf24de5b9d', 'type': 'ddg', 'title': 'Β系数公式推导以及实战 - Csdn博客'}
