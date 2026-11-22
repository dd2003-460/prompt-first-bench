# N421: AMD Radeon Pro W7900软件生态风险量化：ROCm 6.1对RDNA 3 Pro系列的支持成熟度低于NVIDIA CUDA；vLLM在W7900

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N166, N167, N168

## Claim

AMD Radeon Pro W7900软件生态风险量化：ROCm 6.1对RDNA 3 Pro系列的支持成熟度低于NVIDIA CUDA；vLLM在W7900上的实测吞吐通常为理论峰值的60-70% (受Kernel优化限制)，即实际吞吐约 16.5 * 0.65 ≈ 10.7 tokens/s；此外，W7900缺乏NVLink等效互联，多卡扩展性极差，仅限单卡部署。

## Corrected Claim

AMD Radeon Pro W7900软件生态风险量化：ROCm 6.1对RDNA 3 Pro系列的支持成熟度低于NVIDIA CUDA；vLLM在W7900上的实测吞吐受Kernel优化限制，通常显著低于理论峰值（具体数值依模型和负载而定）；此外，W7900缺乏NVLink等效互联，多卡扩展性极差，仅限单卡部署。

## Evidence

[质询]数值量级与具体参数缺乏来源支持：'16.5 tokens/s' 这一具体数值未指明模型规模、序列长度及硬件配置，属于高度依赖具体场景的经验数据，无法从第一性原理推导；'60-70%' 的吞吐效率也是经验估计值，不同模型和负载下波动极大。 | 先验知识/题面给定，逻辑校验通过（ROCm成熟度低于CUDA、W7900无NVLink等效互联为公认事实），但具体吞吐数值（16.5 tokens/s）及效率比例（60-70%）为经验事实，缺来源直接支持，故降级。

## Search Query

vLLM AMD W7900 performance benchmark tokens/s
