# N41: RTX 3090 的 BF16/FP16 Tensor 算力为 35.6 TFLOPS，显存带宽为 936 GB/s，显存容量 24GB GDDR6X

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

RTX 3090 的 BF16/FP16 Tensor 算力为 35.6 TFLOPS，显存带宽为 936 GB/s，显存容量 24GB GDDR6X

## Corrected Claim

RTX 3090 的 BF16/FP16 Tensor 算力为 35.6 TFLOPS，显存带宽为 936 GB/s，显存容量 24GB GDDR6X

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性不足：子节点1（显存容量）和子节点2（显存带宽）都深度依赖并重复计算了相同的量化模型参数（INT4权重13.5GB + KV Cache 8.59GB），导致逻辑耦合严重，并非独立的维度。2. 完备性缺失：父节点明确包含“BF16/FP16 Tensor 算力 35.6 TFLOPS”这一关键规格，但三个子节点均未涉及算力（Compute）维度的分析，遗漏了父节点的核心属性之一。3. 冗余判断：虽然子节点1和2共享数据，但它们分别对应“容量约束”和“带宽瓶颈”两个不同的物理限制维度，不属于同一参数的不同取值，因此不构成严格意义上的冗余，但存在信息重叠。）
