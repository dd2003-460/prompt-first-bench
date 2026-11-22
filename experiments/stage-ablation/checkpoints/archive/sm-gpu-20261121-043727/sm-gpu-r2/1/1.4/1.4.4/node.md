# N50: NVIDIA RTX 4090 的精确规格为：24GB GDDR6X, 内存带宽 1.0TB/s, TDP 450W, 支持 FP8 (通过 Tensor Co

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

NVIDIA RTX 4090 的精确规格为：24GB GDDR6X, 内存带宽 1.0TB/s, TDP 450W, 支持 FP8 (通过 Tensor Core), 单卡价格区间 $1,600-$1,800 (2024 Q3 市场价)

## Corrected Claim

NVIDIA RTX 4090 的规格为：24GB GDDR6X, 内存带宽 1008 GB/s (约 1.0TB/s), TDP 450W, 支持 FP8 (通过 Tensor Core), 2024 Q3 市场价约 $1,600-$1,800 (需结合实时市场数据确认)

## Evidence

[质询]陈述中提到的内存带宽为 1.0TB/s，而参考来源 [1] 明确指出 RTX 4090 的显存带宽为 1008 GB/s（即约 1.008 TB/s）。虽然 1.0TB/s 是 1008 GB/s 的合理近似值，但在精确规格描述中，通常应使用官方标称值 1008 GB/s 或更精确的 1.008 TB/s。此外，价格区间 $1,600-$1,800 属于 2024 Q3 的市场经验事实，参考来源未提供价格信息，无法通过现有来源直接验证该具体数值区间，且市场价格波动较大，该区间可能仅适用于特定时期或特定渠道，缺乏多源一致性支持。 | 来源 [1] 直接支持 24GB GDDR6X 和约 1.0TB/s (1008 GB/s) 的带宽，但 TDP 450W、FP8 支持及具体价格区间缺乏来源直接支持或存在近似误差，且价格属于经验事实，仅凭逻辑自洽不足以判 verified。

## Search Query

NVIDIA RTX 4090 specifications price 2024

## Retrieval Sources

- {'url': 'https://wenku.baidu.com/view/2c9659ca8362caaedd3383c4bb4cf7ec4afeb63a.html&rut=bcd0ac5d691ab123ce66735fd376a0cdc2bebafe30ef2aa63b4ef1a7a4f9244c', 'type': 'ddg', 'title': 'Rtx 4090显存多大？深度解析24gb Gddr6x显存规格与真实性能'}
