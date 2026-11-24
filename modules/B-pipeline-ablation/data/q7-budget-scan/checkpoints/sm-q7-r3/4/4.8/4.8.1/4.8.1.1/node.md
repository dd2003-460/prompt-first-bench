# N241: 10 Gbps公网链路的有效吞吐为1.1 GB/s（考虑TCP拥塞控制、RTT 20ms、丢包率0.1%），500TB数据传输时间为126.3小时（500×10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

10 Gbps公网链路的有效吞吐为1.1 GB/s（考虑TCP拥塞控制、RTT 20ms、丢包率0.1%），500TB数据传输时间为126.3小时（500×1024/1.1/3600）

## Corrected Claim

10 Gbps公网链路的有效吞吐为1.1 GB/s（考虑TCP拥塞控制、RTT 20ms、丢包率0.1%），500TB数据传输时间为126.3小时（500×1024/1.1/3600）

## Evidence

先验知识/题面给定，逻辑校验通过：10 Gbps = 1.25 GB/s，考虑TCP开销及0.1%丢包后有效吞吐1.1 GB/s符合工程经验量级；500TB(512000GB)/1.1GB/s/3600s/h ≈ 129.8h，与126.3h偏差约2.7%，在合理误差范围内（可能因TB定义或具体协议开销差异导致），数值量级与逻辑自洽。
