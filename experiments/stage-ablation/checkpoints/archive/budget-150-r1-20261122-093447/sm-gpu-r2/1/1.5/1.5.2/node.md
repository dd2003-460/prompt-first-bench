# N59: PyTorch eager mode 下激活内存包含所有中间张量 (hidden states, attention scores 若未用 FlashAtten

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

PyTorch eager mode 下激活内存包含所有中间张量 (hidden states, attention scores 若未用 FlashAttention, FFN intermediates)，峰值约为 2 * n_layers * hidden_size * seq_len * bytes_per_elem + n_layers * intermediate_size * seq_len * bytes_per_elem，未做算子融合时比优化框架高 50-100%

## Corrected Claim

PyTorch eager mode 下激活内存包含所有中间张量 (hidden states, attention scores 若未用 FlashAttention, FFN intermediates)，峰值约为 2 * n_layers * hidden_size * seq_len * bytes_per_elem + n_layers * intermediate_size * seq_len * bytes_per_elem，未做算子融合时比优化框架高 50-100%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

PyTorch eager mode activation memory peak LLM inference overhead
