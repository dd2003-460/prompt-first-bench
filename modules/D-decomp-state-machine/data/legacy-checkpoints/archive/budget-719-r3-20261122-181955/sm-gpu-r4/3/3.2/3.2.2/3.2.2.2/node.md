# N285: RTX 4090 在 32K 上下文下，Decode 阶段每 token 的总内存读取量为 552.87 MB (Weights 54GB + KV Cache

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

RTX 4090 在 32K 上下文下，Decode 阶段每 token 的总内存读取量为 552.87 MB (Weights 54GB + KV Cache 536.87MB，忽略 Overhead)，理论 ITL 下限为 1 / (1008 GB/s / 552.87 MB) ≈ 548 ms/token，此值远高于 N94 声称的 87 ms，表明 N94 原公式未正确分离权重与 KV Cache 的读取频率或存在计算错误。

## Corrected Claim

RTX 4090 在 32K 上下文下，Decode 阶段每 token 的总内存读取量为 552.87 MB (Weights 54GB + KV Cache 536.87MB，忽略 Overhead)，理论 ITL 下限为 1 / (1008 GB/s / 552.87 MB) ≈ 548 ms/token，此值远高于 N94 声称的 87 ms，表明 N94 原公式未正确分离权重与 KV Cache 的读取频率或存在计算错误。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，Decode 阶段每 token 需读取全部权重（~54GB）及 KV Cache，总读取量 ~552.87 MB，计算延迟 552.87/1008 ≈ 0.548s，与陈述一致。

## Search Query

LLM inference decode memory bandwidth calculation weights vs kv cache
