# N50: 基于 s_avg=950KB 和日均下载 2TB，日均请求量 N_total = 2TB / 950KB ≈ 2,193,000 次；若 s_avg 取 500

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

基于 s_avg=950KB 和日均下载 2TB，日均请求量 N_total = 2TB / 950KB ≈ 2,193,000 次；若 s_avg 取 500KB（纯图片），N_total ≈ 4,000,000 次；若 s_avg 取 5MB（纯视频），N_total ≈ 400,000 次。

## Corrected Claim

基于 s_avg=950KB 和日均下载 2TB，日均请求量 N_total = 2TB / 950KB ≈ 2,193,000 次；若 s_avg 取 500KB（纯图片），N_total ≈ 4,000,000 次；若 s_avg 取 5MB（纯视频），N_total ≈ 400,000 次。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅选取了父节点中三个计算案例里的两个（750KB和1.4MB），遗漏了父节点明确列出的基准情况（950KB）和极端情况（500KB/5MB），导致覆盖不全；同时，两个子节点本质上是同一公式 $N = S/s$ 在不同 $s$ 参数下的取值，结构高度同构，属于参数化冗余，而非概念上的独立维度。）

## Search Query

CDN request count calculation 2TB daily traffic
