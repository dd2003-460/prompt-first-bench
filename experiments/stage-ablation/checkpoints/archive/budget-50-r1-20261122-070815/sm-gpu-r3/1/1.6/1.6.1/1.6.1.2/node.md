# N203: KV Cache 卸载至 CPU 内存的可行性分析：在 32K 上下文下，Qwen3-27B 的 KV Cache 约为 2.0 GB (BF16)。若将 KV

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

KV Cache 卸载至 CPU 内存的可行性分析：在 32K 上下文下，Qwen3-27B 的 KV Cache 约为 2.0 GB (BF16)。若将 KV Cache 卸载至 CPU，每次生成新 token 时需从 CPU 读取历史 KV 并写回，传输数据量约为 2 * seq_len * hidden_dim * dtype_size。对于 seq_len=32768，hidden_dim=4096 (假设)，dtype=2 bytes，每次更新传输量约为 512 MB，PCIe 4.0 传输时间 16 ms，加上内存延迟，每 token 额外延迟约 20-30 ms，导致吞吐量从 65 tokens/s 降至 ~30-40 tokens/s，性能损失 40-50%。相比权重卸载，KV Cache 卸载的延迟影响较小，但仍显著降低性能，需评估是否值得以 40-50% 的吞吐损失换取显存容量。

## Corrected Claim

在 32K 上下文下，Qwen3-27B 的 KV Cache 约为 2.0 GB (BF16)。若将 KV Cache 卸载至 CPU，每次生成新 token 时需从 CPU 读取当前 token 的 KV 增量并写回，传输数据量约为 2 * 1 * hidden_dim * dtype_size（~16KB），PCIe 4.0 传输时间 <1ms，加上内存延迟，每 token 额外延迟约 1-5ms，导致吞吐量从 65 tokens/s 降至 ~60-65 tokens/s，性能损失 <10%。相比权重卸载，KV Cache 卸载的延迟影响较小，但仍需评估是否值得以 <10% 的吞吐损失换取显存容量。

## Evidence

[质询]传输量计算存在量级错误：每次生成新 token 仅需读取/写入当前层的 KV（或增量），而非整个 seq_len 的历史 KV；若按全量传输计算，512MB 数据量对应 PCIe 4.0 带宽（~32GB/s）理论时间应为 ~16ms，但实际 KV Cache 卸载通常采用分页或流式传输，且 32K 上下文下 Qwen3-27B 的 hidden_dim 并非 4096（Qwen3-27B 实际 hidden_dim 为 4096 是假设，但 Qwen3-27B 的层数和头数需核实），更关键的是，每次 token 生成只需传输当前 token 的 KV 增量（~2 * 1 * hidden_dim * dtype_size = ~16KB），而非 512MB，因此 20-30ms 延迟和 40-50% 吞吐损失严重高估。 | 经验事实，逻辑自洽但缺来源支持；传输量计算错误导致延迟和吞吐损失高估，需修正为增量传输模型。

## Search Query

KV cache offloading CPU memory LLM inference performance degradation
