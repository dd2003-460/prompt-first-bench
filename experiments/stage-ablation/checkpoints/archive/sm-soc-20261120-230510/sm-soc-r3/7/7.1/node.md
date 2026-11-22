# N97: 平台算法权重比 w_ctr/w_cvr 的行业基准值：根据二手电商平台（如闲鱼、eBay）公开技术博客及第三方审计报告，w_ctr/w_cvr 的中位数为 2.

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

平台算法权重比 w_ctr/w_cvr 的行业基准值：根据二手电商平台（如闲鱼、eBay）公开技术博客及第三方审计报告，w_ctr/w_cvr 的中位数为 2.5，标准差为 0.8，该比值直接决定了高挂价商品（高CTR低CVR）在推荐系统中的优先级。

## Corrected Claim

平台算法中CTR与CVR的权重比（w_ctr/w_cvr）通常根据业务目标动态调整，不同平台及场景下数值差异较大，无统一的公开行业基准值；高CTR低CVR商品在推荐系统中的优先级取决于具体的排序公式及业务侧重。

## Evidence

[质询]该陈述声称存在具体的行业基准数值（中位数2.5，标准差0.8），但参考来源中完全未提及任何具体数值，且此类内部算法权重通常属于商业机密，极少有公开且统一的“行业基准”统计分布，极大概率为虚构数据。 | 参考来源[1]和[2]仅讨论了CTR/CVR指标体系及动态调整策略（如DC-LTR算法），均未提供w_ctr/w_cvr的具体数值分布或行业基准，无法支持该具体数值陈述。

## Search Query

second-hand marketplace algorithm CTR CVR weight ratio recommendation system

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2040796958546191518&rut=044e2ac87d6901234d0624bdba5a9dd7aea660847952c825006f74ef0bed833b', 'type': 'ddg', 'title': '一文讲清搜广推的核心指标体系：从 Ctr、Cvr 到 Auc、Roi'}
- {'url': 'https://zhuanlan.zhihu.com/p/466917357&rut=d9cb30abe547ba9fc1dcd84c1a6d1ed05e6ed3a26c5ad315ef6a25a8f1563cf9', 'type': 'ddg', 'title': 'Aaai 2021 基于神经网络的ctr-cvr权重动态调整策略 - 知乎'}
