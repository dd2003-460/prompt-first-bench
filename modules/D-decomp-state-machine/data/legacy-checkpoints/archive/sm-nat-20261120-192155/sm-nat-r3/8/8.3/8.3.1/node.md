# N131: 工作点1（高更新敏感/低频率）：中尾部对象（i≈k）的更新驱逐概率 p_evict_i = U / (r_i + U)，其中 r_i = R_max * i^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点1（高更新敏感/低频率）：中尾部对象（i≈k）的更新驱逐概率 p_evict_i = U / (r_i + U)，其中 r_i = R_max * i^{-0.9}。由于 r_i 随 i 指数衰减，当 i 增大到 r_i << U 时，p_evict_i 趋近于 1。此工作点代表命中率损失的主要来源，需计算 i 从 100 到 k 的积分贡献。

## Corrected Claim

工作点1（高更新敏感/低频率）：中尾部对象（i≈k）的更新驱逐概率 p_evict_i = U / (r_i + U)，其中 r_i = R_max * i^{-0.9}。由于 r_i 随 i 指数衰减，当 i 增大到 r_i << U 时，p_evict_i 趋近于 1。此工作点代表命中率损失的主要来源，需计算 i 从 100 到 k 的积分贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU/近似LRU驱逐概率公式 p=U/(r+U) 符合排队论/缓存替换基本模型，幂律衰减 r_i 随 i 增大导致 p 趋近 1 的数学推导自洽，量级合理。
