# N581: 13.42GB 余量充足的前提是权重和 KV Cache 已完全加载。若启用量化 (如 FP8/INT8)，权重大小减半，余量增加至 ~27GB，可支持更大 b

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N177

## Claim

13.42GB 余量充足的前提是权重和 KV Cache 已完全加载。若启用量化 (如 FP8/INT8)，权重大小减半，余量增加至 ~27GB，可支持更大 batch_size 或更长上下文 (如 64K/128K)，此时 OOM 风险进一步降低，但需权衡量化对质量的影响。

## Corrected Claim

13.42GB 余量充足的前提是权重和 KV Cache 已完全加载。若启用量化 (如 FP8/INT8)，权重大小减半，余量增加至 ~27GB，可支持更大 batch_size 或更长上下文 (如 64K/128K)，此时 OOM 风险进一步降低，但需权衡量化对质量的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：量化（如FP8/INT8）确实将权重大小减半，从而增加显存余量，逻辑自洽且符合工程常识。
