# N119: RTX 4090 单卡在 Qwen3-27B BF16 32K 上下文下无法运行完整模型（显存需求 55GB > 24GB），其'单卡'吞吐量数值为 0 tok

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

RTX 4090 单卡在 Qwen3-27B BF16 32K 上下文下无法运行完整模型（显存需求 55GB > 24GB），其'单卡'吞吐量数值为 0 tokens/s；该配置仅在模型量化至 INT4（显存需求约 15GB）或启用 CPU Offload（导致延迟激增）时可行，需标注为 [不可行/需量化]。

## Corrected Claim

RTX 4090 单卡在 Qwen3-27B BF16 32K 上下文下无法运行完整模型（显存需求 55GB > 24GB），其'单卡'吞吐量数值为 0 tokens/s；该配置仅在模型量化至 INT4（显存需求约 15GB）或启用 CPU Offload（导致延迟激增）时可行，需标注为 [不可行/需量化]。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中提到的三种不同状态（BF16不可行、INT4量化可行、CPU Offload可行），彼此之间在技术实现路径和结果上互斥且无重叠。它们共同完整覆盖了父节点关于‘无法运行完整模型’及‘仅在量化或Offload时可行’的所有关键方面。虽然INT4和CPU Offload都是‘可行’方案，但它们代表了不同的权衡维度（质量vs延迟/成本），不属于同一参数的简单取值，因此不构成冗余。）
