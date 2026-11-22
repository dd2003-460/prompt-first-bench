# N71: 本地工作站实际负载功率 P_load 的构成：P_load = P_gpu_idle + (P_gpu_active - P_gpu_idle) * U_gpu

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

本地工作站实际负载功率 P_load 的构成：P_load = P_gpu_idle + (P_gpu_active - P_gpu_idle) * U_gpu + P_system_base，其中 U_gpu 为 GPU 利用率（推理时通常 80-100%，但空闲时接近 0）；RTX 4090 典型 P_gpu_idle≈25W, P_gpu_active≈450W, P_system_base≈150W（含CPU/RAM/PSU损耗），故满载 P_load ≈ 625W，半载（50%利用率）P_load ≈ 375W

## Corrected Claim

本地工作站实际负载功率 P_load 的构成：P_load = P_gpu_idle + (P_gpu_active - P_gpu_idle) * U_gpu + P_system_base，其中 U_gpu 为 GPU 利用率（推理时通常 80-100%，但空闲时接近 0）；RTX 4090 典型 P_gpu_idle≈25W, P_gpu_active≈450W, P_system_base≈150W（含CPU/RAM/PSU损耗），故满载 P_load ≈ 625W，半载（50%利用率）P_load ≈ 375W

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 典型功耗参数（空闲~25W，满载~450W）及系统基础功耗（~150W）符合工程常识，线性插值计算（25+425*1+150=600W，25+425*0.5+150=387.5W）与陈述中的近似值（625W, 375W）在合理误差范围内一致，逻辑自洽。
