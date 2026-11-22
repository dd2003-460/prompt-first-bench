# N621: AMD EPYC 9654 的 TDP 为 360W，在 LLM 推理负载下（CPU 密集型矩阵运算），实际平均功耗约为 TDP 的 80%-90%（即 288

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

AMD EPYC 9654 的 TDP 为 360W，在 LLM 推理负载下（CPU 密集型矩阵运算），实际平均功耗约为 TDP 的 80%-90%（即 288W-324W/颗），双路 CPU 总平均功耗约为 576W-648W，修正 N219 中 500-700W 的宽泛区间。

## Corrected Claim

AMD EPYC 9654 的 TDP 为 360W，在 LLM 推理负载下（CPU 密集型矩阵运算），实际平均功耗约为 TDP 的 80%-90%（即 288W-324W/颗），双路 CPU 总平均功耗约为 576W-648W，修正 N219 中 500-700W 的宽泛区间。

## Evidence

先验知识/题面给定，逻辑校验通过：AMD EPYC 9654 TDP 360W 符合官方规格，CPU 密集型负载下 80%-90% 的功耗占比符合工程经验，双路计算逻辑自洽。
