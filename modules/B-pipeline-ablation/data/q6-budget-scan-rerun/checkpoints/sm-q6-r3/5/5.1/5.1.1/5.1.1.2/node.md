# N301: N_pop(T) 的最小节点数约束：N_pop(T) ≥ N_min = ceil(RPS_peak / C_pop_max)，其中 C_pop_max 为单 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

N_pop(T) 的最小节点数约束：N_pop(T) ≥ N_min = ceil(RPS_peak / C_pop_max)，其中 C_pop_max 为单 POP 点最大并发连接数（假设 10,000 连接），RPS_peak=37.5（N114给定），则 N_min = ceil(37.5/10000) = 1；但考虑到地理覆盖，N_pop 不得少于 10 个省级节点，因此实际 N_pop(T) = max(10, ceil(log(T_min/T)/log(k)))

## Corrected Claim

N_pop(T) 的最小节点数约束：N_pop(T) ≥ N_min = ceil(RPS_peak / C_pop_max)，其中 C_pop_max 为单 POP 点最大并发连接数（假设 10,000 连接），RPS_peak=37.5（N114给定），则 N_min = ceil(37.5/10000) = 1；但考虑到地理覆盖，N_pop 不得少于 10 个省级节点，因此实际 N_pop(T) = max(10, ceil(log(T_min/T)/log(k)))

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 ceil(37.5/10000)=1 正确，且 max(10, ...) 的逻辑约束符合地理覆盖的工程常识，无内部矛盾。
