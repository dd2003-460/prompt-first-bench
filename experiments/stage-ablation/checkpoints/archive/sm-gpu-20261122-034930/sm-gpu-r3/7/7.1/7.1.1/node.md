# N390: AMD MI300X单卡Qwen3-27B INT8理论吞吐上限：显存带宽5.3 TB/s，单次token生成读取数据量37.7GB（权重27GB+KV Cac

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139

## Claim

AMD MI300X单卡Qwen3-27B INT8理论吞吐上限：显存带宽5.3 TB/s，单次token生成读取数据量37.7GB（权重27GB+KV Cache 10.7GB）。理论峰值=5300 GB/s / 37.7 GB ≈ 140.6 tokens/s。对比RTX 4090的26.7 tokens/s，理论加速比为5.27倍。考虑ROCm软件栈效率损失（假设80%效率），实际预期吞吐约为112.5 tokens/s。

## Corrected Claim

AMD MI300X单卡Qwen3-27B INT8理论吞吐上限：显存带宽5.3 TB/s，单次token生成读取数据量37.7GB（权重27GB+KV Cache 10.7GB）。理论峰值=5300 GB/s / 37.7 GB ≈ 140.6 tokens/s。对比RTX 4090的26.7 tokens/s，理论加速比为5.27倍。考虑ROCm软件栈效率损失（假设80%效率），实际预期吞吐约为112.5 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X显存带宽5.3TB/s及Qwen3-27B INT8权重约27GB符合硬件与模型规格常识，算术推导（5300/37.7≈140.6）正确，逻辑自洽。
