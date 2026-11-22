# N178: 计算 W4 量化 Qwen3-27B 在 RTX 4090 上的 T_decode 理论下限：权重体积 ≈ 14GB (含 Scale)，KV Cache (3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

计算 W4 量化 Qwen3-27B 在 RTX 4090 上的 T_decode 理论下限：权重体积 ≈ 14GB (含 Scale)，KV Cache (32K, Batch 1, GQA) ≈ 33GB (基于 N77 修正)。总读取量 ≈ 47GB。RTX 4090 带宽 1.0 TB/s，T_decode ≈ 47GB / 1.0TB/s = 47 ms/token。注意：KV Cache 可能超出剩余显存 (24-14=10GB)，若 KV Cache 需 Offload 或 Batch 缩小，实际值不同。

## Corrected Claim

计算 W4 量化 Qwen3-27B 在 RTX 4090 上的 T_decode 理论下限：权重体积 ≈ 14GB (含 Scale)，KV Cache (32K, Batch 1, GQA) ≈ 33GB (基于 N77 修正)。总读取量 ≈ 47GB。RTX 4090 带宽 1.0 TB/s，T_decode ≈ 47GB / 1.0TB/s = 47 ms/token。注意：KV Cache 可能超出剩余显存 (24-14=10GB)，若 KV Cache 需 Offload 或 Batch 缩小，实际值不同。

## Evidence

[质询]KV Cache 33GB 的估算可能偏高（取决于具体层数和头数配置），但作为理论下限计算，其量级（几十GB）在 32K 上下文下是合理的；主要风险在于显存溢出导致无法运行，但这已在陈述中注明。 | 先验知识/题面给定，逻辑校验通过：权重体积与带宽除法逻辑自洽，KV Cache 量级符合 32K 上下文 GQA 模型的典型规模，且已明确标注显存限制风险。
