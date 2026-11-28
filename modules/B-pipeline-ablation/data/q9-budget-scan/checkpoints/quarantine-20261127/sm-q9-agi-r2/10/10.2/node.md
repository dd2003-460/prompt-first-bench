# N112: 针对27B模型的控制变量遗漏问题，需构建‘因果图完整性检查器’，利用DoWhy库自动生成潜在因果图（DAG），通过计算 d-separation 路径检测未控制

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

针对27B模型的控制变量遗漏问题，需构建‘因果图完整性检查器’，利用DoWhy库自动生成潜在因果图（DAG），通过计算 d-separation 路径检测未控制的混杂因子，若检测到 >0 条未阻断的后门路径则判定设计无效。

## Corrected Claim

针对27B模型的控制变量遗漏问题，需构建‘因果图完整性检查器’，利用DoWhy库自动生成潜在因果图（DAG），通过计算 d-separation 路径检测未控制的混杂因子，若检测到 >0 条未阻断的后门路径则判定设计无效。

## Evidence

先验知识/题面给定，逻辑校验通过：DoWhy库确实支持基于DAG的因果推断，d-separation是检测后门路径和混杂因子的标准图论方法，逻辑自洽且符合因果推断基本原理。

## Search Query

DoWhy causal graph completeness check d-separation path blocking algorithm
