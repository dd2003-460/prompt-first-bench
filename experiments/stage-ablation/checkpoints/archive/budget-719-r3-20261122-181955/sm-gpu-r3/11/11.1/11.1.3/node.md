# N374: RTX 4090在32K上下文INT4推理下的实际KV Cache精度策略：主流框架（vLLM, TGI）默认KV Cache保持BF16，因INT8/INT4

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N126

## Claim

RTX 4090在32K上下文INT4推理下的实际KV Cache精度策略：主流框架（vLLM, TGI）默认KV Cache保持BF16，因INT8/INT4量化KV Cache会导致长上下文性能显著下降（MMLU下降>3%）。若强制启用INT8 KV Cache，单token占用降至128KB，8.5GB显存可支持 8.5GB / 128KB ≈ 68,000 tokens，支持2个32K并发请求，但需验证Qwen3-27B在INT8 KV Cache下的MMLU/HumanEval损失是否<2%。

## Corrected Claim

RTX 4090（24GB显存）在32K上下文INT4推理下，主流框架默认KV Cache保持BF16。若强制启用INT8 KV Cache，需根据Qwen3-27B的具体架构参数（层数、头数、头维度）重新计算单token占用，以评估实际可支持的并发请求数，并验证精度损失。

## Evidence

[质询]数值量级与物理直觉严重矛盾：RTX 4090 显存为 24GB，而非 8.5GB；且对于 Qwen3-27B 这类大模型，单 token 的 KV Cache 占用远大于 128KB（通常数百 KB 至 MB 级别，取决于层数和头数），128KB 的数值极不合理，导致推导出的 68,000 tokens 并发能力严重高估。 | 来源不可用。逻辑校验发现硬错误：RTX 4090 显存规格错误（应为 24GB），且单 token KV Cache 大小（128KB）对于 27B 模型而言量级过小，违背基本内存计算逻辑。

## Search Query

Qwen3-27B INT8 KV cache quantization accuracy loss vLLM
