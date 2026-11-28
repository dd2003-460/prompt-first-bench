# N8: V100-SXM2-16GB 不支持 FP8 硬件加速 (Compute Cap 7.0 < 8.9)，vLLM 中的 'fp8 KV cache' 实为软件模

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

V100-SXM2-16GB 不支持 FP8 硬件加速 (Compute Cap 7.0 < 8.9)，vLLM 中的 'fp8 KV cache' 实为软件模拟或降级为 FP16/INT8，导致 KV 读写带宽需求翻倍，有效吞吐降低至理论值的 50-60%

## Corrected Claim

V100-SXM2-16GB 不支持 FP8 硬件加速 (Compute Cap 7.0 < 8.9)，vLLM 中的 'fp8 KV cache' 实为软件模拟或降级处理，这会增加计算与内存访问开销，导致有效吞吐相较于原生支持的硬件显著降低，但具体降幅取决于工作负载特征。

## Evidence

[质询]陈述中关于“有效吞吐降低至理论值的 50-60%”的具体数值缺乏通用性，实际性能损失高度依赖于模型架构、序列长度及具体软件实现（如量化算法效率），并非固定常数；此外，将“KV读写带宽需求翻倍”直接等同于“吞吐降低50-60%”忽略了计算密集度与其他开销的影响，属于过度简化的因果推断。 | 来源[1]直接支持V100硬件不支持FP8及需软件模拟的核心事实，但未提供具体的吞吐损失百分比数据，该数值属于经验事实且缺乏多源一致支持。

## Search Query

v100 compute capability 7.0 fp8 support vllm performance degradation

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/b0e0f75da72d7375a417866fb84ae45c3a35c27d.html&rut=dcd5b4e93be6715c7836ae5e91419bfdaba89174244840c1660f55aa742faa9e', 'type': 'ddg', 'title': '特斯拉V100能解锁FP8吗？一文搞懂硬件限制与替代方案'}
