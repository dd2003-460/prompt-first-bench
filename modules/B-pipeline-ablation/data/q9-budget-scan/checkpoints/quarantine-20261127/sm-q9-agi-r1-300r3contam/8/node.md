# N30: V100 (Compute Cap 7.0) 缺乏原生 FP8 支持导致的性能惩罚因子：虽然配置了 fp8 KV cache，但 V100 不支持 FP8 Te

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

V100 (Compute Cap 7.0) 缺乏原生 FP8 支持导致的性能惩罚因子：虽然配置了 fp8 KV cache，但 V100 不支持 FP8 Tensor Core 运算，KV Cache 需在加载时动态转换为 FP16 或在 CPU/GPU 间搬运，导致内存带宽利用率下降约 30-40%，这是长上下文 (262k) 场景下推理速度远低于 H100/A100 同配置的关键硬件瓶颈。

## Corrected Claim

V100 (Compute Cap 7.0) 缺乏原生 FP8 支持，导致配置 FP8 KV Cache 时需进行动态格式转换或额外数据搬运，增加了计算和内存访问开销，从而在长上下文场景下显著降低推理效率，使其性能远低于支持原生 FP8 的 H100/A100。

## Evidence

[质询]陈述中关于“内存带宽利用率下降约 30-40%”的具体数值缺乏直接来源支持，且将“缺乏原生 FP8 支持”直接量化为固定的带宽利用率损失比例属于过度推断，实际性能瓶颈更多源于数据转换开销和内存访问模式改变，而非单纯的带宽利用率线性下降。 | 来源 [1] 直接支持 V100 硬件不支持 FP8 Tensor Core 运算这一核心事实，但未提供具体的 30-40% 带宽利用率下降数据；该数值属于经验性估算，缺乏多源一致或第一性原理推导支持，故降级。

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/b0e0f75da72d7375a417866fb84ae45c3a35c27d.html&rut=dcd5b4e93be6715c7836ae5e91419bfdaba89174244840c1660f55aa742faa9e', 'type': 'ddg', 'title': '特斯拉V100能解锁FP8吗？一文搞懂硬件限制与替代方案'}
