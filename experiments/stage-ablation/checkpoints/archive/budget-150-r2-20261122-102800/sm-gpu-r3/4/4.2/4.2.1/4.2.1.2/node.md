# N271: A100 在 INT8 精度下的有效峰值为 624 TOPS (非 1248，1248 为 FP16 下的 INT8 等效或特定配置错误)，在 LLM 推理中 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99

## Claim

A100 在 INT8 精度下的有效峰值为 624 TOPS (非 1248，1248 为 FP16 下的 INT8 等效或特定配置错误)，在 LLM 推理中 INT8 量化通常带来 1.5x-2.0x 的吞吐量提升，但精度损失需通过校准集验证。

## Corrected Claim

A100 在 INT8 精度下的稀疏峰值为 624 TOPS（稠密为 312 TOPS），1248 TOPS 通常指其 FP16/BF16 稀疏峰值。在 LLM 推理中，INT8 量化通常带来 1.5x-2.0x 的吞吐量提升（具体取决于实现和硬件利用率），精度损失需通过校准集验证。

## Evidence

[质询]A100 的 INT8 峰值算力通常标称为 624 TOPS（稀疏）或 312 TOPS（稠密），而 1248 TOPS 通常是 A100 在 FP16/BF16 下的稀疏峰值（或 INT8 稀疏峰值的误读/混淆）。陈述中称 1248 为 'FP16 下的 INT8 等效' 这一解释在技术术语上不准确，且 1.5x-2.0x 的吞吐量提升是经验值，受具体模型架构、Batch Size 和硬件利用率影响极大，并非固定物理常数。 | 先验知识/题面给定，逻辑校验通过。A100 的 INT8 峰值确为 624 TOPS (Sparse) / 312 TOPS (Dense)，1248 TOPS 通常指 FP16 Sparse 峰值，陈述对 1248 的归因解释存在术语混淆，但核心数值 624 正确。量化加速倍数 1.5-2.0x 为合理经验范围。因 source 为 knowledge，逻辑自洽即判 verified，但鉴于对 1248 的解释存在轻微技术瑕疵，且无外部来源佐证具体倍数，保守判定为 degraded 以提示术语精确性问题。

## Search Query

A100 INT8 TOPS specification LLM inference
