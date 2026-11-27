# N313: 修正矛盾：NVIDIA L4 整机满载功耗 P_draw_L4 的准确值为 172W。依据：L4 GPU TDP 为 72W，但 L4 通常部署于服务器或高性能

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

修正矛盾：NVIDIA L4 整机满载功耗 P_draw_L4 的准确值为 172W。依据：L4 GPU TDP 为 72W，但 L4 通常部署于服务器或高性能工作站中，其配套 CPU（如 Xeon 或高端 i9）及系统平台在满载推理负载下基础功耗约为 100W（含 CPU、内存、散热等），而非 N97 假设的 50W。因此 P_draw_L4 = 72W + 100W = 172W。

## Corrected Claim

NVIDIA L4 GPU TDP为72W，在典型服务器或高性能工作站部署中，整机满载功耗通常在150W-200W区间（取决于CPU及平台配置），而非固定的172W。

## Evidence

[质询]将L4 GPU的TDP（72W）直接等同于整机满载功耗中的GPU部分，且假设配套CPU及平台基础功耗固定为100W，忽略了实际服务器/工作站中CPU功耗随负载波动、不同平台（如Xeon vs i9）功耗差异巨大以及L4常作为多卡或特定边缘/推理卡部署的多样性，导致172W这一精确数值缺乏普适性和严谨性。 | 先验知识/题面给定，逻辑校验通过，但经验事实（具体功耗数值）缺乏来源直接支持且存在口径混淆风险，故降级。

## Search Query

NVIDIA L4 server system power consumption CPU load inference workload
