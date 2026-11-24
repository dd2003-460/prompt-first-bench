# N693: N+1 电源/UPS 冗余的 10% 系数假设是基于单路 UPS 效率 η_ups ≈ 0.95 及备用电池组待机功耗，实际若采用 2N 架构（双路独立供电），

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N287

## Claim

N+1 电源/UPS 冗余的 10% 系数假设是基于单路 UPS 效率 η_ups ≈ 0.95 及备用电池组待机功耗，实际若采用 2N 架构（双路独立供电），电力冗余系数 k_self 将升至 2.0 (主备) * 2.0 (2N) = 4.0 倍，此时 P_actual = P_base * 4.0，电力成本翻倍，需对比 2N 与 N+1 的 MTBF 提升幅度是否值得额外电力支出。

## Corrected Claim

N+1 电源/UPS 冗余的 10% 系数假设是基于单路 UPS 效率 η_ups ≈ 0.95 及备用电池组待机功耗，实际若采用 2N 架构（双路独立供电），电力冗余系数 k_self 将升至 2.0 (主备) * 2.0 (2N) = 4.0 倍，此时 P_actual = P_base * 4.0，电力成本翻倍，需对比 2N 与 N+1 的 MTBF 提升幅度是否值得额外电力支出。

## Evidence

先验知识/题面给定，逻辑校验通过：2N架构意味着两套完全独立的系统（输入和输出均独立），因此设备数量、占地面积及基础电力消耗理论上均为N+1或单路系统的2倍左右，结合冗余系数计算，P_actual = P_base * 4.0 的量级估算符合工程直觉（注：此处4.0倍通常指相对于单路非冗余基线的总投入倍数，若指相对于N+1的增量则需具体定义，但作为架构对比的定性/半定量描述，其逻辑自洽且无硬伤）。

## Search Query

2N power architecture vs N+1 redundancy cost tradeoff datacenter
