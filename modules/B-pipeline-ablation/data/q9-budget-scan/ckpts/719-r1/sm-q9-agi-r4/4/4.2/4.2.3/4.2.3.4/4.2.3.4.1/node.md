# N615: TTR（Type-Token Ratio）的样本量偏差校正：由于max_tokens=128较短，TTR随文本长度增加而单调递减，需使用Root-TTR或MTL

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

TTR（Type-Token Ratio）的样本量偏差校正：由于max_tokens=128较短，TTR随文本长度增加而单调递减，需使用Root-TTR或MTLD（Measure of Textual Lexical Diversity）作为更稳定的多样性指标，避免短文本导致的TTR虚高

## Corrected Claim

TTR（Type-Token Ratio）的样本量偏差校正：由于max_tokens=128较短，TTR随文本长度增加而单调递减，需使用Root-TTR或MTLD（Measure of Textual Lexical Diversity）作为更稳定的多样性指标，避免短文本导致的TTR虚高

## Evidence

先验知识/题面给定，逻辑校验通过：TTR随样本量增加单调递减是统计学基本性质，Root-TTR和MTLD确实是用于校正长度偏差的标准指标，逻辑自洽且符合语言学常识。
