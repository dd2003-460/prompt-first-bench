# N230: Qwen3-27B 在 BF16 下 Prefill 阶段在 RTX 4090 上的实际吞吐量修正：理论峰值 330 TFLOPS / 540 TOPS = 0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N63

## Claim

Qwen3-27B 在 BF16 下 Prefill 阶段在 RTX 4090 上的实际吞吐量修正：理论峰值 330 TFLOPS / 540 TOPS = 0.61 TFLOP/token，考虑 MFU 40-60% 后，实际吞吐量为 330 * 0.5 / 540 ≈ 305 tokens/s，而非原估的 240-360 tokens/s 区间中心值。

## Corrected Claim

Qwen3-27B 在 BF16 下 Prefill 阶段在 RTX 4090 上的实际吞吐量需重新计算：若理论峰值为 330 TFLOPS，每 token 计算量为 540 GFLOP (0.54 TFLOP)，则理论上限约为 330/0.54 ≈ 611 tokens/s。考虑 MFU 40-60% 后，实际吞吐量约为 244-366 tokens/s。原陈述中 305 tokens/s 的数值虽在合理区间内，但推导过程 '330 * 0.5 / 540 ≈ 305' 存在数学错误（应为 0.305 或单位换算错误），且具体数值缺乏直接来源支持。

## Evidence

[质询]计算逻辑存在严重错误：330 * 0.5 / 540 的数学结果约为 0.305，而非 305。陈述中混淆了单位或数量级（可能误将 TFLOPS 当作 GFLOPS 或漏掉了 1000 倍的换算），导致最终吞吐量数值（305 tokens/s）与计算过程（0.305）严重不符，且 305 tokens/s 对于 27B 模型在单卡 4090 上的 Prefill 阶段而言，数值量级也偏高（通常 Prefill 受限于内存带宽和计算峰值，27B 模型在 4090 上 Prefill 吞吐通常在几十到一百多 tokens/s 量级，具体取决于序列长度和实现，但 305 这一具体数值缺乏可靠来源支持且计算过程自相矛盾）。 | 逻辑校验失败：330 * 0.5 / 540 ≈ 0.305，不等于 305。陈述中的数学推导存在数量级错误，且作为经验事实（具体吞吐量数值）缺乏来源支持，无法通过第一性原理直接验证其具体数值。
