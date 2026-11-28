# N242: PyTorch运行时碎片预留量化：使用torch.cuda.memory_stats()监测，在vLLM初始化后，reserved-but-unallocate

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

PyTorch运行时碎片预留量化：使用torch.cuda.memory_stats()监测，在vLLM初始化后，reserved-but-unallocated显存通常占总reserved显存的5-10%。若reserved为14GB，碎片预留约0.7-1.4GB/卡。此部分可通过torch.cuda.empty_cache()回收，但在持续推理中会因分配模式再次积累，构成动态波动上限。

## Corrected Claim

PyTorch运行时碎片预留量化：使用torch.cuda.memory_stats()监测，在vLLM初始化后，reserved-but-unallocated显存通常占一定比例（具体比例依负载和版本而异）。若reserved为14GB，碎片预留约为相应比例的数值/卡。此部分可通过torch.cuda.empty_cache()回收，但在持续推理中会因分配模式再次积累，构成动态波动上限。

## Evidence

[质询]该陈述包含具体的经验性数值范围（5-10%），这属于特定软件版本和硬件环境下的观测数据，无法从第一性原理推导，且缺乏来源支持其普遍适用性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PyTorch cuda memory fragmentation reserved unallocated ratio inference server
