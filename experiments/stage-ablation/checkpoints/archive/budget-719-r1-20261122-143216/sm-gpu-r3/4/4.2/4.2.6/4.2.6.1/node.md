# N292: Qwen3-27B NVFP4/W4 量化输出分布与 BF16 输出分布的 KL 散度计算公式：同 N151，但需特别注意 W4 量化因位宽极低，Logits 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

Qwen3-27B NVFP4/W4 量化输出分布与 BF16 输出分布的 KL 散度计算公式：同 N151，但需特别注意 W4 量化因位宽极低，Logits 分布可能出现长尾截断，导致 KL 散度在低概率 Token 上计算不稳定，需设定概率阈值（如 P>0.01）进行截断计算

## Corrected Claim

Qwen3-27B NVFP4/W4 量化输出分布与 BF16 输出分布的 KL 散度计算公式：同 N151，但需特别注意 W4 量化因位宽极低，Logits 分布可能出现长尾截断，导致 KL 散度在低概率 Token 上计算不稳定，需设定概率阈值（如 P>0.01）进行截断计算

## Evidence

先验知识/题面给定，逻辑校验通过：KL散度在低概率区域确实对数值误差敏感，W4量化易导致长尾截断，设定概率阈值是标准且合理的工程实践。
