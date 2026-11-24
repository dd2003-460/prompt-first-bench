# N127: 修复误判所需的重新平衡开销 C_rebalance = (Migration_Bandwidth_Overhead * Time_Rebalance) + (M

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

修复误判所需的重新平衡开销 C_rebalance = (Migration_Bandwidth_Overhead * Time_Rebalance) + (Metadata_Update_Cost)。若每日执行一次基于热度评分的重新平衡，迁移量 ΔV_rebalance ≈ P_misjudge * V_total * Turnover_Rate。假设Turnover_Rate=5%/day，ΔV_rebalance=25TB。迁移期间占用I/O带宽导致正常查询延迟增加，隐性成本 = 25TB / (Migration_Throughput * (1 - Interference_Factor)) * OpCost_Hourly。

## Corrected Claim

修复误判所需的重新平衡开销 C_rebalance = (Migration_Bandwidth_Overhead * Time_Rebalance) + (Metadata_Update_Cost)。若每日执行一次基于热度评分的重新平衡，迁移量 ΔV_rebalance ≈ P_misjudge * V_total * Turnover_Rate。假设Turnover_Rate=5%/day，ΔV_rebalance=25TB。迁移期间占用I/O带宽导致正常查询延迟增加，隐性成本 = 25TB / (Migration_Throughput * (1 - Interference_Factor)) * OpCost_Hourly。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式 C_rebalance 中的三个主要组成部分：迁移带宽开销（影响隐性成本/干扰）、重平衡时间（直接计算项）和元数据更新成本（直接计算项）。三者定义清晰，无逻辑重叠或矛盾。虽然父节点中提到的“隐性成本”依赖于 Migration_Bandwidth_Overhead 和 Time_Rebalance，但子节点正确分解了这两个依赖变量以及独立的 Metadata_Update_Cost，覆盖了所有关键量化方面。）
