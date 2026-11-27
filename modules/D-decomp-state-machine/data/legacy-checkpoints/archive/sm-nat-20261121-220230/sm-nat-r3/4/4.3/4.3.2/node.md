# N69: LFU 保留集合与 LRU 保留集合的对称差集大小 K_diff 的估算：在 β=0.9 和 α=1.1 下，K_diff ≈ N * (1 - C_norm)

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

LFU 保留集合与 LRU 保留集合的对称差集大小 K_diff 的估算：在 β=0.9 和 α=1.1 下，K_diff ≈ N * (1 - C_norm)^{1/β} - N * (1 - C_norm)^{1/α}，该数值决定了 LFU 能额外保留多少个高热度对象。

## Corrected Claim

在特定热度分布假设下，LFU 与 LRU 保留集合的对称差集大小 K_diff 可通过基于热度阈值的积分估算，具体公式需结合 C_norm 的定义及热度分布模型确定，而非简单的幂函数形式。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 779)
