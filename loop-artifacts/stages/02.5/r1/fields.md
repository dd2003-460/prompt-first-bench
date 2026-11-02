# 02.5 阶段字段快照

> 由 `ralph render` 自动从 `loop-artifacts/stages/02.5/r1/fields.json` 生成，请勿手改。

> 生成时间：2026-11-03 06:32

## 概览

- 字段总数：**14**
- 待办（pending / research_required）：**2**
- 分组：background×1、output×4、input×9

## 字段明细

### background

| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |
|---|---|---|---|---|---|
| 用户原始任务 | 任务描述 | confirmed | 1.00 | material | 否 |

### output

| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |
|---|---|---|---|---|---|
| goal | decision_object | confirmed |  |  |  |
| research_findings | non_qwen_judge_availability | confirmed | 0.90 | material | 是 |
| non_qwen_judge_availability | research_findings | confirmed | 0.90 | material | 是 |
| local_dual_channel_verification | non_qwen_judge_availability | confirmed | 0.90 | material | 是 |

### input

| 要素 (concept) | 属性 | 状态 | 置信度 | 影响 | 可逆 |
|---|---|---|---|---|---|
| known | background_facts | confirmed | 0.90 | material | 是 |
| unknown | open_questions | confirmed | 0.85 |  |  |
| research_findings: local_non_qwen_endpoints | local_endpoint_probe | confirmed | 0.90 | material | 是 |
| research_findings: external_non_qwen_api_keys | external_api_credentials | assumed_default | 0.80 | material | 是 |
| research_findings: judge_output_format_compatibility | judge_format_compatibility | research_required | 0.40 | material | 是 |
| local_artifact_inventory | background_facts | research_required | 0.90 | material | 是 |
| internal_known_background | local_artifact_inventory | confirmed | 0.90 | material | 是 |
| research_findings: non_qwen_judge_availability | non_qwen_judge_availability | confirmed | 0.90 | material | 是 |
| known_local_artifact_inventory | background_facts | confirmed | 0.90 | material | 是 |

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

已知因素（全部为本地仓库工件事实，非外部 web 事实；Commander 于 2026-11-03 直接 Read 核验）：(1) pilot 6 cells（A-full/B-nofreeze/B-none × D2-file-collab）stage01/02/03 工件共 18 份已存在且完整——receipt-r265-pilot-v2.json cells_completed 列出 6 个 cell 均 status:complete，cells_pending 为空；(2) r265 同源 judge（qwen3.8-27b，与生成器同 family）已完成 J1+J2 双判并产出 receipt-r265-pilot-v2.json；(3) G2 区分力（同 domain 跨 config spread）r265 结果为 1/12 PASS，结论为消融信号 < 测量噪声；(4) 评分协议固定为 J1-strict-v3 + J2-lenient-v3（judge-prompts-rubric-v3.json），计分规则为 m8fixed-protocol-v1.json；(5) 本会话模型 qwen3.8-27b 属 Qwen family，不可作为异源 judge 使用。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json

### unknown

阶段 02 调研闭环（r266）：三项未知因素全部带回证据。(1) local_non_qwen_endpoints——实际探测完成，确认本机不存在非 Qwen 可调用端点（evidence: loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md；LM Studio :1234 / Ollama :11434 CLOSED，唯一 LLM 端点 127.0.0.1:8787 仅服务 qwen3.8-27b）。(2) external_non_qwen_api_keys——环境变量与 shell rc 中无任何非 Qwen provider 凭据，免费额度渠道在无凭据下不可验证；按任务书失败降级条款处置为 blocked_human（需用户提供 key 或确认替代方案），不阻塞其他任务。(3) judge_output_format_compatibility——无可用异源端点则无法实测，属依赖项(2)解锁后的后续验证，不构成阶段 02 的独立未闭环缺口。结论：所有可由 Commander 单方面调研的字段均已带回 evidence_refs；剩余唯一缺口为外部凭据，走 blocked_human 通道。（本地探测完整命令与输出见仓库内 loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md）

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json

### research_findings: local_non_qwen_endpoints

本地非 Qwen 端点探测（r266 实证）：LM Studio :1234 与 Ollama :11434 端口均 CLOSED；全量 LISTEN 端口枚举后唯一 LLM 推理端点 127.0.0.1:8787（node/ninfer）仅服务 qwen3.8-27b（Qwen family）。结论：本机不存在可用的非 Qwen family 可调用端点。完整命令与输出见 evidence/unknown-local-probe-r266.md。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md

### research_findings: external_non_qwen_api_keys

外部非 Qwen API key 调研结论：环境变量与 shell rc 中不存在 OpenAI/OpenRouter/Gemini/Mistral/Cohere/DeepSeek 等任何指向其他 provider 的凭据（r266 探测确认）；免费额度渠道在无凭据情况下无法验证。默认假设：无可用外部 key → 按任务书失败降级条款标记 blocked_human（需用户提供 key 或确认替代方案），不阻塞其他任务。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md

### research_findings: judge_output_format_compatibility

所选异源 judge 对 J1/J2 prompt 的输出格式兼容性与解析失败率：属未验证事实，保留 research_required。当前无法闭环的原因：依赖外部非 Qwen 端点（external_api_credentials 已按任务书降级条款走 blocked_human 通道）。处置：不伪造结论；该字段随用户 key 到位后由阶段 02.5/04 实测回填（J1-strict-v3/J2-lenient-v3 要求 JSON 输出，主流模型预期可满足，实际解析失败率以实测为准，若 >20% 按任务书条款记录为技术故障）。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md

