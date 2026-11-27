# N358: AMD RX 7900 XTX 在 ROCm 环境下运行 BF16 LLM 推理时，由于缺乏针对 RDNA3 架构的专用 Tensor Core 优化 kern

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N141

## Claim

AMD RX 7900 XTX 在 ROCm 环境下运行 BF16 LLM 推理时，由于缺乏针对 RDNA3 架构的专用 Tensor Core 优化 kernel，其实际有效带宽利用率比 NVIDIA 同级硬件低约 15-25%，导致在相同显存容量下吞吐量下降，具体系数需通过 vLLM 在 ROCm 上的实测 tokens/s 与理论峰值之比确定。

## Corrected Claim

AMD RX 7900 XTX 在 ROCm 环境下运行 BF16 LLM 推理时，由于软件栈成熟度及针对 RDNA3 架构的优化 kernel 覆盖度低于 NVIDIA 同级硬件，其实际有效带宽利用率通常低于 NVIDIA 同级硬件，具体性能差距需通过 vLLM 在 ROCm 上的实测 tokens/s 与理论峰值之比确定。

## Evidence

[质询]该陈述包含具体的经验性数值范围（15-25%带宽利用率差异）和特定技术归因（缺乏RDNA3专用Tensor Core优化kernel），属于经验事实而非第一性原理可推导结论。在无任何参考来源支持的情况下，无法验证该具体数值范围和归因的准确性，且不同模型、不同序列长度下该差异可能波动较大，固定区间表述缺乏严谨性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

AMD RX 7900 XTX ROCm LLM inference performance vs NVIDIA benchmark
