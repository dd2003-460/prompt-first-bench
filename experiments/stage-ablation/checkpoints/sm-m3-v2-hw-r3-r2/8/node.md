# N31: 针对‘方法论严谨性’的自动化评估，需构建 ‘Experimental Design Validity Checker’。该模块基于预定义的科研范式模板（如 RC

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

针对‘方法论严谨性’的自动化评估，需构建 ‘Experimental Design Validity Checker’。该模块基于预定义的科研范式模板（如 RCT, Cross-sectional, Simulation），检查生成文本中是否包含必要的控制变量描述、样本量计算公式（如基于 power analysis 的 n ≥ 80 for α=0.05, power=0.8）以及统计检验方法的选择依据。若缺失关键统计参数或逻辑断层，自动评分低于 70/100，判定为‘不可发表级’。此检查项弥补了 LLM 常忽略统计前提的缺陷。

## Corrected Claim

针对‘方法论严谨性’的自动化评估，需构建 ‘Experimental Design Validity Checker’。该模块基于预定义的科研范式模板（如 RCT, Cross-sectional, Simulation），检查生成文本中是否包含必要的控制变量描述、样本量计算公式以及统计检验方法的选择依据。若缺失关键统计参数或存在逻辑断层，系统将给予低分评价，以弥补 LLM 常忽略统计前提的缺陷。

## Evidence

[质询]该陈述包含具体的工程实现细节（如“自动评分低于 70/100”、“判定为‘不可发表级’”的具体阈值和标签），这些属于特定系统的设计参数或经验性规定，并非通用的科学事实或第一性原理可推导内容，且参考来源未提供此类具体量化标准的支持。 | 来源 [1] 间接支持了实验设计严谨性的重要性及核心要素（如变量控制），但未涉及自动化评估工具的具体评分阈值（70分）或特定模块名称，属于经验事实缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1956674179043689725&rut=fe4e1e0d2169b37d03a6c5df0f01406597fd6d08d739c469c8c0820bf012f76c', 'type': 'ddg', 'title': '实验设计（Experimental Design）全攻略：五大步骤 - 知乎'}
