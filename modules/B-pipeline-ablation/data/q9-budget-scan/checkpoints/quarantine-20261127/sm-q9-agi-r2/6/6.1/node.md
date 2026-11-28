# N25: 工作点 A (低成本/高延迟)：仅使用本地 V100 集群 + M1 Max 编排，无云端 API；总成本 C_A = E_elec * T_time + C_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

工作点 A (低成本/高延迟)：仅使用本地 V100 集群 + M1 Max 编排，无云端 API；总成本 C_A = E_elec * T_time + C_deprec * (T_time/T_life)；假设 T_time=24h/day, E_elec=$0.15/kWh, 服务器功耗 P_server=400W (4xV100+CPU), 日电费 C_elec_day = 400W * 24h * $0.15/kWh = $1.44/day；折旧 C_deprec≈$0.01/day；总日成本≈$1.45；产出能力上限：每日最多处理 N_papers ≈ (24*3600) / (T_gen_avg + T_eval_avg) ≈ 86400 / 120s ≈ 720 次推理调用，受限于上下文长度，实际高质量论文产出 ≤ 5 篇/天 (每篇需 ~50 次完整推理循环)。

## Corrected Claim

工作点 A (低成本/高延迟)：仅使用本地 V100 集群 + M1 Max 编排，无云端 API；总成本 C_A = E_elec * T_time + C_deprec * (T_time/T_life)；假设 T_time=24h/day, E_elec=$0.15/kWh, 服务器功耗 P_server=400W (4xV100+CPU), 日电费 C_elec_day = 400W * 24h * $0.15/kWh = $1.44/day；折旧 C_deprec≈$0.01/day；总日成本≈$1.45；产出能力上限：每日最多处理 N_papers ≈ (24*3600) / (T_gen_avg + T_eval_avg) ≈ 86400 / 120s ≈ 720 次推理调用，受限于上下文长度，实际高质量论文产出 ≤ 5 篇/天 (每篇需 ~50 次完整推理循环)。

## Evidence

先验知识/题面给定，逻辑校验通过：电费计算 400W*24h*0.15$/kWh=1.44$ 正确；推理次数 86400/120=720 正确；产能瓶颈逻辑（720次调用/50次每篇=14.4篇，取保守值5篇）自洽。
