# N445: RTX 4090 在 32K 上下文长度下的 KV Cache 显存占用计算：2 * 32 (layers) * 8 (KV heads) * 128 (hea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N144

## Claim

RTX 4090 在 32K 上下文长度下的 KV Cache 显存占用计算：2 * 32 (layers) * 8 (KV heads) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes, BF16) = 4.29 GB；若使用 INT8 KV Cache 则为 2.15 GB

## Corrected Claim

RTX 4090 在 32K 上下文长度下的 KV Cache 显存占用计算：2 * 32 (layers) * 8 (KV heads) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes, BF16) = 4.29 GB；若使用 INT8 KV Cache 则为 2.15 GB

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 搭载的 LLaMA-2 70B 等主流大模型架构中，32层、8个KV头、128维头维度是标准配置；计算公式 2 * 32 * 8 * 128 * 32768 * 2 bytes = 4,294,967,296 bytes = 4.29 GB (GiB) 数学推导正确，INT8 减半为 2.15 GB 亦符合逻辑。
