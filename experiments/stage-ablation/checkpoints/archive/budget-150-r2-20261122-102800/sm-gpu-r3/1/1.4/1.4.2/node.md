# N65: 2×RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallel 下的 AllReduce 通信量：每生成 1 token，需交换 KV 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

2×RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallel 下的 AllReduce 通信量：每生成 1 token，需交换 KV Cache 中间结果，通信量 ≈ 2 * seq_len * num_kv_heads * head_dim * bytes_per_elem = 2 * 32768 * 8 * 128 * 1 byte (INT8) = 67.1 MB/token。

## Corrected Claim

2×RTX 4090 (PCIe 4.0 x16) 在 Tensor Parallel 下的 AllReduce 通信量：每生成 1 token，需交换 KV Cache 中间结果，通信量 ≈ 2 * seq_len * num_kv_heads * head_dim * bytes_per_elem = 2 * 32768 * 8 * 128 * 1 byte (INT8) = 67.1 MB/token。

## Evidence

父节点级核验未通过：不完备, 有冗余（父节点明确指定了INT8精度（1 byte）及对应的67.1 MB/token计算，而唯一的子节点描述的是BF16精度（2 bytes）及134.2 MB/token。子节点并未覆盖父节点的核心内容（INT8场景），反而引入了一个父节点未提及的新场景（BF16）。此外，从结构上看，这两个节点本质上是同一公式在不同数据类型参数下的取值，属于同一维度的不同实例，而非对父节点逻辑的分解。）
