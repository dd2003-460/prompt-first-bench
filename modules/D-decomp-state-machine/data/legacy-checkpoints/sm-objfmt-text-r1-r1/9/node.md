# N22: 首字延迟 (TTFT) 主要受限于 Prefill 阶段的算力 (FLOPS)，计算公式近似为 TTFT_ms ≈ (Seq_Len * Model_Size 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

首字延迟 (TTFT) 主要受限于 Prefill 阶段的算力 (FLOPS)，计算公式近似为 TTFT_ms ≈ (Seq_Len * Model_Size * 2 * FLOPs_per_Flop) / (GPU_FLOPS * Batch_Size_Efficiency)；对于 32K context，Prefill 阶段耗时占比极高，因此高算力 GPU (如 H100 > A100 > 4090) 在长文本场景下 TTFT 优势明显，而 TPOT (每 token 生成时间) 主要受限于显存带宽。

## Corrected Claim

首字延迟 (TTFT) 主要受限于 Prefill 阶段的算力 (FLOPS)。对于长上下文（如 32K），Prefill 阶段耗时占比极高，高算力 GPU (如 H100) 在此场景下优势明显；而 TPOT 主要受限于显存带宽。具体耗时需结合模型架构、序列长度及硬件特性综合评估，简化公式仅供参考。

## Evidence

[质询]公式中 'FLOPs_per_Flop' 术语冗余且定义模糊（通常应为 FLOPs_per_token 或隐含系数），且 Batch_Size_Efficiency 在 Prefill 阶段并非简单的线性分母关系，而是受限于显存容量和计算并行度，该简化公式在工程实践中缺乏严谨性。 | 来源 [1] 确认了 TTFT 主要由 Prefill 阶段决定，但未提供具体的 FLOPS 计算公式，且该公式属于经验性估算模型，非第一性原理严格推导，故降级。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2045607023673450979&rut=a8d8fbb6b8f8f452a4464b3c56e1f876e6482e7d3ca75047efcfcf4f87038add', 'type': 'ddg', 'title': '首Token延迟（TTFT）优化：从原理到工程实践 - 知乎'}
