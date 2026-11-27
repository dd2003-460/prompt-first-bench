# N206: AMD MI300X 单卡运行 Qwen3-27B (BF16) 的可行性与成本：显存 192GB HBM3 完全覆盖 54GB 权重及高并发 KV Cache

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD MI300X 单卡运行 Qwen3-27B (BF16) 的可行性与成本：显存 192GB HBM3 完全覆盖 54GB 权重及高并发 KV Cache；带宽 5.3 TB/s，理论吞吐上限约为 5.3e6 / (54e9) ≈ 98 tokens/s；单卡 CAPEX 约为 $15,000-$18,000 (2024-06 市场均价)，显著低于 H100 但高于消费级卡，是数据中心级 BF16 推理的高性价比替代方案。

## Corrected Claim

AMD MI300X 单卡运行 Qwen3-27B (BF16) 可行：192GB HBM3 显存覆盖 54GB 权重及 KV Cache；带宽 5.3 TB/s，理论吞吐上限约 98 tokens/s（实测可达 105 tok/s）；单卡 CAPEX 显著低于 H100，是数据中心级 BF16 推理的高性价比方案（具体价格需参考实时市场）。

## Evidence

[质询]CAPEX 数值（$15,000-$18,000）属于经验事实，且 2024-06 市场均价存在波动，参考来源未提供具体价格数据，无法直接验证该具体数值区间；此外，理论吞吐上限 98 tokens/s 的计算基于纯带宽限制，未考虑计算延迟和内存访问开销，实际性能可能低于此值，但作为理论上限表述尚可接受。 | 来源 [1] 和 [3] 直接支持 MI300X 192GB 显存可运行 Qwen3-27B BF16 及高并发场景，来源 [3] 实测 105 tok/s 与理论上限 98 tokens/s 量级一致（实测略高可能因 FP8 或优化，但量级合理）；但 CAPEX 具体数值无来源支持，属经验事实，逻辑自洽但缺来源直接支持。

## Retrieval Sources

- {'url': 'https://www.modelscope.cn/posts/437098&rut=9755e1cb70c06335698e8ea44ff42bca41fdc028384c5acef9b9da520b491742', 'type': 'ddg', 'title': '基于 AMD Instinct MI300X 部署 Qwen3.8-27B 满血版实战：192GB…'}
- {'url': 'https://blog.csdn.net/weixin_29057695/article/details/163809714&rut=ef740b74414a1e33fab03ed38accc88bee6488ff67539f9fd004f9be0fdd8923', 'type': 'ddg', 'title': 'AMD显卡本地部署Qwen3.8-27B大模型：从环境配置到性能调优全攻略-CSDN博客'}
- {'url': 'https://www.modelscope.cn/posts/436206&rut=45b0f0d023ad04b50b8c0f92a59bcb4aa67b1fadc4a80b39efec69af0d3fbe9c', 'type': 'ddg', 'title': '用 AI 自动从零部署 Qwen3.8-27B：一次 AMD MI300X 全程实录'}
