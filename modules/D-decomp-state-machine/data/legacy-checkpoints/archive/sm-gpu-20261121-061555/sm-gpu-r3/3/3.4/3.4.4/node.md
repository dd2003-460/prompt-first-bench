# N90: NVFP4精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.70-0.75，因NVFP4反量化路径更复杂，实际吞吐量

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20, N21, N24

## Claim

NVFP4精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率修正因子为0.70-0.75，因NVFP4反量化路径更复杂，实际吞吐量基准需乘以该因子。

## Corrected Claim

NVFP4精度下Qwen3-27B在H100 (80GB HBM3)上的有效显存带宽利用率会因反量化路径复杂而低于理论峰值，实际吞吐量基准需乘以小于1的修正因子（具体数值需根据实际基准测试确定，通常低于0.8）。

## Evidence

[质询]该修正因子（0.70-0.75）属于具体的经验性能参数，缺乏公开基准测试数据的直接支持，且不同硬件实现和软件栈下反量化开销差异较大，该具体数值范围可能过于精确或基于特定未公开环境。 | 先验知识/题面给定，逻辑校验通过（反量化确实增加计算开销，导致有效带宽利用率低于理论峰值，量级合理），但作为经验事实缺乏外部来源直接支持具体数值。

## Search Query

H100 NVFP4 LLM inference bandwidth utilization efficiency factor
