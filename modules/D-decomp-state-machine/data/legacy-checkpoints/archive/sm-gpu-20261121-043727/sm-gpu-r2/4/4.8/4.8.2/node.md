# N84: WSL2 下 GPU 推理性能损失量化：相比原生 Linux，WSL2 引入的额外延迟主要源于 GPU 内存映射开销，典型吞吐损失为 3-8%（非 N29 所述

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N29

## Claim

WSL2 下 GPU 推理性能损失量化：相比原生 Linux，WSL2 引入的额外延迟主要源于 GPU 内存映射开销，典型吞吐损失为 3-8%（非 N29 所述的 5-10%，需以最新 benchmark 为准），公式：Throughput_WSL2 = Throughput_Linux * (1 - Loss_Ratio)，其中 Loss_Ratio ∈ [0.03, 0.08] [待核验]。

## Corrected Claim

WSL2 下 GPU 推理性能相比原生 Linux 有轻微损失，主要源于内存映射开销，典型吞吐损失通常在个位数百分比范围内（如 3-8%），具体数值依硬件与驱动版本而异。

## Evidence

[质询]具体数值区间（3-8%）缺乏权威基准测试支持，且来源[1]仅给出利用率（98%）而非吞吐损失率，两者虽相关但非直接等价，且不同模型/驱动版本下波动较大，固定区间可能误导。 | 来源[1]间接支持WSL2性能接近原生（利用率98%），但未直接提供3-8%的吞吐损失量化数据，属经验事实且缺直接来源支持。

## Search Query

WSL2 GPU inference performance loss percentage vs native Linux benchmark 2024

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/155481325&rut=0d48123ab262a5af8c82c7f7211e41b4f65bab5f2edcb91f141b97840fbadf3b', 'type': 'ddg', 'title': 'WSL2与GPU的奇妙邂逅：从零构建跨平台深度学习环境_GPU_7up55-亚马逊云科技技术品牌专区'}
