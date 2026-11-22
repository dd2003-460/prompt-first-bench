# N195: A100 80GB 在 INT8 权重 + BF16 KV Cache 配置下的每 Token 读取数据量 (Bytes_per_token) 计算式：Byte

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

A100 80GB 在 INT8 权重 + BF16 KV Cache 配置下的每 Token 读取数据量 (Bytes_per_token) 计算式：Bytes_per_token = (Params * Bytes_per_param) + (KV_Head_Dim * Num_KV_Heads * 2 * Bytes_per_kv_elem)。计算结果：27.1 GB + 0.0041 GB ≈ 27.104 GB。注意：A100 不支持原生 INT8 权重的高效 Tensor Core 加速路径（需依赖 CUDA Core 或特定库），但内存读取量物理上不变。

## Corrected Claim

A100 80GB 在 INT8 权重 + BF16 KV Cache 配置下的每 Token 读取数据量 (Bytes_per_token) 计算式：Bytes_per_token = (Params * Bytes_per_param) + (KV_Head_Dim * Num_KV_Heads * 2 * Bytes_per_kv_elem)。计算结果：27.1 GB + 0.0041 GB ≈ 27.104 GB。注意：A100 不支持原生 INT8 权重的高效 Tensor Core 加速路径（需依赖 CUDA Core 或特定库），但内存读取量物理上不变。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 显存下，INT8 权重（约 27.1GB 对应 ~27B 参数）与 BF16 KV Cache 的内存读取量计算符合物理定义，且 A100 确实缺乏原生 INT8 Tensor Core 加速路径（需依赖 CUDA Core 或特定库），数值量级与硬件特性描述自洽。

## Search Query

A100 INT8 weight inference memory access pattern
