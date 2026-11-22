# N425: 高并发场景下的吞吐量扩展性差异：RTX 4090 在 batch=8 时，Decode 吞吐量线性度较差（受限于 PCIe 带宽和内存控制器），实际吞吐仅提升 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N167

## Claim

高并发场景下的吞吐量扩展性差异：RTX 4090 在 batch=8 时，Decode 吞吐量线性度较差（受限于 PCIe 带宽和内存控制器），实际吞吐仅提升 3-4 倍；H100 在 batch=8 时，得益于 HBM 高带宽和 NVLink（若多卡），Decode 吞吐量可提升 5-6 倍。因此，在 batch=8 场景下，H100 的单位 token 成本优势缩小至 1.5-2 倍，但仍高于 RTX 4090。

## Corrected Claim

高并发场景下，H100凭借HBM高带宽和NVLink互联，在Decode阶段的吞吐量扩展性通常优于受限于PCIe带宽的RTX 4090，其单位token成本优势在高batch size下相对缩小但仍保持领先。

## Evidence

[质询]具体数值（3-4倍、5-6倍、1.5-2倍）缺乏通用基准测试支持，且高度依赖具体模型大小、序列长度及硬件配置（如是否多卡NVLink），将特定实验结果泛化为通用结论存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过：H100的HBM带宽和NVLink确实优于RTX 4090的GDDR6X和PCIe，高并发下显存带宽瓶颈会放大H100优势，但具体倍数属于经验事实，无来源直接支持，故降级。

## Search Query

H100 vs RTX 4090 batch inference throughput scaling efficiency
