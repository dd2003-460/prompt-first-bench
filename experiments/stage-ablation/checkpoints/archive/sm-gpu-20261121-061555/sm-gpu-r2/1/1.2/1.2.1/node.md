# N43: NVIDIA H200 (Hopper) 的显存规格为 141GB HBM3e，带宽 4.8 TB/s，TDP 700W；其显存容量是 H100 的 1.76 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

NVIDIA H200 (Hopper) 的显存规格为 141GB HBM3e，带宽 4.8 TB/s，TDP 700W；其显存容量是 H100 的 1.76 倍，带宽提升 13%，需核实其二手或租赁市场价格，以评估其在 BF16 全精度推理下的单卡可行性及 TCO [待核验]

## Corrected Claim

NVIDIA H200 (Hopper) 的显存规格为 141GB HBM3e，带宽 4.8 TB/s（约为 H100 的 1.4 倍）；其显存容量是 H100 的 1.76 倍。TDP 通常为 700W（SXM 版本）。二手或租赁市场价格需另行核实，以评估其在 BF16 全精度推理下的单卡可行性及 TCO。

## Evidence

[质询]陈述中关于H200显存容量（141GB）和带宽（4.8 TB/s）的描述与来源一致，但关于TDP 700W的具体数值未在提供的摘要中直接体现（通常H100/H200 SXM版本TDP为700W，PCIe版本较低，需确认具体型号），且关于二手/租赁市场价格的部分完全缺乏来源支持，属于经验事实且无法从第一性原理推导。 | 来源[1]直接支持141GB HBM3e和4.8 TB/s带宽，并指出带宽是H100的1.4倍（即提升40%，而非陈述中的13%），容量是H100的1.76倍（141/80≈1.76，逻辑自洽）；但TDP具体数值及市场价格无来源支持，且带宽提升比例与来源描述（1.4X）存在数值偏差（1.4X意味着提升40%，陈述称13%可能混淆了不同版本或计算错误，H100 SXM带宽为3.35TB/s，4.8/3.35≈1.43，提升约43%；若H100 PCIe为2TB/s，则提升140%。来源明确说1.4X more bandwidth，陈述称13%提升明显错误）。

## Search Query

NVIDIA H200 specs HBM3e bandwidth price used market

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/data-center/h200/&rut=ac2487b35b09c1eb9b3c6e332fe2dd6dc5269ac5b1a280b5f0c417d2c696037c', 'type': 'ddg', 'title': 'Nvidia H200 Gpu'}
- {'url': 'https://resources.nvidia.com/en-us-gpu-resources/hpc-datasheet-sc23&rut=57ee9b1e301dec0017772604660c030bf091b76dd2aa9f20350c60e9f06a4570', 'type': 'ddg', 'title': 'NVIDIA H200 GPU Datasheet'}
