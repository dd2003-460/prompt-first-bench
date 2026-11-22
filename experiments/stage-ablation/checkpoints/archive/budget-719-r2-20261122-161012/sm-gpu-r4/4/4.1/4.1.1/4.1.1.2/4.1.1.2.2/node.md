# N477: 32K 上下文长度下 KV Cache 总显存占用（BF16）为 4.0 GB，计算公式为 128 KB/token * 32,768 tokens = 4,1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

32K 上下文长度下 KV Cache 总显存占用（BF16）为 4.0 GB，计算公式为 128 KB/token * 32,768 tokens = 4,194,304 KB = 4.0 GB；若使用 N197 错误的 256 KB/token 值，则错误估算为 8.0 GB，这将直接影响单卡/双卡方案的显存可行性判断（例如 24GB 卡是否足够）。

## Corrected Claim

32K 上下文长度下 KV Cache 总显存占用（BF16）为 4.0 GB，计算公式为 128 KB/token * 32,768 tokens = 4,194,304 KB = 4.0 GB；若使用 N197 错误的 256 KB/token 值，则错误估算为 8.0 GB，这将直接影响单卡/双卡方案的显存可行性判断（例如 24GB 卡是否足够）。

## Evidence

先验知识/题面给定，逻辑校验通过：128 KB * 32,768 = 4,194,304 KB，换算为 GB 即 4.0 GB，数学推导正确且量级合理。
