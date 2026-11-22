# N19: 计算密度（TFLOPS）影响 prefill 阶段速度，需对比各硬件在 FP16/BF16/INT8 下的峰值算力

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

计算密度（TFLOPS）影响 prefill 阶段速度，需对比各硬件在 FP16/BF16/INT8 下的峰值算力

## Corrected Claim

计算密度（TFLOPS）影响 prefill 阶段速度，需对比各硬件在 FP16/BF16/INT8 下的峰值算力

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点结构上是将'硬件规格'作为独立节点，存在严重的结构性冗余（本质是同一类数据的不同实例）。此外，父节点明确要求'对比'以得出'影响速度'的结论，但子节点仅罗列了静态参数和理论FLOPs计算，缺失了基于这些参数推导出的实际时间估算或速度对比结论（即'需对比'这一动作的结果未体现）。）
