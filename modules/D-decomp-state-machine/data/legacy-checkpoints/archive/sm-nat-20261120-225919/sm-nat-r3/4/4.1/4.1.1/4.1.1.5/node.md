# N178: 在‘内容更新’口径下（ID 不变但 ETag/MD5 变化），命中率折损取决于缓存一致性检查频率 f_check 与更新率 λ 的比值：若每次请求都校验（f_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61, N62, N63

## Claim

在‘内容更新’口径下（ID 不变但 ETag/MD5 变化），命中率折损取决于缓存一致性检查频率 f_check 与更新率 λ 的比值：若每次请求都校验（f_check=1），折损因子为 (1-λ)；若采用 TTL 策略（TTL=1/λ=100天），则折损因子为 e^(-λ * TTL_avg)，其中 TTL_avg 为对象实际驻留时间。

## Corrected Claim

在‘内容更新’口径下（ID 不变但 ETag/MD5 变化），命中率折损取决于缓存一致性检查频率 f_check 与更新率 λ 的比值：若每次请求都校验（f_check=1），折损因子为 (1-λ)；若采用 TTL 策略（TTL=1/λ=100天），则折损因子为 e^(-λ * TTL_avg)，其中 TTL_avg 为对象实际驻留时间。

## Evidence

先验知识/题面给定，逻辑校验通过
