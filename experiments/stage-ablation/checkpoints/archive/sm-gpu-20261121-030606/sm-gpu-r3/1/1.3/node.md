# N9: 数据中心级GPU候选集包含H100 SXM (80GB) 和 A100 SXM (80GB)，因为H100提供900GB/s HBM3带宽和NVLink互联，A

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

数据中心级GPU候选集包含H100 SXM (80GB) 和 A100 SXM (80GB)，因为H100提供900GB/s HBM3带宽和NVLink互联，A100提供800GB/s HBM2e带宽，两者均支持FP8/INT8加速，是单卡部署27B模型的标准选择；H800/A800因出口限制不纳入主流性价比比较。

## Corrected Claim

数据中心级GPU候选集包含H100 SXM (80GB) 和 A100 SXM (80GB)，因为H100提供约3.35TB/s HBM3带宽、NVLink互联及FP8/INT8加速，A100提供约2TB/s HBM2e带宽及INT8/FP16加速，两者是单卡部署27B模型的标准选择；H800/A800因出口限制不纳入主流性价比比较。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 完备性缺失：父节点核心论点是关于‘数据中心级GPU (H100/A100)’的候选集及其带宽/互联优势，但子节点完全聚焦于‘消费级GPU (RTX 4090/5090)’的显存计算和吞吐量估算，完全未覆盖父节点中提到的H100/A100的具体性能对比或选型理由。2. 冗余性高：子节点3、4、5结构高度相似，均为‘精度-显存下限计算’，且子节点6、7、8均为‘带宽-吞吐量估算’，属于同一逻辑链条下的不同参数实例，可合并。）

## Search Query

H100 vs A100 LLM inference cost per token
