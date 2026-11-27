# N262: RTX 4090 的 BF16 峰值算力 82.6 TFLOPS 是理论最大值，实际 Prefill 吞吐受限于 Tensor Core 利用率，通常有效算力为

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

RTX 4090 的 BF16 峰值算力 82.6 TFLOPS 是理论最大值，实际 Prefill 吞吐受限于 Tensor Core 利用率，通常有效算力为峰值的 60-75%（即 ~50-62 TFLOPS），需参考 vLLM 或 TensorRT-LLM 在 RTX 4090 上运行 7B-30B 模型的实测 Prefill 吞吐（tokens/s）反推有效算力系数 η_eff，以校准 N79 的延迟预测。

## Corrected Claim

RTX 4090 的 BF16 峰值算力约为 82.6 TFLOPS（需核实具体规格表），实际 Prefill 吞吐受限于 Tensor Core 利用率，有效算力通常低于峰值。建议参考 vLLM 或 TensorRT-LLM 在 RTX 4090 上运行 7B-30B 模型的实测 Prefill 吞吐（tokens/s）反推有效算力系数 η_eff，以校准 N79 的延迟预测。

## Evidence

[质询]该陈述包含具体的硬件规格（RTX 4090 BF16 峰值算力 82.6 TFLOPS）和具体的工程经验参数（有效算力系数 60-75%），属于经验事实。由于检索失败，无法通过外部来源验证这些具体数值是否准确或该范围是否适用于所有 7B-30B 模型的 Prefill 场景。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090 的 BF16 峰值算力量级（~80 TFLOPS）符合 Ada Lovelace 架构的一般认知，Prefill 阶段受 Tensor Core 利用率限制导致有效算力低于峰值符合物理直觉，但具体数值和系数范围缺乏本轮检索来源的直接支持。

## Search Query

RTX 4090 LLM inference prefill throughput benchmark vLLM TensorRT-LLM effective TFLOPS
