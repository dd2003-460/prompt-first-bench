# N169: RTX 4090 在满载运行 1 小时后，若机箱风道设计不佳（如进风口被遮挡或排风受阻），GPU 核心温度通常升至 85-90°C 以上，触发 NVIDIA 的

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

RTX 4090 在满载运行 1 小时后，若机箱风道设计不佳（如进风口被遮挡或排风受阻），GPU 核心温度通常升至 85-90°C 以上，触发 NVIDIA 的功率限制（Power Limit）或频率限制（Frequency Limit），导致实际运行频率从峰值 2520 MHz 下降 5-10%（至约 2270-2390 MHz），进而使推理吞吐量波动 5-10%。

## Corrected Claim

RTX 4090 在满载运行 1 小时后，若机箱风道设计不佳（如进风口被遮挡或排风受阻），GPU 核心温度通常升至 85-90°C 以上，触发 NVIDIA 的功率限制（Power Limit）或频率限制（Frequency Limit），导致实际运行频率从峰值 2520 MHz 下降 5-10%（至约 2270-2390 MHz），进而使推理吞吐量波动 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过
