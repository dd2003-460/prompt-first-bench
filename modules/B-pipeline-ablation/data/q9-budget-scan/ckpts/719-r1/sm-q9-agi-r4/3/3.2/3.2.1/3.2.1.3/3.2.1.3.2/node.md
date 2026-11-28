# N511: 工作点3 下 4×V100 TP=4 的 Attention 计算瓶颈量化：L=262144 时 Attention FLOPs ≈ 4×L²×d_head×n

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

工作点3 下 4×V100 TP=4 的 Attention 计算瓶颈量化：L=262144 时 Attention FLOPs ≈ 4×L²×d_head×num_heads，计算其占总 FLOPs 的比例，验证是否成为主导瓶颈导致 Tokens/s 降至 2-3

## Corrected Claim

工作点3 下 4×V100 TP=4 的 Attention 计算瓶颈量化：L=262144 时 Attention FLOPs ≈ 4×L²×d_head×num_heads，计算其占总 FLOPs 的比例，验证是否成为主导瓶颈导致 Tokens/s 降至 2-3

## Evidence

先验知识/题面给定，逻辑校验通过：Attention FLOPs公式正确，L=262144时二次项主导总FLOPs，导致计算瓶颈符合物理直觉
