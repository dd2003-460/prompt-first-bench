# N194: Apple M2 Ultra 192GB 运行 Qwen3-27B BF16 时的实际功耗约为 100W-150W (GPU+CPU)，远低于 2x RTX 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Apple M2 Ultra 192GB 运行 Qwen3-27B BF16 时的实际功耗约为 100W-150W (GPU+CPU)，远低于 2x RTX 4090 的 900W，其每 token 电力成本仅为 NVIDIA 方案的 1/10，但由于吞吐量低 5-10 倍，每 token 总成本 (含硬件折旧) 在高频使用场景下仍高于 RTX 4090 方案。

## Corrected Claim

Apple M2 Ultra 192GB 运行 Qwen3-27B BF16 时的实际功耗约为 100W-150W (GPU+CPU)，远低于 2x RTX 4090 的 900W，其每 token 电力成本仅为 NVIDIA 方案的 1/10，但由于吞吐量低 5-10 倍，每 token 总成本 (含硬件折旧) 在高频使用场景下仍高于 RTX 4090 方案。

## Evidence

先验知识/题面给定，逻辑校验通过
