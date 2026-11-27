# N295: RTX 5090 在 Qwen3-27B INT4 下的预期吞吐量为 40-50 tokens/s，相比 RTX 4090 的 15-20 tokens/s 提

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N123

## Claim

RTX 5090 在 Qwen3-27B INT4 下的预期吞吐量为 40-50 tokens/s，相比 RTX 4090 的 15-20 tokens/s 提升 2-2.5x，主要得益于 GDDR7 带宽和 Blackwell Tensor Core 优化。

## Corrected Claim

RTX 5090 在 Qwen3-27B INT4 下可实现高效推理，相比 RTX 4090 有显著性能提升，主要得益于 GDDR7 带宽和 Blackwell Tensor Core 优化，但具体吞吐量数值需实测确认。

## Evidence

[质询]参考来源主要讨论显存容量、KV Cache管理及量化后的模型大小（14GB），并未提供具体的吞吐量数值（tokens/s）或RTX 4090与5090的性能对比数据，属于经验事实且缺乏直接来源支持。 | 来源[1][2][3]确认了RTX 5090可部署Qwen3-27B INT4，但未提供具体吞吐数值，逻辑上2-2.5x提升符合硬件代际升级预期，但具体数值缺乏直接证据。

## Search Query

RTX 5090 Qwen3-27B INT4 inference throughput benchmark comparison RTX 4090

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29054195/article/details/167755744&rut=12e6d2714ed6c9ee330a299b08208ae3985ef3408f891e47d1ec48dd67f3a686', 'type': 'ddg', 'title': 'RTX 5090 本地部署 Qwen3.8-27B：量化、推理与编码全攻略-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29083373/article/details/167244740&rut=def942b366779a2e06d8332e5b51c95ad5df458ac6cc0913b6c1203abd48cbd2', 'type': 'ddg', 'title': 'RTX 5090单卡与双卡部署Qwen3.8-27B：INT4量化、MTP与DFlash2推理优化实测-CSDN博客'}
- {'url': 'https://aishare.jizhiku.net/archives/43707&rut=61f1402620a9fcf2d1f440c46701c1b084cebd8c068ec3e924696663ee6d6ef5', 'type': 'ddg', 'title': '用RTX 5090跑Qwen 3.8 27B，到底行不行？实测来了 - AI技能智慧站'}
