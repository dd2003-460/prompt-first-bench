# N117: Qwen3-27B在vLLM中启用Tensor Parallelism (TP=2)时，Transformer层内每层需执行2次All-Reduce操作（Att

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Qwen3-27B在vLLM中启用Tensor Parallelism (TP=2)时，Transformer层内每层需执行2次All-Reduce操作（Attention输出后FFN输出后），每层通信数据量约为 2 * Batch_Size * Seq_Length * Hidden_Dim * 2bytes (BF16)。

## Corrected Claim

Qwen3-27B在vLLM中启用Tensor Parallelism (TP=2)时，Transformer层内每层需执行2次All-Reduce操作（Attention输出后FFN输出后），每层通信数据量约为 2 * Batch_Size * Seq_Length * Hidden_Dim * 2bytes (BF16)。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上层层递进（单层计算->总层汇总->性能占比），无重复或矛盾，正交性良好。但存在完备性问题：父节点核心在于描述TP=2下的通信机制（2次All-Reduce, BF16, 数据量公式），而子节点引入了父节点未提及的硬件假设（PCIe 4.0 x16, 4090 GPU）和具体业务场景（batch_size=1, seq_len=32768）。这使得分解从“通用机制描述”变成了“特定场景下的性能估算”，偏离了父节点的抽象层级。此外，子节点中隐含了Hidden_Dim=4096的参数，虽然符合Qwen3-27B事实，但父节点未明确给出，属于外部知识注入，导致分解不够自包含。）

## Search Query

vLLM tensor parallelism allreduce frequency per layer
