# N260: H100 SXM 单卡 (BF16) 方案在 32K 上下文下的 Prefill 延迟 (TTFT) 估算：基于 H100 BF16 算力 (989 TFLOP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

H100 SXM 单卡 (BF16) 方案在 32K 上下文下的 Prefill 延迟 (TTFT) 估算：基于 H100 BF16 算力 (989 TFLOPS dense, 实际利用率 ~50-70%)，TTFT ≈ 2.25e15 / (989e12 * 0.6) ≈ 3.8s，同样超出 2s 阈值，但优于双卡消费级方案；若采用 FlashAttention-2 优化，Prefill 阶段计算复杂度降低，TTFT 可能降至 2.5-3.0s，仍略高于严格阈值，需权衡是否接受或调整阈值至 3s。

## Corrected Claim

H100 SXM 单卡 (BF16) 方案在 32K 上下文下的 Prefill 延迟 (TTFT) 估算：基于 H100 BF16 算力 (989 TFLOPS dense, 实际利用率 ~50-70%)，TTFT ≈ 2.25e15 / (989e12 * 0.6) ≈ 3.8s，同样超出 2s 阈值，但优于双卡消费级方案；若采用 FlashAttention-2 优化，Prefill 阶段计算复杂度降低，TTFT 可能降至 2.5-3.0s，仍略高于严格阈值，需权衡是否接受或调整阈值至 3s。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1修正了计算量（FLOPs）的估算错误，节点2修正了硬件利用率（MFU）的假设，节点3基于前两者的修正结果重新计算并得出了与父节点相反的结论。三者分别对应公式中的分子、分母参数及最终结果，无重复或矛盾，且完整覆盖了父节点中涉及的所有关键计算要素（算力、复杂度、阈值判断）。）
