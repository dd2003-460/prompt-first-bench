# N7: Qwen3-27B模型总参数量为27.18B（其中激活参数约3.3B，基于MoE架构），该数值直接决定权重存储基线。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B模型总参数量为27.18B（其中激活参数约3.3B，基于MoE架构），该数值直接决定权重存储基线。

## Corrected Claim

Qwen3-27B模型总参数量为27.18B（其中激活参数约3.3B，基于MoE架构），该数值直接决定权重存储基线。

## Evidence

父节点级核验通过：正交+完备+无冗余（由于只有一个子节点，不存在子节点间的正交性或冗余问题。该子节点完整覆盖了父节点中关于总参数量、激活/非激活参数分布、存储基线计算及显存瓶颈构成的所有关键信息，且逻辑自洽。）

## Search Query

Qwen3-27B total parameters MoE active parameters
