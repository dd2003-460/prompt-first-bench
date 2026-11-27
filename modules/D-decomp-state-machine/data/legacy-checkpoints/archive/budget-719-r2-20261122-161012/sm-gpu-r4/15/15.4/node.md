# N324: H100 SXM 的 BF16 Tensor Core 峰值算力为 989 TFLOPS，是 RTX 5090 的约 9.4 倍，因此在纯 TTFT 性能上 H

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

H100 SXM 的 BF16 Tensor Core 峰值算力为 989 TFLOPS，是 RTX 5090 的约 9.4 倍，因此在纯 TTFT 性能上 H100 具有绝对优势，但需结合其高昂的 Capex 计算性价比。

## Corrected Claim

H100 SXM 的 BF16 Tensor Core 峰值算力为 989 TFLOPS，显著高于 RTX 5090（约为其 9-10 倍量级），在计算密集型场景下具有算力优势，但 TTFT 实际性能还需考虑内存带宽与软件优化，且需结合高昂 Capex 评估性价比。

## Evidence

[质询]RTX 5090 的 BF16 Tensor Core 峰值算力具体数值（约 105 TFLOPS）属于经验事实，且不同来源对是否计入稀疏加速或特定精度支持存在口径差异，导致倍数计算（9.4倍）可能存在偏差；此外，'纯 TTFT 性能'受内存带宽、显存容量及软件栈优化影响极大，仅凭峰值算力断定'绝对优势'在逻辑上过于简化。 | H100 SXM BF16 峰值算力 989 TFLOPS 为公认稳定参数，逻辑自洽；但 RTX 5090 具体算力及倍数关系缺乏本轮来源支持，且 TTFT 性能与峰值算力非简单线性关系，故降级。
