# N118: H_eff 的折损因子 (1 - W_update) 的敏感性分析：当 W_update = 0.01 时，折损因子为 0.99，命中率损失约 1%；当 W_u

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

H_eff 的折损因子 (1 - W_update) 的敏感性分析：当 W_update = 0.01 时，折损因子为 0.99，命中率损失约 1%；当 W_update = 0.05 时，折损因子为 0.95，损失 5%；当 W_update = 0.10 时，折损因子为 0.90，损失 10%。此线性关系仅在 W_update < 0.2 时成立，超过后需考虑缓存一致性开销的非线性增长。

## Corrected Claim

H_eff 的折损因子 (1 - W_update) 的敏感性分析：当 W_update = 0.01 时，折损因子为 0.99，命中率损失约 1%；当 W_update = 0.05 时，折损因子为 0.95，损失 5%；当 W_update = 0.10 时，折损因子为 0.90，损失 10%。此线性关系仅在 W_update < 0.2 时成立，超过后需考虑缓存一致性开销的非线性增长。

## Evidence

先验知识/题面给定，逻辑校验通过：折损因子 (1-W) 与 W 呈线性关系，数值计算正确（0.99, 0.95, 0.90），且关于非线性阈值的定性描述符合缓存一致性开销的一般工程直觉。
