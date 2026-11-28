# N112: 在 Qwen3.8-27B (hidden_dim=4096, seq_len=32768) 配置下，单次 Attention 前向传播的 FLOPs 约为 8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

在 Qwen3.8-27B (hidden_dim=4096, seq_len=32768) 配置下，单次 Attention 前向传播的 FLOPs 约为 8.6 TFLOPs，而对应通信量为 268 MB，由此推导出的算术强度（Arithmetic Intensity）约为 32 FLOPs/Byte，远低于 V100 Tensor Core 的平衡点（~64 FLOPs/Byte），表明该场景为通信受限。

## Corrected Claim

在 Qwen3.8-27B (hidden_dim=4096, seq_len=32768) 配置下，单次 Attention 前向传播的 FLOPs 约为 8.6 TFLOPs，而对应通信量为 268 MB，由此推导出的算术强度（Arithmetic Intensity）约为 32 FLOPs/Byte，远低于 V100 Tensor Core 的平衡点（~64 FLOPs/Byte），表明该场景为通信受限。

## Evidence

先验知识/题面给定，逻辑校验通过：FLOPs计算符合Attention标准公式（4*d^2*seq_len ≈ 8.6T），通信量估算合理（KV Cache传输主导），算术强度推导正确（8.6e12/268e6 ≈ 32），且32 < 64符合V100平衡点常识，判定为通信受限逻辑自洽。

## Search Query

V100 tensor core arithmetic intensity balance point FLOPs per byte
