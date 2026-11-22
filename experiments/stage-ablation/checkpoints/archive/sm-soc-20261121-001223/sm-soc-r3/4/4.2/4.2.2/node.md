# N62: IV 工具变量排他性约束的敏感性分析：使用平台历史 A/B 测试随机分组作为工具变量 Z，计算第一阶段 F 统计量；若 F < 10，则存在弱工具变量问题，需报

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

IV 工具变量排他性约束的敏感性分析：使用平台历史 A/B 测试随机分组作为工具变量 Z，计算第一阶段 F 统计量；若 F < 10，则存在弱工具变量问题，需报告 Anderson-Rubin 置信区间以评估因果效应的下界。

## Corrected Claim

IV 工具变量排他性约束的敏感性分析：使用平台历史 A/B 测试随机分组作为工具变量 Z，计算第一阶段 F 统计量；若 F < 10，则存在弱工具变量问题，需报告 Anderson-Rubin 置信区间以评估因果效应的下界。

## Evidence

先验知识/题面给定，逻辑校验通过：F<10是弱工具变量的标准经验法则，Anderson-Rubin区间是处理弱IV的标准方法，逻辑自洽且符合计量经济学规范。

## Search Query

Weak instrument test Anderson-Rubin confidence interval IV
