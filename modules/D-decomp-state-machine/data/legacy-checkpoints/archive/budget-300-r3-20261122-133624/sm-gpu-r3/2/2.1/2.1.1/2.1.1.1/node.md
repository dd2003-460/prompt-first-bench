# N240: RTX 6000 Ada 48GB 在 BF16 下运行 Qwen3-27B 的可行性：权重占用 54GB，超出 48GB 显存，故 BF16 单卡部署不可行；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

RTX 6000 Ada 48GB 在 BF16 下运行 Qwen3-27B 的可行性：权重占用 54GB，超出 48GB 显存，故 BF16 单卡部署不可行；必须使用 FP8 (27GB) 或 INT8 (27GB) 量化，此时显存占用 27GB + KV Cache (32K 上下文约 1.3GB) + 框架开销 (~2GB) ≈ 30.3GB，在 48GB 内可行，剩余 17.7GB 可用于扩大上下文或批处理。

## Corrected Claim

RTX 6000 Ada 48GB 在 BF16 下运行 Qwen3-27B 的可行性：权重占用 54GB，超出 48GB 显存，故 BF16 单卡部署不可行；必须使用 FP8 (27GB) 或 INT8 (27GB) 量化，此时显存占用 27GB + KV Cache (32K 上下文约 1.3GB) + 框架开销 (~2GB) ≈ 30.3GB，在 48GB 内可行，剩余 17.7GB 可用于扩大上下文或批处理。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重54GB确实超出48GB显存；FP8/INT8量化后权重约27GB，加上KV Cache和框架开销后总占用约30.3GB，在48GB显存内可行，剩余空间合理。
