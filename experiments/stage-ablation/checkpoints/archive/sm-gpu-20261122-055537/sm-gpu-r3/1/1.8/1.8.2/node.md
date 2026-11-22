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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1和2分别独立修正了权重和KV Cache的计算错误（指出原父节点假设MHA导致KV Cache高估），节点3基于修正值重新推导最小显存需求，节点4进一步利用剩余显存推导并发能力。各节点关注点不同（参数修正、架构修正、总需求验证、扩展能力），无重复或矛盾。）
