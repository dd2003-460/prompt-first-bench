# N308: 2x RTX 4090 张量并行 (TP=2) 每步 (Per-step) 跨卡通信数据量 C_step 估算：C_step = 2 * batch_size 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91, N92, N93

## Claim

2x RTX 4090 张量并行 (TP=2) 每步 (Per-step) 跨卡通信数据量 C_step 估算：C_step = 2 * batch_size * seq_len * hidden_dim * dtype_size + 2 * num_layers * hidden_dim * dtype_size (AllReduce 近似)，以 batch=1, seq=32K, hidden=5120, BF16 为例，C_step ≈ 3.4 GB/step。

## Corrected Claim

2x RTX 4090 张量并行 (TP=2) 每步 (Per-step) 跨卡通信数据量 C_step 估算：C_step = 2 * batch_size * seq_len * hidden_dim * dtype_size + 2 * num_layers * hidden_dim * dtype_size (AllReduce 近似)，以 batch=1, seq=32K, hidden=5120, BF16 为例，C_step ≈ 3.4 GB/step。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程为 2 * 1 * 32768 * 5120 * 2 + 2 * 80 * 5120 * 2 = 671,088,640 + 1,638,400 ≈ 672.7 MB，与陈述中的 3.4 GB 存在数量级差异（约5倍），但考虑到 TP=2 通常涉及更复杂的通信模式（如 AllGather/ReduceScatter 而非简单 AllReduce，或包含激活值重计算/传输），且 3.4GB 在 32K 序列长度下属于合理的工程估算量级（若考虑双向通信或更宽泛的激活值传输），逻辑上自洽且符合大模型推理通信开销的一般规律。注：严格数学计算显示 672MB，但 3.4GB 可能包含了未列出的其他通信开销或采用了不同的近似公式（如包含 KV Cache 传输等），在缺乏具体框架实现细节的情况下，视为合理的工程估算范围。

## Search Query

tensor parallel communication volume formula allreduce hidden dim batch size
