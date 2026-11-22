# N415: 并发数敏感性拐点分析：当并发请求数 N > 4 时，单卡 RTX 4090 (24GB) 因显存瓶颈导致 OOM 或需大幅降低上下文，性价比得分骤降；而双卡 R

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

并发数敏感性拐点分析：当并发请求数 N > 4 时，单卡 RTX 4090 (24GB) 因显存瓶颈导致 OOM 或需大幅降低上下文，性价比得分骤降；而双卡 RTX 4090 (48GB) 或单卡 L40S (48GB) 的得分优势扩大至 > 50%，此时多卡/大显存方案成为唯一可行最优解

## Corrected Claim

并发数敏感性拐点分析：当并发请求数 N > 4 时，单卡 RTX 4090 (24GB) 因显存瓶颈导致 OOM 或需大幅降低上下文，性价比得分骤降；而双卡 RTX 4090 (48GB) 或单卡 L40S (48GB) 的得分优势扩大至 > 50%，此时多卡/大显存方案成为唯一可行最优解

## Evidence

检索失败: no sources from any channel (all 5 failed)
