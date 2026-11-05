# 01 阶段字段快照

> 由 `ralph render` 自动从 `loop-artifacts/stages/01/r1/tasks/01-r1-field-unknown-b23a6a8439.json` 生成，请勿手改。

> 生成时间：2026-11-03 06:04

## 概览

- 字段总数：**4**
- 待办（pending / research_required）：**1**
- 分组：background×1、output×1、input×2

## 字段明细

### background

| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |
|---|---|---|---|---|---|
| 用户原始任务 | 任务描述 | confirmed | 1.00 | material | 否 |

### output

| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |
|---|---|---|---|---|---|
| goal | decision_object | confirmed |  |  |  |

### input

| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |
|---|---|---|---|---|---|
| known | background_facts | confirmed |  |  |  |
| unknown | open_questions | research_required | 0.50 |  |  |

## 证据与备注

### 用户原始任务

用户初始任务输入，作为本阶段已知背景字段。

证据：
- user:initial_task

### goal

T8-C3-v3-fullloop 异源 judge 验证：用非 Qwen family 的 LLM 作为 judge，重新评分 pilot 6 cells 的 stage01/02/03 工件（18 份），检验消融信号是否被同源偏差淹没。验收标准：(1) 找到至少 1 个可用非 Qwen judge 端点；(2) 完成 6 cells × 3 stages 的 J1+J2 双判；(3) 计算 G2 区分力并与 r265 同源结果对比；(4) 输出 receipt-r266-hetero-judge.json；(5) 若异源确认信号仍弱则 T8 收口，若信号出现则启动 54-cell 全量。失败降级：无可用非 Qwen 端点则 blocked_human；本地有其他非 Qwen 模型则直接用 conf-0.3；judge 解析失败率大于 20% 则记录技术故障。

证据：
- experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json
- experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json
- experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json

### known

已知因素：(1) pilot 6 cells（A-full/B-nofreeze/B-none × D2-file-collab）stage01/02/03 工件共 18 份已存在且完整；(2) r265 同源 judge（qwen3.8-27b，与生成器同 family）已完成 J1+J2 双判并产出 receipt-r265-pilot-v2.json；(3) G2 区分力（同 domain 跨 config spread）r265 结果为 1/12 PASS，结论为消融信号 < 测量噪声；(4) 评分协议固定为 J1-strict-v3 + J2-lenient-v3（judge-prompts-rubric-v3.json），计分规则为 m8fixed-protocol-v1.json；(5) 当前会话模型 qwen3.8-27b 属 Qwen family，不可作为异源 judge 使用。

证据：
- experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json
- experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json
- experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json

### unknown

本地探测已完成（r266, 2026-11-03）：未发现任何可用的非 Qwen family 可调用模型端点。LM Studio(:1234) 与 Ollama(:11434) 端口均无监听（curl exit=7 / nc CLOSED）；全量 LISTEN 端口枚举后逐个指纹探测，本机唯一 LLM 推理端点为 127.0.0.1:8787（node/ninfer），仅服务 qwen3.8-27b（即当前 ANTHROPIC_BASE_URL 后端）；18787 为 api.anthropic.com 透传代理（依赖外部凭据，未验证）。完整命令与输出见 evidence/unknown-local-probe-r266.md。剩余两项未知因素留待阶段 02/用户确认：(1) 外部 API key 可用性（Anthropic/OpenAI/Gemini 等非 Qwen 凭据，需用户提供或确认替代方案）；(2) 所选异源 judge 对 J1/J2 prompt 的输出格式兼容性与解析失败率（仅实际调用后可知）。

证据：
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md
