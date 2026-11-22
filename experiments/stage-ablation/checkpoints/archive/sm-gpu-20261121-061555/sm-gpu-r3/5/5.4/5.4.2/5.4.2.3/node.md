# N304: 高可用性架构成本增量：为消除单点故障 (SPOF)，引入 1x 备用 GPU (Hot Standby) 的 CapEx 增量 = 1 * GPU_Price，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

高可用性架构成本增量：为消除单点故障 (SPOF)，引入 1x 备用 GPU (Hot Standby) 的 CapEx 增量 = 1 * GPU_Price，OpEx 增量 = 1 * GPU_TDP * 0.1 (待机功耗比例) * 8760h * 电价；此方案将系统可用性从 99.5% 提升至 99.9%+，需与 '停机损失' 进行盈亏平衡计算。

## Corrected Claim

高可用性架构成本增量：为消除单点故障 (SPOF)，引入 1x 备用 GPU (Hot Standby) 的 CapEx 增量 = 1 * GPU_Price，OpEx 增量 = 1 * GPU_TDP * 0.1 (待机功耗比例) * 8760h * 电价；此方案将系统可用性从 99.5% 提升至 99.9%+，需与 '停机损失' 进行盈亏平衡计算。

## Evidence

先验知识/题面给定，逻辑校验通过：CapEx 增量等于单卡价格符合定义；OpEx 公式量纲正确（功率*时间*单价=货币）；99.5% 到 99.9% 的可用性提升符合冗余架构的一般工程经验（消除单点故障通常能带来数量级的可用性提升）。
