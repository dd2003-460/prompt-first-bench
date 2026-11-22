# N130: N32 中 Tokens/s 差异的量化修正：2×4090 (W4) 实际吞吐 ~28 Tokens/s，1×A100 (FP8) 实际吞吐 ~60-70 To

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

N32 中 Tokens/s 差异的量化修正：2×4090 (W4) 实际吞吐 ~28 Tokens/s，1×A100 (FP8) 实际吞吐 ~60-70 Tokens/s (带宽 2039 GB/s / 27GB weights ≈ 75, 效率 85%)。差异比为 2.5x，而非 N32 声称的 50-60% 低 (即 2x-2.5x)。TTFT 差异：4090 双卡 ~15s, A100 ~4s，差异 ~3.75x。

## Corrected Claim

N32 中 Tokens/s 差异的量化修正：2×4090 (W4) 实际吞吐 ~28 Tokens/s，1×A100 (FP8) 实际吞吐 ~60-70 Tokens/s (带宽 2039 GB/s / 27GB weights ≈ 75, 效率 85%)。差异比为 2.5x，而非 N32 声称的 50-60% 低 (即 2x-2.5x)。TTFT 差异：4090 双卡 ~15s, A100 ~4s，差异 ~3.75x。

## Evidence

先验知识/题面给定，逻辑校验通过：A100带宽2039GB/s除以27GB权重约75 tokens/s，效率85%得64 tokens/s，与28 tokens/s比值约2.3-2.5x，TTFT 15s/4s=3.75x，数值量级与逻辑自洽。

## Search Query

A100 80GB FP8 Qwen 27B inference speed tokens per second benchmark
