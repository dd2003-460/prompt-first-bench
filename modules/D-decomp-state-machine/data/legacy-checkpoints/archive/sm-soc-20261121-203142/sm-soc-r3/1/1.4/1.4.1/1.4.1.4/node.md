# N133: 共享随机源：平台流量分配中的基础曝光量 Base_Imp 由类目热度 H_category 和商品新鲜度 F_freshness 决定，Base_Imp = H

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

共享随机源：平台流量分配中的基础曝光量 Base_Imp 由类目热度 H_category 和商品新鲜度 F_freshness 决定，Base_Imp = H_category * F_freshness * C_base，其中 C_base 为平台基准常数，需确定 H_category 和 F_freshness 在二手交易中的典型取值范围。

## Corrected Claim

在典型的推荐系统流量分配模型中，基础曝光量通常受类目热度、商品新鲜度及平台基准系数影响，具体公式及二手交易场景下的参数取值需依据特定平台的实际策略文档确定，通用文献中无统一标准。

## Evidence

[质询]该陈述描述了一个具体的平台内部算法公式（Base_Imp = H_category * F_freshness * C_base）及特定参数（二手交易中的典型取值范围）。这属于特定平台的经验性工程实现细节或黑盒逻辑，并非通用的第一性原理或公开标准。参考来源[1]讨论的是GEO优化（AI搜索排名），与电商流量分配公式无关；来源[2]讨论的是AB测试的流量分流（随机化实验），而非推荐系统中的基础曝光量计算公式。因此，该具体公式和参数范围缺乏来源支持，且无法从通用逻辑推导得出。 | 逻辑上公式结构自洽（曝光量由热度、新鲜度和基准常数决定符合推荐系统常识），但参考来源[1]和[2]均未涉及该具体公式或二手交易参数范围，属于经验事实且缺来源支持。

## Search Query

second hand platform base exposure calculation category freshness

## Retrieval Sources

- {'url': 'https://gitcode.csdn.net/6a16b845662f9a54cb779581.html&rut=d8dce0131393c7d6c67b8b562424c6ecb02c7a3f11711d225f32d31fa23de6ea', 'type': 'ddg', 'title': 'Geo优化ai搜索推广排名系统怎么做？2026 Ai流量获取与全网曝光实战（附代码示例）'}
- {'url': 'https://devpress.csdn.net/avi/69c56d6c54b52172bc64ccdb.html&rut=98f725baffb714288b9a5365deafd86be1411847868704daa8065eb8af1605b4', 'type': 'ddg', 'title': 'AB测试主模型实战：从流量分配到效果评估的全链路实现'}
