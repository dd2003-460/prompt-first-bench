# N311: Batch Size 对 P_avg 的影响：当 Batch Size 从 1 增加到 8 时，RTX 4090 的 P_avg 从 ~315W 上升至 ~36

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102, N103, N104

## Claim

Batch Size 对 P_avg 的影响：当 Batch Size 从 1 增加到 8 时，RTX 4090 的 P_avg 从 ~315W 上升至 ~360W（+14%），因为并行计算提高了 GPU 利用率，减少了等待内存带宽的空闲时间。

## Corrected Claim

Batch Size 对 P_avg 的影响：当 Batch Size 从 1 增加到 8 时，RTX 4090 的 P_avg 通常会上升，因为并行计算提高了 GPU 利用率，减少了等待内存带宽的空闲时间。

## Evidence

[质询]具体数值（315W, 360W, +14%）属于特定工作负载下的经验测量值，无法从第一性原理推导，且缺乏来源支持具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 power consumption batch size inference
