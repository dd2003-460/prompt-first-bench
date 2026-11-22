# N36: 数据中心级 GPU 候选集（2024-2025）：NVIDIA A100 80GB SXM ($15,000-$18,000, 2TB/s HBM2e, 312

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

数据中心级 GPU 候选集（2024-2025）：NVIDIA A100 80GB SXM ($15,000-$18,000, 2TB/s HBM2e, 312 TFLOPS BF16), H100 80GB SXM ($25,000-$30,000, 3.35TB/s HBM3, 989 TFLOPS FP8), L40S 48GB ($8,000-$10,000, 864GB/s GDDR6, 362 TFLOPS FP8), MI300X 192GB ($15,000, 5.3TB/s HBM3, 1307 TFLOPS FP8)。注意：L40S 虽为数据中心卡但显存仅 48GB，需双卡或量化以支持 32K BF16/FP8 场景。

## Corrected Claim

数据中心级 GPU 候选集（2024-2025）：NVIDIA A100 80GB SXM, H100 80GB SXM, L40S 48GB, MI300X 192GB。注意：L40S 虽为数据中心卡但显存仅 48GB，需双卡或量化以支持 32K BF16/FP8 场景。

## Evidence

[质询]来源仅覆盖A100的通用描述，未提供H100、L40S、MI300X的具体参数及价格，且A100的具体数值（如312 TFLOPS BF16）未在摘要中直接体现，属于经验事实缺乏直接来源支持。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2]仅确认A100存在，未覆盖具体参数；来源[3]无关具体数值）

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/data-center/a100/&rut=9ed5540d7ec6cdbdb7a1670c8b42a58b1e52e1baf76efcad693847ebd775106a', 'type': 'ddg', 'title': 'NVIDIA A100 Tensor Core GPU'}
- {'url': 'https://www.nvidia.com/en-eu/data-center/a100/&rut=d84be5bd3c6b00b1b6dc1f4114382b589e18b08a9e5e5e9f56c2c72eb1885424', 'type': 'ddg', 'title': 'Nvidia A100 | Nvidia'}
- {'url': 'https://zhuanlan.zhihu.com/p/2092271469376161383&rut=6cd248b8994c28c1b2b8713bdbc1d4ce39ea8ab81e018739b19bb8f075cea33f', 'type': 'ddg', 'title': '2026年A100、H800、H20、4090 GPU榜单：大模型Token推理性能、显存、带宽与架构评测'}
