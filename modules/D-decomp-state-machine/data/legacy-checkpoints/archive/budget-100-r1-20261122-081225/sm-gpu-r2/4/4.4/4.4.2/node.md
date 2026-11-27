# N133: H100 SXM 80GB 在 BF16 精度下运行 Qwen3-27B (32K ctx) 时的理论显存需求为 81.65 GB，超出 80GB 物理显存 1

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

H100 SXM 80GB 在 BF16 精度下运行 Qwen3-27B (32K ctx) 时的理论显存需求为 81.65 GB，超出 80GB 物理显存 1.65 GB (2.06%)，必须通过启用 FlashAttention-2 或 KV Cache 量化至 FP16/INT8 才能避免 OOM 错误。

## Corrected Claim

H100 SXM 80GB 在 BF16 精度下运行 Qwen3-27B (32K ctx) 时，基础显存需求（权重+KV Cache）通常低于 80GB，但在高并发或大 batch size 场景下可能接近或超出显存限制，建议启用 FlashAttention-2 以优化 KV Cache 显存占用。

## Evidence

[质询]数值计算存在逻辑矛盾：Qwen3-27B 模型权重在 BF16 下约为 54GB，加上 32K 上下文的 KV Cache（约 10-15GB），总显存需求通常在 65-70GB 左右，远低于 80GB 物理显存，因此‘超出 80GB 物理显存’的结论与常规推理显存估算不符，可能混淆了‘理论最大激活值/中间层显存’与‘常驻显存’，或错误地假设了全量激活存储。 | 逻辑校验发现显存估算与模型规模及上下文长度不匹配，27B 模型在 32K 上下文下通常可装入 80GB 显存，无需强制量化或 FlashAttention 才能避免 OOM（除非使用极大 batch size 或特殊推理框架），且来源缺失无法验证具体 81.65GB 的计算依据。
