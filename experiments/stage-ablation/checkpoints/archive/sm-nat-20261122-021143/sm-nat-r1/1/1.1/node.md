# N6: 对象大小分布的累积分布函数 CDF_S(s) = 1 - (s_min/s)^1.1，其中 s_min 由总内存 128GB 和对象总数 10万反推：总数据量 

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

对象大小分布的累积分布函数 CDF_S(s) = 1 - (s_min/s)^1.1，其中 s_min 由总内存 128GB 和对象总数 10万反推：总数据量 = 10^5 * E[S] = 10^5 * (s_min * 1.1 / (1.1-1)) = 128 * 10^9 bytes，解得 s_min = 128 * 10^9 / (10^5 * 11) ≈ 116.36 bytes

## Corrected Claim

对象大小分布的累积分布函数 CDF_S(s) = 1 - (s_min/s)^1.1，其中 s_min 由总内存 128GB 和对象总数 10万反推：总数据量 = 10^5 * E[S] = 10^5 * (s_min * 1.1 / (1.1-1)) = 128 * 10^9 bytes，解得 s_min = 128 * 10^9 / (10^5 * 11) ≈ 116.36 bytes

## Evidence

先验知识/题面给定，逻辑校验通过：幂律分布期望公式 E[S] = s_min * α / (α-1) 在 α=1.1 时推导正确，数值计算 128e9 / (1e5 * 11) ≈ 116.36 无误。
