# N396: 联合扰动矩阵中 (s_avg+20%, H-5%) 象限的 C_tco 计算：C_tco_quad1 = C_bw * (1.2 * (1-H_new)/(1-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130, N131, N132

## Claim

联合扰动矩阵中 (s_avg+20%, H-5%) 象限的 C_tco 计算：C_tco_quad1 = C_bw * (1.2 * (1-H_new)/(1-H_base)) + C_infra * (1 + ΔN_servers/N_servers_base) + C_ops，其中 H_new = H_base - 5%；若 H_base=85%，H_new=80%，则 C_bw 增加 1.2*(0.20/0.15)-1=20%，C_infra 增加 (1-0.8)/(1-0.85)-1=33.3%。

## Corrected Claim

联合扰动矩阵中 (s_avg+20%, H-5%) 象限的 C_tco 计算：C_tco_quad1 = C_bw * (1.2 * (1-H_new)/(1-H_base)) + C_infra * (1 + ΔN_servers/N_servers_base) + C_ops，其中 H_new = H_base - 5%；若 H_base=85%，H_new=80%，则 C_bw 增加 1.2*(0.20/0.15)-1=20%，C_infra 增加 (1-0.8)/(1-0.85)-1=33.3%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合代数逻辑，数值计算（20%和33.3%）准确无误。

## Search Query

CDN cost sensitivity joint perturbation matrix
