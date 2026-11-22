# N442: NVIDIA L4 的显存容量与 Qwen3-27B 兼容性：L4 显存 24GB，INT8 权重 27GB，单卡不可行。2×L4 总显存 48GB，单卡负载 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N173

## Claim

NVIDIA L4 的显存容量与 Qwen3-27B 兼容性：L4 显存 24GB，INT8 权重 27GB，单卡不可行。2×L4 总显存 48GB，单卡负载 16.3GB，可行。但 L4 的 PCIe 4.0 x16 带宽为 32 GB/s (单向)，TP=2 通信开销占比 = (2 * 27B * 2bytes * 64layers) / (32 GB/s * 1000) ≈ 10.8ms/step，占 Decode 延迟 (1/50.4s ≈ 19.8ms) 的 54.5%，导致有效吞吐量下降至理论值的 45.5%，即 50.4 * 0.455 ≈ 22.9 tokens/s。

## Corrected Claim

NVIDIA L4 显存 24GB，INT8 权重约 27GB，单卡不可行。2×L4 总显存 48GB，单卡负载约 13.5GB（27GB/2），显存可行。但 L4 为 PCIe 4.0 x16 接口，带宽有限，TP=2 的通信开销会显著增加 Decode 延迟，具体吞吐量需实测，理论估算值 22.9 tokens/s 因计算模型错误而不准确。

## Evidence

[质询]TP=2 通信开销计算逻辑存在严重错误：1. 张量并行（TP）在 Decode 阶段通常仅涉及激活值（Activations）的 AllReduce，而非整个权重矩阵的传输；2. 即使按权重传输计算，公式中 `27B * 2bytes` 已包含参数量与精度，再乘以 `64layers` 属于重复计算（27B 是总参数量，不应再乘层数）；3. 将通信时间简单叠加并直接折算为吞吐量下降比例，忽略了计算与通信的潜在重叠及具体实现细节，属于过度简化的工程估算。 | 先验知识/题面给定，逻辑校验未通过：TP 通信开销计算模型错误（混淆了权重加载与推理时激活值通信，且参数量与层数重复计算），导致推导出的延迟占比和吞吐量数值不可信。
