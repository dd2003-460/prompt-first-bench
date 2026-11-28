# N510: 工作点3 (BS=1, L=262144) 下 4×V100 TP=4 的 KV Cache 显存占用极限计算：Mem_KV = num_layers × nu

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N183

## Claim

工作点3 (BS=1, L=262144) 下 4×V100 TP=4 的 KV Cache 显存占用极限计算：Mem_KV = num_layers × num_kv_heads × head_dim × 262144 × 1 × 2 (fp8 bytes)，需验证是否超过单卡 16GB 物理上限或触发 OOM

## Corrected Claim

工作点3 (BS=1, L=262144) 下 4×V100 TP=4 的 KV Cache 显存占用需根据具体模型的层数、KV头数和头维度计算：Mem_KV = num_layers × num_kv_heads × head_dim × 262144 × 1 × 2 (fp8 bytes)。若使用 16GB 版本的 V100，需验证该值是否超过单卡 16GB 上限；若使用 32GB 版本则阈值不同。

## Evidence

[质询]该陈述包含具体的硬件参数（V100 16GB）和模型架构假设（num_layers, num_kv_heads, head_dim），属于经验事实。虽然 V100 16GB 是常见规格，但 V100 也有 32GB 版本，且未指定具体模型（如 LLaMA-7B 还是其他），导致 'num_layers' 等变量未定义，无法从第一性原理严格推出唯一数值，且缺乏来源支持具体的模型配置。 | 经验事实，逻辑自洽但缺来源支持。公式结构符合 KV Cache 计算原理（层数*头数*维度*序列长度*Batch*字节数），但具体数值依赖未给定的模型参数，且 V100 显存规格存在 16GB/32GB 两种，无法确证 '16GB 物理上限' 为绝对前提。

## Search Query

Qwen3.8-27B max context length 262144 vllm oom memory limit v100 16gb
