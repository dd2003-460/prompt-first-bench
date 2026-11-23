# N326: 自建策略的边际成本 $MC_{self}(R)$ 定义为增加 1 个请求所需的额外成本，在带宽预留固定的前提下，$MC_{self} \approx 0$（直到

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N122

## Claim

自建策略的边际成本 $MC_{self}(R)$ 定义为增加 1 个请求所需的额外成本，在带宽预留固定的前提下，$MC_{self} \approx 0$（直到带宽饱和），仅当请求量导致需升级带宽或增加服务器时发生跳跃式增加，需确定带宽饱和对应的请求量阈值 $R_{sat}^{self}$。

## Corrected Claim

自建策略的边际成本 $MC_{self}(R)$ 定义为增加 1 个请求所需的额外成本，在带宽预留固定的前提下，$MC_{self} \approx 0$（直到带宽饱和），仅当请求量导致需升级带宽或增加服务器时发生跳跃式增加，需确定带宽饱和对应的请求量阈值 $R_{sat}^{self}$。

## Evidence

先验知识/题面给定，逻辑校验通过：在固定带宽预留的阶梯成本模型中，未达饱和前边际成本确实近似为0，符合经济学与系统资源管理的基本逻辑。
