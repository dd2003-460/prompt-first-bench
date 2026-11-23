# N202: POP点非均匀负载：不同城市的流量占比不同（如北京/上海/广州各占15%，其他城市各占5%），高流量POP点需更多服务器，低流量POP点可缩减配置；总电费 = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

POP点非均匀负载：不同城市的流量占比不同（如北京/上海/广州各占15%，其他城市各占5%），高流量POP点需更多服务器，低流量POP点可缩减配置；总电费 = Σ(各POP点服务器数 * 单台电费 * PUE)，而非简单均分10台/点

## Corrected Claim

POP点非均匀负载：不同城市的流量占比不同（如北京/上海/广州各占15%，其他城市各占5%），高流量POP点需更多服务器，低流量POP点可缩减配置；总电费 = Σ(各POP点服务器数 * 单台电费 * PUE)，而非简单均分10台/点

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN traffic distribution by city China major urban areas
