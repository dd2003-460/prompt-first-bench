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


## E6 — verify_node 无异常路径但进程仍静默死（2026-11-11 r2 smoke 实测）
- **症状**：`runs-s5-sm-gpu-fbeta-r2.log` 停在 `[SM] L1: 25 nodes`，无 DONE 无 Traceback，PID 消失；直接重放 `_verify_batch(25节点)` 前台跑却正常。
- **根因**：未定——单发/连发 5 次 verify_node 全过（各 ~1.7s），说明不是 proxy 拒绝某条特定 claim；怀疑是后台进程 + 长 LLM 调用组合下的环境因素（macOS 睡眠断网 / 终端会话回收）。r1 smoke 也是同样模式死于 L1 之后。
- **处理**：这正是要修的可靠性问题本身。方向：① run() 每轮结束落盘 checkpoint（nodes JSON），死了能 resume；② 启动统一走 `scripts/launch.sh`（tee + EXIT code），至少死因可见；③ 关键 LLM 调用加 timeout + 单次重试。先复现：用 launch.sh 起 r2 重跑，看是否再次静默死、EXIT code 是什么。
- **状态**：[待核验] 复现中。


## E7 — 全链路（联网检索）核验批次挂死，--no-verify 模式正常（2026-11-11 对照实验定位）
- **症状**：r2/r3 smoke 都停在 L1 之后的 VERIFY 阶段，无 Traceback；进程有时静默消失（r2），有时 ESTABLISHED 挂着不动（r3 pid 72070）。
- **对照实验（本轮关键证据）**：同一台机器、同一个 8787 proxy，两个进程同时跑——
  - `--no-verify` 模式（跳过 search_node，只过 verify_node）：9 分钟已到 r1，+59 节点，ver=29/59，活着且在推进。
  - 全链路模式（search_node 联网检索 + verify_node）：4 分钟卡在 L1 后，CPU 0%，TCP ESTABLISHED 无流量。
  → 变量隔离出来了：**卡点是 search_node（ego-browser 联网检索通道），不是 verify_node，不是 proxy，不是状态机逻辑。**
- **根因**：[待核验] ego-browser 会话掉线/登录态失效时 research_hook 的超时行为——它可能无限等待而不是返回 err 降级。
- **处理**：① 给 search_node 加硬超时（如 120s）+ 失败降级为 degraded（设计里本来就有这个分支，但前提是它能"失败返回"而不是挂住）；② bench 跑之前先单测 research_hook 一次确认通道活着。
- **附带发现**：--no-verify r1 已 +59 节点（total 81），necessary 过滤在跑（ver=29/59 说明有节点被丢），F_β 方向有效，AC1 ≤200 大概率能达标。
