# N8: 显存占用模型：总显存消耗 = (27B params × 4-bit quant size ≈ 13.5GB) + (KV Cache per seq × ma

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

显存占用模型：总显存消耗 = (27B params × 4-bit quant size ≈ 13.5GB) + (KV Cache per seq × max_num_seqs(8) × max_model_len(262144)) + (Activation memory for batch) + (TP communication buffers)，其中 KV Cache 在 fp8 下约为 [待核验] GB/seq@262k，导致有效并发数远低于 max_num_seqs=8。

## Corrected Claim

显存占用模型：总显存消耗 = (27B params × 4-bit quant size ≈ 13.5GB) + (KV Cache per seq × max_num_seqs(8) × max_model_len(262144)) + (Activation memory for batch) + (TP communication buffers)，其中 KV Cache 在 fp8 下取决于模型注意力头配置，通常占据显著比例，导致有效并发数受限于显存上限。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点之间存在严重的逻辑依赖和数值冗余。子节点1计算出的'单序列33.5GB'是子节点2推导'并发能力'的核心输入变量，两者并非正交关系，而是'参数定义'与'系统容量推演'的层级关系。此外，子节点2中关于'短上下文支持6-7个序列'的结论基于错误的硬件假设（V100不支持FP8且显存带宽极低，无法承载此量级KV Cache），与父节点隐含的高性能推理场景（通常指A100/H100等）存在潜在矛盾，导致整体分解在事实层面不一致。）
