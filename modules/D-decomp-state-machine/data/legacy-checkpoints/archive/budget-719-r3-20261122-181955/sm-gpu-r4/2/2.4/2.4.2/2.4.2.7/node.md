# N261: INT4 (AWQ) 精度下总内存需求修正值：Weights (13.5GB) + KV_Cache (4.30GB) + Overhead (3GB) = 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83, N84, N85

## Claim

INT4 (AWQ) 精度下总内存需求修正值：Weights (13.5GB) + KV_Cache (4.30GB) + Overhead (3GB) = 20.80 GB。该数值低于 RTX 4090 的 24GB 显存上限，剩余可用显存为 24 - 20.80 = 3.20 GB。此余量足以覆盖操作系统驱动占用（~0.5GB）及临时缓冲区，确认 RTX 4090 在 INT4 下可运行 32K 上下文。

## Corrected Claim

INT4 (AWQ) 精度下总内存需求修正值：Weights (13.5GB) + KV_Cache (4.30GB) + Overhead (3GB) = 20.80 GB。该数值低于 RTX 4090 的 24GB 显存上限，剩余可用显存为 24 - 20.80 = 3.20 GB。此余量足以覆盖操作系统驱动占用（~0.5GB）及临时缓冲区，确认 RTX 4090 在 INT4 下可运行 32K 上下文。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别独立处理了权重显存修正、运行时开销修正、剩余显存重新计算以及最终可行性验证，逻辑链条清晰且无重叠。虽然子节点3和4都涉及显存数值的比较，但3侧重于计算过程的修正（Available Space），4侧重于最终结论的判定（Match/No Match），属于因果递进关系而非重复。）
