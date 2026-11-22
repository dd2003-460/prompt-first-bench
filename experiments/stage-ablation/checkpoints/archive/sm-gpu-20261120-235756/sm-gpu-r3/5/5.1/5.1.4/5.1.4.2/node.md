# N285: 在 32K 上下文、Batch Size=1 场景下，vLLM PagedAttention 的基线 TTFT 估算值：TTFT_base = (Prefill

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

在 32K 上下文、Batch Size=1 场景下，vLLM PagedAttention 的基线 TTFT 估算值：TTFT_base = (Prefill_FLOPs / GPU_TFLOPS) + (KV_Storage_Time)，其中 Prefill_FLOPs = 2 * 27.18e9 * 32768，需结合具体硬件（如 RTX 4090 FP8）的 Prefill 实测吞吐（Tokens/s）计算，通常比 Decode 阶段慢 10-20 倍。

## Corrected Claim

在 32K 上下文、Batch Size=1 场景下，vLLM PagedAttention 的基线 TTFT 估算值：TTFT_base = (Prefill_FLOPs / GPU_TFLOPS) + (KV_Storage_Time)，其中 Prefill_FLOPs = 2 * 27.18e9 * 32768，需结合具体硬件（如 RTX 4090 FP8）的 Prefill 实测吞吐（Tokens/s）计算，通常比 Decode 阶段慢 10-20 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill FLOPs 公式符合 Transformer 计算量估算标准（2*Params*SeqLen），TTFT 构成逻辑自洽，且 Prefill 比 Decode 慢 10-20 倍符合大模型推理的一般工程经验（Prefill 计算密集，Decode 访存密集，且 Batch=1 时 Decode 吞吐极低）。

## Search Query

vLLM PagedAttention prefill latency 32k context RTX 4090 benchmark
