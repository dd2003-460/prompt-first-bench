# N113: 修正 N58 的 KV Cache 计算：基于 N71 验证的正确公式（2 KB/token），15k tokens 的上下文占用显存为 15,000 * 2 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57, N58, N59

## Claim

修正 N58 的 KV Cache 计算：基于 N71 验证的正确公式（2 KB/token），15k tokens 的上下文占用显存为 15,000 * 2 KB = 30 MB，而非 N58 声称的 960 MB；N58 错误地使用了 64 KB/token（未除以 GQA 分组数或误算层数），导致高估 32 倍，结论'60% of budget'完全失效，实际占用仅占单卡剩余显存的 ~0.2%。

## Corrected Claim

修正 N58 的 KV Cache 计算：基于 N71 验证的正确公式（2 KB/token），15k tokens 的上下文占用显存为 15,000 * 2 KB = 30 MB，而非 N58 声称的 960 MB；N58 错误地使用了 64 KB/token（未除以 GQA 分组数或误算层数），导致高估 32 倍，结论'60% of budget'完全失效，实际占用仅占单卡剩余显存的 ~0.2%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 15,000 * 2 KB = 30 MB 正确；30 MB 相对于典型单卡剩余显存（如 20 GB+）占比约 0.15%-0.2%，量级合理；N58 的 960 MB 与 30 MB 之比确为 32 倍，逻辑自洽。
