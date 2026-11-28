# N716: 1Hz 采样频率对于捕获 V100 毫秒级的瞬态温度尖峰（Spikes）是不够的，可能导致错过短暂的过热事件，建议将采样频率提升至 10Hz 或使用 nvidi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N263

## Claim

1Hz 采样频率对于捕获 V100 毫秒级的瞬态温度尖峰（Spikes）是不够的，可能导致错过短暂的过热事件，建议将采样频率提升至 10Hz 或使用 nvidia-smi dmon 的实时流模式，以捕捉更细粒度的热瞬变行为

## Corrected Claim

1Hz 采样频率对于捕获 V100 毫秒级的瞬态温度尖峰（Spikes）是不够的，可能导致错过短暂的过热事件，建议将采样频率提升至 10Hz 或使用 nvidia-smi dmon 的实时流模式，以捕捉更细粒度的热瞬变行为

## Evidence

先验知识/题面给定，逻辑校验通过：1Hz采样周期为1秒，根据奈奎斯特采样定理及工程实践，无法可靠捕获毫秒级（<100ms）的瞬态信号，提升采样率至10Hz或使用实时流是合理的工程建议。

## Search Query

nvidia-smi sampling rate transient thermal spike detection GPU monitoring best practices
