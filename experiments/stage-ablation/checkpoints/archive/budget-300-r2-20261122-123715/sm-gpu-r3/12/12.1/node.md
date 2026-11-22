# N376: Apple M2 Ultra 在 Qwen3-27B W4 量化、32K 上下文预填充阶段的首字延迟 (TTFT) 理论下限计算公式为 TTFT_M2 ≈ (2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

Apple M2 Ultra 在 Qwen3-27B W4 量化、32K 上下文预填充阶段的首字延迟 (TTFT) 理论下限计算公式为 TTFT_M2 ≈ (2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size_bytes) / Memory_Bandwidth_GBps，其中 Memory_Bandwidth_GBps 为 800 GB/s，需代入 N109 确认的 GQA 参数计算具体秒数。

## Corrected Claim

Apple M2 Ultra 在 Qwen3-27B W4 量化、32K 上下文预填充阶段的首字延迟 (TTFT) 理论下限计算公式为 TTFT_M2 ≈ (2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size_bytes) / Memory_Bandwidth_GBps，其中 Memory_Bandwidth_GBps 为 800 GB/s，需代入 N109 确认的 GQA 参数计算具体秒数。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合大模型推理中KV Cache读取带宽瓶颈的理论推导，M2 Ultra带宽800GB/s符合硬件规格，量纲与逻辑自洽。
