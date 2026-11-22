# N6: 对象大小分布的累积分布函数 CDF_S(s) = 1 - (s/s_min)^(-1.1)，其中 s_min 为最小对象大小（需假设 s_min=1KB 或从总

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对象大小分布的累积分布函数 CDF_S(s) = 1 - (s/s_min)^(-1.1)，其中 s_min 为最小对象大小（需假设 s_min=1KB 或从总字节数反推），用于计算任意大小阈值下的对象占比。

## Corrected Claim

对象大小分布的累积分布函数 CDF_S(s) = 1 - (s/s_min)^(-1.1)，其中 s_min 为最小对象大小（需假设 s_min=1KB 或从总字节数反推），用于计算任意大小阈值下的对象占比。

## Evidence

先验知识/题面给定，逻辑校验通过
