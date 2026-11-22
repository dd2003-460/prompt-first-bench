# N95: E2 级证据（准实验）的具体来源定义为：利用平台算法版本切换时间点作为断点回归（RDD）的自然实验，通过比较切换前后'降价商品'的咨询率差异，计算平均处理效应（

- **status**: pending
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

父节点级核验未通过：不完备（子节点在逻辑上分别对应带宽确定、标准误计算和显著性判断，彼此正且不重复。但在完备性上存在缺失：父节点明确提到利用'平台算法版本切换时间点作为断点'，这涉及RDD的核心前提——'断点处的不可操纵性（no-manipulation）'或'跳跃的因果解释'。子节点仅关注统计计算（h, SE, CI），未涵盖如何验证该自然实验的有效前提（即排除在断点处操纵行为的可能性），也未明确ATE的定义是局部平均处理效应（LATE）还是全局ATE（在RDD中通常估计的是LATE，除非有特定假设）。此外，父节点提到的'准实验'属性依赖于断点的有效性，而子节点未涉及对断点有效性的检验（如McCrary密度测试等）。）

## Search Query

regression discontinuity design e-commerce algorithm change causal inference

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/697393865&rut=de68dd7dc8de67f2920a5e22d389f5548ef028475ca4abf8746902be2424cf54', 'type': 'ddg', 'title': '循证医学的证据来源、分级标准及推荐等级 - 知乎'}
- {'url': 'https://baike.baidu.com/item/%E5%87%86%E5%AE%9E%E9%AA%8C%E7%A0%94%E7%A9%B6/8157845&rut=be7b5a15f8aaa0e3402d14288a15de3fbf99b9384b22bacd8bfadbfb9780a668', 'type': 'ddg', 'title': '准实验研究_百度百科'}
