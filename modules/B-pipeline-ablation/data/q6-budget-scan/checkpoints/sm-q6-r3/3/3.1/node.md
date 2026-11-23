# N26: 请求分布的Zipf参数：α_zipf ∈ [0.8, 1.2]，其中α越小表示长尾越显著，α越大表示热点越集中，图片+短视频平台的典型α值为0.9-1.1，需基

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

请求分布的Zipf参数：α_zipf ∈ [0.8, 1.2]，其中α越小表示长尾越显著，α越大表示热点越集中，图片+短视频平台的典型α值为0.9-1.1，需基于实际日志数据校准

## Corrected Claim

请求分布通常可用Zipf分布建模，参数α反映热点集中度（α越大越集中）。具体α值需基于实际日志数据校准，不同业务场景（如图片/短视频）的典型值需通过实证分析确定，而非固定为0.9-1.1。

## Evidence

父节点级核验未通过：不完备（子节点中包含了大量与父节点（Zipf参数）完全无关的内容（如CDN监控人员、薪资、支持费用、缓存命中率公式、对象总数估算），严重偏离主题；同时，父节点提到的'基于实际日志数据校准'这一关键步骤仅由一个子节点覆盖，而另外两个子节点直接给出了经验值范围，导致逻辑上存在'先给结论后给方法'的割裂，且未完整覆盖'校准'这一核心动作的所有必要子步骤（如数据清洗、拟合验证等）。）

## Search Query

Zipf parameter for image and video CDN request distribution

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_36069590/article/details/83106894&rut=87a443075388a560051367ed5bc50b3f60bbaf8532ae2aa8a49ae5891e21dbaf', 'type': 'ddg', 'title': '【扫盲】------Zipf分布-CSDN博客'}
- {'url': 'https://docs.scipy.org.cn/doc/scipy/tutorial/stats/discrete_zipf.html&rut=6610a76c0317b80fd649ef0ffaffed79131e9fa2e58ed192bdb7c824babd0f71', 'type': 'ddg', 'title': 'Zipf (Zeta) 分布 — SciPy v1.18.0 手册 - SciPy 科学计算库'}
- {'url': 'https://blog.csdn.net/m0_37816922/article/details/130482955&rut=2f756be035176bd37a2327e9070bece1850f400b80aadbebada12c5b40e02521', 'type': 'ddg', 'title': '【分布族谱】Zipf分布及其Python可视化 - CSDN博客'}
