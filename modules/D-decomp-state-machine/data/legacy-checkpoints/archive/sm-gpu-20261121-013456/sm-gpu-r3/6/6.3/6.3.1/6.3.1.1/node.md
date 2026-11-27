# N259: 单卡 4090 吞吐量优化上限：通过启用 Flash Attention 2 和增大 Batch Size（至显存允许上限，约 4-8），Qwen3-27B I

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

单卡 4090 吞吐量优化上限：通过启用 Flash Attention 2 和增大 Batch Size（至显存允许上限，约 4-8），Qwen3-27B INT4 在 RTX 4090 上的吞吐量可从 12.5 tokens/s 提升至 15-18 tokens/s（来源：vLLM 基准测试，[时效待核]）；若优化后吞吐量仍 < 需求值，则必须切换至 2×4090。

## Corrected Claim

单卡 4090 吞吐量优化上限：通过启用 Flash Attention 2 和增大 Batch Size，Qwen3-27B INT4 在 RTX 4090 上的吞吐量预计可显著提升（具体数值需实测验证）；若优化后吞吐量仍 < 需求值，则必须切换至 2×4090。

## Evidence

[质询]具体吞吐量数值（12.5至15-18 tokens/s）及Batch Size范围（4-8）属于特定硬件与模型配置下的经验事实，缺乏通用理论推导基础，且参考来源未提供具体基准数据，存在数值不准确或过时风险。 | 逻辑自洽（优化后吞吐量提升符合直觉），但参考来源[1]仅讨论Flash Attention 3对4090的支持性，未提供Qwen3-27B INT4的具体吞吐量基准数据，属于经验事实且缺直接来源支持。

## Search Query

RTX 4090 Qwen3-27B vLLM Flash Attention 2 throughput optimization batch size

## Retrieval Sources

- {'url': 'https://github.com/Dao-AILab/flash-attention/issues/1121&rut=b54d0df619abafdc1896bf4a216f9f9f5458fb610a680f35fc23c0b6b0e76128', 'type': 'ddg', 'title': 'Flash Attention 3 fp8 support 4090? - GitHub'}
