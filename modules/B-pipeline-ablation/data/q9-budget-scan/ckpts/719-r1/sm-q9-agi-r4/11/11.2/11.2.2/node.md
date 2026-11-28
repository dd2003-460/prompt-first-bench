# N320: JAX batching 策略下内存峰值占用 M_peak_batched = batch_size * d_dimensions * 4bytes + ove

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

JAX batching 策略下内存峰值占用 M_peak_batched = batch_size * d_dimensions * 4bytes + overhead，当 d=10000，batch_size=250000 时，M_peak_batched = 250000 * 10000 * 4 = 10GB，加上 JAX 运行时开销（~2GB）和 CUDA context（~1GB），总内存 ~13GB，低于 16GB 限制；但若 d=100000，batch_size=250000 时，M_peak_batched = 100GB，远超 16GB，需进一步减小 batch_size 至 25000，M_peak_batched = 10GB，总内存 ~13GB，满足限制

## Corrected Claim

JAX batching 策略下内存峰值占用 M_peak_batched = batch_size * d_dimensions * 4bytes + overhead，当 d=10000，batch_size=250000 时，M_peak_batched = 250000 * 10000 * 4 = 10GB，加上 JAX 运行时开销（~2GB）和 CUDA context（~1GB），总内存 ~13GB，低于 16GB 限制；但若 d=100000，batch_size=250000 时，M_peak_batched = 100GB，远超 16GB，需进一步减小 batch_size 至 25000，M_peak_batched = 10GB，总内存 ~13GB，满足限制

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（250k*10k*4B=10GB, 250k*100k*4B=100GB, 25k*100k*4B=10GB），内存估算符合JAX/CUDA常规量级，逻辑自洽。
