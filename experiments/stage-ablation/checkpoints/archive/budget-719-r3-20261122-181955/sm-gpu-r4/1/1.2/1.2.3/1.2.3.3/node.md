# N158: H100 SXM5 在 FP8 精度下的 BF16 等效算力为 1979 TFLOPS (稠密) / 3958 TFLOPS (稀疏) [待核验]，其理论 Pr

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

H100 SXM5 在 FP8 精度下的 BF16 等效算力为 1979 TFLOPS (稠密) / 3958 TFLOPS (稀疏) [待核验]，其理论 Prefill 吞吐量约为 563 tokens/s (稠密)，是 BF16 方案的 2 倍，但 H100 的 FP8 支持需确认 Qwen3-27B 在 FP8 下的精度损失是否满足 <2% 阈值，且 H100 价格约为 $30,000-$40,000，TCO 优势可能不足以抵消性能提升。

## Corrected Claim

H100 SXM5 在 FP8 精度下的理论算力为 1979 TFLOPS (稠密) / 3958 TFLOPS (稀疏)。其实际 Prefill 吞吐量取决于具体实现和负载，约为 BF16 方案的 2 倍（理论上限）。Qwen3-27B 在 FP8 下的精度损失需实测验证，通常可能在 1%-3% 之间波动，不一定严格满足 <2% 阈值。H100 市场价格约为 $30,000-$40,000，TCO 优势需结合具体业务场景评估。

## Evidence

[质询]H100 SXM5 的 FP8 稠密算力官方规格通常为 1979 TFLOPS，但稀疏算力通常为 3958 TFLOPS 的 2 倍即 3958 TFLOPS 是 BF16 稀疏值，FP8 稀疏值应为 3958 TFLOPS 的 2 倍即 3958 TFLOPS? 不，H100 SXM5 FP8 稠密是 1979 TFLOPS，稀疏是 3958 TFLOPS。这里陈述说 FP8 等效算力为 1979 (稠密) / 3958 (稀疏)，这与 NVIDIA 官方 H100 SXM5 规格一致。但是，Prefill 吞吐量 563 tokens/s 是一个高度依赖模型架构、序列长度、Batch Size 和具体实现（如 FlashAttention 版本）的经验值，无法从算力直接推导，且 Qwen3-27B 在 FP8 下的精度损失 <2% 是一个未经证实的经验假设，不同数据集和任务下波动较大。此外，H100 价格 $30,000-$40,000 是市场波动值，非固定事实。 | 来源 [1] 仅列出 GPU 列表，未提供 H100 具体算力数值或 Qwen3 精度数据，无法直接支持；FP8 算力数值符合 NVIDIA 公开规格（逻辑自洽），但吞吐量、精度损失阈值及价格均为经验事实，缺乏来源直接支持，故降级。

## Search Query

H100 FP8 tensor core performance TFLOPS dense sparse

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units', 'type': 'wikipedia', 'title': 'List of Nvidia graphics processing units'}
