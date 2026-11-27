# N28: 演化压力量化：在重复博弈中，卖家演化稳定策略（ESS）的挂价偏移系数 k_evolve 满足 k_evolve = (r_holding / (1 + r_ho

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

演化压力量化：在重复博弈中，卖家演化稳定策略（ESS）的挂价偏移系数 k_evolve 满足 k_evolve = (r_holding / (1 + r_holding)) * 0.2，其中 r_holding 为年化持有成本率；若 r_holding > 5%，则 k_evolve > 10%，支持'高挂价'作为演化最优试探策略。

## Corrected Claim

在特定演化博弈模型中，若假设卖家ESS的挂价偏移系数 k_evolve 与年化持有成本率 r_holding 满足 k_evolve = (r_holding / (1 + r_holding)) * 0.2，则当 r_holding > 5% 时，k_evolve > 10%，支持'高挂价'作为演化最优试探策略。

## Evidence

[质询]该公式 k_evolve = (r_holding / (1 + r_holding)) * 0.2 缺乏通用的演化博弈论理论支持，属于特定模型假设或经验拟合，并非ESS的普适定义；且0.2这一系数无明确理论依据，可能为任意设定的参数。 | 来源[1]仅介绍演化博弈论和ESS的一般概念，未提供具体的挂价偏移系数公式或数值关系，无法直接支持该特定量化结论；但逻辑上若r_holding>5%，计算结果确实>10%，数学自洽。

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E6%BC%94%E5%8C%96%E5%8D%9A%E5%BC%88%E7%90%86%E8%AE%BA/765053&rut=8a58b199de0d9cca403b04b80ce511883eeffc3c657840df467f21e7f6fafc0c', 'type': 'ddg', 'title': '演化博弈论（多学科融合的理论）_百度百科'}
