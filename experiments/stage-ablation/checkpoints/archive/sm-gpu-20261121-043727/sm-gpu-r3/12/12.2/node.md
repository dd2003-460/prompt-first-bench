# N288: Ascend 910B (64GB HBM) 的 Qwen3 适配状态与性能损失量化：截至 2024Q4，CANN 8.0.RC1 支持 Qwen2 系列，Qw

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104

## Claim

Ascend 910B (64GB HBM) 的 Qwen3 适配状态与性能损失量化：截至 2024Q4，CANN 8.0.RC1 支持 Qwen2 系列，Qwen3 支持需等待 CANN 8.0 正式版或更高。910B 的 HBM 带宽为 1.6 TB/s，理论上 T_decode (W4) ≈ 14GB / 1.6TB/s ≈ 8.75 ms/token。但受限于算子库不完整（如 Flash Attention 支持滞后），实际 MFU 可能仅为 NVIDIA 同代产品的 50-70%，导致实际 T_decode 增加至 12-17 ms/token。获取渠道限制导致价格不透明，预估溢价 20-30% 相比 H100。

## Corrected Claim

Ascend 910B (64GB HBM) 已具备部署 Qwen3 系列模型的能力（如通过 vLLM-Ascend），但具体 CANN 版本支持状态及性能损失量化（如 MFU 50-70%、T_decode 12-17 ms/token）需依据最新官方文档或实测数据确认，当前陈述中的具体数值与版本限制缺乏直接来源支持。

## Evidence

[质询]陈述中关于CANN版本支持状态（CANN 8.0.RC1仅支持Qwen2，Qwen3需正式版）及具体性能损失量化（MFU 50-70%，T_decode 12-17ms）属于高度具体的经验事实与版本依赖信息，参考来源仅证实了910B硬件规格（64GB HBM）及Qwen3在vLLM-Ascend上的部署可行性，未提供CANN具体版本支持列表或精确的性能基准数据，且来源[1]标题提及Qwen3.5暗示时间线可能晚于2024Q4，存在版本状态过时的风险。 | 来源[1]直接支持910B 64GB HBM硬件规格，来源[2]证实Qwen3可在910B上部署，但缺乏对CANN版本支持细节及具体性能数值（MFU、T_decode、溢价）的直接支持，属于经验事实缺来源支持。

## Search Query

Huawei Ascend 910B Qwen3 support status CANN performance benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32597009/article/details/166111987&rut=4ab89e31ea4ba6c8b07f425790e9d388d665480e7065826958ece9e54a664b7b', 'type': 'ddg', 'title': '昇腾910B部署Qwen3.5实战：vLLM Ascend性能调优与避坑指南-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/155973960&rut=bee87ddd061a14409eab1f66c994bed4529ebb5f39cffa78d39225afb6c65e8c', 'type': 'ddg', 'title': '基于昇腾910B使用vLLM-Ascend部署Qwen3大模型'}
