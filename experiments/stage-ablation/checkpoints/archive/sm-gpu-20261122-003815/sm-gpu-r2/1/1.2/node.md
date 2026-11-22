# N8: NVIDIA数据中心级GPU候选集：A100 80GB (SXM/PCIe), H100 80GB (SXM/PCIe), L40S 48GB, A6000 4

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

NVIDIA数据中心级GPU候选集：A100 80GB (SXM/PCIe), H100 80GB (SXM/PCIe), L40S 48GB, A6000 48GB (专业工作站卡)。

## Corrected Claim

NVIDIA数据中心级GPU候选集：A100 80GB (SXM/PCIe), H100 80GB (SXM/PCIe), L40S 48GB, A6000 48GB (专业工作站卡)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对四款不同的GPU型号进行了独立的可行性或性能分析，彼此之间没有重叠或矛盾。A100和H100分别分析了余量和性能增益，L40S分析了量化可行性，A6000通过与L40S对比突出了多卡互联的限制。虽然H100和A100、L40S和A6000存在对比关系，但这种对比是为了服务于各自型号在特定场景下的定位，属于合理的正交维度（单卡性能 vs 多卡互联 vs 量化支持 vs 余量）。所有候选集中的GPU均被覆盖，且每个子节点提供了该型号在Qwen3-27B推理场景下的关键决策信息，完备性良好。没有明显的冗余，因为每个子节点针对的是不同硬件架构或不同关键约束（如NVLink支持、FP8支持、带宽差异）。）

## Search Query

NVIDIA A100 H100 L40S A6000 specs VRAM price 2024
