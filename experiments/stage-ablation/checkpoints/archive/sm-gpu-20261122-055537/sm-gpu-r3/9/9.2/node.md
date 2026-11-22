# N112: RTX 4090 在长上下文 (32K) 下吞吐量从 80-100 tokens/s 降至 40-60 tokens/s 的瓶颈归因：量化分析 Attentio

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

RTX 4090 在长上下文 (32K) 下吞吐量从 80-100 tokens/s 降至 40-60 tokens/s 的瓶颈归因：量化分析 Attention 计算量（O(N^2)）与 KV Cache 读取带宽（O(N)）在总延迟中的占比，确定是算力瓶颈（Compute-bound）还是带宽瓶颈（Memory-bound），以判断是否可通过 FlashAttention-2/3 优化恢复部分性能。

## Corrected Claim

RTX 4090 在长上下文 (32K) 下吞吐量下降（例如从 80-100 tokens/s 降至 40-60 tokens/s，具体数值依模型而定）的瓶颈通常涉及 Attention 计算量（O(N^2)）与 KV Cache 读取带宽（O(N)）的权衡；需通过量化分析确定是算力瓶颈（Compute-bound）还是带宽瓶颈（Memory-bound），以评估 FlashAttention-2/3 等优化的潜在收益。

## Evidence

父节点级核验未通过：不完备（子节点逻辑链条清晰且互不重叠（正交性良好），无冗余。但存在完备性缺陷：父节点要求归因于'Attention 计算量'与'KV Cache 读取带宽'的占比对比，子节点2仅估算了总内存读取量（权重+KV Cache），未单独量化 KV Cache 在总带宽消耗中的占比，也未在子节点3中明确展示 Attention 计算耗时与内存读取耗时的具体对比数据，导致无法严格满足'量化分析...占比'这一核心要求。）

## Search Query

RTX 4090 LLM inference long context bottleneck compute vs memory bandwidth FlashAttention
