# N358: 在 RTX 4090 (1008 GB/s) 上，64K 上下文 BF16 因显存不足不可行；在 A100 (2039 GB/s) 上，64K BF16 的理论

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N124

## Claim

在 RTX 4090 (1008 GB/s) 上，64K 上下文 BF16 因显存不足不可行；在 A100 (2039 GB/s) 上，64K BF16 的理论 Decode 速度相比 32K 下降约 14% (从 ~38 tokens/s 降至 ~33 tokens/s)，具体数值需实测校正。

## Corrected Claim

在 RTX 4090 (24GB 显存) 上，64K 上下文 BF16 因显存不足通常不可行；在 A100 (80GB 显存, 2039 GB/s) 上，64K BF16 的理论 Decode 速度相比 32K 会因 KV Cache 读取量增加而下降，具体降幅取决于模型架构和实现，需实测校正。

## Evidence

[质询]具体数值（38 tokens/s 降至 33 tokens/s）属于经验事实，缺乏实测数据支持，且不同模型架构（如是否使用 GQA/MLA）会导致 KV Cache 大小和带宽瓶颈差异巨大，直接给出具体 Token/s 数值过于武断。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090 显存 24GB 确实难以承载 64K BF16 上下文（KV Cache 占用大），A100 带宽 2039 GB/s 高于 4090，但 Decode 速度受 KV Cache 读取带宽限制，上下文长度增加导致 KV Cache 变大，速度下降符合物理直觉，但具体数值需实测。
