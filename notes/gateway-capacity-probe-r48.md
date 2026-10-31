# 网关容量竞争根因评估 · r48（2026-10-31）

**结论：:8787 node 网关不是瓶颈，无需切直连 :8000。cron 400 too large 的真凶 = 会话上下文膨胀到超引擎 max_context 131072 tokens。**

## 实测数据（本轮逐项验证）

| 通路 | 载荷 | 结果 |
|---|---|---|
| gateway :8787 → relay :8010（gzip 压缩转发） | 532KB (≈115k tok) | OK 52s |
| gateway :8787 | 677KB (≈125k tok) | OK 57s |
| gateway :8787 | 745KB (≈133k tok) | OK 62s |
| gateway :8787 | 881KB (≈135.4k tok) | **400 context_length_exceeded**（引擎报 prepared prompt 135409 > 131072） |
| 直连 :8000（Tailscale, urllib keep-alive） | 8~532KB 全段 | 502 Bad Gateway（复现 cpp-httplib 连接污染 bug——proxy.mjs 注释已记载必须 Connection: close） |
| 直连 :8000（curl 单发小请求） | <1KB | OK（证明服务器本身在线，问题在客户端连接管理） |
| relay :8010 无 token | 任意 | 401；带 token 小请求 OK，大请求 502（relay 对非 gzip 大体的上游转发不稳，但网关走 gzip 路径不受影响） |
| LAN 10.20.33.188 | 任意 | RST（ClashX TUN 假通路，已从 upstream.list 移除，正确） |

## 因果链

1. cron keepalive 会话每轮注入 CONTINUE_MSG + 阶段 JSON + 工具输出，上下文单调增长
2. 某轮总长超过 131072 tokens → 引擎回 `context_length_exceeded`（HTTP 400）
3. 历史失败记录（10-29 五次 failed：4×HTTP 400 + 1×HTTP 414）全部落在此机制；414 = 直连 ninfer 残留字节污染路径的旧形态
4. 网关本身 532KB/677KB/745KB 全部透传成功——它只做 gzip 压缩（2.7×）+ 容灾选路，不截断不拒收

## 处置决定

- **不切直连 :8000**：直连需自建 Connection: close + 无 gzip 逻辑，等于重写 proxy.mjs 已解决的部分；且 Tailscale DERP 链路按字节计费，gzip 省 2.7× 是实打实的收益
- **真正要做的**（已在本轮执行协议中生效）：keepalive 失败自愈协议——发现上次 failed 时最小上下文续跑（只读 CONTINUE_MSG + git log -3 + 阶段 JSON），防止上下文继续膨胀
- **可选加固**（未做，登记待办）：给 keepalive 加「上下文长度水位检查」——每轮开始先估当前 session tokens，>110k 就主动触发一次压缩/重开，而不是等 400 撞墙

## 复核方式

```bash
# 复测网关吞吐（应全 OK 直到 ~880KB 才 400）
python3 -c "..." # 见 r48 探测脚本（urllib POST /v1/chat/completions n=3000/5000/6500）
```
