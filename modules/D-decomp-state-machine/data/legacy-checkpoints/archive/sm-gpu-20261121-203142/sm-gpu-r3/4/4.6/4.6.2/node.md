# N98: 激活值显存占用量化：在32K上下文下，每层激活值占用 ≈ batch_size * seq_len * hidden_dim * 2 bytes (BF16)，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

激活值显存占用量化：在32K上下文下，每层激活值占用 ≈ batch_size * seq_len * hidden_dim * 2 bytes (BF16)，对于Qwen3-27B (hidden_dim=4096)，单请求单层激活值约为 32768 * 4096 * 2 ≈ 256 MB，需累加所有层或根据Pipeline Parallelism分布计算总占用，这直接影响B_max的上限。

## Corrected Claim

激活值显存占用量化：在32K上下文下，每层激活值占用 ≈ batch_size * seq_len * hidden_dim * 2 bytes (BF16)，对于Qwen3-27B (hidden_dim=4096)，单请求单层激活值约为 32768 * 4096 * 2 ≈ 256 MB，需累加所有层或根据Pipeline Parallelism分布计算总占用，这直接影响B_max的上限。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：子节点1纠正了父节点中关于‘激活值’定义的简化误区（指出父节点公式仅覆盖残差流，忽略了FFN/Attention中间层）；子节点2基于修正后的定义进行具体数值估算；子节点3将估算结果应用于B_max约束分析，并解释了流式计算对总占用的影响。三者分别解决了定义、计算、应用三个不同层面的问题，无重复或矛盾。）