### research_findings

阶段 02 required_output 汇总：本机不存在可用的非 Qwen family 可调用模型端点（本地探测 r266 实证）；外部环境变量中不存在任何非 Qwen provider API key；因此异源 judge 验证在现有资源下不可执行，按任务书【失败降级】条款标记 blocked_human（需要用户提供非 Qwen key 或确认使用其他本地模型），不阻塞其他任务。若用户提供 key，验收标准 1-5 可按原协议继续执行。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md

### local_artifact_inventory

已知因素（全部为本地仓库工件事实，非外部 web 事实；Commander 于 2026-11-03 直接 Read 核验）：(1) pilot 6 cells（A-full/B-nofreeze/B-none × D2-file-collab）stage01/02/03 工件共 18 份已存在且完整——receipt-r265-pilot-v2.json cells_completed 列出 6 个 cell 均 status:complete，cells_pending 为空；(2) r265 同源 judge（qwen3.8-27b，与生成器同 family）已完成 J1+J2 双判并产出 receipt-r265-pilot-v2.json；(3) G2 区分力（同 domain 跨 config spread）r265 结果为 1/12 PASS，结论为消融信号 < 测量噪声；(4) 评分协议固定为 J1-strict-v3 + J2-lenient-v3（judge-prompts-rubric-v3.json），计分规则为 m8fixed-protocol-v1.json；(5) 当前会话模型 qwen3.8-27b 属 Qwen family，不可作为异源 judge 使用。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/pilot/A-full/D2-file-collab/stage01.md

### non_qwen_judge_availability

调研结论汇总：本机不存在可用的非 Qwen family 可调用模型端点（本地探测 r266 实证）；外部环境变量中不存在任何非 Qwen provider API key；因此异源 judge 验证在现有资源下不可执行，按任务书【失败降级】条款标记 blocked_human（需要用户提供非 Qwen key 或确认使用其他本地模型），不阻塞其他任务。若用户提供 key，验收标准 1-5 可按原协议继续执行。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md
- loop-state.json

### internal_known_background

已知因素（全部为本地仓库工件事实，非外部 web 事实；Commander 于 2026-11-03 直接 Read 核验）：(1) pilot 6 cells（A-full/B-nofreeze/B-none × D2-file-collab）stage01/02/03 工件共 18 份已存在且完整——receipt-r265-pilot-v2.json cells_completed 列出 6 个 cell 均 status:complete，cells_pending 为空；(2) r265 同源 judge（qwen3.8-27b，与生成器同 family）已完成 J1+J2 双判并产出 receipt-r265-pilot-v2.json；(3) G2 区分力（同 domain 跨 config spread）r265 结果为 1/12 PASS，结论为消融信号 < 测量噪声；(4) 评分协议固定为 J1-strict-v3 + J2-lenient-v3（judge-prompts-rubric-v3.json），计分规则为 m8fixed-protocol-v1.json；(5) 当前会话模型 qwen3.8-27b 属 Qwen family，不可作为异源 judge 使用。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json

### research_findings: non_qwen_judge_availability

阶段 02 required_output 汇总：本机不存在可用的非 Qwen family 可调用模型端点（本地探测 r266 实证）；外部环境变量中不存在任何非 Qwen provider API key；因此异源 judge 验证在现有资源下不可执行，按任务书【失败降级】条款标记 blocked_human（需要用户提供非 Qwen key 或确认使用其他本地模型），不阻塞其他任务。若用户提供 key，验收标准 1-5 可按原协议继续执行。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json
- loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md

### known_local_artifact_inventory

已知因素（全部为本地仓库工件事实，非外部 web 事实；Commander 于 2026-11-03 直接 Read 核验）：(1) pilot 6 cells（A-full/B-nofreeze/B-none × D2-file-collab）stage01/02/03 工件共 18 份已存在且完整——receipt-r265-pilot-v2.json cells_completed 列出 6 个 cell 均 status:complete，cells_pending 为空；(2) r265 同源 judge（qwen3.8-27b，与生成器同 family）已完成 J1+J2 双判并产出 receipt-r265-pilot-v2.json；(3) G2 区分力（同 domain 跨 config spread）r265 结果为 1/12 PASS，结论为消融信号 < 测量噪声；(4) 评分协议固定为 J1-strict-v3 + J2-lenient-v3（judge-prompts-rubric-v3.json），计分规则为 m8fixed-protocol-v1.json；(5) 本会话模型 qwen3.8-27b 属 Qwen family，不可作为异源 judge 使用。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/judge-prompts-rubric-v3.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/calibration/m8fixed-protocol-v1.json
- https://github.com/dd2003-460/prompt-first-bench/blob/main/experiments/T8-matrix/runs/c3-v3/runs-fullloop/receipt-r265-pilot-v2.json

### local_dual_channel_verification

阶段 02 核心 claim 已完成本地双通道独立验证：TCP 端口探测（1234/11434 refused，8787 仅 qwen3.8-27b）与进程环境变量枚举（无外部 provider key）两通道方法学独立、结论一致、无矛盾。web-llm 外源核验不可用（3 providers 登录失败），该 claim 属本地环境事实，本地探测即权威来源。

证据：
- https://github.com/dd2003-460/prompt-first-bench/blob/main/loop-artifacts/stages/01/r1/evidence/unknown-local-probe-r266.md
