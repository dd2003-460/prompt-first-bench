# T23 Hetero-Judge — 通道阻塞状态 & 恢复方案

> origin: ai · 2026-11-05 · Lead 记录
> 任务书：`tasks/T23-stage-ablation-hetero-judge-task.md`
> 工件数据：`runs/*.json`（18 份，已在 arena/4a614e63-prompt-first-bench @ 9744b36）

## 阻塞原因（2026-11-05 确认）

| 通道 | 状态 | 根因 |
|------|------|------|
| Arena agent mode | ❌ reCAPTCHA Enterprise 持续触发 | IP/会话级限制，bframe 在 y=-9999 隐藏，send button disabled。短消息(1KB)也触发。 |
| 本地 GLM-4.7-Flash (智谱) | ❌ 推理死循环 | 纯推理模型，简单事实核查烧完 2000 token 仍在打转，content 永远为空 |
| 本地 Qwen2.5-7B | ⚠️ 可用但同族 | 能输出 JSON，但和被评模型同属 Qwen 系，异源性不足（conf 上限应降 0.5） |
| 外部 API (OpenAI/Anthropic/Gemini/DeepSeek) | ❌ 无 key | 本机无任何外部 LLM API 凭证 |

## 恢复路径（按优先级）

### P0: 提供外部 API key（最快，~30min）
任一 OpenAI/Anthropic/Gemini/DeepSeek key 即可。执行方式：
```python
# 用 openai-compatible API 逐批判分
# 18 工件 × 6 维 = 108 判定
# 每批 3 工件 + 对应 gold，控制 prompt < 8K tokens
# 温度 0，max_tokens 2000
# 产出 hetero-scores-blind.jsonl → 对照 scoring.md → 出 analysis
```

### P1: Arena reCAPTCHA 冷却后重试（不确定时间，预计 1h+）
- 等 reCAPTCHA 消失后，分小批（每批 ≤2KB）喂数据
- Agent Mode 无文件写入能力，需在回复中直接输出 JSONL
- 风险：agent context window 可能装不下 18 工件全文（~195KB），需分批判分再汇总
- 预计 3-4h（含等待）

### P2: 降级 Qwen2.5-7B 半异源（立即可做，~20min）
- LM Studio 端口 1234，model=qwen2.5-7b-original
- 局限：同族（Qwen），不同代际/规模。conf 上限 0.5，标注 "semi-hetero"
- 价值：验证同源 27b judge 的 per-dimension 方向是否稳健（即使 conf 低）
- 执行：直接调 /v1/chat/completions，temperature=0

### P3: 暂缓 T23
- 同源结果已完整（scoring.md, 90 runs, conf cap 0.7）
- 核心结论（S1 分解正贡献 +0.089, S2 调研最大增益 +0.072, S3 规划负效应 -0.046）在 conf 0.7 下已可引用
- 异源 judge 是 conf 升档路径，不是结论成立的前提

## 工件清单（18 份）

| 组 | 文件 | 用途 |
|----|------|------|
| A | S0-Q1-r1/r2, S1-Q1-r1/r2, S2-Q1-r1/r2 | H1/H2 主战场 |
| B | S1-Q3-r1, S2-Q3-r1, S1-Q4-r1, S2-Q4-r1 | 跨域确认 |
| C | S2-Q2-r1, S3-Q2-r1, S2-Q5-r1, S3-Q5-r1 | H3 负效应 |
| D | S4-Q1-r1, S5-Q1-r1 | H4 终审 |
| E | D1-Q1, D1-Q4 | 外部基线 M4 短板 |

Gold: `gold/Q{1..5}.md`

## 评分规则摘要

M1 事实准确率 / M2 无来源数字率(反向) / M3 矛盾对数(反向) / M4 缺口标注覆盖率 / M5 坏消息位置(反向) / M6 调研真实性
权重: M1:0.25 M2:0.20 M3:0.15 M4:0.20 M5:0.10 M6:0.10
