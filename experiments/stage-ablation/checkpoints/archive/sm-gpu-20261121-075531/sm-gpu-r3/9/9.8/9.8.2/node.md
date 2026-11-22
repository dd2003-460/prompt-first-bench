# N369: PCIe x8 带宽瓶颈导致的延迟惩罚百分比 (Latency Penalty %) 计算公式为：(T_allreduce_pcie - T_allreduce

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N124

## Claim

PCIe x8 带宽瓶颈导致的延迟惩罚百分比 (Latency Penalty %) 计算公式为：(T_allreduce_pcie - T_allreduce_nvlink) / T_total_decode * 100%；在 27B INT8 模型中，由于单层通信量小且计算密集，该惩罚通常 <5% [待核验]，但在 W4 或大 Batch 场景下可能上升至 5-10%。

## Corrected Claim

PCIe x8 带宽瓶颈导致的延迟惩罚百分比计算公式为：(T_allreduce_pcie - T_allreduce_nvlink) / T_total_decode * 100%；在 27B INT8 模型中，由于单层通信量小且计算密集，该惩罚通常较低，但在 W4 或大 Batch 场景下可能显著上升。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（<5% 和 5-10%），属于硬件性能与模型配置相关的经验事实，无法仅通过第一性原理或逻辑推导得出，且缺乏具体实验数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值阈值非数学/物理定律推论）

## Search Query

Tensor Parallelism PCIe x8 vs NVLink latency penalty LLM inference
