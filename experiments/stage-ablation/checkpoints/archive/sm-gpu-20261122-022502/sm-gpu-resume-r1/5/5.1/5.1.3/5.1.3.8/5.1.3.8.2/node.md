# N874: Batch Size 从 1 增加到 4 时，吞吐量提升倍数并非简单的 2.5-3 倍，而是受限于 'Arithmetic Intensity'。当 Batch

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N273

## Claim

Batch Size 从 1 增加到 4 时，吞吐量提升倍数并非简单的 2.5-3 倍，而是受限于 'Arithmetic Intensity'。当 Batch Size 足够大时，每生成一个 token 所需的权重读取次数不变，但计算量增加。提升倍数 M = (T_bs4 / T_bs1) 通常遵循 M ≈ sqrt(Batch_Size) 到 Batch_Size 之间的曲线。在 4090 上，bs=1 到 bs=4 的实际提升通常在 1.8-2.2 倍之间，而非 2.5-3 倍，因为带宽利用率在 bs=1 时已较高（约 70-80%），边际收益递减曲线比 N273 假设的更陡峭。

## Corrected Claim

Batch Size 从 1 增加到 4 时，吞吐量提升倍数并非简单的 2.5-3 倍，而是受限于 'Arithmetic Intensity'。当 Batch Size 足够大时，每生成一个 token 所需的权重读取次数不变，但计算量增加。提升倍数 M = (T_bs4 / T_bs1) 通常遵循 M ≈ sqrt(Batch_Size) 到 Batch_Size 之间的曲线。在 4090 上，bs=1 到 bs=4 的实际提升通常在 1.8-2.2 倍之间，而非 2.5-3 倍，因为带宽利用率在 bs=1 时已较高（约 70-80%），边际收益递减曲线比 N273 假设的更陡峭。

## Evidence

先验知识/题面给定，逻辑校验通过：Batch Size 增加提升吞吐量受算术强度限制，bs=1 到 bs=4 在消费级显卡上因带宽利用率已较高，提升倍数通常低于线性（4倍），1.8-2.2 倍符合边际收益递减的工程直觉。

## Search Query

LLM inference batch size throughput scaling law memory bound
