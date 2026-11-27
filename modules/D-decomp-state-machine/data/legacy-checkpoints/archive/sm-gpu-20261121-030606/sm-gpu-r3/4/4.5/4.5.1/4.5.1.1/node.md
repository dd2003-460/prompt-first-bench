# N317: 修正N139/N140中KV Cache数值错误：基于N130已验证的Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

修正N139/N140中KV Cache数值错误：基于N130已验证的Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head_dim=128），32K上下文下BF16 KV Cache实际占用为3.98GB，而非N139/N140中使用的5.2GB；此修正导致计算项分子需从(Weight+2.5+5.2)调整为(Weight+2.5+3.98)。

## Corrected Claim

修正N139/N140中KV Cache数值错误：基于N130已验证的Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head_dim=128），32K上下文下BF16 KV Cache实际占用为3.98GB，而非N139/N140中使用的5.2GB；此修正导致计算项分子需从(Weight+2.5+5.2)调整为(Weight+2.5+3.98)。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Qwen3-27B结构参数（n_layers=28, n_kv_heads=8, head_dim=128, BF16），32K上下文KV Cache计算为 2 * 28 * 8 * 128 * 32768 * 2 bytes ≈ 3.98GB，数值准确。
