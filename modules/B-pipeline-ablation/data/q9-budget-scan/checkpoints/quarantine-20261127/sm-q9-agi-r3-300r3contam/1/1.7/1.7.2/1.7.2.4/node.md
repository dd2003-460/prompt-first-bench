# N140: CosineSim 计算的数值稳定性修正：为防止零向量或极小范数导致的除零错误，计算前对 E 向量加 L2 归一化，若范数 < 1e-6 则视为无效输出，直接判

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

CosineSim 计算的数值稳定性修正：为防止零向量或极小范数导致的除零错误，计算前对 E 向量加 L2 归一化，若范数 < 1e-6 则视为无效输出，直接判定 Deviation=1.0。

## Corrected Claim

CosineSim 计算的数值稳定性修正：为防止零向量或极小范数导致的除零错误，计算前对 E 向量加 L2 归一化，若范数 < 1e-6 则视为无效输出，直接判定 Deviation=1.0。

## Evidence

先验知识/题面给定，逻辑校验通过：余弦相似度涉及除法，对零向量或极小范数进行阈值保护（如1e-6）并赋予最大偏差值（1.0）是标准的数值稳定性处理手段，符合工程实践逻辑。

## Search Query

cosine similarity numerical stability normalization zero vector handling
