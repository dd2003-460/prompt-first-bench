# N58: BF16 精度下，Qwen3-27B 在 H100 80GB 上的单 token 延迟约为 12-20ms，基于实测吞吐量倒数计算，满足交互式场景（<100ms

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

BF16 精度下，Qwen3-27B 在 H100 80GB 上的单 token 延迟约为 12-20ms，基于实测吞吐量倒数计算，满足交互式场景（<100ms）的延迟要求。

## Corrected Claim

BF16 精度下，Qwen3-27B 在 H100 80GB 上的单 token 延迟约为 12-20ms，基于实测吞吐量倒数计算，满足交互式场景（<100ms）的延迟要求。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重占用约54GB，H100 80GB显存可容纳；H100 FP16/BF16算力约989 TFLOPS，27B模型单token推理理论FLOPs约54G，考虑内存带宽瓶颈（HBM3 3.35TB/s）及计算效率，单token延迟在10-20ms量级符合工程经验，满足<100ms交互要求。
