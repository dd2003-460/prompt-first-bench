# N174: 计算 Qwen3-27B 在 BF16 精度下处理 32K prompt 的总 FLOPs：基于 Transformer 推理近似公式 Total_FLOPs 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

计算 Qwen3-27B 在 BF16 精度下处理 32K prompt 的总 FLOPs：基于 Transformer 推理近似公式 Total_FLOPs ≈ 2 * P * L，其中 P=27.2e9 (参数量), L=32768 (序列长度)，得出 Total_FLOPs ≈ 1.78e15 FLOPs (1.78 PFLOPs)。

## Corrected Claim

计算 Qwen3-27B 在 BF16 精度下处理 32K prompt 的总 FLOPs：基于 Transformer 推理近似公式 Total_FLOPs ≈ 2 * P * L，其中 P=27.2e9 (参数量), L=32768 (序列长度)，得出 Total_FLOPs ≈ 1.78e15 FLOPs (1.78 PFLOPs)。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 27.2e9 * 32768 = 1.778e15，数值量级与计算过程自洽。
