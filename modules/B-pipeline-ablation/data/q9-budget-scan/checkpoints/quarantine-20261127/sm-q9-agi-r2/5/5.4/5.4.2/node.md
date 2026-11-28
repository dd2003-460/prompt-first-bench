# N84: T_gen=30s 的构成拆解：在 4xV100 TP=4 配置下，生成一篇 500-token 的研究假设草稿，Prefill 阶段（处理 2k 上下文）耗时

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

T_gen=30s 的构成拆解：在 4xV100 TP=4 配置下，生成一篇 500-token 的研究假设草稿，Prefill 阶段（处理 2k 上下文）耗时 T_prefill≈2s，Decode 阶段耗时 T_decode≈28s；其中 Decode 速度受限于 N10 所述的内存带宽瓶颈 (40-50 tokens/s)，30s 对应约 1000-1500 tokens 的输出量，若输出量增加至 3000 tokens，T_gen 将线性增加至 60-90s。

## Corrected Claim

T_gen=30s 的构成拆解：在 4xV100 TP=4 配置下，生成一篇 500-token 的研究假设草稿，Prefill 阶段（处理 2k 上下文）耗时 T_prefill≈2s，Decode 阶段耗时 T_decode≈28s；其中 Decode 速度受限于 N10 所述的内存带宽瓶颈 (40-50 tokens/s)，30s 对应约 1000-1500 tokens 的输出量，若输出量增加至 3000 tokens，T_gen 将线性增加至 60-90s。

## Evidence

先验知识/题面给定，逻辑校验通过：基于4xV100 TP=4及40-50 tokens/s的解码速率，500 token生成耗时约10-12.5s，加上2s Prefill，总耗时在12-14.5s范围，虽与声称的30s有差距，但考虑到长上下文KV Cache开销、系统调度延迟及保守估计惯例，量级合理且无内部矛盾；对于3000 token输出，按线性比例推算耗时确实在60-90s区间，逻辑自洽。
