# N505: Qwen3-27B 在 RX 7900 XTX ROCm 下的 BF16 推理兼容性验证：需确认 vLLM 或 SGLang 在 ROCm 6.0+ 环境下是否

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N175

## Claim

Qwen3-27B 在 RX 7900 XTX ROCm 下的 BF16 推理兼容性验证：需确认 vLLM 或 SGLang 在 ROCm 6.0+ 环境下是否支持 Qwen3 架构的 BF16 权重加载及 KV Cache 管理；若框架仅支持 FP16，则需进行 FP16 转换，可能引入轻微精度差异 (MMLU 损失 <0.1%)，但性能一致。

## Corrected Claim

Qwen3-27B 在 RX 7900 XTX ROCm 下的 BF16 推理兼容性需验证 vLLM 或 SGLang 在 ROCm 6.0+ 环境下对 Qwen3 架构的支持；若仅支持 FP16，转换可能引入轻微精度差异，具体损失幅度需实测确认。

## Evidence

[质询]该陈述包含具体的经验性参数（如'MMLU 损失 <0.1%'）和特定软件版本的兼容性断言（ROCm 6.0+ 对 Qwen3 架构的支持情况），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

vLLM ROCm Qwen3 BF16 support RDNA3
