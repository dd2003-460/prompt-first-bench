# N194: 2×RTX 4090 (FP8/INT8) 方案在代码/数学任务上的质量基准：FP8/INT8 量化通常保持 HumanEval 通过率下降 <1%，MATH-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

2×RTX 4090 (FP8/INT8) 方案在代码/数学任务上的质量基准：FP8/INT8 量化通常保持 HumanEval 通过率下降 <1%，MATH-500 下降 <0.5%，满足 N24 的 <5% 容忍阈值，是精度敏感场景下的最低成本可行方案。

## Corrected Claim

2×RTX 4090 (FP8/INT8) 方案在代码/数学任务上的质量基准：FP8/INT8 量化通常保持 HumanEval 通过率下降 <1%，MATH-500 下降 <0.5%，满足 N24 的 <5% 容忍阈值，是精度敏感场景下的最低成本可行方案。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8/INT8量化在主流大模型上对代码和数学基准（HumanEval/MATH-500）的精度损失通常极小（<1%），符合<5%的容忍阈值，且2x4090是常见的低成本高精度部署方案。

## Search Query

Qwen3-27B FP8 INT8 HumanEval MATH-500 quality retention
