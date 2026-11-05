# 本地非 Qwen LLM 端点探测记录（r266）

- 时间戳: 2026-11-03 06:01–06:05 CST (darwin, a1-6)
- 任务: 01-r1-field-unknown-b23a6a8439 (research_required 字段补证据)
- 结论: **未发现任何可用的非 Qwen family 可调用模型端点。** 本机唯一暴露的 LLM 推理端点是 127.0.0.1:8787，仅服务 qwen3.8-27b。

## 1. 默认端口探测（均失败）

| 命令 | 结果 |
|---|---|
| `curl -s --max-time 5 http://localhost:1234/v1/models` | curl exit=7 (connection refused)，HTTP 000；`nc -z 127.0.0.1 1234` → CLOSED |
| `curl -s --max-time 5 http://localhost:11434/api/tags` | curl exit=7 (connection refused)，HTTP 000；`nc -z 127.0.0.1 11434` → CLOSED |

→ LM Studio server 与 Ollama 均未在运行。

## 2. 环境变量扫描（只看变量名与 base url，key 已脱敏）

```
LMSTUDIO_API_KEY=<present>          # 有 key 但 :1234 无监听 → server 未启动
ANTHROPIC_AUTH_TOKEN=<present>
ANTHROPIC_BASE_URL=http://127.0.0.1:8787
ANTHROPIC_MODEL=qwen3.8-27b
ANTHROPIC_DEFAULT_{SONNET,OPUS,HAIKU}_MODEL=qwen3.8-27b
```
无 OPENAI_BASE_URL / OPENROUTER_API_KEY / GEMINI / MISTRAL / COHERE / DEEPSEEK 等指向其他 provider 的变量。

## 3. 应用目录检查

- `~/Library/Application Support/LM Studio` — 存在（Electron app 数据目录，最后活动 2026-04-21），但对应 server 进程/端口不存在 → 仅为残留安装痕迹。
- `~/.config/LM Studio`、`~/.config/ollama`、`~/.ollama`、`~/Library/Application Support/Ollama` — 均不存在。

## 4. 全量 LISTEN 端口枚举 + 逐个指纹探测

`lsof -nP -iTCP -sTCP:LISTEN` 中候选端口逐一探测：

| 端口 | 进程 | 探测结果 | 判定 |
|---|---|---|---|
| 8787 | node | `/v1/models` → 200 `{"data":[{"id":"qwen3.8-27b","owned_by":"ninfer"}]}` | **Qwen family**（即当前 ANTHROPIC_BASE_URL 代理后端，ninfer） |
| 8648 | node | `/health` → `platform: hermes-agent v0.10.0`，agent gateway/webui | 非模型服务端点 |
| 18787 | node | root → `{"ok":true,"upstream":"https://api.anthropic.com"}`；`/v1/models` → 401 需 x-api-key | Anthropic API 透传代理，上游为 api.anthropic.com（外部服务，非本地模型；是否可用取决于外部 key） |
| 9092 | Python | `/v1/models`、`/`、`/api/tags` 均 404 | 无模型服务指纹 |
| 9111 | python3.1 | `/v1/models`、`/`、`/api/tags` 均 404 | 无模型服务指纹 |
| 其余 (ClashX 7890/9090/7777, grafana 3000, prometheus 9091, ControlCe 5000/7000, Electron 多端口, Microsoft 9222, ARDAgent 3283, Agents 64713, editor_sd 39099, DSH 多端口, Code Helper 65514) | — | 代理/监控/Electron/调试端口，无 LLM 特征，未逐探 | 排除 |

## 5. 剩余未知因素（留待阶段 02 / 用户确认）

1. **外部 API key 可用性**：18787 是 api.anthropic.com 透传代理，若环境中有有效 Anthropic key，理论上可获得非 Qwen 模型，但本探测不验证外部凭据有效性，且项目语境下 judge 应基于本地可控端点。
2. **judge 输出格式兼容性**：即使未来引入非 Qwen 端点，其 judge 评分格式与本 loop 契约的兼容性未验证。

## 6. 如实声明

所有探测均为实际执行；无任何端点被假设或伪造存在。探测失败的端口按失败记录。
