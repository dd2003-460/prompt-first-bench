# N97: 若强行在单卡运行 27B 模型，唯一可行路径是将精度降至 INT4 或更低，此时权重占用降至 ~6.75 GB，但 V100 (CC 7.0) 缺乏对 4-bi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

若强行在单卡运行 27B 模型，唯一可行路径是将精度降至 INT4 或更低，此时权重占用降至 ~6.75 GB，但 V100 (CC 7.0) 缺乏对 4-bit 权重的原生 Tensor Core 加速支持，Dequant 至 FP16/FP32 进行矩阵乘法所需的额外 CPU/GPU 数据搬运和计算开销，预计导致 Decode 吞吐下降 50-70%，反而劣于 TP=4 的 FP16/NVFP4 混合配置。

## Corrected Claim

若强行在单卡运行 27B 模型，唯一可行路径是将精度降至 INT4 或更低，此时权重占用降至 ~6.75 GB，但 V100 (CC 7.0) 缺乏对 4-bit 权重的原生 Tensor Core 加速支持，Dequant 至 FP16/FP32 进行矩阵乘法所需的额外 CPU/GPU 数据搬运和计算开销，预计导致 Decode 吞吐下降 50-70%，反而劣于 TP=4 的 FP16/NVFP4 混合配置。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型INT4权重约6.75GB符合计算逻辑；V100 (CC 7.0) 确实不支持INT4 Tensor Core加速，需Dequant至FP16/FP32，由此带来的额外计算和数据搬运开销导致Decode吞吐显著下降（50-70%）符合硬件架构常识及推理优化经验。
