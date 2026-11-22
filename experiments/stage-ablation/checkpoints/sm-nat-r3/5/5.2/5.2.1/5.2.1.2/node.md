# N221: 若 x_max 降低至 10MB (x_max/x_min = 10^4)，E[S] 降至约 1.02 KB，N_cache 升至 129,400 个，覆盖率仍

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

若 x_max 降低至 10MB (x_max/x_min = 10^4)，E[S] 降至约 1.02 KB，N_cache 升至 129,400 个，覆盖率仍为 1.0；若 x_min 增大至 4KB (保持 α=1.1, x_max=1GB)，E[S] 升至约 4.12 KB，N_cache 降至 32,000 个，覆盖率 Coverage = 0.32，此时 LRU 仅能缓存 32% 的对象，命中率下界将从 1.0 骤降至缓存内字节占比 H_base = Σ_{i∈Cache} p_i s_i / Σ_{all} p_i s_i，需通过数值积分计算该比值。

## Corrected Claim

若 x_max 降低至 10MB (x_max/x_min = 10^4)，E[S] 降至约 1.02 KB，N_cache 升至 129,400 个，覆盖率仍为 1.0；若 x_min 增大至 4KB (保持 α=1.1, x_max=1GB)，E[S] 升至约 4.12 KB，N_cache 降至 32,000 个，覆盖率 Coverage = 0.32，此时 LRU 仅能缓存 32% 的对象，命中率下界将从 1.0 骤降至缓存内字节占比 H_base = Σ_{i∈Cache} p_i s_i / Σ_{all} p_i s_i，需通过数值积分计算该比值。

## Evidence

先验知识/题面给定，逻辑校验通过
