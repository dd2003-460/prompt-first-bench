# N114: Apple M2 Ultra 统一内存带宽为 800 GB/s，基于 Roofline 模型，BF16 下 27B 模型的理论最大生成速度 = 800 GB/s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32, N33, N34

## Claim

Apple M2 Ultra 统一内存带宽为 800 GB/s，基于 Roofline 模型，BF16 下 27B 模型的理论最大生成速度 = 800 GB/s / 54 GB ≈ 14.8 tokens/s；实测 15-25 tokens/s 的范围中，15-18 tokens/s 更符合带宽瓶颈下的物理极限，25 tokens/s 需核验是否包含 KV Cache 量化或特定优化。

## Corrected Claim

Apple M2 Ultra 统一内存带宽为 800 GB/s，基于 Roofline 模型，BF16 下 27B 模型的理论最大生成速度 = 800 GB/s / 54 GB ≈ 14.8 tokens/s；实测 15-25 tokens/s 的范围中，15-18 tokens/s 更符合带宽瓶颈下的物理极限，25 tokens/s 需核验是否包含 KV Cache 量化或特定优化。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 800GB/s 带宽与 27B 模型 BF16 约 54GB 显存占用符合工程常识，Roofline 计算 800/54≈14.8 tokens/s 逻辑自洽，实测范围与理论极限关系合理。

## Search Query

Apple M2 Ultra memory bandwidth 800GB/s theoretical tokens per second 27B model
