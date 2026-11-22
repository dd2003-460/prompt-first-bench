# N117: Qwen3-27B在vLLM中启用Tensor Parallelism (TP=2)时，Transformer层内每层需执行2次All-Reduce操作（Att

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：标准Transformer层包含Attention和FFN两个子层，每个子层输出后需进行All-Reduce以同步TP分片，故每层2次；通信量为激活值大小（Batch*Seq*Hidden）乘以精度字节数（BF16为2字节），乘以2次操作，公式推导正确。

## Search Query

vLLM tensor parallelism allreduce frequency per layer
