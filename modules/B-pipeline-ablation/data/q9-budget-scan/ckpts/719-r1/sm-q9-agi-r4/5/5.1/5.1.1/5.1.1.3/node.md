# N230: 4x V100 集群在持续满载推理下的总稳态功耗估算值为 600W-800W (取中值 700W)，该数值已包含 PSU 转换损耗 (~5%) 及风扇散热功耗，

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66, N67, N68

## Claim

4x V100 集群在持续满载推理下的总稳态功耗估算值为 600W-800W (取中值 700W)，该数值已包含 PSU 转换损耗 (~5%) 及风扇散热功耗，但不含机房空调制冷成本 (PUE)。

## Corrected Claim

4x V100 集群在持续满载推理下的总稳态功耗估算值为 600W-800W (取中值 700W)，该数值已包含 PSU 转换损耗 (~5%) 及风扇散热功耗，但不含机房空调制冷成本 (PUE)。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式（P_total = 700W * PUE）在不同 PUE 参数下的两个取值，属于高度冗余的参数化变体，而非独立的正交维度。此外，父节点明确声明‘不含机房空调制冷成本 (PUE)’，但子节点却基于 PUE 进行计算并得出包含制冷的总功耗，导致子节点与父节点的约束定义存在逻辑矛盾或范畴错位（父节点是 IT 负载估算，子节点变成了设施总功耗估算）。）

## Search Query

4x V100 server steady state power consumption LLM inference
