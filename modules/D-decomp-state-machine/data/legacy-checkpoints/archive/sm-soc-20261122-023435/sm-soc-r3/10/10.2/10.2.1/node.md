# N252: 平台抽成阈值 P_min 的量化定义：P_min = C_operation / r_take，其中 C_operation 为单笔交易运营成本（如支付手续费、

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

平台抽成阈值 P_min 的量化定义：P_min = C_operation / r_take，其中 C_operation 为单笔交易运营成本（如支付手续费、客服成本），r_take 为平台抽成比例（如 5%）；若 C_operation ≈ 2.5 元，r_take = 5%，则 P_min = 50 元。

## Corrected Claim

平台抽成阈值 P_min 的量化定义：P_min = C_operation / r_take，其中 C_operation 为单笔交易运营成本（如支付手续费、客服成本），r_take 为平台抽成比例（如 5%）；若 C_operation ≈ 2.5 元，r_take = 5%，则 P_min = 50 元。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_min = C_operation / r_take 符合盈亏平衡点的基本经济逻辑（收入=成本），数值计算 2.5 / 0.05 = 50 正确，量纲合理。
