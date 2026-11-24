# N657: 档位临界工作点（Traffic=10 TB）：Cost_10TB = 10,000 GB * 0.24 CNY/GB = 2,400 CNY；此工作点定义了第一

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N222

## Claim

档位临界工作点（Traffic=10 TB）：Cost_10TB = 10,000 GB * 0.24 CNY/GB = 2,400 CNY；此工作点定义了第一档计费上限，当业务流量从9.9 TB增至10.1 TB时，边际成本从0.24 CNY/GB突变为0.20 CNY/GB，产生非线性成本下降，是优化流量调度以跨越档位阈值的关键决策点。

## Corrected Claim

在采用阶梯计费模式的场景中，当流量跨越档位阈值（如 10 TB）时，边际成本会发生突变（例如从较高单价降至较低单价），形成非线性成本结构，这是流量调度优化的关键决策点。

## Evidence

[质询]该陈述包含具体的经验性价格参数（0.24 CNY/GB 和 0.00 CNY/GB 的突变），属于特定云服务商或特定计费模型的细节，无法从第一性原理推导。参考来源 [2] 提供的是 AWS 美元计价（$0.09/GB 降至 $0.085/GB），与陈述中的人民币计价及具体数值不符，且其他来源仅为通用计算器，无法验证该特定计费档位的存在及具体数值。 | 逻辑上，阶梯计费在阈值处确实会产生边际成本的非线性变化，计算过程（10000 * 0.24 = 2400）自洽。但作为经验事实（具体价格参数），缺乏直接来源支持（来源 [2] 为 AWS 美元价格，不匹配；来源 [1][3] 为通用工具，无关），故降级。

## Search Query

Alibaba Cloud CDN traffic tier pricing 10TB threshold cost calculation

## Retrieval Sources

- {'url': 'https://calculator.academy/price-per-gigabyte-calculator/&rut=11d25b430cf217b808adb23153530e3d4ced4c752c8f0b3467a375e4e273215f', 'type': 'ddg', 'title': 'Price Per GB Calculator (Cost per Gigabyte & TB Storage)'}
- {'url': 'https://egresscost.com/aws/data-transfer-pricing/&rut=cf887110b8aab68afb95eceedb2c9b234f7eecf79dfed1361a18a3da21eceb85', 'type': 'ddg', 'title': 'AWS Data Transfer Out to Internet Pricing 2026 (Per GB)'}
- {'url': 'https://calculator.academy/cost-per-tb-calculator/&rut=9a81b868fdbacd3b60699ed446044945bef4cdfdc74a90502a84230925313069', 'type': 'ddg', 'title': 'Price per TB Calculator (Cost per Terabyte & per GB)'}
