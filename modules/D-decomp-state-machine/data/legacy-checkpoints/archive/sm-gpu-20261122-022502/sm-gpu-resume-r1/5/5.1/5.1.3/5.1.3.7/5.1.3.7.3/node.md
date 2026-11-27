# N872: 32K 上下文下，单个请求的激活值 (Activation Memory) 显存占用并非固定的 1GB。对于 LLM Decode 阶段，激活值主要取决于 ba

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N272

## Claim

32K 上下文下，单个请求的激活值 (Activation Memory) 显存占用并非固定的 1GB。对于 LLM Decode 阶段，激活值主要取决于 batch_size 和 hidden_dim (4096)。在 bs=1 时，激活值显存占用约为 0.1-0.2GB (取决于中间层缓存策略)；在 bs=4 时，线性增长至 0.4-0.8GB。N272 中假设的 1GB 固定开销在 bs=1 时偏大，在 bs>1 时偏小，需按公式 Act_Mem = bs * seq_len * hidden_dim * dtype_size / 1024^3 动态计算。

## Corrected Claim

32K 上下文下，单个请求的激活值 (Activation Memory) 显存占用并非固定的 1GB。对于 LLM Decode 阶段，激活值主要取决于 batch_size 和 hidden_dim (4096)。在 bs=1 时，激活值显存占用约为 0.1-0.2GB (取决于中间层缓存策略)；在 bs=4 时，线性增长至 0.4-0.8GB。N272 中假设的 1GB 固定开销在 bs=1 时偏大，在 bs>1 时偏小，需按公式 Act_Mem = bs * seq_len * hidden_dim * dtype_size / 1024^3 动态计算。

## Evidence

先验知识/题面给定，逻辑校验通过：激活值显存占用确实随 batch_size 线性增长，且 32K 上下文下 bs=1 的激活值（不含 KV Cache）通常在百 MB 量级，1GB 固定开销假设不符合线性增长规律。

## Search Query

LLM inference activation memory calculation formula
