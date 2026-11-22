# N167: 流量重分配噪声方差 σ_traffic² 的修正：假设 σ_traffic² = 0.05 为相对方差（即 5%），需转换为绝对流量变化标准差 σ_traffi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

流量重分配噪声方差 σ_traffic² 的修正：假设 σ_traffic² = 0.05 为相对方差（即 5%），需转换为绝对流量变化标准差 σ_traffic_abs = sqrt(0.05) * Q_base ≈ 0.2236 * Q_base，其中 Q_base 为基准成交量，用于量化干预初期流量分配的随机波动幅度。

## Corrected Claim

流量重分配噪声方差 σ_traffic² 的修正：假设 σ_traffic² = 0.05 为相对方差（即 5%），需转换为绝对流量变化标准差 σ_traffic_abs = sqrt(0.05) * Q_base ≈ 0.2236 * Q_base，其中 Q_base 为基准成交量，用于量化干预初期流量分配的随机波动幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：相对方差定义为 (σ_abs / Q_base)²，故 σ_abs = sqrt(相对方差) * Q_base，数值计算 sqrt(0.05) ≈ 0.2236 正确，量纲与逻辑自洽。

## Search Query

algorithmic intervention traffic reallocation noise variance standard deviation estimation
