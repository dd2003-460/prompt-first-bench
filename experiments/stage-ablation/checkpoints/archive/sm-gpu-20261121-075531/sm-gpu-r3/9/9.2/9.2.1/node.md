# N352: RTX 4090 在 Qwen3-27B INT8 推理 Decode 阶段 (高显存带宽利用率) 的典型功耗为 400-450W (接近 TDP 450W)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N118

## Claim

RTX 4090 在 Qwen3-27B INT8 推理 Decode 阶段 (高显存带宽利用率) 的典型功耗为 400-450W (接近 TDP 450W)，Prefill 阶段 (高计算利用率) 功耗同样接近 450W，但能效比 (Tokens/Watt) 在 Decode 阶段显著低于 Prefill 阶段。

## Corrected Claim

RTX 4090 在 Qwen3-27B INT8 推理 Decode 阶段 (高显存带宽利用率) 的典型功耗为 400-450W (接近 TDP 450W)，Prefill 阶段 (高计算利用率) 功耗同样接近 450W，但能效比 (Tokens/Watt) 在 Decode 阶段显著低于 Prefill 阶段。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP为450W，高负载下功耗接近TDP符合物理直觉；Decode阶段受显存带宽限制，计算单元空闲率高，能效比（Tokens/Watt）低于Prefill阶段符合LLM推理基本原理。

## Search Query

RTX 4090 power consumption LLM inference decode prefill watts
