# N691: 云存储SLA承诺与实际冗余架构的映射关系：若阿里云OSS承诺99.99%可用性，其底层是否必然需要3副本？还是可通过EC+快速重建达到相同SLA？计算不同架构下

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N286

## Claim

云存储SLA承诺与实际冗余架构的映射关系：若阿里云OSS承诺99.99%可用性，其底层是否必然需要3副本？还是可通过EC+快速重建达到相同SLA？计算不同架构下的年度不可用时间（SLO violation probability）及对应电力成本，确定最小必要冗余系数

## Corrected Claim

云存储SLA承诺与冗余架构存在映射关系：达到99.99%可用性不一定必须采用3副本架构，也可通过纠删码（EC）结合快速重建机制实现。具体架构选择取决于存储成本、电力成本及重建时间的权衡，需根据具体厂商的技术文档和实际运行数据进行量化评估以确定最小必要冗余系数。

## Evidence

[质询]该陈述包含具体的商业SLA数值（99.99%）和特定的技术实现假设（阿里云OSS是否必然使用3副本），属于经验事实。由于缺乏外部来源支持，无法验证阿里云OSS的具体底层架构细节及其对应的精确电力成本数据，且‘必然需要’这一绝对化表述在工程实践中可能存在例外（如混合架构）。 | 经验事实，逻辑自洽但缺来源支持。虽然从可靠性理论（First Principles）可以推导出EC（纠删码）在同等可用性下通常比多副本更节省存储和电力，但具体到阿里云OSS的实现细节、确切的SLA数值以及具体的电力成本计算，属于特定厂商的工程实践数据，无法仅凭逻辑推导得出确切结论，且本轮检索无可用来源。

## Search Query

cloud storage SLA 99.99% minimum redundancy requirement erasure coding vs replication cost
