# N275: RTX 4090 (24GB) 在 INT8 精度下运行 Qwen3-27B 的 Batch Size 上限计算：权重 27GB > 24GB，单卡仍不可行。若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

RTX 4090 (24GB) 在 INT8 精度下运行 Qwen3-27B 的 Batch Size 上限计算：权重 27GB > 24GB，单卡仍不可行。若使用 W4 精度 (13.5GB)，可用显存 = 24GB - 13.5GB - 2.4GB(overhead) = 8.1GB。Batch Size 上限 = floor(8.1GB / 8.0GB) = 1。即在 W4 精度下，RTX 4090 单卡仅能支持 Batch Size=1 的 32K 上下文推理，无法支持 Batch Size > 1。

## Corrected Claim

RTX 4090 (24GB) 在 INT8 精度下运行 Qwen3-27B 的 Batch Size 上限计算：权重 27GB > 24GB，单卡仍不可行。若使用 W4 精度 (13.5GB)，可用显存 = 24GB - 13.5GB - 2.4GB(overhead) = 8.1GB。Batch Size 上限 = floor(8.1GB / 8.0GB) = 1。即在 W4 精度下，RTX 4090 单卡仅能支持 Batch Size=1 的 32K 上下文推理，无法支持 Batch Size > 1。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型W4量化后权重约13.5GB，扣除2.4GB开销后剩余8.1GB，单条32K上下文KV Cache占用约8.0GB，计算得出Batch Size上限为1，符合显存约束逻辑。
