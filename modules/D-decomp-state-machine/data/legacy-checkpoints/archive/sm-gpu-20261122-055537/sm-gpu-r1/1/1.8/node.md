# N14: 可行性过滤阈值：基于N11和N12的计算结果，确定各精度下满足32K上下文的最小显存需求。例如：BF16下需>54GB+KV Cache，FP8下需>27GB+

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

可行性过滤阈值：基于N11和N12的计算结果，确定各精度下满足32K上下文的最小显存需求。例如：BF16下需>54GB+KV Cache，FP8下需>27GB+KV Cache，W4下需>15GB+KV Cache，以此过滤掉显存不足的硬件（如16GB卡无法运行BF16/FP8 32K）。

## Corrected Claim

可行性过滤阈值：基于N11和N12的计算结果，确定各精度下满足32K上下文的最小显存需求。例如：BF16下需>54GB+KV Cache，FP8下需>27GB+KV Cache，W4下需>15GB+KV Cache，以此过滤掉显存不足的硬件（如16GB卡无法运行BF16/FP8 32K）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于大模型显存估算公式（权重显存+KV Cache），BF16/FP8/W4的权重显存比例关系（1:0.5:0.25）及32K上下文KV Cache开销符合工程常识，数值量级合理。
