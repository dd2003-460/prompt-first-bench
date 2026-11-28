# N58: 适用域边界：Self-Consistency 仅在输出空间离散且可枚举的任务（如选择题、分类、短代码生成）中有效；对于开放式文本生成（如 Hypothesis 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

适用域边界：Self-Consistency 仅在输出空间离散且可枚举的任务（如选择题、分类、短代码生成）中有效；对于开放式文本生成（如 Hypothesis Generation），投票机制无法直接应用，需改用 Self-Refine (Critique-Revise loop) 策略，其成本模型为 Cost = Base + Sum(Critique_i + Revise_i)。

## Corrected Claim

适用域边界：Self-Consistency 仅在输出空间离散且可枚举的任务（如选择题、分类、短代码生成）中有效；对于开放式文本生成（如 Hypothesis Generation），投票机制无法直接应用，需改用 Self-Refine (Critique-Revise loop) 策略，其成本模型为 Cost = Base + Sum(Critique_i + Revise_i)。

## Evidence

先验知识/题面给定，逻辑校验通过：Self-Consistency依赖多数投票，确实仅适用于离散可枚举输出；开放式生成需迭代优化（如Self-Refine），其成本结构符合累积计算逻辑。
