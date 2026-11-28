# N10: 基于 32K context 窗口和 BF16 KV Cache，Qwen3-27B 的单请求 KV Cache 峰值显存占用约为 [待核验: 需代入 N9 参

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

基于 32K context 窗口和 BF16 KV Cache，Qwen3-27B 的单请求 KV Cache 峰值显存占用约为 [待核验: 需代入 N9 参数计算，预计 10-20GB 量级]，加上权重后总需求决定最小显存档位

## Corrected Claim

基于 32K context 窗口和 BF16 KV Cache，Qwen3-27B 的单请求 KV Cache 峰值显存占用约为 [待核验: 需代入 N9 参数计算，预计 10-20GB 量级]，加上权重后总需求决定最小显存档位

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3和子节点4高度冗余，它们本质上是同一公式在不同量化精度下的实例化，且都依赖于子节点2的计算结果。此外，子节点1中的参数与子节点2中的数值存在包含关系，导致结构松散。）
