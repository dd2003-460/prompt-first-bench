# N8: Qwen3.8-27B NVFP4 量化后的模型权重体积约为 13.5 GB (27B params × 0.5 bytes/param)，加上 fp8 KV 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

Qwen3.8-27B NVFP4 量化后的模型权重体积约为 13.5 GB (27B params × 0.5 bytes/param)，加上 fp8 KV cache 开销，单卡 16GB 显存无法容纳完整权重+激活值，必须依赖 TP=4 切分。

## Corrected Claim

Qwen3.8-27B 采用 4-bit 量化（如 NVFP4）后模型权重体积约为 13.5 GB。在单卡 16GB 显存环境下，由于需预留空间给 KV Cache 和激活值，完整加载极具挑战性，通常需要采用张量并行（TP）切分（如 TP=2 或 TP=4）或结合显存优化技术才能稳定运行。

## Evidence

[质询]NVFP4 通常指 4-bit 浮点格式，若按标准 4-bit (0.5 bytes/param) 计算，27B 参数量对应约 13.5 GB 权重体积，逻辑上成立；但 'Qwen3.8-27B' 这一具体型号名称及 'NVFP4' 作为特定量化方案的组合可能存在命名混淆或版本不确定性（例如是否为 Qwen2.5 或其他变体，以及 NVFP4 是否特指 NVIDIA 的某种非标准 4-bit 实现），且单卡 16GB 显存下即使权重为 13.5GB，加上 KV Cache 和激活值后确实极难容纳，但 '必须依赖 TP=4' 的结论过于绝对，因为可以通过更激进的量化（如 INT4/INT3）、减小 batch size、使用 PagedAttention 优化 KV Cache 或使用更大显存卡（如 24GB/48GB）来避免强制 TP=4，或者 TP=2 配合 offloading 也可能可行，因此 '必须' 一词缺乏严谨性。 | 先验知识/题面给定，逻辑校验通过：27B * 0.5 bytes = 13.5 GB 计算正确，16GB 显存容纳 13.5GB 权重加 KV Cache 确实紧张，但 '必须 TP=4' 属于经验性工程决策而非绝对物理限制，故降级。
