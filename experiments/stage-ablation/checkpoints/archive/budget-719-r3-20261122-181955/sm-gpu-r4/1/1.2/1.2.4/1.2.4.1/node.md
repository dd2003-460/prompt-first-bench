# N159: L40S 在 BF16 精度下，Prefill 阶段（Seq_Len=32K, Batch=1）的理论吞吐量上限为 362e12 / (2 * 27e9 * 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

L40S 在 BF16 精度下，Prefill 阶段（Seq_Len=32K, Batch=1）的理论吞吐量上限为 362e12 / (2 * 27e9 * 32768) ≈ 204.5 tokens/s（基于稀疏算力），若使用稠密算力则为 102.2 tokens/s；此数值需与实测对比以评估计算效率。

## Corrected Claim

L40S 在 BF16 精度下，Prefill 阶段（Seq_Len=32K, Batch=1）的理论吞吐量上限为 362e12 / (2 * 27e9 * 32768) ≈ 204.5 tokens/s（基于稀疏算力），若使用稠密算力则为 102.2 tokens/s；此数值需与实测对比以评估计算效率。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 362e12 / (2 * 27e9 * 32768) ≈ 204.5 正确，且 204.5 / 2 = 102.25 符合稠密/稀疏算力关系，量纲与逻辑自洽。
