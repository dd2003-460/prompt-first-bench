# N190: CPU Offloading 在 Decode 阶段的具体执行机制：区分 'Weight-Only Offload'（每层推理前从 CPU 加载权重到 GPU）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

CPU Offloading 在 Decode 阶段的具体执行机制：区分 'Weight-Only Offload'（每层推理前从 CPU 加载权重到 GPU）与 'KV-Cache Offload'（KV 留在 GPU，仅权重卸载），计算单层权重加载延迟 T_layer = Weight_Size_Per_Layer / PCIe_Bandwidth，对于 Qwen3-27B (64层, 27.2B参数, BF16)，单层权重约 0.85GB，PCIe 4.0 x16 有效带宽 50GB/s，T_layer ≈ 17ms

## Corrected Claim

CPU Offloading 在 Decode 阶段的具体执行机制：区分 'Weight-Only Offload'（每层推理前从 CPU 加载权重到 GPU）与 'KV-Cache Offload'（KV 留在 GPU，仅权重卸载），计算单层权重加载延迟 T_layer = Weight_Size_Per_Layer / PCIe_Bandwidth，对于 Qwen3-27B (64层, 27.2B参数, BF16)，单层权重约 0.85GB，PCIe 4.0 x16 有效带宽 50GB/s，T_layer ≈ 17ms

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 64层，27.2B参数，BF16下总权重约54.4GB，单层约0.85GB；PCIe 4.0 x16有效带宽50GB/s，T_layer = 0.85GB / 50GB/s ≈ 17ms，计算自洽。
