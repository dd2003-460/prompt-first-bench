# N22: NVIDIA RTX 4090 (24 GB) 的 BF16 Tensor Core 峰值算力为 82.6 TFLOPS，FP8 峰值算力为 165.2 TFL

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

NVIDIA RTX 4090 (24 GB) 的 BF16 Tensor Core 峰值算力为 82.6 TFLOPS，FP8 峰值算力为 165.2 TFLOPS，INT8 峰值算力为 330.3 TOPS。

## Corrected Claim

NVIDIA RTX 4090 (24 GB) 的 BF16 Tensor Core 峰值算力为 82.6 TFLOPS，FP8 峰值算力为 165.2 TFLOPS，INT8 峰值算力为 330.3 TOPS。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性违背：子节点N22包含大量非结构化的纠错叙述（如'中声称...是错误的'、'修正自矛盾检测'），且其核心事实（不支持原生FP8）与父节点（声称FP8为165.2 TFLOPS）直接矛盾，导致逻辑冲突而非正交分解。2. 完备性缺失：父节点包含BF16、FP8、INT8三个指标，但子节点完全遗漏了INT8 330.3 TOPS这一关键数据，且未对BF16和FP8进行对等的有效算力/利用率分析，导致信息覆盖不全。3. 子节点N22格式不规范，包含无关的元数据描述。）
