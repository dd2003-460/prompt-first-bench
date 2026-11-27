# N321: T_1（当前期成交周期）的测量需定义‘成交’为支付完成而非订单创建，且需剔除取消订单；T_1 = sum(T_i) / n_active，其中 n_active

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

T_1（当前期成交周期）的测量需定义‘成交’为支付完成而非订单创建，且需剔除取消订单；T_1 = sum(T_i) / n_active，其中 n_active 为当前活跃交易数，若 n_active < 30，则 T_1 的标准误 SE_T1 > 15%，k% 计算不可靠。

## Corrected Claim

T_1（当前期成交周期）的测量需定义‘成交’为支付完成而非订单创建，且需剔除取消订单；T_1 = sum(T_i) / n_active，其中 n_active 为当前活跃交易数，若 n_active < 30，则 T_1 的标准误 SE_T1 > 15%，k% 计算不可靠。

## Evidence

先验知识/题面给定，逻辑校验通过：定义成交为支付完成并剔除取消订单符合业务逻辑；n_active < 30 时样本量过小导致标准误过大（>15%）从而使得 k% 计算不可靠，符合统计学基本原理。

## Search Query

definition of transaction completion time in e-commerce data analysis sample size requirement
