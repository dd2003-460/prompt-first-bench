# N8: NVIDIA数据中心/专业级GPU候选集：A100 40GB/80GB, H100 80GB, L40S 48GB, A6000 48GB；需确认其FP16/B

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

NVIDIA数据中心/专业级GPU候选集：A100 40GB/80GB, H100 80GB, L40S 48GB, A6000 48GB；需确认其FP16/BF16算力、显存带宽及单卡/多卡互联带宽（NVLink/NVSwitch）。

## Corrected Claim

NVIDIA数据中心/专业级GPU候选集包括A100 40GB/80GB, H100 80GB, L40S 48GB, A6000 48GB；当前来源仅确认A100的存在及Ampere架构，其余型号及具体FP16/BF16算力、显存带宽及互联带宽数据缺失，需补充来源。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点按GPU型号维度划分，各节点内容互不重叠且无矛盾，覆盖了父节点要求的算力、显存带宽及互联带宽等关键参数，且TDP作为补充信息合理存在，未构成冗余。）

## Search Query

NVIDIA A100 H100 L40S A6000 specs TFLOPS memory bandwidth NVLink bandwidth

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/data-center/a100/&rut=9ed5540d7ec6cdbdb7a1670c8b42a58b1e52e1baf76efcad693847ebd775106a', 'type': 'ddg', 'title': 'NVIDIA A100 Tensor Core GPU'}
- {'url': 'https://www.nvidia.com/zh-tw/data-center/a100/&rut=cadd54030a56742894de95d233e144763b3e87d84289ab945f0cc8602100a19e', 'type': 'ddg', 'title': 'Nvidia A100 | Nvidia'}
- {'url': 'https://www.techpowerup.com/gpu-specs/a100-pcie-40-gb.c3623&rut=b07994f6f82f9f795e91d63b85f77f69c373af4106f8336459c3578db2a5ea46', 'type': 'ddg', 'title': 'NVIDIA A100 PCIe 40 GB Specs | TechPowerUp GPU Database'}
