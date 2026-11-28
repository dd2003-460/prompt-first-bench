# N39: 数据清洗任务在27b模型上的能力量化指标：定义为对含噪CSV/JSON数据的结构化重构，要求代码执行成功率(Code Pass Rate) > 95%且数据完整

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

数据清洗任务在27b模型上的能力量化指标：定义为对含噪CSV/JSON数据的结构化重构，要求代码执行成功率(Code Pass Rate) > 95%且数据完整性校验通过率(Completeness Check) = 100%，低于此阈值需引入人工规则引擎兜底。

## Corrected Claim

数据清洗任务在27b模型上的能力量化指标：定义为对含噪CSV/JSON数据的结构化重构，要求代码执行成功率(Code Pass Rate) > 95%且数据完整性校验通过率(Completeness Check) = 100%，低于此阈值需引入人工规则引擎兜底。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM data cleaning code generation pass rate benchmark
