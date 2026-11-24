# N737: 加权平均速率的精确计算验证：T_rebuild = (V_total / Rate_avg) * (1 + Overhead_Factor)。Rate_avg 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256, N257, N258

## Claim

加权平均速率的精确计算验证：T_rebuild = (V_total / Rate_avg) * (1 + Overhead_Factor)。Rate_avg = (0.5 * 50%_Capacity + 0.5 * 100%_Capacity) * Max_Rate。若Max_Rate=100GB/h，则Rate_avg=75GB/h。Overhead_Factor=1.15代表RAID校验/元数据开销。此计算假设白天和夜间各占12小时，且重建任务在两个时段均匀分布，实际可能因任务调度碎片化导致效率略低。

## Corrected Claim

加权平均速率的精确计算验证：T_rebuild = (V_total / Rate_avg) * (1 + Overhead_Factor)。Rate_avg = (0.5 * 50%_Capacity + 0.5 * 100%_Capacity) * Max_Rate。若Max_Rate=100GB/h，则Rate_avg=75GB/h。Overhead_Factor=1.15代表RAID校验/元数据开销。此计算假设白天和夜间各占12小时，且重建任务在两个时段均匀分布，实际可能因任务调度碎片化导致效率略低。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（0.5*50+0.5*100=75），公式结构符合加权平均及开销叠加的基本逻辑，量纲一致。

## Search Query

weighted average throughput calculation RAID rebuild overhead factor
