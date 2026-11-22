# N206: 长序列推理中峰值内存波动（Peak Memory Spikes）的来源与量化：主要来源于 Prefill 阶段的激活值（Activations）和 LayerN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54, N56, N57

## Claim

长序列推理中峰值内存波动（Peak Memory Spikes）的来源与量化：主要来源于 Prefill 阶段的激活值（Activations）和 LayerNorm/GEMM 中间临时张量。对于 32K 上下文，Prefill 阶段激活值峰值约为 $0.5 - 1.5$GB（取决于 Batch Size 和模型结构），且该峰值是瞬时的。若硬件显存余量 $< 1.5$GB，可能导致 OOM 崩溃，因此安全缓冲下限应设为 $2$GB 以覆盖此瞬态峰值。

## Corrected Claim

长序列推理中峰值内存波动（Peak Memory Spikes）的来源与量化：主要来源于 Prefill 阶段的激活值（Activations）和 LayerNorm/GEMM 中间临时张量。对于 32K 上下文，Prefill 阶段激活值峰值约为 $0.5 - 1.5$GB（取决于 Batch Size 和模型结构），且该峰值是瞬时的。若硬件显存余量 $< 1.5$GB，可能导致 OOM 崩溃，因此安全缓冲下限应设为 $2$GB 以覆盖此瞬态峰值。

## Evidence

先验知识/题面给定，逻辑校验通过
