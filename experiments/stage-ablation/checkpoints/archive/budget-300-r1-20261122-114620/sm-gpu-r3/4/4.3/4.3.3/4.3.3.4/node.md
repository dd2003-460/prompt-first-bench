# N342: 在 batch_size=1 的 Decode 阶段，每生成一个 token 的 T_compute 约为 20ms (RTX 4090, 50 tokens/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

在 batch_size=1 的 Decode 阶段，每生成一个 token 的 T_compute 约为 20ms (RTX 4090, 50 tokens/s)，T_comm 仍为 0.064 秒/层但仅发生一次，η_comm_decode ≈ 0.064 / (0.02 + 0.064) ≈ 76%，表明 Decode 阶段通信开销占比极高，需区分 Prefill 和 Decode 阶段的 η_comm

## Corrected Claim

在 batch_size=1 的 Decode 阶段，每生成一个 token 的 T_compute 约为 20ms (RTX 4090, 50 tokens/s)，T_comm 仍为 0.064 秒/层但仅发生一次，η_comm_decode ≈ 0.064 / (0.02 + 0.064) ≈ 76%，表明 Decode 阶段通信开销占比极高，需区分 Prefill 和 Decode 阶段的 η_comm

## Evidence

先验知识/题面给定，逻辑校验通过：50 tokens/s 对应 20ms/token 计算时间，0.064s 通信时间占比 76% 的算术推导正确，符合 Decode 阶段通信瓶颈的物理直觉。
