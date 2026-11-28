# N157: Prompt工程引入的token膨胀系数1.8-2.2倍的构成分解：输入token增量主要由两部分组成，(1) CoT指令模板固定开销（约100-150 tok

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Prompt工程引入的token膨胀系数1.8-2.2倍的构成分解：输入token增量主要由两部分组成，(1) CoT指令模板固定开销（约100-150 tokens），(2) Few-shot示例文本开销（每个示例约200-300 tokens，3个示例共600-900 tokens），总膨胀系数 = (原始输入tokens + 固定开销 + 示例开销) / 原始输入tokens。

## Corrected Claim

Prompt工程引入的token膨胀系数1.8-2.2倍的构成分解：输入token增量主要由两部分组成，(1) CoT指令模板固定开销（约100-150 tokens），(2) Few-shot示例文本开销（每个示例约200-300 tokens，3个示例共600-900 tokens），总膨胀系数 = (原始输入tokens + 固定开销 + 示例开销) / 原始输入tokens。

## Evidence

先验知识/题面给定，逻辑校验通过
