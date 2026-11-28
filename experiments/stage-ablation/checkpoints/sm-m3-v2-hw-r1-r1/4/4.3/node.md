# N28: 短期工作记忆采用滑动窗口策略：保留最近 W=8192 tokens 的对话历史，超出部分压缩为摘要（Summary Compression Ratio r=0.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

短期工作记忆采用滑动窗口策略：保留最近 W=8192 tokens 的对话历史，超出部分压缩为摘要（Summary Compression Ratio r=0.2，即 8192 tokens 压缩至 1638 tokens），压缩后摘要插入上下文头部，总有效上下文长度 L_eff = W + 1638 ≈ 9830 tokens

## Corrected Claim

短期工作记忆采用滑动窗口策略：保留最近 W=8192 tokens 的对话历史，超出部分压缩为摘要（Summary Compression Ratio r=0.2，即 8192 tokens 压缩至 1638 tokens），压缩后摘要插入上下文头部，总有效上下文长度 L_eff = W + 1638 ≈ 9830 tokens

## Evidence

先验知识/题面给定，逻辑校验通过：W=8192, r=0.2 -> 摘要长度 8192*0.2=1638.4≈1638, L_eff=8192+1638=9830，计算无误且符合滑动窗口压缩机制的逻辑定义。

## Search Query

sliding window context management summary compression ratio LLM agent memory
