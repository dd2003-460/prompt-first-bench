# S0 气象臂 — 仪器伪影记录（2026-11-27 21:30 Lead 核出）
> 承重发现: S0 SM 臂运行时**检索通道(webllm)早期崩溃**, 后 143 次 LLM 调用全是无检索退化态。
> 这是仪器问题, 不是 OOD 迁移失败。解读 S0 记分时必须带此 caveat。

## 一手证据 (sm-arm.log)
- L54 `[WEBLLM-EMPTY] perplexity: no links returned`
- L55 `[WEBLLM-EMPTY] chatgpt: no links returned`
- L56 `[WEBLLM-BROKEN] all endpoints failed, skipping future webllm calls`
- 崩溃点 L56 = 第 18 次 LLM call 之后; 其后还有 143 次 call(全跳过 webllm)
- 根因: `research_hook.py:751` 的 `_WEBLLM_BROKEN` 是**进程内内存 flag** —— 一旦三端点(deepseek/perplexity/chatgpt)全 EMPTY, 本次 run 剩余全程不再尝试 webllm
- 端点为何 EMPTY: ego-browser 无头会话里 deepseek 跳 sign_in(未登录态), perplexity/chatgpt 无返回 → 全空

## 对 S0 记分的影响
- SM 臂 40 节点 = 16 search 源 + 18 knowledge 源 + 6 其他; 但 search 通道 L56 后已死
- **search 源节点(N17-N28)若建于 L56 后, 实际是 arxiv/ddg 等其他通道或 knowledge 兜底, 不是 webllm** —— 需 P2 按节点时间戳细分
- degraded 24/40 的主因是**检索缺失**(evidence="检索失败: no sources"), 不是模型不懂气象
- 对照: 裸基线臂(单发)**不用任何检索**, 不受此伪影影响 → "SM vs 基线" 比较被 confound: SM 少了检索腿

## 解读修正
1. S0 测的是 **"SM 在无检索退化态下的 OOD 迁移"**, 不是完整 SM(带检索)
2. 若 S0 无检索态仍覆盖 ≥3/4 机制 → 更强 claim(SM 对检索缺失鲁棒); 若覆盖差 → 不能归因 OOD, 先修检索再判
3. **K2/K3 臂(S1 剥离版 + 硬件对照)跑前必须先核 webllm 通道健康**:
   - 健康 → 正常跑(与 S0 的"无检索态"不同口径, 需在记分里标 S0=degraded-instrument)
   - 不健康 → 三臂统一关检索(公平), 或先修登录态再跑
   - 判据: ego-browser 打 deepseek 是否跳 sign_in; 或 research_hook 单发一次 webllm 看是否 BROKEN

## 待决
- [ ] P2 记分: 按节点创建顺序细分 search 节点在 L56 前/后(前=真检索, 后=兜底)
- [ ] K2 派前: webllm 健康检查(ego-browser deepseek 登录态)
- [ ] 若 S0 判 inconclusive 且主因是检索缺失 → 修 webllm 登录态后重跑 S0(1 rep 即可, 40 节点 ~36min)
