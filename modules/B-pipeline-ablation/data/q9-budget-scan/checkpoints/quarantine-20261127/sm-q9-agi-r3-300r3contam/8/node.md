# N30: V100 (Compute Cap 7.0) 缺乏原生 FP8 支持导致的性能惩罚因子：虽然配置了 fp8 KV cache，但 V100 不支持 FP8 Te

- **status**: pending
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

父节点级核验未通过：不完备（子节点正交且无冗余，但不完备。父节点的核心是'FP8支持缺失导致的性能惩罚'及其具体机制（动态转换/搬运），而现有子节点仅描述了V100的硬件带宽基准和通用长上下文内存墙效应，完全遗漏了'FP8到FP16动态转换带来的额外计算开销'以及'CPU/GPU数据搬运导致的延迟增加'这两个导致30-40%性能损失的具体因果环节。）

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/b0e0f75da72d7375a417866fb84ae45c3a35c27d.html&rut=dcd5b4e93be6715c7836ae5e91419bfdaba89174244840c1660f55aa742faa9e', 'type': 'ddg', 'title': '特斯拉V100能解锁FP8吗？一文搞懂硬件限制与替代方案'}
