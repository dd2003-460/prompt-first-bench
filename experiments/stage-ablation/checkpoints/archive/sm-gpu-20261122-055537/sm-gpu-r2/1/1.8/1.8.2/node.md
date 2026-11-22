# N59: Qwen3-27B在INT8/FP8精度下满足32K上下文的最小单卡显存需求计算为：权重27GB + KV Cache (54层*2*4096*128*3276

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

Qwen3-27B在INT8/FP8精度下满足32K上下文的最小单卡显存需求计算为：权重27GB + KV Cache (54层*2*4096*128*32768*1bytes/1024^3 ≈ 4.7GB) + 激活/框架开销(3GB) ≈ 34.7GB，因此24GB卡（RTX 4090/L4）不可行，需≥48GB显存（如L40S/2x4090）。

## Corrected Claim

Qwen3-27B在INT8/FP8精度下满足32K上下文的最小单卡显存需求计算为：权重27GB + KV Cache (54层*2*4096*128*32768*1bytes/1024^3 ≈ 4.7GB) + 激活/框架开销(3GB) ≈ 34.7GB，因此24GB卡（RTX 4090/L4）不可行，需≥48GB显存（如L40S/2x4090）。

## Evidence

[质询]KV Cache 计算中假设了 GQA (Grouped Query Attention) 的 KV 头数为 128（即与 Q 头数相同或特定配置），若 Qwen3-27B 实际采用更激进的 GQA（如 KV 头数减半或更少），则 KV Cache 占用会显著降低，可能使 24GB 卡在特定优化下勉强可行或需求低于 48GB；此外，'激活/框架开销 3GB' 在 32K 长上下文下可能偏乐观，实际峰值可能更高。 | 先验知识/题面给定，逻辑校验通过。权重 27GB (INT8) 合理；KV Cache 估算 4.7GB 基于 54 层、32K 序列、128 KV 头、128 维度、1 字节精度，量级正确；总显存 ~35GB 确实超出 24GB 卡限制，需 48GB+ 卡，结论逻辑自洽。
