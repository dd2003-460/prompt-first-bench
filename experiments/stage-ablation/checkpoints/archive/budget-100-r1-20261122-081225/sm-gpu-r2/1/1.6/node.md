# N11: NVIDIA H100 80GB (SXM/PCIe) 的显存带宽为 3350 GB/s (HBM3)，单卡市场均价约为 $25000-$30000 [时效待核

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

NVIDIA H100 80GB (SXM/PCIe) 的显存带宽为 3350 GB/s (HBM3)，单卡市场均价约为 $25000-$30000 [时效待核]。

## Corrected Claim

NVIDIA H100 80GB (SXM/PCIe) 的显存带宽为 3350 GB/s (HBM3)；单卡市场均价随市场波动，需实时查询，历史参考区间约为 $25000-$30000。

## Evidence

[质询]市场均价属于动态变化的经验事实，且受供需、渠道、时间影响极大，提供的参考来源均为技术规格文档，完全未包含任何价格信息，无法通过现有来源验证该数值区间。 | 显存带宽3350 GB/s与来源[2][3]的技术规格一致（逻辑自洽），但价格部分为经验事实，来源未覆盖且无法从第一性原理推出，故降级。

## Search Query

NVIDIA H100 80GB HBM3 bandwidth 3350 GB/s price

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/data-center/h100/&rut=b695255f846adc7174798289444e4bed46da6c78cf486b29ebacd705d4adf6e9', 'type': 'ddg', 'title': 'Nvidia H100 Gpu'}
- {'url': 'https://resources.nvidia.com/en-us-gpu-resources/h100-datasheet-24306&rut=0706b5150305d57aec8ecefdc5f7d57d922ae382f061c95b5a46a37a96d7a2d7', 'type': 'ddg', 'title': 'NVIDIA H100 GPU Datasheet'}
- {'url': 'https://www.techpowerup.com/gpu-specs/h100-sxm5-80-gb.c3900&rut=7f09b993aaca417c6d41aa8399b54260e9db367c890d472157a2dd44b4964b15', 'type': 'ddg', 'title': 'NVIDIA H100 SXM5 80 GB Specs | TechPowerUp GPU Database'}
