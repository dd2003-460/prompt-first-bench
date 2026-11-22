# N146: Qwen3-27B 在 Ada 架构 (RTX 4090) 上通过软件模拟 (如 vLLM FP8 emulation 或 Marlin kernel) 运行 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Qwen3-27B 在 Ada 架构 (RTX 4090) 上通过软件模拟 (如 vLLM FP8 emulation 或 Marlin kernel) 运行 FP8 模型时的实际吞吐量 (tokens/s) 与 BF16 吞吐量的比值，以量化 10-20% 损失的具体数值

## Corrected Claim

Qwen3-27B 在 Ada 架构 (RTX 4090) 上通过软件模拟运行 FP8 模型时的实际吞吐量与 BF16 吞吐量的比值缺乏具体数据支持；现有来源显示在 RTX 4090 上 FP8 通常比 BF16 更快（如来源[1]显示快42%），而非存在10-20%的损失。

## Evidence

[质询]来源[1]显示在RTX 4090上FP8比BF16快42%，这与陈述中隐含的'10-20%损失'（即FP8更慢或仅略快）存在方向性矛盾；且来源未提供Qwen3-27B在Ada架构上通过软件模拟FP8的具体吞吐量比值数据，无法验证'10-20%损失'这一具体数值。 | 来源[1]直接测量了RTX 4090上FP8 vs BF16的性能，但显示FP8更快（42%），与'损失'表述矛盾；来源[2]提供硬件规格但未提供具体模型吞吐量比值；来源[3]讨论精度损失而非吞吐量。所有来源均未提供Qwen3-27B在Ada架构上软件模拟FP8的具体吞吐量比值，无法支持'10-20%损失'的具体数值。

## Search Query

RTX 4090 FP8 emulation vs BF16 inference speed ratio vLLM

## Retrieval Sources

- {'url': 'https://www.tokenwatt.io/blog/fp8-vs-bf16-llm-inference.html&rut=8e19c8111d4297d0984617e7e8f1f190e62b459227c07492b034dd94bd0f5185', 'type': 'ddg', 'title': 'FP8 vs BF16 for LLM Inference: Measured Speed and Capacity'}
- {'url': 'https://inferencebench.io/gpus/nvidia-rtx-4090/&rut=a284dc34ecfc8d9cf57f554b9710fd7b1d75a399834817c27bbf8adcc329ff98', 'type': 'ddg', 'title': 'RTX 4090 — Inference Specs & Pricing | InferenceBench'}
- {'url': 'https://www.spheron.network/blog/fp8-vs-bf16-accuracy-loss/&rut=3b61e8f0756c12165b5b7d6e9e0e56b8c62d5f4ad477cd09118743199553c0cf', 'type': 'ddg', 'title': 'FP8 vs BF16: What You Actually Lose in Accuracy (2026) | Spheron'}
