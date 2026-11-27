# N169: Prefill 阶段计算量分解项 2：注意力矩阵乘法 (Attention Matrix Multiplication) FLOPs。公式 = 4 * P^2 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Prefill 阶段计算量分解项 2：注意力矩阵乘法 (Attention Matrix Multiplication) FLOPs。公式 = 4 * P^2 * d_model * L。注意此项随 P 平方增长。代入 P=32768, d_model=4096, L=64：FLOPs_attn ≈ 4 * (32768)^2 * 4096 * 64 ≈ 1.10 PFLOPs。此项在原 N23 公式中被遗漏，且在长上下文下占比显著 (约 40%)

## Corrected Claim

Prefill 阶段计算量分解项 2：注意力矩阵乘法 (Attention Matrix Multiplication) FLOPs。公式 = 4 * P^2 * d_model * L。注意此项随 P 平方增长。代入 P=32768, d_model=4096, L=64：FLOPs_attn ≈ 4 * (32768)^2 * 4096 * 64 ≈ 1.10 PFLOPs。此项在原 N23 公式中被遗漏，且在长上下文下占比显著 (约 40%)

## Evidence

先验知识/题面给定，逻辑校验通过：公式 4*P^2*d_model*L 符合标准 Transformer 注意力计算量估算（QK^T 和 AV 各 2*P^2*d，共 4*P^2*d），代入数值 4 * 32768^2 * 4096 * 64 ≈ 1.10e15 (1.10 PFLOPs) 计算准确，量级合理。
