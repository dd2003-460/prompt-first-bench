# N72: B3区间(50k+ CNY)内的硬件组合可行性：包含 1×H100 (80GB) 或 1×A100 (80GB) 支持 BF16 及高并发 KV Cache，以

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

B3区间(50k+ CNY)内的硬件组合可行性：包含 1×H100 (80GB) 或 1×A100 (80GB) 支持 BF16 及高并发 KV Cache，以及多卡集群方案；需评估高预算下是否因边际效用递减而不再增加卡数。

## Corrected Claim

B3区间(50k+ CNY)内的硬件组合可行性：包含 1×H100 (80GB) 或 1×A100 (80GB) 支持 BF16 及高并发 KV Cache，以及多卡集群方案；需评估高预算下是否因边际效用递减而不再增加卡数。

## Evidence

先验知识/题面给定，逻辑校验通过：H100/A100 80GB 显存支持 BF16 及 KV Cache 符合硬件规格，50k+ CNY 预算覆盖单卡成本，边际效用递减符合经济学直觉。
