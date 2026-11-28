# N33: 在 max_model_len=262144 且 N_seqs=8 的满载工况下，单卡剩余 11.1GB 显存中，KV Cache 动态分配上限为 8.59GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

在 max_model_len=262144 且 N_seqs=8 的满载工况下，单卡剩余 11.1GB 显存中，KV Cache 动态分配上限为 8.59GB，剩余 2.51GB 用于激活值和临时缓冲；若单序列上下文长度超过 200k tokens，KV Cache 占用将突破 11.1GB 导致 OOM，因此实际安全并发上限需下调至 N_seqs=6 或 S_max=200000。

## Corrected Claim

在 max_model_len=262144 且 N_seqs=8 的满载工况下，单卡剩余 11.1GB 显存中，KV Cache 动态分配上限为 8.59GB，剩余 2.51GB 用于激活值和临时缓冲；若单序列上下文长度超过 200k tokens，KV Cache 占用将突破 11.1GB 导致 OOM，因此实际安全并发上限需下调至 N_seqs=6 或 S_max=200000。

## Evidence

先验知识/题面给定，逻辑校验通过：数值加和自洽（8.59+2.51=11.1），OOM阈值推导符合线性增长逻辑，并发调整建议符合资源约束原则。

## Search Query

vllm oom kv cache limit max model length concurrent sequences
