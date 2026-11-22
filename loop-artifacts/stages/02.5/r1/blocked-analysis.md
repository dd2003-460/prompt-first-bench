# 02.5 阻塞分析（自指 claim 死锁）

> origin: ai | 2026-11-20 | pfb 02.5 阶段 | D 数字分身推进记录

## 现状

pfb 卡在 02.5（调研后交叉验证）。实质核验已完成，但机器门禁（`ralph field-apply`）
要求"必须引用 `ralph web-llm-check` 产生的成功回执（≥2 successful_provider_ids）"，
而 ralph 的独立 browser-profile 未登录 → 回执 0 成功 → field-apply 拒绝 → 无法 advance 到 03。

## 死锁结构（自指 claim）

1. 02 阶段的核心 claim：**本机无非 Qwen LLM 端点，异源 judge 不可行**
2. 02.5 要交叉验证这个 claim
3. ralph field-apply 硬门禁：cross_validation 字段必须引用 `ralph web-llm-check` 的成功回执（≥2 provider）
4. `ralph web-llm-check` 用**独立 browser-profile**（`~/.local/share/ralph-runtime/browser-profile/`，
   隐私设计，不复用用户浏览器登录态）→ 该 profile 里 perplexity/chatgpt 无登录态 → 3/3 error
5. 我用 ego-browser（复用 D 的 ego-lite 登录态）已拿到 2 个独立 LLM 一致核验（perplexity + chatgpt），
   但门禁只认 ralph 自己 profile 跑的回执，不认 ego-browser 通道

→ claim 说"异源不可用"，门禁却要求"异源回执"，形成死锁。

## 已完成的实质核验（证据充分，只是门禁不认）

- **本地双通道**（独立方法学）：TCP 端口探测（1234/11434 refused，8787 仅 qwen3.8-27b）
  + process/env 枚举（无外部 provider key）。两通道一致。
- **ego-browser 2 个独立 web-LLM**（2026-11-20，D 登录态）：
  - Perplexity：结论基本成立但"不可行"过强；给出 macOS 未列途径（llama.cpp:8080/9931、vLLM:8000、
    MLX:8080、Jan:1337、GPT4All:4891 等）+ 同源 judge 7 项缓解。
  - ChatGPT：逐条评级一致（env 无 key=证据不足，未覆盖 Keychain/配置/CLI 登录/代理）；
    建议状态标 `heterogeneous_judge: unavailable (verified endpoints only)` 而非 `impossible`。
  - 裁决：事实部分（已探测端点/已加载模型/env 无 key）三源一致成立；绝对化结论降级为限定表述。
    confidence 0.9 维持。
- 证据已写入：`advance.json`（cross_validation payload，含 3 个 validated_field + 矛盾记录）
  + `fields.json`（cross_validation 字段，含 validation_records）。

## 解除死锁的唯一人工步骤（只有 D 能做）

ralph 的 browser-profile 登录一次，之后所有项目复用。正确序列（decomp TASKS.md 2026-09-23 记过同一阻塞；
命令签名 2026-11-20 用 `ralph web-llm-* --help` 核实）：

```bash
# 1. 逐 provider 打开可见浏览器（ralph 的独立 profile），在弹出的窗口里手动登录
ralph web-llm-login perplexity
ralph web-llm-login chatgpt
# 2. 授权 + 校验
ralph web-llm-authorize . --providers perplexity chatgpt
ralph web-llm-check . loop-artifacts/stages/02.5/r1/webllm-request.json
```

登录态持久化到 `~/.local/share/ralph-runtime/browser-profile/`。

**杠杆：一次登录同时解锁两个项目** —— pfb（02.5 交叉验证）+ decomp（T-webllm-login-blocker，
decomp/tasks/TASKS.md 2026-09-23 已记同一阻塞，根因相同：ralph 独立 profile 未登录）。

## D 登录完成后，我自动执行（无需再指令）

1. `ralph web-llm-check . loop-artifacts/stages/02.5/r1/webllm-request.json` → 生成成功回执
2. `ralph field-apply . loop-artifacts/stages/02.5/r1/fields.json` → cross_validation 字段过门禁
3. `ralph apply . loop-artifacts/stages/02.5/r1/advance.json` → 推进到 03
4. pfb 解锁 → G1（"激发煮东西"调研）触发条件满足，建 goal 推进

## 不改代码的替代（若 D 不想登录）

改 ralph_runtime 门禁，允许"本地双通道 + ego-browser 独立 LLM"作为 02.5 的等价证据。
但这动框架源码（`loop/ralph_runtime/ralph_runtime/web_llm.py` 的 field-apply 校验），
需 D 明令（红线：改框架源码）。不推荐——登录一次更干净，且符合 ralph 的隐私设计意图。

## 边界说明

- 这不是"等数据"阻塞，是"门禁机制对自指 claim 无解 + ralph profile 需登录"的程序性阻塞。
- 实质核验已完成，不是空等。登录是唯一的外部依赖（账号凭证，红线：我不能猜/代输）。
