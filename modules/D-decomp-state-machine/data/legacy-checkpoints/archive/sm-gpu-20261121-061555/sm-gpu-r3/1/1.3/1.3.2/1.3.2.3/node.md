# N164: Mac Studio M2 Ultra 的 192GB 统一内存支持 Qwen3-27B 在 BF16 精度下完整加载 (~54GB 权重) 并保留 >100G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

Mac Studio M2 Ultra 的 192GB 统一内存支持 Qwen3-27B 在 BF16 精度下完整加载 (~54GB 权重) 并保留 >100GB 余量用于 KV Cache，支持 >100K 上下文窗口，远超 32K 下限，但在 32K 固定窗口下存在严重的内存带宽利用率浪费 (Memory Wall)。

## Corrected Claim

Mac Studio M2 Ultra 的 192GB 统一内存支持 Qwen3-27B 在 BF16 精度下完整加载 (~54GB 权重) 并保留 >100GB 余量用于 KV Cache，支持 >100K 上下文窗口，远超 32K 下限，但在 32K 固定窗口下存在严重的内存带宽利用率浪费 (Memory Wall)。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 内存减去 ~54GB 权重后余量充足，支持长上下文；高内存带宽下固定短窗口确实存在带宽利用率浪费（Memory Wall）现象，符合硬件架构常识。
