# N42: 1×NVIDIA A100 80GB PCIe 二手市场单价约为 $8000-$12000，全新价格已不可得或极高；相比之下，2×RTX 4090 的显存总量 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

1×NVIDIA A100 80GB PCIe 二手市场单价约为 $8000-$12000，全新价格已不可得或极高；相比之下，2×RTX 4090 的显存总量 (48GB) 小于 A100 (80GB)，但若采用W4量化，2×4090可承载模型，而A100可承载BF16模型，需对比两者在相同精度下的TCO。

## Corrected Claim

1×NVIDIA A100 80GB PCIe 二手市场单价约为 $8000-$12000（来源[1]显示约$10,999）；关于2×RTX 4090与A100在W4/BF16量化下的TCO对比，因缺乏来源支持，仅作为定性参考：2×4090显存总量(48GB)小于A100(80GB)，但在低精度量化下可能具备成本优势。

## Evidence

[质询]陈述中关于2×RTX 4090显存总量为48GB的描述存在事实错误（RTX 4090单卡显存为24GB，双卡应为48GB，此处数值正确但需确认是否指代特定型号或存在笔误，通常4090为24GB，若指4090D或其他变体需核实，但主流4090为24GB，2*24=48，数值本身无误。主要攻击点在于：来源仅覆盖了A100的价格，完全未覆盖RTX 4090的价格、显存对比及TCO分析，导致后半部分关于4090与A100对比的结论缺乏外部证据支持，属于经验事实且无来源直接支持。 | 来源[1]直接支持A100 80GB二手价格约为$10,999（在$8000-$12000区间内），但所有来源均未提供RTX 4090的相关数据或两者TCO对比，后半部分为经验事实且缺来源支持。

## Retrieval Sources

- {'url': 'https://gpudojo.com/a100-80gb&rut=8a3fb049a5bc8cc8a3e7962fd671c1ac077896344a9f7652309161bba580ea4c', 'type': 'ddg', 'title': 'A100 80GB Used Price & History (Nov 2026) | GPUDojo'}
- {'url': 'https://www.suanli.ai/gpus/A100-PCIE-80GB&rut=54ef967914fe2a76e29e6853b679aebeac6afe438af010a592ccf21fee2bc04f', 'type': 'ddg', 'title': 'NVIDIA A100 80GB PCIe 租用价格:最低 $0.500/卡·时,37 家服务商实时比价 | 算力.ai'}
- {'url': 'https://www.ebay.com/sch/i.html?_nkw=nvidia+a100+80gb+USED&_sop=12&rut=ceb581955a6e2ca2c3097220adf70bae5180fc7ce583bce6177d74ec02e2dcb2', 'type': 'ddg', 'title': 'Nvidia A100 80GB Used for sale - eBay'}
