# N170: Hit_Rate（缓存命中率）基于 Zipf 分布修正公式：Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_tot

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Hit_Rate（缓存命中率）基于 Zipf 分布修正公式：Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_total)^α)，其中 K 为边缘节点可缓存对象数（由存储容量决定），N_total 为总对象数，α 为 Zipf 指数（典型 0.8-1.2）；若 K=100,000，N_total=1,000,000，α=1.0，则 Hit_Rate ≈ 1 - (1 - 0.1) / (1 - 0.001) ≈ 0.909

## Corrected Claim

Hit_Rate（缓存命中率）基于 Zipf 分布修正公式：Hit_Rate = 1 - (1 - (K/N_total)^α) / (1 - (1/N_total)^α)，其中 K 为边缘节点可缓存对象数（由存储容量决定），N_total 为总对象数，α 为 Zipf 指数（典型 0.8-1.2）；若 K=100,000，N_total=1,000,000，α=1.0，则 Hit_Rate ≈ 1 - (1 - 0.1) / (1 - 0.001) ≈ 0.909

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式在参数 K 不同取值下的计算结果，属于参数扫描而非独立维度的分解。虽然数值上互斥（正交），但逻辑上高度冗余（都是 K 的变化）。此外，完备性不足，未涵盖 α（Zipf指数）变化或 N_total 变化对命中率的影响，仅固定了 α 和 N_total。）
