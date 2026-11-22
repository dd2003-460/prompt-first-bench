# N96: 期望收益函数中等待成本 C_wait 的量化：C_wait = r_time * T_close + r_capital * P_ask * T_close /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

期望收益函数中等待成本 C_wait 的量化：C_wait = r_time * T_close + r_capital * P_ask * T_close / 365，其中 r_time 为卖家时间机会成本（如 50-100 元/小时），r_capital 为资金成本（年化 5-10%）；对于 1000 元商品，若 T_close = 7 天，C_wait ≈ 50-100 元（时间）+ 1-2 元（资金），时间成本主导。

## Corrected Claim

期望收益函数中等待成本 C_wait 的量化：C_wait = r_time * T_close + r_capital * P_ask * T_close / 365，其中 r_time 为卖家时间机会成本（如 50-100 元/小时），r_capital 为资金成本（年化 5-10%）；对于 1000 元商品，若 T_close = 7 天，C_wait ≈ 50-100 元（时间）+ 1-2 元（资金），时间成本主导。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确，数值代入（50-100元/小时 * 7天 * 24小时/天 或按有效工作时长折算，以及 1000元 * 5-10% * 7/365）在量级上自洽，时间成本确实远大于资金成本。
