# N115: N43 中 'T_window 为观察窗口（如1小时）' 假设的敏感性分析：τ_LFU = 1 / λ_decay = T_window，当 T_window 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

N43 中 'T_window 为观察窗口（如1小时）' 假设的敏感性分析：τ_LFU = 1 / λ_decay = T_window，当 T_window 从 1 小时变化到 10 分钟或 1 天时，τ_LFU 分别为 600s 或 86400s；在 T_shift=30 分钟 (1800s) 的热度漂移周期下，ΔH_drift 分别为 (1800/600) * (H_LFU_static - H_LRU_static) = 3.0 * ΔH_static 和 (1800/86400) * ΔH_static = 0.0208 * ΔH_static，表明 T_window 的选择对 LFU 性能影响可达 150 倍。

## Corrected Claim

N43 中 'T_window 为观察窗口（如1小时）' 假设的敏感性分析：τ_LFU = 1 / λ_decay = T_window，当 T_window 从 1 小时变化到 10 分钟或 1 天时，τ_LFU 分别为 600s 或 86400s；在 T_shift=30 分钟 (1800s) 的热度漂移周期下，ΔH_drift 分别为 (1800/600) * (H_LFU_static - H_LRU_static) = 3.0 * ΔH_static 和 (1800/86400) * ΔH_static = 0.0208 * ΔH_static，表明 T_window 的选择对 LFU 性能影响可达 150 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：时间单位换算正确（1h=3600s, 10min=600s, 1d=86400s），比例计算正确（1800/600=3, 1800/86400≈0.0208），倍数差异计算正确（3/0.0208≈144，约150倍），符合线性敏感性分析逻辑。

## Search Query

LFU cache time window sensitivity analysis hotness drift adaptation
