# N95: E2 级证据（准实验）的具体来源定义为：利用平台算法版本切换时间点作为断点回归（RDD）的自然实验，通过比较切换前后'降价商品'的咨询率差异，计算平均处理效应（

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

E2 级证据（准实验）的具体来源定义为：利用平台算法版本切换时间点作为断点回归（RDD）的自然实验，通过比较切换前后'降价商品'的咨询率差异，计算平均处理效应（ATE），ATE 的置信区间若包含 0 则证明干预无效，标准误 SE_RDD 需基于带宽选择计算 [待核验]。

## Corrected Claim

E2级证据（准实验）通常包括利用自然实验（如政策或算法变更）进行的研究，断点回归（RDD）是其中一种典型方法，通过比较断点前后的结果差异来估计因果效应（如ATE），其标准误需基于带宽选择计算。

## Evidence

[质询]该陈述将特定的统计方法（RDD）和具体的业务场景（平台算法切换、降价商品咨询率）定义为通用的“E2级证据”标准，存在以偏概全的风险。E2级（准实验）是一个证据等级分类，而非特定方法的定义；并非所有准实验都使用RDD，也并非所有RDD都用于此特定场景。此外，来源仅确认RDD属于准实验方法，未确认其作为E2级证据的“具体来源定义”或该特定业务场景的通用性。 | 来源[2]确认断点回归设计（RDD）是准实验研究的典型方法，支持了方法论归属；但来源未支持将特定业务场景（算法切换/降价咨询）定义为E2级证据的通用标准，且该陈述包含具体经验场景，缺乏直接来源支持其作为通用定义，故降级。

## Search Query

regression discontinuity design e-commerce algorithm change causal inference

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/697393865&rut=de68dd7dc8de67f2920a5e22d389f5548ef028475ca4abf8746902be2424cf54', 'type': 'ddg', 'title': '循证医学的证据来源、分级标准及推荐等级 - 知乎'}
- {'url': 'https://baike.baidu.com/item/%E5%87%86%E5%AE%9E%E9%AA%8C%E7%A0%94%E7%A9%B6/8157845&rut=be7b5a15f8aaa0e3402d14288a15de3fbf99b9384b22bacd8bfadbfb9780a668', 'type': 'ddg', 'title': '准实验研究_百度百科'}
