# N38: 长上下文窗口 (262k tokens) 在 V100 16GB 显存限制下的有效可用长度 L_eff：受 KV Cache 占用影响，当 max_model_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

长上下文窗口 (262k tokens) 在 V100 16GB 显存限制下的有效可用长度 L_eff：受 KV Cache 占用影响，当 max_model_len=262144 时，KV Cache 显存占用 O(L*D*KH) 将挤占权重显存，导致实际并发序列数 max_num_seqs 降至 1 或触发 OOM，需计算临界长度 L_crit = (Total_VRAM - Weight_VRAM - Activation_VRAM) / (Layers * Heads * Head_Dim * 2 * Bytes_per_KV)，该值决定单次科研实验能注入的最大文献量。

## Corrected Claim

长上下文窗口 (262k tokens) 在 V100 16GB 显存限制下的有效可用长度 L_eff：受 KV Cache 占用影响，当 max_model_len=262144 时，KV Cache 显存占用 O(L*D*KH) 将挤占权重显存，导致实际并发序列数 max_num_seqs 降至 1 或触发 OOM，需计算临界长度 L_crit = (Total_VRAM - Weight_VRAM - Activation_VRAM) / (Layers * Heads * Head_Dim * 2 * Bytes_per_KV)，该值决定单次科研实验能注入的最大文献量。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用公式及临界长度推导符合 Transformer 架构基本原理，量纲与逻辑自洽。

## Search Query

vLLM KV cache memory calculation long context V100 16GB max model length effective context limit
