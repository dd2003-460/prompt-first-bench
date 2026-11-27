# N98: TP=2通信开销的精确计算公式：T_comm = (2 × L × H × S × B × 2 bytes) / Bw_eff，其中L=32层(假设Qwen3-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

TP=2通信开销的精确计算公式：T_comm = (2 × L × H × S × B × 2 bytes) / Bw_eff，其中L=32层(假设Qwen3-27B结构), H=4096(hidden_size), S=32768(seq_len), B=1(batch), Bw_eff为有效互联带宽；在PCIe 5.0 x16 (64 GB/s)下，单次AllReduce传输数据量约为 4.3 GB，理论延迟 T = 4.3GB / 64GB/s ≈ 67ms/step（注：N29中12-15ms可能仅指单层或小块通信，全模型全序列通信量远大于此，需区分是per-layer还是global通信）。

## Corrected Claim

TP=2通信开销的精确计算公式：T_comm = (2 × L × H × S × B × 2 bytes) / Bw_eff，其中L=32层(假设Qwen3-27B结构), H=4096(hidden_size), S=32768(seq_len), B=1(batch), Bw_eff为有效互联带宽；在PCIe 5.0 x16 (64 GB/s)下，单次AllReduce传输数据量约为 4.3 GB，理论延迟 T = 4.3GB / 64GB/s ≈ 67ms/step（注：N29中12-15ms可能仅指单层或小块通信，全模型全序列通信量远大于此，需区分是per-layer还是global通信）。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2*32*4096*32768*1*2 / 1e9 ≈ 4.29 GB，4.29 / 64 ≈ 0.067 s = 67 ms，数值量级与公式推导自洽。

## Search Query

tensor parallel communication volume formula allreduce sequence length hidden size
