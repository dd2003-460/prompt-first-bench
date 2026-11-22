# N253: 在 BF16 量化且 Batch Size=1 的工作点下，显存需求为 权重 54.2 GB + KV Cache 3.14 GB (BF16 KV) + 开销

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

在 BF16 量化且 Batch Size=1 的工作点下，显存需求为 权重 54.2 GB + KV Cache 3.14 GB (BF16 KV) + 开销 2.03 GB = 59.37 GB，加 10% 余量为 65.31 GB。该值低于 80 GB 显存上限，验证了 A100/H100 80GB 单卡可运行 BF16 模型；但 48 GB 显存的 A6000 Ada 因 65.31 GB > 48 GB 而不可行，必须使用双卡（总显存 96 GB）或 80 GB+ 单卡，这直接排除了中预算区间使用 BF16 的单卡方案。

## Corrected Claim

在 BF16 量化且 Batch Size=1 的工作点下，显存需求为 权重 54.2 GB + KV Cache 3.14 GB (BF16 KV) + 开销 2.03 GB = 59.37 GB，加 10% 余量为 65.31 GB。该值低于 80 GB 显存上限，验证了 A100/H100 80GB 单卡可运行 BF16 模型；但 48 GB 显存的 A6000 Ada 因 65.31 GB > 48 GB 而不可行，必须使用双卡（总显存 96 GB）或 80 GB+ 单卡，这直接排除了中预算区间使用 BF16 的单卡方案。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（54.2+3.14+2.03=59.37，59.37*1.1=65.307≈65.31），显存对比逻辑自洽（65.31 < 80 且 65.31 > 48），符合硬件规格常识。

## Search Query

BF16 LLM 27B full precision memory requirement 80GB vs 48GB GPU
