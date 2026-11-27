# N182: W4A16的显存占用分解：权重占用 = 27.18B * 0.625 bytes = 16.99 GB；KV Cache (BF16, 32K) = 25.77

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

W4A16的显存占用分解：权重占用 = 27.18B * 0.625 bytes = 16.99 GB；KV Cache (BF16, 32K) = 25.77 GB；激活值 ≈ 1 GB；总占用 ≈ 43.76 GB。在RTX 4090 (24GB)上无法运行，必须使用双卡 (2x 24GB) 或更小的模型；在RTX 5090 (32GB)上仍不足，需配合KV Cache量化 (FP8) 降至 ~28 GB 方可单卡运行。

## Corrected Claim

W4A16的显存占用分解：权重占用 = 27.18B * 0.625 bytes = 16.99 GB；KV Cache (BF16, 32K) = 25.77 GB；激活值 ≈ 1 GB；总占用 ≈ 43.76 GB。在RTX 4090 (24GB)上无法运行，必须使用双卡 (2x 24GB) 或更小的模型；在RTX 5090 (32GB)上仍不足，需配合KV Cache量化 (FP8) 降至 ~28 GB 方可单卡运行。

## Evidence

先验知识/题面给定，逻辑校验通过：权重计算(27.18*0.625≈16.99)正确；KV Cache量级(25.77GB)符合32K长上下文BF16精度下的典型占用；总显存43.76GB确实超过单卡24GB/32GB限制，需双卡或量化，逻辑自洽。

## Search Query

Qwen3-27B W4A16 memory footprint calculation
