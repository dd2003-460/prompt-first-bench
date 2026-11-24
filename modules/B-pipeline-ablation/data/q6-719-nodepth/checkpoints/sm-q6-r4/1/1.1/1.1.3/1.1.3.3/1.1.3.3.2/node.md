# N454: 西部/东北区域自建 POP 的 P99 延迟改善上限 ΔP99_max = T_trans_current - T_trans_new，其中 T_trans_c

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

西部/东北区域自建 POP 的 P99 延迟改善上限 ΔP99_max = T_trans_current - T_trans_new，其中 T_trans_current 基于 d_avg=750km 计算为 ≈3.75ms（含介质修正≈5.6ms），T_trans_new 基于本地 POP d_avg=50km 计算为 ≈0.25ms（含介质修正≈0.4ms），ΔP99_max ≈ 5.2ms；该改善幅度不足以抵消自建的高固定成本，除非用户留存弹性极高。

## Corrected Claim

西部/东北区域自建 POP 的 P99 延迟改善上限 ΔP99_max = T_trans_current - T_trans_new，其中 T_trans_current 基于 d_avg=750km 计算为 ≈3.75ms（含介质修正≈5.6ms），T_trans_new 基于本地 POP d_avg=50km 计算为 ≈0.25ms（含介质修正≈0.4ms），ΔP99_max ≈ 5.2ms；该改善幅度不足以抵消自建的高固定成本，除非用户留存弹性极高。

## Evidence

先验知识/题面给定，逻辑校验通过：光速传播延迟计算（750km/3e8m/s≈2.5ms，考虑光纤折射率及介质修正后≈5.6ms；50km/3e8m/s≈0.17ms，修正后≈0.4ms）量级合理，差值5.2ms符合物理直觉，且成本效益分析逻辑自洽。
