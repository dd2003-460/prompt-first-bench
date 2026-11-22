# N136: RTX 4080 Super 的显存带宽为 736 GB/s，若强行在短上下文（如 4K）下运行 INT4 模型，理论 Decode 吞吐上限约为 736 / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

RTX 4080 Super 的显存带宽为 736 GB/s，若强行在短上下文（如 4K）下运行 INT4 模型，理论 Decode 吞吐上限约为 736 / (13.5 + 1.1) ≈ 50 tokens/s（假设 KV Cache 1.1GB），但其性价比低于 RTX 4090（45.5 tokens/s @ 32K），因为 4080 Super 无法支持题目要求的 32K 上下文，故在本题约束下被排除。

## Corrected Claim

RTX 4080 Super 的显存带宽为 736 GB/s，若强行在短上下文（如 4K）下运行 INT4 模型，理论 Decode 吞吐上限约为 736 / (13.5 + 1.1) ≈ 50 tokens/s（假设 KV Cache 1.1GB），但其性价比低于 RTX 4090（45.5 tokens/s @ 32K），因为 4080 Super 无法支持题目要求的 32K 上下文，故在本题约束下被排除。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1侧重于‘性价比/经济性’维度的对比分析（解释为何在特定场景下虽便宜但不可行），子节点2侧重于‘决策逻辑/架构约束’维度的排除依据（解释为何在硬约束下直接排除及多卡方案的排除理由）。两者视角不同，无重复，且共同覆盖了父节点中关于‘排除原因’和‘性价比对比’的所有关键信息。）
