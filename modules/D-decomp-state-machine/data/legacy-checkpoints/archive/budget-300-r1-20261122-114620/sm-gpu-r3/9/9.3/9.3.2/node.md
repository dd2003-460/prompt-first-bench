# N390: RTX 4090 (24GB) 在 W4 精度下运行 Qwen3-27B 时，权重占用 13.5GB，框架开销 5GB，剩余显存 5.5GB，单请求 32K K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

RTX 4090 (24GB) 在 W4 精度下运行 Qwen3-27B 时，权重占用 13.5GB，框架开销 5GB，剩余显存 5.5GB，单请求 32K KV Cache 需 1.6GB，理论最大并发数 N_max = floor(5.5 / 1.6) = 3。

## Corrected Claim

RTX 4090 (24GB) 在 W4 精度下运行 Qwen3-27B 时，权重占用 13.5GB，框架开销 5GB，剩余显存 5.5GB，单请求 32K KV Cache 需 1.6GB，理论最大并发数 N_max = floor(5.5 / 1.6) = 3。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在W4下约13.5GB，24GB总显存扣除权重与5GB框架开销后剩5.5GB，32K KV Cache约1.6GB，5.5/1.6=3.43，向下取整为3，计算自洽。
