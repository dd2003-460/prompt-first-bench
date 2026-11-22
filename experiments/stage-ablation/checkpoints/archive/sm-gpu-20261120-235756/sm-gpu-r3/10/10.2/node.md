# N131: AMD MI300X 在 BF16 精度下运行 Qwen3-27B 的理论 TPOT 上限为 10.23ms/token (计算式: (27.18e9 para

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

AMD MI300X 在 BF16 精度下运行 Qwen3-27B 的理论 TPOT 上限为 10.23ms/token (计算式: (27.18e9 params * 2 bytes/param) / 5300 GB/s)，对应理论吞吐量约 97.8 tokens/s；考虑 MoE 架构的稀疏激活特性 (激活参数仅 3.3B)，实际 TPOT 可能降至 1.25ms/token (计算式: (3.3e9 * 2) / 5300)，但需确认推理框架是否有效利用 MoE 稀疏性以避免全参数加载。

## Corrected Claim

AMD MI300X 在 BF16 精度下运行 Qwen3-27B 的理论 TPOT 上限为 10.23ms/token (计算式: (27.18e9 params * 2 bytes/param) / 5300 GB/s)，对应理论吞吐量约 97.8 tokens/s；考虑 MoE 架构的稀疏激活特性 (激活参数仅 3.3B)，实际 TPOT 可能降至 1.25ms/token (计算式: (3.3e9 * 2) / 5300)，但需确认推理框架是否有效利用 MoE 稀疏性以避免全参数加载。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM3 带宽约 5.3TB/s，Qwen3-27B 总参数量约 27B，BF16 下 2 字节/参数，计算式 (27.18e9 * 2) / 5300 ≈ 10.23ms 符合算术逻辑；MoE 激活参数 3.3B 对应 1.25ms 亦符合稀疏激活理论上限推导。
