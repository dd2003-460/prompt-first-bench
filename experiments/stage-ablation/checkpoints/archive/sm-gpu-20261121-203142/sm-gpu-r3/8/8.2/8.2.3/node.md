# N347: B200 实际 TPS 提升受限于计算单元效率差异：B200 的 BF16 算力约为 H100 的 2.5 倍 (具体数值需核验，假设 ~2000 TFLOPS

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N112

## Claim

B200 实际 TPS 提升受限于计算单元效率差异：B200 的 BF16 算力约为 H100 的 2.5 倍 (具体数值需核验，假设 ~2000 TFLOPS vs 989 TFLOPS)，但在 Decode 阶段为 Memory-bound，计算单元利用率较低；若带宽利用率维持在 75-85%，则实际 TPS 约为 103-117 tokens/s，相比 H100 实际 43-49 tokens/s，提升倍数约为 2.4-2.7 倍，略高于纯带宽倍数，因 B200 内存控制器效率可能更优

## Corrected Claim

B200 的 BF16 算力显著高于 H100（约2.5倍），但在 Decode 阶段为 Memory-bound，计算单元利用率较低；实际 TPS 提升主要受限于内存带宽及控制器效率，通常略高于纯带宽倍数，具体数值取决于模型大小和硬件配置。

## Evidence

[质询]具体数值（如B200 ~2000 TFLOPS、H100 989 TFLOPS、具体TPS范围）属于经验事实，缺乏来源支持，且不同模型大小和配置下TPS差异巨大，直接给出固定数值范围缺乏严谨性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVIDIA B200 vs H100 LLM inference throughput benchmark memory bound
