# N99: NVIDIA H100 80GB SXM 方案在 Qwen3-27B BF16 精度下的理论解码吞吐上限为 145.5 tokens/s (基于 54GB 权重

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

NVIDIA H100 80GB SXM 方案在 Qwen3-27B BF16 精度下的理论解码吞吐上限为 145.5 tokens/s (基于 54GB 权重 / 3350GB/s HBM3 带宽)，实际实测吞吐约为 100-110 tokens/s；其硬件成本约为 A100 的 2.5-3 倍 ($25,000-$30,000 vs $10,000-$15,000)，但每美元获得的吞吐量 (tokens/s per $) 低于 A100，仅在需要极低延迟或极高并发时具备 TCO 优势。

## Corrected Claim

NVIDIA H100 80GB SXM 方案在 Qwen3-27B BF16 精度下的理论解码吞吐上限约为 145.5 tokens/s，实际实测吞吐通常在 100-200+ tokens/s 之间（视并发和实现而定）；其硬件成本约为 A100 的 2-2.5 倍，但在大多数场景下每美元获得的吞吐量（tokens/s per $）高于 A100，具备显著的 TCO 优势。

## Evidence

[质询]数值量级与成本对比存在显著偏差：1. H100 SXM 价格通常在 $30k-$40k 区间，A100 为 $15k-$20k，2.5-3倍的说法偏低；2. Qwen3-27B 在 H100 上的实测解码吞吐通常高于 110 tokens/s（取决于具体实现和 batch size，单流可能更高，多流聚合更高），100-110 的区间可能过于保守或特定于极低并发场景；3. '每美元吞吐量低于 A100' 的结论在多数基准测试中不成立，H100 通常具有更高的性价比（TCO 优势更明显）。 | 先验知识/题面给定，逻辑校验通过，但具体数值（价格、吞吐）与当前市场主流数据存在偏差，且无外部来源支持，故降级。
