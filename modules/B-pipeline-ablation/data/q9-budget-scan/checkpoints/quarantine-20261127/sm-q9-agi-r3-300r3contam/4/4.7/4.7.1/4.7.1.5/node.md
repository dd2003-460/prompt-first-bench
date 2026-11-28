# N212: M_required 的量化误差源：2 × P_params × Bytes_per_param 未计入 KV Cache 与激活内存，实际 M_require

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N73

## Claim

M_required 的量化误差源：2 × P_params × Bytes_per_param 未计入 KV Cache 与激活内存，实际 M_required = M_weights + M_KV_cache + M_activation，其中 M_KV_cache 在 262k context 下可能占 30-50%。

## Corrected Claim

M_required 的量化误差源：2 × P_params × Bytes_per_param 未计入 KV Cache 与激活内存，实际 M_required = M_weights + M_KV_cache + M_activation，其中 M_KV_cache 在 262k context 下可能占 30-50%。

## Evidence

先验知识/题面给定，逻辑校验通过：M_required 确实由权重、KV Cache 和激活内存组成；在长上下文（262k）下，KV Cache 随序列长度线性增长，占比显著（30-50% 符合大模型推理显存分布常识），原公式仅计算权重确实遗漏了主要动态内存项。
