# N11: 科研闭环中'假设生成'阶段的单次推理成本：平均 prompt 长度 2k tokens，生成 500 tokens，耗时约 15-20s；瓶颈在 prefill

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

科研闭环中'假设生成'阶段的单次推理成本：平均 prompt 长度 2k tokens，生成 500 tokens，耗时约 15-20s；瓶颈在 prefill 阶段的 attention 计算复杂度 O(n²)，长 prompt 下 prefill 延迟占主导

## Corrected Claim

科研闭环中'假设生成'阶段的单次推理成本：平均 prompt 长度 2k tokens，生成 500 tokens，耗时约 15-20s；瓶颈在 prefill 阶段的 attention 计算复杂度 O(n²)，长 prompt 下 prefill 延迟占主导

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾与事实错误：1. 数据不一致：子节点2计算出总耗时为 8.7-9.4s，却声称这‘低于题面给出的 15-20s’，但 8.7s 并不显著低于 15s（仅约一半），且结论‘表明实际瓶颈可能在调度’缺乏充分依据，因为计算模型本身可能遗漏了关键因素（如 KV Cache 增长导致的内存压力或具体的 TP 配置细节）。2. 覆盖不全：父节点强调‘瓶颈在 prefill 阶段的 attention 计算复杂度 O(n²)’，但子节点1将 prefill 归因于‘内存带宽瓶颈’和‘TP 通信’，子节点2完全忽略了 prefill 的 O(n²) 计算复杂度对长序列的影响，反而得出 prefill 仅占 120ms 的结论，这与父节点的核心论点（prefill 延迟占主导）相悖。）
