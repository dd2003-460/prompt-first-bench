# N42: 消费级单卡工作点（RTX 4090 24GB）：因 24GB < 81.65GB (BF16)，无法原生运行 BF16 32K 上下文；若采用 W4 量化 (2

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

消费级单卡工作点（RTX 4090 24GB）：因 24GB < 81.65GB (BF16)，无法原生运行 BF16 32K 上下文；若采用 W4 量化 (27.32GB)，仍超出 24GB 上限，需启用 PagedAttention 或 offload，导致吞吐量下降约 40% [待核验]，单卡成本 $1600，tokens/sec per dollar 估算为 0.05。

## Corrected Claim

消费级单卡工作点（RTX 4090 24GB）：因 24GB < 81.65GB (BF16)，无法原生运行 BF16 32K 上下文；若采用 W4 量化 (27.32GB)，仍超出 24GB 上限，需启用 PagedAttention 或 offload，导致吞吐量显著下降（具体幅度视实现而定），单卡成本 $1600。

## Evidence

[质询]吞吐量下降约40%及tokens/sec per dollar 0.05为具体经验数值，缺乏直接来源支持，且不同量化/Offload策略下性能损耗差异巨大，该具体数值可能不准确或仅适用于特定极端场景。 | 逻辑上24GB显存确实无法容纳81.65GB的BF16模型及27.32GB的W4量化模型（需Offload），但参考来源[1][2][3]仅讨论1B-7B小模型或通用显存适配，未提供针对32K上下文大模型在RTX 4090上因Offload导致40%吞吐下降及具体成本效益比的数据支持，属于经验事实缺来源。

## Search Query

RTX 4090 Qwen3 27B 32K context inference throughput tokens per second

## Retrieval Sources

- {'url': 'https://blog.csdn.net/victory0431/article/details/153623952&rut=14e5e3633709386d9ed49b8ba27448fe0167402754c5a773e204b7b5eb3e7f7e', 'type': 'ddg', 'title': '评估8张RTX 4090（单卡24GB显存）对1B、7B参数模型的推理和微调能力_7b模型要多少g显卡-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_54447959/article/details/151923286&rut=c70c092cb88351a2de12ee7c9999043e0889fd0e56935211d1db150eda7a2306', 'type': 'ddg', 'title': 'RTX 4090 24GB 显存大模型实战指南：从推理优化到训练落地_rtx4090能跑7b大模型吗-CSDN博客'}
- {'url': 'https://modelers.csdn.net/69a7d1ee7bbde9200b9da148.html&rut=0e2c70bf1fa23fde6e237627addcc4851de0463bec06bdbdfd8b3eb7e08ec2cf', 'type': 'ddg', 'title': '评估8张rtx 4090（单卡24gb显存）对1b、7b参数模型的推理和微调能力'}
