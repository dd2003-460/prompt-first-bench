# N180: Mac Studio M2 Ultra (192GB) 运行 Qwen3-27B (BF16) 的吞吐量约为 10-15 tokens/s，受限于 800 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

Mac Studio M2 Ultra (192GB) 运行 Qwen3-27B (BF16) 的吞吐量约为 10-15 tokens/s，受限于 800 GB/s 统一内存带宽，虽满足 32K 上下文容量，但交互延迟 >60s/1000 tokens，不适合实时推理

## Corrected Claim

Mac Studio M2 Ultra (192GB) 运行 Qwen3-27B (BF16) 的吞吐量约为 10-15 tokens/s，受限于 800 GB/s 统一内存带宽，虽满足 32K 上下文容量，但交互延迟 >60s/1000 tokens，不适合实时推理

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽 800GB/s，Qwen3-27B BF16 模型大小约 54GB，理论解码上限约 14.8 tokens/s，实际受开销影响降至 10-15 tokens/s 合理；1000 tokens 耗时约 66-100s，符合 >60s 描述。

## Search Query

Mac Studio M2 Ultra 192GB Qwen 27B inference speed tokens per second
