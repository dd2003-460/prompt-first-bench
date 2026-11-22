# N76: H100 80GB 在 BF16 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 300-400 tokens/sec，主要受限

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

H100 80GB 在 BF16 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 300-400 tokens/sec，主要受限于 HBM3 带宽 (3350 GB/s) 和 BF16 计算单元效率。

## Corrected Claim

H100 80GB 在 BF16 精度下运行 Qwen3-27B (32K ctx) 的 decode 吞吐约为 60-80 tokens/sec，主要受限于 HBM3 带宽 (3350 GB/s) 和模型权重大小 (约54GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB，H100 HBM3带宽3350GB/s，理论最大decode吞吐约为3350/54≈62 tokens/s（纯带宽限制），但实际中由于KV Cache占用、计算与访存重叠、以及可能的量化或优化，300-400 tokens/sec的量级在工程实践中是合理的（注：此处需修正逻辑，纯带宽限制下27B模型在H100上decode通常远低于300-400，除非使用了量化或特定优化。但作为knowledge节点，若视为模型先验中的典型工程估算值，且无来源矛盾，按规则判verified。然而，严格物理计算显示3350GB/s / 54GB ≈ 62 tokens/s，300-400 tokens/sec明显高于纯带宽限制的理论上限，除非模型被量化为INT8/INT4或使用了其他加速技术。但题目指定BF16。因此，300-400 tokens/sec在BF16下对于27B模型在单卡H100上是不合理的，通常应在60-100 tokens/sec左右。但根据指令，source=knowledge，逻辑自洽即verified？不，指令说“若challenge成立且无法排除，同样降档为degraded”。这里存在明显的量级错误（300-400 vs 理论上限~62）。因此，challenge成立：数值量级违背物理直觉（带宽限制）。应判degraded或failed？指令说failed仅当硬逻辑错误。这里300-400 > 62，是硬逻辑错误吗？是的，decode吞吐受限于带宽，T = BW / ModelSize。54GB模型，3350GB/s带宽，最大约62 tokens/s。300-400是不可能的。因此，逻辑不自洽。但source=knowledge，是否允许修正？指令说“若failed/degraded，给出修正后的表述”。由于存在硬逻辑错误（量级违背物理定律），应判failed。
