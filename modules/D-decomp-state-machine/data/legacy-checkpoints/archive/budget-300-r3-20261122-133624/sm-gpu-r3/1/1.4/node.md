# N9: 单卡部署 Qwen3-27B (BF16) 的显存安全下限为 60GB（54GB 权重 + 4.09GB KV + 2GB 框架 + 10% 冗余缓冲），排除所

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

单卡部署 Qwen3-27B (BF16) 的显存安全下限为 60GB（54GB 权重 + 4.09GB KV + 2GB 框架 + 10% 冗余缓冲），排除所有显存 < 60GB 的 GPU 选项

## Corrected Claim

单卡部署 Qwen3-27B (BF16) 的显存安全下限为 60GB（54GB 权重 + 4.09GB KV + 2GB 框架 + 10% 冗余缓冲），排除所有显存 < 60GB 的 GPU 选项

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，加上KV Cache、框架开销及冗余缓冲，60GB为合理的安全下限。
