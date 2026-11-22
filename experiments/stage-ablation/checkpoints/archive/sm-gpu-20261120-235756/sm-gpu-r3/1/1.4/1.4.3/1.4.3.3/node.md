# N162: FP8 推理对 TTFT (Time To First Token) 的影响：FP8 权重体积减半导致预填充阶段 (Prefill) 的内存读取量减少 50%，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

FP8 推理对 TTFT (Time To First Token) 的影响：FP8 权重体积减半导致预填充阶段 (Prefill) 的内存读取量减少 50%，理论上 TTFT 可缩短 30%-50%（取决于计算与内存带宽的平衡）；需实测 Qwen3-27B 在 32K 上下文下，FP8 相比 BF16 的 TTFT 具体降低百分比。

## Corrected Claim

FP8 推理对 TTFT (Time To First Token) 的影响：FP8 权重体积减半导致预填充阶段 (Prefill) 的内存读取量减少 50%，理论上 TTFT 可缩短 30%-50%（取决于计算与内存带宽的平衡）；需实测 Qwen3-27B 在 32K 上下文下，FP8 相比 BF16 的 TTFT 具体降低百分比。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重体积减半直接导致Prefill阶段内存读取量减少50%，在内存带宽受限场景下TTFT缩短30%-50%符合Roofline模型及硬件工程常识，量级合理且无内部矛盾。

## Search Query

FP8 quantization TTFT reduction prefill phase LLM inference 32K context
