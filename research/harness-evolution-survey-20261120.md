# Harness 进化与记忆召回调研（2026-11-20）

> origin: ai · 2026-11-20 · 触发：D 问"hermes 的进化/其他进化，recall 是最大问题，装 mem0 会好吗"
> 范围：两条线——① 记忆/召回（对应 recall 痛点）② 自我改进机制（对应"进化"）。
> 方法：local-first 检查（本地 lit-survey 为空、pfb/research 无覆盖）→ arXiv 官方页 web_extract 查证。
> 置信度：所有 arXiv ID/摘要/数字来自 arxiv.org 官方页（单源，本轮工具输出 = 来源①），
> 论文自报数字未经独立复现，交叉验证待做（标 [待交叉验证]）。

## §1 核心论文（6 篇，全部已查证 arXiv 官方页）

### 记忆/召回线

**1. Mem0** — arXiv:2504.19413（2025-04-28，Chhikara et al.）
生产级可扩展长期记忆。机制：动态提取→整合→检索对话中的关键信息；增强版用图记忆表示关系结构。
关键数字 [待交叉验证]：LOCOMO 基准四类问题（single-hop/temporal/multi-hop/open-domain）全胜 6 类 baseline；
LLM-as-a-Judge 比 OpenAI 高 26% 相对提升；p95 延迟比 full-context 低 91%；token 成本省 90%+。
开源：github.com/mem0ai/mem0

**2. MemGPT / Letta** — arXiv:2310.08560（2023-10-12，Packer et al.，UC Berkeley）
"LLM 即操作系统"：虚拟上下文管理，借鉴 OS 分层内存（快/慢存储间数据搬运）在有限窗口内提供扩展上下文；
interrupt 机制管理控制流。两个域：文档分析（超窗口大文档）+ 多会话聊天（跨长期交互记忆/反思/演化）。
开源：research.memgpt.ai（现 Letta）

**3. Reflexion** — arXiv:2303.11366（2023-03-20，Shinn et al.）
语言反馈强化：不改权重，agent 对任务反馈做语言化反思，存 episodic memory buffer 改进后续 trial。
关键数字 [待交叉验证]：HumanEval pass@1 91%（超 GPT-4 baseline 80%）。
与我们的关系：memory 分类（decision/approach/result/reflection）+ skill_manage 机制与之同构。

**4. Voyager** — arXiv:2305.16291（2023-05-25，Wang et al.，NVIDIA）
Minecraft 终身学习 agent，三组件：① 自动课程（最大化探索）② 持续增长的技能库（可执行代码存复杂行为，
检索复用）③ 迭代 prompting（环境反馈+执行错误+自验证改进程序）。
关键数字 [待交叉验证]：3.3x 独特物品、2.3x 距离、科技树里程碑快 15.3x；技能库可迁移新世界。
开源：voyager.minedojo.org

### 自我改进线

**5. Darwin Gödel Machine (DGM)** — arXiv:2505.22954（2025-05-29，v3 2026-03-12，Zhang/Clune et al.，UBC）
自我改进系统：迭代修改自身代码（含改进"修改自身代码的能力"），用 coding benchmark 实证验证每次改动。
机制：维护 agent 档案（archive），采样→foundation model 生成新变体→benchmark 验证→入档（Darwin 式开放探索）。
关键数字 [待交叉验证]：SWE-bench 20.0%→50.0%，Polyglot 14.2%→30.7%；自动发现改进
（更好的代码编辑工具、长上下文管理、peer-review 机制）。
开源：github.com/jennyzzt/dgm

**6. Agent 架构综述** — arXiv:2404.11584（2024-04-17，Masterman et al.）
单/多 agent 架构设计模式：规划/执行/反思阶段、leadership、通信风格。13 页 38 引，入门级。

## §2 与我们痛点的映射

| 痛点 | 对应机制 | 判断 |
|------|---------|------|
| recall：事实/状态召不回 | Mem0 提取-整合-检索管道 + 图记忆 | 对"离散事实"有效；对"抽象准则"无效（embedding 相似度≠相关性，准则无语义锚点） |
| recall：准则靠 hook always 注入会退化 | MemGPT 自主换页（模型自己决定加载什么） | 我们靠 hook 触发注入，缺"模型自主决定加载"这层；方向可借鉴 |
| 进化：自己优化+subagent 测试 | DGM archive+变异+benchmark 验证 | 机制直接对应，但成本重（每个变体跑完整 benchmark）；27b+pfb bench 可跑小规模版 |
| 进化：经验教训固化 | Reflexion 语言反思 + Voyager 技能库 | 我们已有同构物（memory 分类 + skill_manage）；Voyager 技能是可执行代码，可验证性比 markdown 规则强 |

## §3 关键判断（conf 0.8）

1. **装 Mem0 解决一半**：事实类记忆（"soc gate 之前多少"）改善明显；抽象准则（"先调研复用"）
   不解决——准则不是事实，召回不了，得内化成默认行为（persona 层）。
2. **DGM 式自进化太重，机制可小规模借鉴**：archive+benchmark 验证对应"自己优化+subagent 测试"，
   但完整 DGM 每个变体跑完整 SWE-bench 级 benchmark，我们跑不起；
   可借鉴的最小版：prompt/规则改动 → pfb bench 验证 → 改动入 archive（对应 unattended-longrun-framework 的验收器）。
3. **真正缺口在召回侧**：
   - 事实召回：装 Mem0（或先试 Letta，MemGPT 是它的学术前身，工程更成熟）
   - 准则内化：改 persona（调研复用/全局视角写进 persona 不靠注入）
   - 自主换页：让模型自己决定加载什么规则，而不是 hook 关键词触发（MemGPT 思路）

## §4 待办

- [ ] Mem0 LOCOMO 数字交叉验证（ego-browser 问 ≥2 个 LLM：LOCOMO 上 Mem0 vs OpenAI 的 26% 是否被独立复现/质疑）
- [ ] 决定装 Mem0 还是 Letta（Letta 更成熟但重；Mem0 轻但新）
- [ ] DGM 小规模版可行性：pfb bench 能否当"benchmark 验证"用（成本估算）
- [ ] 本调研与 unattended-longrun-framework.md（archived）合并：验收器组件 = DGM 最小版
