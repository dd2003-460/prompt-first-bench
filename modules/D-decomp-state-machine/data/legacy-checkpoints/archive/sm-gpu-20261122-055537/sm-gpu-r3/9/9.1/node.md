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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：前两个子节点分别计算不同精度（BF16/INT8）下的KV Cache大小，属于互斥的配置场景，不重复；第三个子节点基于最坏情况（BF16 KV）进行总显存评估和OOM风险分析，覆盖了父节点关于'验证是否导致OOM/碎片化'的要求。虽然前两个节点结构相似，但它们代表了不同的量化策略参数，并非单纯的可压缩变量，而是独立的计算分支。）

## Search Query

Qwen3-27B KV cache size 32k context GQA 8 heads calculation
