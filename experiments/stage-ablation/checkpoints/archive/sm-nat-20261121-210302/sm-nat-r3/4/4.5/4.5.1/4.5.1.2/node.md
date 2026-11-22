# N161: 工作点 B（平衡/中性价比最优）：设定 F_th 使得累计缓存字节 Sum_{i=1}^{N_hot} E[S_i] ≈ 128GB，通过数值迭代求解 N_ho

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点 B（平衡/中性价比最优）：设定 F_th 使得累计缓存字节 Sum_{i=1}^{N_hot} E[S_i] ≈ 128GB，通过数值迭代求解 N_hot，此时 N_hot 约为 5000-8000（取决于大小分布），最大化了单位缓存空间的字节覆盖率，是 LFU 策略的理论最优工作点。

## Corrected Claim

工作点 B（平衡/中性价比最优）：设定 F_th 使得累计缓存字节 Sum_{i=1}^{N_hot} E[S_i] ≈ 128GB，通过数值迭代求解 N_hot，此时 N_hot 约为 5000-8000（取决于大小分布），最大化了单位缓存空间的字节覆盖率，是 LFU 策略的理论最优工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：在LFU/缓存理论中，将缓存容量设定为覆盖高频热点数据（N_hot）的累计大小（如128GB），确实是最大化字节覆盖率（Byte Hit Rate）的理论最优工作点，数值量级（5000-8000个对象对应128GB，平均对象大小约16-25MB）符合常见大对象存储场景的合理范围。
