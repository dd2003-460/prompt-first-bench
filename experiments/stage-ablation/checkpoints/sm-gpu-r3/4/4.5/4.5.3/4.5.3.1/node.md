# N238: Mac Studio M3 Ultra (800 GB/s) 运行 BF16 Qwen3-27B (55GB) 的理论 Decode 吞吐上限为 800/55 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

Mac Studio M3 Ultra (800 GB/s) 运行 BF16 Qwen3-27B (55GB) 的理论 Decode 吞吐上限为 800/55 ≈ 14.5 tokens/s，实际受内存控制器效率影响预计为 13-14 tokens/s。

## Corrected Claim

Mac Studio M3 Ultra (800 GB/s) 运行 BF16 Qwen3-27B (55GB) 的理论 Decode 吞吐上限为 800/55 ≈ 14.5 tokens/s，实际受内存控制器效率影响预计为 13-14 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：800GB/s带宽除以55GB模型大小得出约14.5 tokens/s的理论上限，符合内存带宽瓶颈下的解码吞吐计算逻辑，且实际效率折损符合工程常识。
