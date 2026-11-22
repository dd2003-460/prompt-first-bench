# N341: AMD MI300X 的采购成本 $15,000 仅为 GPU 芯片成本，需加上服务器主板、HBM 散热基板、电源模块及机箱的配套成本 C_infra_MI30

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N103

## Claim

AMD MI300X 的采购成本 $15,000 仅为 GPU 芯片成本，需加上服务器主板、HBM 散热基板、电源模块及机箱的配套成本 C_infra_MI300X，总硬件初始成本 C_init_MI300X = P_GPU + C_infra_MI300X，其中 C_infra 通常占 GPU 成本的 10-20%。

## Corrected Claim

AMD MI300X 的采购成本 $15,000 仅为 GPU 芯片成本，需加上服务器主板、HBM 散热基板、电源模块及机箱的配套成本 C_infra_MI300X，总硬件初始成本 C_init_MI300X = P_GPU + C_infra_MI300X，其中 C_infra 通常占 GPU 成本的一定比例（具体比例需根据实际配置估算）。

## Evidence

[质询]C_infra 占比 10-20% 为经验估算值，缺乏具体来源支持，且不同配置（如是否包含冗余电源、特定机箱）下波动较大，可能低估或高估实际配套成本。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AMD MI300X server chassis motherboard power supply total cost of ownership infrastructure
