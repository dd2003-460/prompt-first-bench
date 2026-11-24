# N1231: WebP 质量因子 q 从 60 降至 50 时的文件大小缩减比例 R_q_drop；根据经验公式，每降低 10 个质量点，文件大小约减少 10-15%，因此 

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N422

## Claim

WebP 质量因子 q 从 60 降至 50 时的文件大小缩减比例 R_q_drop；根据经验公式，每降低 10 个质量点，文件大小约减少 10-15%，因此 s_q50 ≈ 0.85 * s_q60，需计算 s_q50 是否满足 ≤ 150 KB 且 MOS 是否跌破 3.5。

## Corrected Claim

WebP 质量因子 q 从 60 降至 50 时的文件大小缩减比例 R_q_drop；根据经验公式，每降低 10 个质量点，文件大小约减少 10-15%，因此 s_q50 ≈ 0.85 * s_q60，需计算 s_q50 是否满足 ≤ 150 KB 且 MOS 是否跌破 3.5。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

WebP file size reduction per quality point drop
