# N431: H100 SXM 四卡配置的实际拓扑修正：NVIDIA HGX 标准配置为 8-GPU 节点，不存在标准的'4-GPU SXM'独立节点产品；若需 4 卡，通常

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N179

## Claim

H100 SXM 四卡配置的实际拓扑修正：NVIDIA HGX 标准配置为 8-GPU 节点，不存在标准的'4-GPU SXM'独立节点产品；若需 4 卡，通常需购买 8-GPU 节点并禁用/移除 4 张卡，或采用 PCIe 版 H100 4 卡配置。若按 8-GPU 节点满载计算，P_total = 8*700W + 2*250W (CPU) + 400W (Platform) = 6400W，1.3 倍冗余后需 8320W 电源，标准配置为 6x 2000W 或 4x 2600W 冗余电源，原 4420W 估算仅适用于非标准的 4 卡 PCIe 改装方案，不适用于 SXM 架构。

## Corrected Claim

H100 SXM 四卡配置的实际拓扑修正：NVIDIA HGX 标准配置为 8-GPU 节点，不存在标准的'4-GPU SXM'独立节点产品；若需 4 卡，通常需购买 8-GPU 节点并禁用/移除 4 张卡，或采用 PCIe 版 H100 4 卡配置。若按 8-GPU 节点满载计算，P_total = 8*700W + 2*250W (CPU) + 400W (Platform) = 6400W，1.3 倍冗余后需 8320W 电源，标准配置为 6x 2000W 或 4x 2600W 冗余电源，原 4420W 估算仅适用于非标准的 4 卡 PCIe 改装方案，不适用于 SXM 架构。

## Evidence

先验知识/题面给定，逻辑校验通过：HGX H100 标准确为 8 卡 SXM 架构，无标准 4 卡 SXM 节点；功率计算 8*700+2*250+400=6400W 符合 HGX 典型功耗模型，冗余系数 1.3 及电源配置（6x2000W 或 4x2600W）符合工业标准冗余设计逻辑。

## Search Query

HGX H100 8-GPU node total power consumption PSU configuration 2000W 2600W
