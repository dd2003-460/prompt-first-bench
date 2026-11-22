# N7: NVIDIA消费级GPU候选集（2024-2025在售）：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 3090/30

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

NVIDIA消费级GPU候选集（2024-2025在售）：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 3090/3090 Ti (24GB), RTX 4070 Ti Super (16GB)；需确认各型号FP16/BF16算力（TFLOPS）与显存带宽（GB/s）的精确值。

## Corrected Claim

NVIDIA消费级GPU候选集（2024-2025在售）包括RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 3090/3090 Ti (24GB), RTX 4070 Ti Super (16GB)等；其具体FP16/BF16算力与显存带宽需查阅NVIDIA官方规格表确认，参考来源未提供精确数值。

## Evidence

父节点级核验未通过：有冗余（子节点在语义上正交且覆盖了父节点要求的所有参数（算力、带宽、显存容量）及额外信息（TDP）。然而，前5个子节点结构高度同质化，本质上是同一数据表的不同行，属于结构性冗余。）

## Search Query

NVIDIA RTX 4090 4080 Super 3090 specs TFLOPS memory bandwidth 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_23625847/article/details/159466219&rut=2be19b2159bad35bc682d05881da3811c25382160d84bbed127aeeeaba5d516c', 'type': 'ddg', 'title': '英伟达（NVIDIA）显卡全系列深度解析：从消费级到数据中心，私有化大模型部署选卡指南_l40s 支持fp4么-CSDN'}
- {'url': 'https://cloudgputracker.com/zh/blog/gpu-benchmark-complete-guide-2026/&rut=5a0590c8a983ade04b59f221e3fe5fb6c66027f56d69e3f5cad03dffbe6f1f4c', 'type': 'ddg', 'title': '2026年 GPU 基准测试完整指南：性能对比与选型建议 | CloudGPUTracker.com'}
- {'url': 'https://blog.csdn.net/weixin_29290963/article/details/158955535&rut=bcc183b7917eab2bb29ad4544f9aa5e2219edd8d231783d14427d26d6fe035d0', 'type': 'ddg', 'title': '2025.4.15 英伟达gpu选型指南：从b300到rtx5090，如何为你的ai项目精准匹配算力-csdn博客'}
