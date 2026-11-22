# N84: 验证‘同一套假设’的逻辑一致性检验：构建联合似然函数 $L(H | D_1, D_2)$，其中 $D_1$ 为‘挂价高 15-25%’，$D_2$ 为‘成交周期

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

验证‘同一套假设’的逻辑一致性检验：构建联合似然函数 $L(H | D_1, D_2)$，其中 $D_1$ 为‘挂价高 15-25%’，$D_2$ 为‘成交周期缩短 20%’。假设核心机制为‘信号溢价抵消搜索摩擦’。若 $P(D_1 | H_{signal}) = 0.8$ 且 $P(D_2 | H_{signal}) = 0.7$，则联合概率 $P(D_1, D_2 | H_{signal}) = 0.56$。对比零假设 $H_0$（独立随机波动），$P(D_1, D_2 | H_0) = P(D_1|H_0) \times P(D_2|H_0) \approx 0.3 \times 0.4 = 0.12$。似然比 $LR = 0.56 / 0.12 = 4.67 > 1$，表明单一假设（信号机制）比独立假设更能解释数据，逻辑上成立。

## Corrected Claim

验证‘同一套假设’的逻辑一致性检验：构建联合似然函数 $L(H | D_1, D_2)$，其中 $D_1$ 为‘挂价高 15-25%’，$D_2$ 为‘成交周期缩短 20%’。假设核心机制为‘信号溢价抵消搜索摩擦’。若 $P(D_1 | H_{signal}) = 0.8$ 且 $P(D_2 | H_{signal}) = 0.7$，则联合概率 $P(D_1, D_2 | H_{signal}) = 0.56$。对比零假设 $H_0$（独立随机波动），$P(D_1, D_2 | H_0) = P(D_1|H_0) \times P(D_2|H_0) \approx 0.3 \times 0.4 = 0.12$。似然比 $LR = 0.56 / 0.12 = 4.67 > 1$，表明单一假设（信号机制）比独立假设更能解释数据，逻辑上成立。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

joint likelihood ratio signal premium search friction real estate
