# N271: 修正后的总显存占用与可行性判断：14.5 GB (权重) + 9.23 GB (KV Cache) + 2.0 GB (激活/框架) = 25.73 GB，超过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

修正后的总显存占用与可行性判断：14.5 GB (权重) + 9.23 GB (KV Cache) + 2.0 GB (激活/框架) = 25.73 GB，超过 RTX 4090 的 24 GB 显存上限，导致 OOM；因此父节点 N82 的'可行'结论在 BF16 KV Cache 下不成立，必须启用 FP8/INT8 KV Cache 或减小上下文窗口。

## Corrected Claim

修正后的总显存占用与可行性判断：14.5 GB (权重) + 9.23 GB (KV Cache) + 2.0 GB (激活/框架) = 25.73 GB，超过 RTX 4090 的 24 GB 显存上限，导致 OOM；因此父节点 N82 的'可行'结论在 BF16 KV Cache 下不成立，必须启用 FP8/INT8 KV Cache 或减小上下文窗口。

## Evidence

先验知识/题面给定，逻辑校验通过：14.5+9.23+2.0=25.73>24，算术正确且符合显存占用逻辑
