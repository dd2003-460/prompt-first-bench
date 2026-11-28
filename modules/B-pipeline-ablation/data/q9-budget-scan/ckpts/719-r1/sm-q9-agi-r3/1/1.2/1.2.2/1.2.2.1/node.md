# N125: Needle-in-a-Haystack 测试中'开头位置'与'中间位置'的标准化定义：开头指上下文的前 5% tokens（即 128K 中的前 6.4K），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Needle-in-a-Haystack 测试中'开头位置'与'中间位置'的标准化定义：开头指上下文的前 5% tokens（即 128K 中的前 6.4K），中间指上下文的 40%-60% 区间（即 51.2K-76.8K），需在此定义下测量准确率差异

## Corrected Claim

Needle-in-a-Haystack 测试中'开头位置'与'中间位置'的标准化定义：开头指上下文的前 5% tokens（即 128K 中的前 6.4K），中间指上下文的 40%-60% 区间（即 51.2K-76.8K），需在此定义下测量准确率差异

## Evidence

先验知识/题面给定，逻辑校验通过：128K * 5% = 6.4K，128K * 40% = 51.2K，128K * 60% = 76.8K，数值计算准确，符合长上下文测试中常见的分段定义逻辑。

## Search Query

needle in a haystack test position definition beginning middle context length
