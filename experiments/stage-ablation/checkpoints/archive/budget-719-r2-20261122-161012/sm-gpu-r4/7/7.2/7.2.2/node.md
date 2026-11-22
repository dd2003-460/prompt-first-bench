# N269: 在 FP8 精度下，RTX 4090 双卡 (TP=2) 方案权重约 27GB + 32K KV Cache 约 1GB，总占用 28GB < 48GB，可行；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

在 FP8 精度下，RTX 4090 双卡 (TP=2) 方案权重约 27GB + 32K KV Cache 约 1GB，总占用 28GB < 48GB，可行；理论 Decode 吞吐上限 = 2016 GB/s (双卡聚合带宽) / 28 GB ≈ 72 tokens/s，但受 PCIe 4.0 All-Reduce 同步开销限制，实际有效带宽利用率预计降至 60-70%，实际吞吐约 43-50 tokens/s [待核验]。

## Corrected Claim

在 FP8 精度下（注：RTX 4090 无原生 FP8 硬件加速，可能需软件模拟或回退），RTX 4090 双卡 (TP=2) 方案权重约 27GB + 32K KV Cache 约 1GB，总占用 28GB < 48GB，显存可行；理论 Decode 吞吐上限受显存带宽限制约为 72 tokens/s，但受 PCIe 4.0 All-Reduce 同步开销及 FP8 非原生支持影响，实际有效带宽利用率及吞吐可能显著低于 60-70% 的估算，实际吞吐可能远低于 43-50 tokens/s。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1修正了显存占用（KV Cache计算），子节点2基于修正后的显存重新计算了理论及实际吞吐上限，子节点3量化并论证了PCIe同步延迟对吞吐的影响机制（证明瓶颈不在同步延迟而在带宽/显存访问）。三者分别对应‘显存状态’、‘吞吐结果’、‘瓶颈归因/机制’，逻辑链条清晰且互不重叠，无矛盾，且覆盖了父节点中关于显存、吞吐估算和同步开销的所有关键方面。）
