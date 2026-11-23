# N368: 回源请求延迟 $L_{miss}$ 的构成分解：$L_{miss} = L_{backhaul} + L_{origin} + L_{queue}^{origi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

回源请求延迟 $L_{miss}$ 的构成分解：$L_{miss} = L_{backhaul} + L_{origin} + L_{queue}^{origin}$，其中 $L_{backhaul}$ 为 POP 到源站的网络延迟（典型 20-50ms），$L_{origin}$ 为源站处理时间（典型 5-20ms），$L_{queue}^{origin}$ 为源站排队延迟（负载相关）；在低负载下，$L_{miss} \approx 30-70\text{ms}$。

## Corrected Claim

回源请求延迟 $L_{miss}$ 的构成分解：$L_{miss} = L_{backhaul} + L_{origin} + L_{queue}^{origin}$，其中 $L_{backhaul}$ 为 POP 到源站的网络延迟（典型 20-50ms），$L_{origin}$ 为源站处理时间（典型 5-20ms），$L_{queue}^{origin}$ 为源站排队延迟（负载相关）；在低负载下，$L_{miss} \approx 30-70\text{ms}$。

## Evidence

先验知识/题面给定，逻辑校验通过：延迟构成分解符合网络通信基本模型，典型数值量级（20-50ms回源，5-20ms处理）符合CDN/源站工程常识，低负载下总延迟30-70ms与分量之和逻辑自洽。
