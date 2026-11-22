# N427: Prefill 与 Decode 阶段的耗时占比对 TCO 权重的影响：若应用场景中 Prefill 耗时占总推理时间的比例从 20% 提升至 40% (例如长

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

Prefill 与 Decode 阶段的耗时占比对 TCO 权重的影响：若应用场景中 Prefill 耗时占总推理时间的比例从 20% 提升至 40% (例如长 Prompt 短 Output 场景)，则硬件选型中 FLOPS/价格 的权重应从 20% 提升至 40%，而 Bandwidth/价格 的权重相应下降，这将改变高算力卡 (如 A100) 相对于高带宽卡 (如 H100) 的性价比排序。

## Corrected Claim

Prefill 与 Decode 阶段的耗时占比对 TCO 权重的影响：若应用场景中 Prefill 耗时占总推理时间的比例从 20% 提升至 40% (例如长 Prompt 短 Output 场景)，则硬件选型中 FLOPS/价格 的权重应从 20% 提升至 40%，而 Bandwidth/价格 的权重相应下降，这将改变高算力卡 (如 A100) 相对于高带宽卡 (如 H100) 的性价比排序。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算密集（Compute-bound），Decode阶段访存密集（Memory-bound），耗时占比直接决定硬件瓶颈类型，进而决定TCO权重分配，逻辑自洽且符合LLM推理基本物理/经济直觉。
