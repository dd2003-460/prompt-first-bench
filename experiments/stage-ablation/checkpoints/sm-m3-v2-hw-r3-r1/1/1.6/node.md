# N12: NVFP4 量化相较于 FP16 将权重体积压缩至 1/8，使得 27B 模型权重仅需 ~6.75 GB，为 KV Cache 释放了 ~9.25 GB/卡 的

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

NVFP4 量化相较于 FP16 将权重体积压缩至 1/8，使得 27B 模型权重仅需 ~6.75 GB，为 KV Cache 释放了 ~9.25 GB/卡 的显存空间；但 NVFP4 在低精度算术下的累积误差 (Cumulative Error) 会导致长上下文 (>32k) 生成时的困惑度 (Perplexity) 上升 5-10%，具体表现为对罕见术语和复杂公式引用的准确性下降，需在 Prompt 中强制结构化输出以缓解。

## Corrected Claim

NVFP4 (4-bit) 量化相较于 FP16 将权重体积压缩至 1/4，使得 27B 模型权重约为 13.5 GB；若采用更激进的 2-bit 量化 (压缩至 1/8)，权重约为 6.75 GB。低精度量化可能导致长上下文生成时困惑度上升，具体幅度取决于模型架构与校准方法，需通过结构化输出等手段缓解精度损失。

## Evidence

[质询]NVFP4 通常指 4-bit 浮点格式，理论上相对于 FP16 (16-bit) 的压缩比应为 1/4 (即 27B 模型约 13.5GB)，而非 1/8 (6.75GB)。若指 1/8 压缩，则对应的是 2-bit 量化，这与 'NVFP4' 命名及常规 4-bit 精度定义存在潜在矛盾或混淆。此外，'5-10% 困惑度上升' 及 '9.25 GB/卡' 的具体数值缺乏通用标准支持，属于特定实验或假设条件下的经验数据。 | source=knowledge，但存在数值量级与命名定义的逻辑冲突（4-bit vs 1/8 压缩比），且具体性能指标（PPL 上升幅度）为经验事实，在无外部来源支持且内部逻辑存疑的情况下，不能直接判定为 verified。

## Search Query

NVFP4 quantization perplexity degradation long context vLLM
