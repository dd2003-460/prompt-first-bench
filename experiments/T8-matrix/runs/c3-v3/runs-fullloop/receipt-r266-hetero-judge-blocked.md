# T8-C3-v3-fullloop 异源 judge 验证 · r266 调研回执（blocked_human）

- 生成时间：2026-11-03T15:30+08:00
- 阶段：pfb loop stage 02 (r1)，主任务路径按任务书【失败降级】条款标记 **blocked_human**
- 本回执为预计算汇总工件：不含任何异源 judge 评分（因无可用端点，无法执行），仅固化 r265 同源基线与 G2 对比骨架。

## 1. 阻塞原因（证据链）

| # | 事实 | 证据 | 观测时间 |
|---|------|------|----------|
| 1 | 本机不存在可用的非 Qwen family 可调用端点：LM Studio :1234 / Ollama :11434 端口均 CLOSED；全量 LISTEN 端口枚举后唯一 LLM 推理端点 127.0.0.1:8787（node/ninfer）仅服务 qwen3.8-27b（Qwen family） | `loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md` | 2026-11-02（探测执行日） |
| 2 | 环境变量与 shell rc 中不存在任何非 Qwen provider（OpenAI/OpenRouter/Gemini/Mistral/Cohere/DeepSeek 等）API key；免费额度渠道在无凭据下不可验证 | 同上（probe 文档 §credentials 节） | 2026-11-02 |
| 3 | 当前会话模型 qwen3.8-27b 属 Qwen family，既当生成器又当裁判（r265 同源偏差来源），不可作为异源 judge | `experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json` channel.model | 2026-11-03T14:30+0800（receipt generated_at） |

结论：验收标准 1（找到 ≥1 个可用非 Qwen judge 端点）在当前资源下无法满足 → 验收标准 2–5 无法启动。缺口属用户侧输入（key 或本地模型确认），Commander 单方面无法补齐。

## 2. r265 同源基线（G2 对比表左列，已提取自 receipt-r265-pilot-v2.json）

- judge 通道：qwen3.8-27b（gen temp 0.7 / judge temp 0），J1-strict-v3 + J2-lenient-v3 双判
- G2 区分力（同 domain 跨 config spread）：**1/12 PASS**
  - 唯一 PASS 项：`D1-meeting-room_S02_J2`，spread = 0.1111
  - 其余 11 项 spread = 0.0（FAIL）
- r265 结论：signal_strength = WEAK —「消融信号 < 测量噪声」
- r265 recommendation：下一步为异源 judge（非 Qwen family）交叉验证，或换更强生成模型（>32B）

## 3. G2 对比表骨架（右列待异源 judge 解锁后填充）

| 项目 (domain_stage_judge) | r265 同源 spread | r266 异源 spread | 判定变化 |
|---|---|---|---|
| D1-meeting-room_S01_J1 | 0.0 FAIL | _pending_ | — |
| D1-meeting-room_S01_J2 | 0.0 FAIL | _pending_ | — |
| D1-meeting-room_S02_J1 | 0.0 FAIL | _pending_ | — |
| D1-meeting-room_S02_J2 | 0.1111 PASS | _pending_ | 关键复测项 |
| D1-meeting-room_S03_J1 | 0.0 FAIL | _pending_ | — |
| D1-meeting-room_S03_J2 | 0.0 FAIL | _pending_ | — |
| D2-file-collab_S01_J1 | 0.0 FAIL | _pending_ | — |
| D2-file-collab_S01_J2 | 0.0 FAIL | _pending_ | — |
| D2-file-collab_S02_J1 | 0.0 FAIL | _pending_ | — |
| D2-file-collab_S02_J2 | 0.0 FAIL | _pending_ | — |
| D2-file-collab_S03_J1 | 0.0 FAIL | _pending_ | — |
| D2-file-collab_S03_J2 | 0.0 FAIL | _pending_ | — |

注：r265 pilot 实际覆盖 6 cells = {A-full, B-nofreeze, B-none} × {D1-meeting-room, D2-file-collab}，上表 12 行对应 2 domains × 3 stages × 2 judges 的 G2 统计单元（spread 在同 domain 内跨 3 configs 计算）。完整逐项数值以 receipt-r265-pilot-v2.json g2_discrimination 节为准。

## 4. 解锁条件（三选一，收到后继续验收标准 2–5）

- (a) 任一非 Qwen 厂商 API key（Anthropic/OpenAI/Gemini/Mistral/DeepSeek 等；只需 base_url + key，勿在共享文档中粘贴完整 key）
- (b) 启动 LM Studio 或 Ollama 并加载一个非 Qwen family 模型（conf-0.3 通道）
- (c) 确认接受降级方案：qwen3.8-27b 同源复判 + 人工抽审（conf-0.2，T8 结论将标注同源偏差风险）

若三者均不可行 → T8 实验线按现有 r265 结论（信号弱）正式收口。

## 5. 基础设施备注（runtime/schema 不匹配，如实上报）

stage-02 advance 校验器对字段强制要求「外部 HTTPS 具体来源 + observed_at」，但本任务全部证据均为本地仓库工件（probe 文档、receipt、rubric JSON），属纯本地研究任务，无外部 web 事实可供引用。advance 通道因此在本轮不可用；本动作改走 allowed_actions 中的 blocked_human 通道，符合任务书失败降级条款。未伪造任何 judge 分数或 HTTPS 引用。