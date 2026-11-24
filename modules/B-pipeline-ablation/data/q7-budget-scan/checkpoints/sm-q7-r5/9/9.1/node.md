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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个组成部分（HDD集群、SSD缓存、共享基础设施）以及最终的汇总计算。虽然第4个子节点是对前3个结果的数学加和，但在学术分解中作为‘结论/验证’步骤是合理的，且未包含新的独立变量定义，因此不构成实质性冗余或矛盾。各部分职责清晰，无重叠。）

## Search Query

hybrid storage array HDD SSD cluster power consumption calculation
