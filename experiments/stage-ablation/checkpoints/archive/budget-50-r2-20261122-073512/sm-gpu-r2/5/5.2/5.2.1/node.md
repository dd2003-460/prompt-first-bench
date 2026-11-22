# N166: 厂商官方基准（如 NVIDIA TensorRT-LLM 文档）通常不包含系统开销（如 CUDA Context 初始化、PCIe 传输延迟），其报告吞吐量比实

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

厂商官方基准（如 NVIDIA TensorRT-LLM 文档）通常不包含系统开销（如 CUDA Context 初始化、PCIe 传输延迟），其报告吞吐量比实际部署高 15-25%，修正系数为 0.75-0.85。

## Corrected Claim

厂商官方基准（如 NVIDIA TensorRT-LLM 文档）通常不包含系统开销（如 CUDA Context 初始化、PCIe 传输延迟），其报告吞吐量通常高于实际部署，具体差异取决于硬件与负载场景，一般需引入 0.75-0.85 左右的经验修正系数进行估算。

## Evidence

[质询]15-25% 的开销比例及 0.75-0.85 的修正系数属于高度依赖具体硬件配置、模型规模及部署场景的经验性数值，并非普适常数；不同场景下（如大模型 vs 小模型、高并发 vs 低并发）该比例波动极大，将其表述为固定区间缺乏严谨性。 | 先验知识/题面给定，逻辑校验通过（官方基准通常忽略初始化等一次性开销，导致稳态吞吐量高于实际部署，方向正确；但具体数值区间为经验估计，非绝对真理）。
