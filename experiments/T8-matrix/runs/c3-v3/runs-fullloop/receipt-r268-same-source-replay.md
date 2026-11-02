# T8-C3-v3-fullloop 同源降级重放 · r268 回执（conf-0.2）

- 生成时间：2026-11-03T~17:00+08:00
- 阶段：pfb loop stage 02.5 降级通道（r266 回执 §4(c)：确认接受同源复判 + 人工抽审，conf-0.2）
- 通道：qwen3.8-27b @ localhost:8787（judge temp 0），J1-strict-v3 / J2-lenient-v3（judge-prompts-rubric-v3.json frozen r249，sha 未变）
- 脚本：`replay-r268-same-source.py`（条目抽取与 replay-rubric-v3.py 同版正则策略；κ 与 G2 机算）
- 数据：`receipt-r268-same-source-replay.json`（18 工件 × 2 判官全量 verdicts + κ rows + G2 表）

## 1. 为什么做这步

异源 judge 端点仍不可用（LM Studio/Ollama 端口 CLOSED、无外部 key，r266 证据链未变）。按 r266 回执 §4(c) 走降级通道：不阻塞推进，先用同源模型把能算的先算掉——双判一致度（κ）和消融区分力（G2 spread）——留一份可对比基线，等异源端点解锁后对同一 18 工件复判逐格对照。

## 2. 读数

### κ（两个裁判去掉瞎蒙后的真实一致度）
- mean κ = **0.441**（17 个可算 cell×stage，n_common≥4）
- 分布：8/17 ≥ 0.6（可用），10/17 < 0.4（分歧大）
- 分歧集中在 **S02（资料搜集）的 J2-lenient**：A-full|D1 0/45、B-none|D1 0/22、B-none|D2 0/9 三个 cell J2 近全零而 J1 正常（0.76–0.82）
- J2 prompt 与 r265 完全相同 → 非 rubric 改动引入；是同一 judge 对同类长工件两次判定不一致，属同源 judge 系统性噪声源之一

### G2（同 domain 内跨 3 config 的分数差，衡量消融是否被量出来）
- 全量条目口径：**10/12 PASS**（r265 冻结 opportunity set 口径 1/12）
- 两个警示，不能解读为「信号被找回」：
  1. D1_S02_J2 的 0.931 spread 由 J2 判分崩塌贡献（A-full/B-none 0.0 vs B-nofreeze 0.931），是噪声不是消融效应
  2. J1 侧 spread 里 B-none 几乎总是最高分（1.0 ×4），方向与「删组件应降质」预期相反——更像条目集大小差异（B-none 工件短、条目少、易全过）而非质量差异
- 口径声明：r265 用冻结 opportunity set（每 stage 5–10 条），本重放用正则全量抽取（9–45 条），两表分数不可直接比较，只作方向性参考

## 3. 结论（标注 conf-0.2 + 同源偏差风险）

- rubric v3 双判在 S02 长工件上不可靠（κ<0.4 占 10/17）→ 修 rubric 或换 judge 之前，S02 的逐条判分不作决策依据
- T8 主结论维持 r265：qwen3.8-27b 生成 + ≤3 structural contracts 下，消融效应未被可靠测出
- 异源 judge 解锁后的验证路径已固化：同一 18 工件复判 → 与本回执逐格对比；若届时 S02 J2 崩塌消失且 G2 仍弱 → 收口证据链闭合

## 4. 仍卡人项（不变）

- web-llm 登录（runtime 门禁 ≥2 successful_provider_ids）：`cd pfb && ralph web-llm-login`
- 异源 judge 三选一：(a) 非 Qwen API key / (b) LM Studio+非 Qwen 模型 / (c) 确认按现有证据收口 T8
- erratum-27 / G1b family_check / R121