# N146: 在典型Research-AGI工作流（假设平均有效上下文长度为4k tokens）下，8序列并发的总KV显存需求为 8 * 4096 * 12KB ≈ 384M

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

在典型Research-AGI工作流（假设平均有效上下文长度为4k tokens）下，8序列并发的总KV显存需求为 8 * 4096 * 12KB ≈ 384MB，仅占单卡11.125GB可用显存的3.4%，表明显存竞争在典型短上下文场景下不构成瓶颈，瓶颈转移至计算带宽与TP通信。

## Corrected Claim

在典型Research-AGI工作流（假设平均有效上下文长度为4k tokens）下，8序列并发的总KV显存需求为 8 * 4096 * 12KB ≈ 384MB，仅占单卡11.125GB可用显存的3.4%，表明显存竞争在典型短上下文场景下不构成瓶颈，瓶颈转移至计算带宽与TP通信。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 8*4096*12KB=384MB 正确，占比 384/11125≈3.4% 正确，符合典型短上下文场景下KV Cache非瓶颈的工程常识。
