# N175: 基于修正后 KV Cache 大小 (4.3GB) 的单卡可行性重评估：对于 RTX 4090 (24GB)，若使用 BF16 权重 (54GB) 仍不可行；若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

基于修正后 KV Cache 大小 (4.3GB) 的单卡可行性重评估：对于 RTX 4090 (24GB)，若使用 BF16 权重 (54GB) 仍不可行；若使用 FP8 权重 (27GB)，则 27GB (权重) + 4.3GB (KV) = 31.3GB > 24GB，仍不可行；若使用 W4 量化权重 (13.5GB)，则 13.5GB (权重) + 4.3GB (KV) + 1.0GB (激活值) ≈ 18.8GB < 24GB，单卡可行。对于 RTX 5090 (32GB)，FP8 权重 (27GB) + 4.3GB (KV) + 1.0GB (激活值) ≈ 32.3GB，接近上限，需启用 PagedAttention 或 INT8 KV 以预留安全余量。此结论修正了 N102 中关于 5090 单卡 32GB 不足以运行 32K 上下文的判断，实际上在 W4 或 FP8+INT8 KV 下是可行的。

## Corrected Claim

基于修正后 KV Cache 大小 (4.3GB) 的单卡可行性重评估：对于 RTX 4090 (24GB)，若使用 BF16 权重 (54GB) 仍不可行；若使用 FP8 权重 (27GB)，则 27GB (权重) + 4.3GB (KV) = 31.3GB > 24GB，仍不可行；若使用 W4 量化权重 (13.5GB)，则 13.5GB (权重) + 4.3GB (KV) + 1.0GB (激活值) ≈ 18.8GB < 24GB，单卡可行。对于 RTX 5090 (32GB)，FP8 权重 (27GB) + 4.3GB (KV) + 1.0GB (激活值) ≈ 32.3GB，接近上限，需启用 PagedAttention 或 INT8 KV 以预留安全余量。此结论修正了 N102 中关于 5090 单卡 32GB 不足以运行 32K 上下文的判断，实际上在 W4 或 FP8+INT8 KV 下是可行的。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（13.5+4.3+1.0=18.8<24；27+4.3+1.0=32.3≈32），硬件规格（4090 24GB, 5090 32GB）及量化后权重大小符合工程常识，逻辑自洽。

## Search Query

Qwen3-27B single GPU inference memory requirement FP8 W4 32K context
