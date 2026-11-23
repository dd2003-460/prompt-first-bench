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

父节点级核验未通过：非正交, 不完备, 有冗余（父节点核心是“Zipf参数α_zipf的分布与校准”，但子节点中包含了大量无关内容（如CDN监控人员数量、年薪、技术支持费、缓存命中率公式、对象总数估算），严重偏离主题。此外，子节点4（通用校准方法）与子节点5（图片/视频具体取值）存在逻辑重叠，且子节点5是对子节点4中“典型值”的具体化，属于冗余或层级不当。）

## Search Query

Zipf parameter for image and video CDN request distribution

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_36069590/article/details/83106894&rut=87a443075388a560051367ed5bc50b3f60bbaf8532ae2aa8a49ae5891e21dbaf', 'type': 'ddg', 'title': '【扫盲】------Zipf分布-CSDN博客'}
- {'url': 'https://docs.scipy.org.cn/doc/scipy/tutorial/stats/discrete_zipf.html&rut=6610a76c0317b80fd649ef0ffaffed79131e9fa2e58ed192bdb7c824babd0f71', 'type': 'ddg', 'title': 'Zipf (Zeta) 分布 — SciPy v1.18.0 手册 - SciPy 科学计算库'}
- {'url': 'https://blog.csdn.net/m0_37816922/article/details/130482955&rut=2f756be035176bd37a2327e9070bece1850f400b80aadbebada12c5b40e02521', 'type': 'ddg', 'title': '【分布族谱】Zipf分布及其Python可视化 - CSDN博客'}
