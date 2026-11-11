# SM 错误路径（T53 D1 · 每种失败模式 + 触发条件 + 处理）

> origin: ai (T53-D1, 成璐要求"所有相关错误放在项目里")
> append-only。每条：症状 / 根因 / 处理 / 先例。

## E1 — LLM 返回无法解析的 JSON（decompose "no nodes parsed"）
- **症状**：log 出现 `[decompose] attempt N: no nodes parsed, retrying...`
- **根因**：模型输出被截断（max_tokens 不够）或带 markdown 围栏/前后废话，`_extract_json` 取不到 dict。
- **处理**：`decompose()` 内置 max_retries=3；状态机侧不额外兜底——3 次全败则该轮无新节点 → J_stop 自然停（饱和语义）。若连续多题都这样，查 8787 proxy 是否限流。
- **先例**：2026-11-11 smoke run proc_aeb63c95fd0d L1 第 1 次即命中，第 2 次成功（28 节点）。属正常噪声，不用修。

## E2 — research_hook 检索通道失败（search_node 返回 err）
- **症状**：节点 status=degraded，evidence="检索失败: ..."
- **根因**：ego-browser 会话掉线 / arXiv API 超时 / ResearchHookUnavailable。
- **处理**：降级不中止（设计如此）；degraded 节点计入 J_verify 未核验比例，比例超阈值触发 REWORK 重搜。若整批全 degraded → 检查 ego-lite 登录态（ego-browser skill），别硬跑。
- **先例**：v17 smoke log 尾部出现过 HTTP 502 Bad Gateway（proxy 抖动），单点重试可恢复。

## E3 — LeakError（防泄漏命中）
- **症状**：`[SM] LEAK in decompose rN: ... LEAK DETECTED: [...]`
- **根因**：子节点 claim 回显了题目关键实体（extract_entities 提取的 >4 字中文词 + 英文专名）。
- **处理**：当前版本该 batch 跳过（continue），leak_hits_total 累计；AC2 要求 bench 全程零命中，任何命中 = 验收 fail，必须回查 prompt 模板哪里把题目结构带进了产出。注意：L1 骨架允许引用题目（目录不是答案），检查只针对 L2+ 展开层。
- **误报处理**：见 sm-leak-sop.md §误报（题目给定的约束/参数如 qwen3-27b、32K 不算泄漏，实体表应剔除 given 参数）。

## E4 — necessary 判定 LLM 调用失败
- **症状**：`[SM] necessary-judge error: <exc>`
- **根因**：8787 超时/5xx。
- **处理**：保守判 False（节点被丢弃）。副作用是漏拆而非刷分——与 v17 的病方向相反，可接受。连续 >5 个 error 说明服务不稳，先修服务再跑 bench。

## E5 — 进程中断（外部 kill / 机器睡眠 / proxy 死）
- **症状**：log 停在某轮中间，无 DONE 行；PID 不存在。
- **根因**：macOS 睡眠断网最常见；其次是 8787 proxy 重启。
- **处理**：runs-s5-sm-*.json 只在 run() 返回时落盘，中途死 = 无产物，直接重跑（状态机无持久 checkpoint，单题 ~30-60min 可接受）。若频繁发生，改用 scripts/launch.sh 包一层 tee + EXIT code（已有工具，commit af0994cd）。

## E6 — 静默死（进程活着但 log 不再增长）
- **症状**：PID 存在、CPU 0%、log 停在某行不动超过 10 分钟。
- **根因**：call_llm 在 502/timeout 上无限阻塞或 retry 循环吞掉异常；或 ego-browser 调用挂起无超时。
- **处理**：r3 已修（commit 96747559）：每轮 checkpoint 落盘 + --resume 续跑 + call_llm retries 有界。发现静默死 → 看最新 checkpoint 从哪轮 resume，不要从头跑。

## E7 — 本机代理端口挂掉导致联网通道全盲
- **症状**：ego-browser goto 全部 ERR_PROXY_CONNECTION_FAILED / ERR_FAILED；Python 直连也 Connection refused；但 ClashX 进程和控制面板 API（9090）还活着。
- **根因（2026-11-11 20:55 定位）**：ClashX 的 HTTP 代理端口 7890 不再监听（mixed-port/port 配置成了 0，只剩 SOCKS 7891 工作），而系统代理仍指向 7890。ego lite 渲染进程出站走系统代理 → 全挂；Python urllib 默认不走系统代理所以部分直连可用。这就是"微信会断"和 r2/r3 挂死的同一类病：**机器网络环境（ClashX）抖动，状态机没有隔离层**。
- **处理**：① 手动把 GLOBAL 切到可用节点 + 确认 7890 监听恢复出口；② 状态机侧加出口健康探针（E8）：Python 通道探活失败不整体死，快速探 ego-browser 是否还能活，能活就继续用 ego 通道，不能才置 network_degraded=True 让 search 节点降级为 degraded 继续跑。
- **先例**：2026-11-11 r2/r3 两次挂死均为此根因；--no-verify 对照 run（pid 69821）同期 9 分钟正常推进 81 节点，证明主循环本身没病。

## E8 — 状态机与本机网络环境解耦（已实现，commit d793b1a6 之后）
- **问题**：research_hook 的 ego-browser 通道依赖系统代理（ClashX 7890），ClashX 一挂整个联网检索通道就死；Python 侧通道（urllib 直连 arXiv/wiki API）反而不受影响。
- **已落地**：
  1. `_probe_network()`：run() 开头先探 Python 直连 → 失败再经 scutil 读出的系统代理试一次 → 两次都失败则快速探 ego-browser（taskSpace+page 存活判断）→ ego 还活就不降级，全死才 network_degraded=True。
  2. `_verify_batch`：network_degraded 时 search 节点跳过联网检索直接标 degraded（evidence 写明原因），不阻塞主循环。
  3. checkpoint 带 network_degraded 字段，resume 继承。
- **未做**：ClashX 自动切换节点（那是环境修复不是状态机职责）；launch.sh 前置网络检查（需要时再加）。

## E9 — 8787 proxy 间歇性 502 Bad Gateway
- **症状**：log 出现 `retry N: HTTP Error 502: Bad Gateway`，重试耗尽后整个 run 崩掉（r3 实际死法）。
- **根因**：8787 是 node proxy → 服务器 ninfer(qwen3.8-27b)，上游偶发 502。旧版 call_llm retries=2 且固定 sleep(5s)，遇到连续 502 窗口（>15s）就全灭。
- **处理**（2026-11-11 修）：① call_llm 按状态码分策略——5xx/429 指数退避（5s/10s/20s/40s），4xx 直接抛不浪费重试；② _decompose_layer retries 2→4，judge_necessary_batch retries 2→3。总最坏等待 ~75s，覆盖常见 502 窗口。
- **验证**：py_compile OK；待下次全链路 run 观察。
