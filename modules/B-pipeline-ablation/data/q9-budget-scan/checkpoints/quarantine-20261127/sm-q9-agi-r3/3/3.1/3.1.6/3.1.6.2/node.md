# N159: 当 L=64k tokens 时，N_max ≈ 4 的计算隐含了每个序列的 KV cache 占用为 2 MB * 64 = 128 MB，4 个序列共 51

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

当 L=64k tokens 时，N_max ≈ 4 的计算隐含了每个序列的 KV cache 占用为 2 MB * 64 = 128 MB，4 个序列共 512 MB，远低于 12.6 GB，说明此处瓶颈并非 KV 显存总量，而是 vLLM 的 max-num-seqs=8 配置或调度器限制。

## Corrected Claim

当 L=64k tokens 时，N_max ≈ 4 的计算隐含了每个序列的 KV cache 占用为 2 MB * 64 = 128 MB，4 个序列共 512 MB，远低于 12.6 GB，说明此处瓶颈并非 KV 显存总量，而是 vLLM 的 max-num-seqs=8 配置或调度器限制。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 占用计算（128MB * 4 = 512MB）远小于总显存（12.6GB），且 512MB 在 12.6GB 中占比极小，逻辑上支持瓶颈非显存总量而是并发数限制的结论。

## Search Query

vLLM max_num_seqs scheduler limit long context concurrency
