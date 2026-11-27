# N60: 平台算法中'价格合理性'的缺失量化：若排序权重 w_price 为 0，则高价商品仅受 w_speed 和 w_ctr 影响，需计算在 w_speed > w_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

平台算法中'价格合理性'的缺失量化：若排序权重 w_price 为 0，则高价商品仅受 w_speed 和 w_ctr 影响，需计算在 w_speed > w_ctr 条件下，溢价率 20% 的商品相比溢价率 0% 的商品获得的曝光量提升倍数 ΔExposure。

## Corrected Claim

在平台算法中，若价格权重 w_price 为 0，高价商品（溢价率 20%）的曝光量将主要受 w_speed 和 w_ctr 影响。由于缺乏具体的排序公式和权重数值，无法计算确切的曝光量提升倍数 ΔExposure，但理论上若 w_speed > w_ctr 且高价商品在速度或点击率指标上无劣势，其曝光量可能高于或等于溢价率为 0% 的商品，具体倍数取决于算法的非线性映射特性。

## Evidence

[质询]该陈述试图计算一个具体的数值倍数（ΔExposure），但缺乏具体的算法公式、权重数值（w_speed, w_ctr的具体值）以及曝光量与排序分数的映射函数（如线性、指数或截断分布）。仅凭定性描述无法推导出唯一的数值结果，属于经验事实/具体参数缺失。 | 参考来源[1][2][3]仅定性提及价格、点击率等是排序因素，未提供具体的权重数值或曝光量计算公式，无法直接支持具体的倍数计算；逻辑上，若缺乏具体函数定义，该数值不可推导，故降级为定性表述。

## Search Query

marketplace algorithm ranking weights price vs speed A/B test results

## Retrieval Sources

- {'url': 'https://infoxlog.com/the-facebook-marketplace-algorithm-explained-2026-guide/&rut=4268586a6e079577f2a5a93d92945b5a811d5605f47b049a7d67778cfd2abb3c', 'type': 'ddg', 'title': 'The Facebook Marketplace Algorithm Explained (2026 Guide)'}
- {'url': 'https://listaro.dev/blog/facebook-marketplace-algorithm&rut=4f386b9e3d16ebf645174d9a7efd95ce4c296446c2ca4a18b35d49e9ca69c519', 'type': 'ddg', 'title': 'How the Facebook Marketplace Algorithm Works (2026 Guide)'}
- {'url': 'https://www.reddog.group/blogs/unleashing-insights/what-is-a-marketplace-algorithm-a-guide-for-sellers&rut=0b45df06e55909739a27edd078107d4b5b8d469188af9da5a5a8355b3ae8bdf0', 'type': 'ddg', 'title': 'What Is a Marketplace Algorithm? A Guide for Sellers'}
