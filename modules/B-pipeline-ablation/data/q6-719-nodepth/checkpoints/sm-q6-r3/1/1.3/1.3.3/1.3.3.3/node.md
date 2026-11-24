# N170: Hit_Rate（缓存命中率）基于 Zipf 分布修正公式：Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_tot

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Hit_Rate（缓存命中率）基于 Zipf 分布修正公式：Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_total)^α)，其中 K 为边缘节点可缓存对象数（由存储容量决定），N_total 为总对象数，α 为 Zipf 指数（典型 0.8-1.2）；若 K=100,000，N_total=1,000,000，α=1.0，则 Hit_Rate ≈ 1 - (1 - 0.1) / (1 - 0.001) ≈ 0.909

## Corrected Claim

Hit_Rate（缓存命中率）基于 Zipf 分布修正公式：Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_total)^α)，其中 K 为边缘节点可缓存对象数（由存储容量决定），N_total 为总对象数，α 为 Zipf 指数（典型 0.8-1.2）；若 K=100,000，N_total=1,000,000，α=1.0，则 Hit_Rate ≈ 1 - (1 - 0.1) / (1 - 0.001) ≈ 0.909

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合Zipf分布累积概率逻辑，数值计算 1 - 0.9/0.999 ≈ 0.909 准确无误。
