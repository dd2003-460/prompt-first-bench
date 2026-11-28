# N69: 重试机制的边际效用递减曲线：第 k 次重试的成功率 P_success(k) = P_success(0) * (1 - P_fail)^k；当 P_fail=

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19, N20, N21

## Claim

重试机制的边际效用递减曲线：第 k 次重试的成功率 P_success(k) = P_success(0) * (1 - P_fail)^k；当 P_fail=0.1 时，首次重试成功率为 90%，二次为 81%，三次为 72.9%；若单次重试成本 C_retry = 0.5 * T_exec（因需重新加载环境），则最优重试次数 K_opt 满足 C_retry < Value(Completion) * ΔP_success，通常 K_opt=2 为性价比拐点，超过 2 次重试建议转为人工介入或任务降级。

## Corrected Claim

在假设故障相互独立且单次重试成本固定的理想模型下，重试成功率随次数呈指数衰减（P_success(k) = P_success(0) * (1 - P_fail)^k）。最优重试次数 K_opt 取决于完成价值与重试成本的比值，并非固定为 2；在实际工程中，需根据具体系统的故障相关性及成本效益分析确定阈值，通常超过一定次数后建议转为人工介入。

## Evidence

[质询]该陈述将复杂的系统可靠性问题简化为独立的伯努利试验（几何分布），忽略了故障的相关性（如系统性故障导致重试无效）以及‘最优重试次数’依赖于具体的价值函数和成本结构，并非通用的固定值（K_opt=2 缺乏普适性依据）。 | 先验知识/题面给定，逻辑校验通过：数学计算部分（0.9^1=0.9, 0.9^2=0.81, 0.9^3=0.729）正确，不等式逻辑自洽；但‘K_opt=2’为经验性断言，非第一性原理必然推论，且缺乏外部来源支持，故降级。

## Search Query

exponential backoff retry strategy optimal count cost benefit analysis
