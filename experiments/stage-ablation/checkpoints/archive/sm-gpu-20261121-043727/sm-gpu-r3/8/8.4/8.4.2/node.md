# N257: H100 SXM 的 MTBF 或数据中心级年故障率数据：查找 NVIDIA 数据中心 GPU 的可靠性指标（通常远高于消费级，MTBF > 100,000 小

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

H100 SXM 的 MTBF 或数据中心级年故障率数据：查找 NVIDIA 数据中心 GPU 的可靠性指标（通常远高于消费级，MTBF > 100,000 小时），并确认其 3-5 年 ProSupport 合同的具体年费标准（占硬件成本百分比或固定金额）

## Corrected Claim

H100 SXM 作为数据中心级 GPU，其可靠性指标（如 MTBF）通常远高于消费级产品（一般认为在 100,000 小时以上量级），但具体 MTBF 数值及 3-5 年 ProSupport 合同的具体年费标准需参考 NVIDIA 官方售后文档或具体合同条款，公开数据表未直接列出。

## Evidence

[质询]NVIDIA 官方数据表（Datasheet）通常仅包含性能规格（算力、带宽、功耗等），极少直接列出 MTBF（平均无故障时间）或具体的 ProSupport 年费标准，这些属于售后/运维指标，往往不在公开的技术规格表中直接呈现，存在来源覆盖不足的风险。 | 来源 [1] 为 H100 数据表，虽确认了产品存在及基本规格，但未直接提供 MTBF 数值或 ProSupport 具体年费，属于间接支持/未覆盖关键数值细节；MTBF > 100,000 小时符合数据中心级硬件的一般工程常识（逻辑自洽），但具体数值和费用缺乏直接来源支持。

## Search Query

NVIDIA H100 SXM MTBF reliability data ProSupport annual cost percentage

## Retrieval Sources

- {'url': 'https://resources.nvidia.com/en-us-gpu/h100-datasheet-24306&rut=e5faf3451996f50cc5d368f84b12e51d5e1cac1f19f2396e52ed3e73a1ed37ea', 'type': 'ddg', 'title': 'NVIDIA H100 GPU Datasheet'}
