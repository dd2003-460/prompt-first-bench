# N195: 多卡 BF16 可行性分析：若使用 2x RTX 4090 (48GB 总显存)，仍 < 72.51 GB，即使 TP=2 也无法在 BF16 下运行 32K 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

多卡 BF16 可行性分析：若使用 2x RTX 4090 (48GB 总显存)，仍 < 72.51 GB，即使 TP=2 也无法在 BF16 下运行 32K 上下文，除非使用 Offloading 或降低上下文长度。

## Corrected Claim

多卡 BF16 可行性分析：若使用 2x RTX 4090 (48GB 总显存)，仍 < 72.51 GB，即使 TP=2 也无法在 BF16 下运行 32K 上下文，除非使用 Offloading 或降低上下文长度。

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 4090 显存为 48GB，小于 72.51GB 的需求，且 TP=2 无法突破单卡/总显存物理限制，结论符合硬件规格与推理显存占用逻辑。
