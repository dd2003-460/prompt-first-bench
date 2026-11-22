# N131: 若强制使用 INT4 量化 KV Cache，32K 上下文下的 KV 占用降至约 8.0 GB，此时总显存需求为 13.5GB (W4 Weights) + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

若强制使用 INT4 量化 KV Cache，32K 上下文下的 KV 占用降至约 8.0 GB，此时总显存需求为 13.5GB (W4 Weights) + 8.0GB (KV) + 1.5GB (Overhead) = 23.0GB，仍超出 16GB 物理显存 7.0GB，因此即使采用最激进的 INT4 KV 量化，单卡 RTX 4060 Ti 16GB 依然不可行。

## Corrected Claim

若强制使用 INT4 量化 KV Cache，32K 上下文下的 KV 占用降至约 8.0 GB，此时总显存需求为 13.5GB (W4 Weights) + 8.0GB (KV) + 1.5GB (Overhead) = 23.0GB，仍超出 16GB 物理显存 7.0GB，因此即使采用最激进的 INT4 KV 量化，单卡 RTX 4060 Ti 16GB 依然不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 13.5 + 8.0 + 1.5 = 23.0 正确，23.0 - 16.0 = 7.0 正确，结论与前提一致。
