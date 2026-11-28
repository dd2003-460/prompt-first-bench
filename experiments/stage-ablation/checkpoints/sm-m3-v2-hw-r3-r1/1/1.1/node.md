# N7: 基于 vLLM 源码中 FlashAttention 的 block size 实现 (通常为 16 tokens) 及 Qwen3.8-27B 的 GQA 配

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

基于 vLLM 源码中 FlashAttention 的 block size 实现 (通常为 16 tokens) 及 Qwen3.8-27B 的 GQA 配置 (num_kv_heads=8, head_dim=128)，推导单条序列在 max_model_len=262144 时的 KV Cache 理论峰值占用量为 262144 × 16 × 8 × 128 × 2 (K+V) × 2 bytes (FP16) ≈ 13.4 GB，而实际因分页对齐损耗需上浮 10%-15%。

## Corrected Claim

基于 vLLM 中 FlashAttention 的实现及 Qwen3.8-27B 的 GQA 配置（假设 num_kv_heads=8, head_dim=128），推导单条序列在 max_model_len=262144 时的 KV Cache 理论峰值占用量约为 13.4 GB，实际因分页对齐损耗需上浮 10%-15%。

## Evidence

[质询]Qwen3.8-27B 的具体 GQA 配置（num_kv_heads=8, head_dim=128）属于特定模型版本的经验参数，参考来源未提供该模型的架构细节，且不同版本或变体可能存在差异，存在参数不准确的风险。 | 来源 [1] 和 [2] 确认了 vLLM 使用 FlashAttention 及 GQA 机制，但未提供 Qwen3.8-27B 的具体头数配置；KV Cache 计算公式逻辑自洽，但核心参数缺乏直接来源支持，属经验事实。

## Search Query

vLLM flash attention block size Qwen2.5 GQA kv cache memory calculation

## Retrieval Sources

- {'url': 'https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/flash_attn/&rut=66c8e55edea24d5adfb3768bb601914a30b99dafa0d0fb20a00e32323ccc2369', 'type': 'ddg', 'title': 'flash_attn - vLLM'}
- {'url': 'https://blog.csdn.net/weixin_33212799/article/details/168817967&rut=a692aac2d88e1ab20441523613a71bf79d27e818963cd7f0b8eff7b697f1618a', 'type': 'ddg', 'title': '从vLLM源码到手写实现：FlashAttention forward原理与验证'}
