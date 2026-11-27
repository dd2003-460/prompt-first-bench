# N88: FP8精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.80-0.85，因FP8反量化路径引入额外计算开销，实际吞吐

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20, N21, N24

## Claim

FP8精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.80-0.85，因FP8反量化路径引入额外计算开销，实际吞吐量基准需乘以该因子。

## Corrected Claim

FP8精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率会因FP8反量化路径引入额外计算开销而低于理论峰值，实际吞吐量基准需根据具体实现乘以相应的修正因子（通常低于1.0）。

## Evidence

[质询]该修正因子（0.80-0.85）属于具体的经验性能参数，缺乏通用物理定律或第一性原理支持，且不同硬件架构、驱动版本及具体算子实现下，FP8反量化的开销比例存在显著差异，固定区间可能过于武断。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 FP8 LLM inference bandwidth utilization efficiency factor
