# N162: 2x RTX 4090 通过 PCIe 4.0 x16 进行张量并行 (TP=2) 时，每层 All-Reduce 通信量 C_layer = 2 * B * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

2x RTX 4090 通过 PCIe 4.0 x16 进行张量并行 (TP=2) 时，每层 All-Reduce 通信量 C_layer = 2 * B * H * S (B=Batch, H=Hidden, S=Bytes/Element)，对于 Qwen3-27B (H=4096, BF16 S=2)，B=1 时 C_layer = 16 KB，32 层总通信量 C_total = 512 KB/step。

## Corrected Claim

2x RTX 4090 通过 PCIe 4.0 x16 进行张量并行 (TP=2) 时，每层 All-Reduce 通信量 C_layer = 2 * B * H * S (B=Batch, H=Hidden, S=Bytes/Element)，对于 Qwen3-27B (H=4096, BF16 S=2)，B=1 时 C_layer = 16 KB，32 层总通信量 C_total = 512 KB/step。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2 All-Reduce 通信量公式为 2*B*H*S，代入 B=1, H=4096, S=2 得 16KB/层，32层总计 512KB，计算无误。
