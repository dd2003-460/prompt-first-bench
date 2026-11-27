# N78: Apple M2 Ultra (192GB Unified Memory) 运行 Qwen3-27B BF16 的可行性分析：统一内存带宽 (~800GB/s)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Apple M2 Ultra (192GB Unified Memory) 运行 Qwen3-27B BF16 的可行性分析：统一内存带宽 (~800GB/s) 对 LLM 推理延迟的理论上限，与消费级 PCIe 4.0 x16 带宽 (~32GB/s) 的对比，确认其是否适合高吞吐场景

## Corrected Claim

Apple M2 Ultra (192GB Unified Memory) 运行 Qwen3-27B BF16 的可行性分析：统一内存带宽 (~800GB/s) 对 LLM 推理延迟的理论上限，与消费级 PCIe 4.0 x16 带宽 (~32GB/s) 的对比，确认其是否适合高吞吐场景

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 统一内存带宽约 800GB/s 与 PCIe 4.0 x16 约 32GB/s 的数值量级符合硬件规格常识，且 LLM 推理受内存带宽限制的理论分析逻辑自洽。
