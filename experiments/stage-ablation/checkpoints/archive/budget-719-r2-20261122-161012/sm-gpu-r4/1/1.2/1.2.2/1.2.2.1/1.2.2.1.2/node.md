# N353: GQA 因子对 KV Cache 带宽压力的量化影响：在 Decode 阶段，读取 KV Cache 的数据量与 num_kv_heads 成正比；Qwen3-

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

GQA 因子对 KV Cache 带宽压力的量化影响：在 Decode 阶段，读取 KV Cache 的数据量与 num_kv_heads 成正比；Qwen3-27B 的 8 个 KV 头使得每 token 读取量为 8 * 128 * 2 * 64 = 128 KB (BF16)，若采用 MHA (40头) 则为 640 KB，GQA 使带宽需求降低 80%，从而允许在相同带宽下支持 5 倍的并发或更长的上下文

## Corrected Claim

GQA 因子对 KV Cache 带宽压力的量化影响：在 Decode 阶段，读取 KV Cache 的数据量与 num_kv_heads 成正比；Qwen3-27B 的 8 个 KV 头使得每 token 读取量为 8 * 128 * 2 * 64 = 128 KB (BF16)，若采用 MHA (40头) 则为 640 KB，GQA 使带宽需求降低 80%，从而允许在相同带宽下支持 5 倍的并发或更长的上下文

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（40 Q heads, 8 KV heads, head_dim 128）符合公开技术报告；计算过程 8*128*2*64=128KB 及 MHA 对比 640KB 数学正确；GQA 降低 80% 带宽需求及 5 倍并发/上下文推论符合线性比例关系。
