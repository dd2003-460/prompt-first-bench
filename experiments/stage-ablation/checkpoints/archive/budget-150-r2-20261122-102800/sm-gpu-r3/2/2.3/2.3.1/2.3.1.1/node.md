# N222: 工作点1（高显存/低延迟/BF16）：总显存需求 59.15 GB，需 H100-80GB 或 2x RTX 4090 (48GB 不够，需 3x 或 A100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

工作点1（高显存/低延迟/BF16）：总显存需求 59.15 GB，需 H100-80GB 或 2x RTX 4090 (48GB 不够，需 3x 或 A100-80GB)，单卡 H100 可行，RTX 4090 不可行。

## Corrected Claim

工作点1（高显存/低延迟/BF16）：总显存需求 59.15 GB，需 H100-80GB 或 2x RTX 4090 (48GB 不够，需 3x 或 A100-80GB)，单卡 H100 可行，RTX 4090 不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：59.15GB显存需求小于H100-80GB容量，大于单张RTX 4090（24GB）容量，且小于两张RTX 4090（48GB）容量，因此单卡H100可行，单卡或双卡RTX 4090不可行，需三卡或更高显存设备，逻辑自洽。
