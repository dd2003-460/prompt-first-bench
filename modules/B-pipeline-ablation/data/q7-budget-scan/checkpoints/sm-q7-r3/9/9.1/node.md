# N130: HDD+SSD 分层方案总功耗 P_total_Hybrid = P_HDD_cluster + P_SSD_cluster + P_Shared_Infra，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

HDD+SSD 分层方案总功耗 P_total_Hybrid = P_HDD_cluster + P_SSD_cluster + P_Shared_Infra，其中 P_HDD_cluster = N_HDD * W_HDD_avg，P_SSD_cache = N_SSD * W_SSD_avg，P_Shared_Infra 包括共用控制器、背板和散热。

## Corrected Claim

HDD+SSD 分层方案总功耗 P_total_Hybrid = P_HDD_cluster + P_SSD_cluster + P_Shared_Infra，其中 P_HDD_cluster = N_HDD * W_HDD_avg，P_SSD_cache = N_SSD * W_SSD_avg，P_Shared_Infra 包括共用控制器、背板和散热。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立组成部分（HDD集群、SSD缓存、共享基础设施）以及最终的汇总计算，逻辑上互斥且无重叠。每个子节点提供了具体的修正参数和计算过程，覆盖了父节点定义的所有关键方面。虽然第4个子节点是对前3个的加和，但作为‘总功耗’这一最终结果的独立验证和对比节点是合理的，不属于冗余的参数变体，而是必要的结论性步骤。）

## Search Query

hybrid storage array HDD SSD cluster power consumption calculation
