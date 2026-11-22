# N321: 工作点C（修正后实际综合延迟）：结合N111/N112修正，RTX 4090 INT8实际延迟 = 17.1 ms (计算) + 33.2 ms (带宽) ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139

## Claim

工作点C（修正后实际综合延迟）：结合N111/N112修正，RTX 4090 INT8实际延迟 = 17.1 ms (计算) + 33.2 ms (带宽) ≈ 50.3 ms/token，吞吐约 19.9 tokens/s；相比N139原估38.1 ms/token，延迟增加32%，主要归因于权重大小误判（13.5GB vs 27GB）导致的带宽项低估。

## Corrected Claim

工作点C（修正后实际综合延迟）：结合N111/N112修正，RTX 4090 INT8实际延迟 = 17.1 ms (计算) + 33.2 ms (带宽) ≈ 50.3 ms/token，吞吐约 19.9 tokens/s；相比N139原估38.1 ms/token，延迟增加32%，主要归因于权重大小误判（13.5GB vs 27GB）导致的带宽项低估。

## Evidence

先验知识/题面给定，逻辑校验通过：17.1+33.2=50.3，1000/50.3≈19.9，(50.3-38.1)/38.1≈32%，数值自洽且归因逻辑合理。
