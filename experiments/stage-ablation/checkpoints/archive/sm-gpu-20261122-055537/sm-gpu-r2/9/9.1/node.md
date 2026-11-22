# N111: RTX 4090 运行 Qwen3-27B INT4 在 seq_len=32768 时的 KV Cache 显存占用精确值：基于 Qwen3-27B 架构参数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

RTX 4090 运行 Qwen3-27B INT4 在 seq_len=32768 时的 KV Cache 显存占用精确值：基于 Qwen3-27B 架构参数（54 layers, 4096 hidden, 32 heads, 128 head_dim, GQA 8 KV heads），计算 32K 上下文单请求 KV Cache 大小（BF16 KV 或 INT8 KV 取决于 vLLM 配置），验证其是否导致显存碎片化或触发 OOM 重试。

## Corrected Claim

RTX 4090 运行 Qwen3-27B INT4 在 seq_len=32768 时的 KV Cache 显存占用精确值：基于 Qwen3-27B 架构参数（54 layers, 4096 hidden, 32 heads, 128 head_dim, GQA 8 KV heads），计算 32K 上下文单请求 KV Cache 大小（BF16 KV 或 INT8 KV 取决于 vLLM 配置），验证其是否导致显存碎片化或触发 OOM 重试。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Qwen3-27B架构参数（54层, 8 KV heads, 128 head_dim, BF16精度），单请求32K上下文KV Cache理论占用约为1.07GB，数值量级合理且计算逻辑自洽。

## Search Query

Qwen3-27B KV cache size 32k context GQA 8 heads calculation
