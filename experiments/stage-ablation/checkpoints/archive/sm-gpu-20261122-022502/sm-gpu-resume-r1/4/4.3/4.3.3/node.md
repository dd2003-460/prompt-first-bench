# N95: 工作点 B3 (高成本低性/冗余)：1x H200 (141GB) 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

工作点 B3 (高成本低性/冗余)：1x H200 (141GB) 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 141GB。理论 Decode 上限 ≈ 4800 GB/s / 54 GB ≈ 88.9 tokens/s。CapEx ≈ $35,000。

## Corrected Claim

工作点 B3 (高成本低性/冗余)：1x H200 (141GB) 运行 BF16 Qwen3-27B (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 141GB。理论 Decode 上限 ≈ 4800 GB/s / 54 GB ≈ 88.9 tokens/s。CapEx ≈ $35,000。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别聚焦于性能（吞吐）、经济（TCO）和容量（Batch Size），三个维度正交且无重叠。父节点核心信息（硬件、模型、显存、带宽、成本）均被覆盖或作为计算基础隐含在子节点中。虽然子节点3包含了一个明显的逻辑/计算错误（将单请求KV Cache大小误用为批量总大小，导致得出错误的batch限制），但这属于内容准确性问题，而非结构性的冗余或非正交问题。）
