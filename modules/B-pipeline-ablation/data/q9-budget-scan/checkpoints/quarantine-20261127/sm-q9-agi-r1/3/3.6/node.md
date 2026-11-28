# N25: 推理吞吐量的端到端基准测试方法：使用locust或wrk进行压力测试，模拟100个并发用户，每个用户发送平均长度512 tokens的请求，测量P95延迟、吞吐

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

推理吞吐量的端到端基准测试方法：使用locust或wrk进行压力测试，模拟100个并发用户，每个用户发送平均长度512 tokens的请求，测量P95延迟、吞吐量（requests/second）与错误率，目标P95延迟≤3秒，吞吐量≥5 requests/second，错误率≤0.1%。

## Corrected Claim

推理吞吐量的端到端基准测试方法：使用locust或wrk进行压力测试，模拟100个并发用户，每个用户发送平均长度512 tokens的请求，测量P95延迟、吞吐量（requests/second）与错误率，目标P95延迟≤3秒，吞吐量≥5 requests/second，错误率≤0.1%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

load testing locust wrk P95 latency throughput error rate vLLM benchmark
