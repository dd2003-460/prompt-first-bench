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

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid storage array HDD SSD cluster power consumption calculation
