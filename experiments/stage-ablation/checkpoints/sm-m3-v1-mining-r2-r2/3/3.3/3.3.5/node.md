# N27: 定义输入验证算法逻辑：input_value vs reference_distribution; if |input - mean| > k*std_dev 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N15, N16

## Claim

定义输入验证算法逻辑：input_value vs reference_distribution; if |input - mean| > k*std_dev OR |input - median| > 50% then flag='WARNING'

## Corrected Claim

定义输入验证算法逻辑：input_value vs reference_distribution; if |input - mean| > k*std_dev OR |input - median| > 50% then flag='WARNING'

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

data validation algorithm statistical deviation threshold
