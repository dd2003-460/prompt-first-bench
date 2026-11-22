# N63: 安慰剂检验阈值：在随机选取的非干预时段或对照组进行伪干预，若伪处理效应 (β_placebo) 的 95% CI 包含 0 且 |β_placebo| < 0.

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

安慰剂检验阈值：在随机选取的非干预时段或对照组进行伪干预，若伪处理效应 (β_placebo) 的 95% CI 包含 0 且 |β_placebo| < 0.1 * |β_treatment|，则支持真实效应的因果归因置信度 > 0.95。

## Corrected Claim

安慰剂检验阈值：在随机选取的非干预时段或对照组进行伪干预，若伪处理效应 (β_placebo) 的 95% CI 包含 0 且 |β_placebo| < 0.1 * |β_treatment|，则增强了对真实效应因果归因的置信度。

## Evidence

[质询]该陈述将统计显著性（CI包含0）和效应量比例（<0.1倍）直接等同于“因果归因置信度 > 0.95”这一具体的后验概率数值，缺乏严格的贝叶斯统计推导支持，属于将启发式规则过度量化为精确概率断言。 | 先验知识/题面给定，逻辑校验通过：安慰剂检验是因果推断中常用的稳健性检查方法，伪处理效应不显著且远小于真实效应通常支持因果解释，但“置信度>0.95”的具体数值断言缺乏通用理论支撑，故降级为定性表述。

## Search Query

Placebo test causal inference threshold relative effect size
