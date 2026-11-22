# N21: 基于Gaussian Copula (rho=-0.3) 的联合分布分析显示，热门对象（高Frequency）倾向于较小尺寸。具体量化为：频率排名前10%的对象

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

基于Gaussian Copula (rho=-0.3) 的联合分布分析显示，热门对象（高Frequency）倾向于较小尺寸。具体量化为：频率排名前10%的对象，其平均大小仅为整体平均大小的约 0.65 倍（基于Copula相关系数对截断Pareto均值的修正估算），这导致LRU在缓存热门对象时，单位请求贡献的字节命中率低于LFU（LFU更倾向于缓存高频且相对较大的对象，若负相关较弱或LFU能捕获中频大对象）。

## Corrected Claim

基于Gaussian Copula (rho=-0.3) 的联合分布分析显示，热门对象（高Frequency）倾向于较小尺寸。这种负相关性导致LRU在缓存热门对象时，单位请求贡献的字节命中率可能低于LFU（若LFU能捕获中频大对象）。

## Evidence

[质询]该陈述包含具体的经验性数值（0.65倍）和特定的统计模型参数（rho=-0.3），这些属于经验事实而非第一性原理可推导的数学恒等式。参考来源仅介绍Copula函数的基本概念，未提供针对特定数据集（热门对象频率与尺寸）的实证分析结果或具体数值支持，因此无法验证该具体量化结论的准确性。 | 逻辑上，负相关（rho=-0.3）确实意味着高频对象倾向于较小尺寸，从而可能导致LRU在字节命中率上低于LFU（若LFU能捕获中频大对象），逻辑链条自洽。但参考来源[1]仅解释Copula定义，与该具体事实主题（缓存策略性能对比及具体数值）无关，属于「无可用外部证据」；且该事实为经验事实，缺乏直接来源支持，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/138800469&rut=6690c74cf525e15e0c00c5a7a141beeccf79817d4033f282eb65688e70abb843', 'type': 'ddg', 'title': 'Copula系列（一）-什么是Copula函数 - 知乎'}
