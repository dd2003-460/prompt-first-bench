# N82: 4x V100-SXM2-16GB集群在满载（4 GPU均利用）时的总功耗约为600W-650W（单卡TDP 250W * 4 + 主板/散热/存储开销~100

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22, N23, N24

## Claim

4x V100-SXM2-16GB集群在满载（4 GPU均利用）时的总功耗约为600W-650W（单卡TDP 250W * 4 + 主板/散热/存储开销~100-150W），而非N23中简化的1.2kW（1.2kW可能是机柜级或包含冗余冷却的保守估计）

## Corrected Claim

4x V100-SXM2-16GB集群在满载时的总功耗约为1100W-1200W（单卡TDP 250W * 4 = 1000W + 主板/散热/存储/CPU开销~100-200W），而非600-650W。

## Evidence

[质询]来源[2]明确提到使用了2000W电源（PSU），这通常意味着系统的设计峰值功耗远高于600-650W，或者该陈述低估了SXM2基板及NVLink桥接器等组件的额外功耗；此外，600-650W仅为GPU+基础开销，未包含CPU、内存等完整节点功耗，与“集群/节点”总功耗的定义可能存在口径偏差。 | 逻辑上单卡250W*4=1000W已超出600-650W范围，此处陈述存在内部逻辑矛盾（250W*4=1000W，加上开销应>1100W，而非600-650W）。等等，重新检查逻辑：单卡TDP 250W，4张卡就是1000W。陈述说总功耗600-650W，这在数学上是不可能的（1000W > 650W）。这是一个硬逻辑错误。

## Search Query

Tesla V100 SXM2 16GB power consumption full load 4 GPU server total wattage

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_42608318/article/details/171226595&rut=3af63792b7f3f3e7788f4f6bd0e615b88abf2b72a04dcafd15666d88aaa29442', 'type': 'ddg', 'title': 'SXM2版V100显卡很麻烦但很香：14B大模型速度超50!附折腾攻略与TaoToken配置-CSDN博客'}
- {'url': 'https://ftulabs.github.io/blog/5.ftu-cluster.html&rut=7a57e658511070542539b85bad44c658d406526e53d23311d9404f062eedd7e5', 'type': 'ddg', 'title': 'Building a V100 SXM2 GPU Cluster on a University Budget'}
