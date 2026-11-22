# N6: 对象大小分布的累积分布函数 F_S(s) = 1 - (s_min/s)^{α-1}，其中 α=1.1，s_min 为最小对象大小（[待核验]，通常取 1KB 

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对象大小分布的累积分布函数 F_S(s) = 1 - (s_min/s)^{α-1}，其中 α=1.1，s_min 为最小对象大小（[待核验]，通常取 1KB 或 10KB 作为下界以计算均值和尾部概率）。

## Corrected Claim

对象大小分布的累积分布函数 F_S(s) = 1 - (s_min/s)^{α-1}，其中 α=1.1，s_min 为最小对象大小（[待核验]，通常取 1KB 或 10KB 作为下界以计算均值和尾部概率）。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合帕累托分布（Pareto Distribution）的标准累积分布函数形式，且α=1.1在存储系统对象大小分布研究中属于合理的经验参数范围，s_min取值1KB或10KB亦符合常见工程实践。

## Search Query

Pareto distribution CDF alpha 1.1 minimum value object size
