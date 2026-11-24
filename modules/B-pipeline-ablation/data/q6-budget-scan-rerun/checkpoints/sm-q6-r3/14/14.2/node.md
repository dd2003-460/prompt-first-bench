# N415: 流量增长率与容量增长率的耦合模型：定义 Traffic_Growth_Rate(t) = Traffic(t+1) / Traffic(t) - 1，Capac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

流量增长率与容量增长率的耦合模型：定义 Traffic_Growth_Rate(t) = Traffic(t+1) / Traffic(t) - 1，Capacity_Growth_Rate(t) = Capacity(t+1) / Capacity(t) - 1；若 Traffic_Growth_Rate > Capacity_Growth_Rate + Safety_Margin（Safety_Margin 通常设为10-20%），则触发扩容需求；扩容瓶颈成本 C_bottleneck = ∫_{t_trigger}^{t_complete} (Traffic(t) - Capacity(t)) × Cost_per_Overloaded_Byte dt

## Corrected Claim

流量增长率与容量增长率的耦合模型：定义 Traffic_Growth_Rate(t) = Traffic(t+1) / Traffic(t) - 1，Capacity_Growth_Rate(t) = Capacity(t+1) / Capacity(t) - 1；若 Traffic_Growth_Rate > Capacity_Growth_Rate + Safety_Margin（Safety_Margin 通常设为10-20%），则触发扩容需求；扩容瓶颈成本 C_bottleneck = ∫_{t_trigger}^{t_complete} (Traffic(t) - Capacity(t)) × Cost_per_Overloaded_Byte dt

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

traffic growth rate capacity growth rate safety margin CDN scaling bottleneck cost
