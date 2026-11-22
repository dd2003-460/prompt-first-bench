# N15: 消费级显卡（如RTX 4090）显存带宽为1008 GB/s，数据中心级（如A100 80GB）为2039 GB/s，前者在单卡场景下吞吐约为后者的50%。

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

消费级显卡（如RTX 4090）显存带宽为1008 GB/s，数据中心级（如A100 80GB）为2039 GB/s，前者在单卡场景下吞吐约为后者的50%。

## Corrected Claim

消费级显卡（如RTX 4090）显存带宽为1008 GB/s，数据中心级（如A100 80GB）为2039 GB/s，前者在单卡场景下吞吐约为后者的50%。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和子节点3结构高度相似，均基于相同的计算逻辑（(权重+KV Cache)/带宽），仅参数（精度、具体数值）不同，属于同一公式的不同实例，缺乏正交性且存在冗余。此外，子节点1中的H100和RTX 5090数据在父节点中未提及，虽不矛盾但略显发散。）

## Search Query

RTX 4090 vs A100 memory bandwidth inference throughput comparison
