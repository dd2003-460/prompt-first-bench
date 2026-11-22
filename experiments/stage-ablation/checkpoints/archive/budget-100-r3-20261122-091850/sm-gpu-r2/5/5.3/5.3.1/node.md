# N90: Apple M3 Ultra 统一内存带宽为 800GB/s，M2 Ultra 为 800GB/s，需核实具体型号差异；与 NVIDIA H100 (3.35T

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

Apple M3 Ultra 统一内存带宽为 800GB/s，M2 Ultra 为 800GB/s，需核实具体型号差异；与 NVIDIA H100 (3.35TB/s) 和 A100 (2TB/s) 相比，其带宽仅为后者的 24%-40%，这是其推理吞吐量（TPS）的理论上限瓶颈。

## Corrected Claim

Apple M3 Ultra 统一内存带宽约为 819GB/s，M2 Ultra 为 800GB/s；与 NVIDIA H100 (3.35TB/s) 和 A100 (2TB/s) 相比，其带宽约为后者的 24%-40%，带宽差异是制约其推理吞吐量（TPS）的关键因素之一，但非唯一理论上限。

## Evidence

[质询]M3 Ultra 的统一内存带宽实际为 819GB/s，而非 800GB/s；虽然量级正确，但具体数值存在偏差，且将带宽直接等同于 TPS 理论上限瓶颈忽略了计算密度（FLOPS）和架构效率的影响，属于过度简化。 | 先验知识/题面给定，逻辑校验通过：M3 Ultra 带宽确为 ~800GB/s 量级（实际 819GB/s），H100/A100 带宽数据准确，比例计算（800/3350≈24%, 800/2000=40%）逻辑自洽；但作为 knowledge 节点，虽逻辑自洽，因具体数值（800 vs 819）存在轻微偏差且因果归因（带宽=TPS瓶颈）过于绝对，依据经验事实排除条款的精神（虽不适用 given/knowledge 的强制降级，但 challenge 成立且无法完全排除数值精确性争议），保守判定为 degraded 以提示数值需精确化。注：根据规则，knowledge 节点逻辑自洽即 verified，但此处 challenge 指出数值不精确（800 vs 819）及因果简化，若严格遵循“challenge 成立且无法排除则降档”，则判 degraded。

## Search Query

Apple M3 Ultra memory bandwidth GB/s
