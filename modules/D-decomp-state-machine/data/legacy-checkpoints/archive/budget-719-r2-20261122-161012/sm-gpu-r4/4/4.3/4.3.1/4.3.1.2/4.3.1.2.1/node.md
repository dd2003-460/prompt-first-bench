# N519: Qwen3-27B 在 TP=2 配置下，每个 Transformer 层包含一个自注意力子层和一个前馈网络子层，每个子层的输出在拼接回主残差流前需执行一次 A

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N214

## Claim

Qwen3-27B 在 TP=2 配置下，每个 Transformer 层包含一个自注意力子层和一个前馈网络子层，每个子层的输出在拼接回主残差流前需执行一次 All-Reduce，因此每层通信次数为 2 次，总通信次数为 2 * 64 = 128 次/Token。

## Corrected Claim

Qwen3-27B 在 TP=2 配置下，每个 Transformer 层包含一个自注意力子层和一个前馈网络子层，每个子层的输出在拼接回主残差流前需执行一次 All-Reduce，因此每层通信次数为 2 次，总通信次数为 2 * 64 = 128 次/Token。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 确实包含 64 层 Transformer，标准 Transformer 架构每层含自注意力和前馈网络两个子层，在张量并行（TP）中每个子层输出需 All-Reduce 同步，故每层 2 次通信，总计 128 次。
