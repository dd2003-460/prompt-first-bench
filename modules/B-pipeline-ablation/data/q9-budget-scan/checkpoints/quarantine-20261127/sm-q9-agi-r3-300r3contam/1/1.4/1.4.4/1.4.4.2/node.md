# N120: Fatal Logic Error 的自动化检测代理指标：定义逻辑一致性分数 LCS = 1 - P(contradiction | generated_pla

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

Fatal Logic Error 的自动化检测代理指标：定义逻辑一致性分数 LCS = 1 - P(contradiction | generated_plan, domain_rules)，需构建包含至少50个已知逻辑谬误模式的负面案例库进行回归测试，若 LCS < 0.95 则判定存在致命逻辑漏洞 [待核验]

## Corrected Claim

Fatal Logic Error 的自动化检测可参考逻辑一致性分数 LCS = 1 - P(contradiction | generated_plan, domain_rules)。建议构建包含已知逻辑谬误模式的负面案例库进行回归测试，并设定 LCS 阈值（如 0.95）作为潜在逻辑漏洞的预警指标，具体阈值需根据领域规则完备性调整。

## Evidence

[质询]LCS 的定义依赖于 'domain_rules' 的完备性和形式化程度，若规则集不完备，P(contradiction) 将低估实际逻辑错误率，导致 LCS 虚高；此外，50 个案例库对于覆盖所有逻辑谬误模式可能不足，阈值 0.95 缺乏统计学显著性支撑。 | 先验知识/题面给定，逻辑校验通过。虽然公式定义在逻辑上自洽（基于概率和规则集），但作为经验性工程指标，其具体阈值（0.95）和样本量要求（50）属于经验设定，缺乏通用标准支持，故降级为定性表述。

## Search Query

automated logical consistency check for experimental plans LLM benchmark
