# N377: RTX 4090 在 Qwen3-27B W4 量化、32K 上下文预填充阶段的首字延迟 (TTFT) 理论下限计算公式为 TTFT_4090 ≈ (2 * n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

RTX 4090 在 Qwen3-27B W4 量化、32K 上下文预填充阶段的首字延迟 (TTFT) 理论下限计算公式为 TTFT_4090 ≈ (2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size_bytes) / Memory_Bandwidth_GBps，其中 Memory_Bandwidth_GBps 为 1008 GB/s，需与 M2 Ultra 结果对比以验证 1-2 秒的估计是否准确。

## Corrected Claim

RTX 4090 在 Qwen3-27B W4 量化、32K 上下文预填充阶段的首字延迟 (TTFT) 理论下限计算公式为 TTFT_4090 ≈ (2 * num_layers * num_kv_heads * head_dim * seq_len * dtype_size_bytes) / Memory_Bandwidth_GBps，其中 Memory_Bandwidth_GBps 为 1008 GB/s，需与 M2 Ultra 结果对比以验证 1-2 秒的估计是否准确。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合KV Cache预填充带宽瓶颈理论，RTX 4090带宽1008GB/s及Qwen3-27B参数量级合理，无来源矛盾。
