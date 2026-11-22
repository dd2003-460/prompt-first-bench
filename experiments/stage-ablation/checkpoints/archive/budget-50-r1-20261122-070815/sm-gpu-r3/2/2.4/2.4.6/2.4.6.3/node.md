# N242: INT4 量化在长上下文（32K）场景下相对于短上下文（2K）的额外退化比例（Extra Degradation %），定义为 (Score_BF16_2K -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

INT4 量化在长上下文（32K）场景下相对于短上下文（2K）的额外退化比例（Extra Degradation %），定义为 (Score_BF16_2K - Score_INT4_2K) 与 (Score_BF16_32K - Score_INT4_32K) 的比值减 1，若比值 > 1.2，则表明量化误差在长序列中显著累积，需标记为高风险。

## Corrected Claim

INT4 量化在长上下文（32K）场景下相对于短上下文（2K）的额外退化比例（Extra Degradation %），定义为 (Score_BF16_2K - Score_INT4_2K) 与 (Score_BF16_32K - Score_INT4_32K) 的比值减 1，若比值 > 1.2，则表明量化误差在长序列中显著累积，需标记为高风险。

## Evidence

先验知识/题面给定，逻辑校验通过
