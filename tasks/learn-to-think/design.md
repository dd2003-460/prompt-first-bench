# learn-to-think 02-design 改动设计

# origin: ai · 2026-11-25 09:50 · stage-gate 02-design 门禁产出
# 性质：本 goal 是实验型（prompt/hook 干预 27b，不改 SM/框架源码），"改动项"= 实验协议三件套
# 原则：最小改动+可回滚——所有改动在 pfb 仓库内，git revert 可回滚，无不可逆项

## 改动项表

| # | 改动项 | 目标文件 | 改动描述 | 回滚方式 | 验证方法（前后对照） |
|---|---|---|---|---|---|
| 1 | 臂C 预注册协议 | tasks/learn-to-think/exp03-armc-prereg-20261125.md | 三臂条件（A/B 复用 T2 数据 + C 新跑 3 次）、采样参数（temp 0.7/max 1024，与 T2 一致保可比）、四维判据（爬层/预言力/边界/flip）、H1 可证伪假设、失败降级 | git revert 该文件（commit 5e6294aba 首预注册 + b02786033 补降级节） | 预注册红线：文件 commit 时间戳早于任何臂C 数据产出（git log 对照）；判据与 T2 preregistration.md 逐条 diff 一致（不重抄，引用） |
| 2 | 臂C runner | tasks/learn-to-think/exp03-armc/run_armc.py | 3 次独立采样调用 8787（qwen3.8-27b-mtp），原始输出落盘 exp03-armc/raw_outputs.json，格式同 T2 | git revert（commit 44350b270） | dry-run 验证过（零 LLM 调用，commit 44350b270 记录）；正式跑时对照 prereg 采样参数逐字段一致（model/temp/max_tokens/指令逐字） |
| 3 | 04-eval 评分协议 | tasks/learn-to-think/lossless-criterion-operationalization.md | 三维=(压缩比, ε_rep[=align], ε_pred)；ε_pred=held-out 预言命中率（N=3 起步，命中 1 即过）；结构对齐=信息流角色非逐字 | git revert（04:45 commit） | 与 04-eval 现有 form/align 维度的关系节（L60-65）：form 降为 ε_rep 廉价代理，不新增平铺维度；待核验节 3 条（标注者一致性 κ≥0.7 / N 取值 / token vs 字符）留作 03 实验内自证 |
| 4 | 05-generalize 接口预留 | tasks/learn-to-think/decomposition.md 05 节 | 03 出结果后的泛化判据：域锚点是否可迁移到其他 D 机制域（缺口 #4 跨域迁移条件） | git revert | 03 的 flip 命中率按域分组（本实验单域 loss-landscape；迁移=换域重跑臂C 指令模板，判据不变） |

## 正交性自检（逐对）

- 1×2：协议（判什么）vs 执行（怎么跑）——正交
- 1×3：实验判据（四维，臂间比较）vs 评估协议（三元组，理解度度量）——正交：四维管"H1 是否成立"，三元组管"27b 理解质量"，前者是干预效果、后者是能力度量
- 2×3：runner 只产出原始数据，评分独立后置——正交
- 3×4：评估协议（单域内）vs 泛化接口（跨域）——正交
- 1×4 / 2×4：协议/runner 不含跨域逻辑，泛化是 03 之后的独立步骤——正交

## 验证矩阵

| 验证点 | 方法 | 状态 |
|---|---|---|
| 预注册先于数据 | git log 时间戳对照（5e6294aba 05:19 < 任何臂C 数据） | ✅ 已核（数据未跑） |
| runner 参数与 prereg 一致 | dry-run 打印参数逐字段 diff | ✅ 已核（44350b270） |
| 判据与 T2 同源 | 判据 1-3 引用 T2 preregistration.md 原文，不重抄 | ✅ 已核（prereg L39-40） |
| gold 隔离 | 臂C 指令文本 grep 无 D 后半段关键词（landscape/非凸/先验信息量） | 待跑前核（runner 指令逐字=prereg L28，已目检无泄露） |
| 评估维度不新增平铺 | 04-eval 三维由 lossless-criterion 导出（form→ε_rep 代理），非并列新增 | ✅ 已核（lossless L60-65） |

## 不可逆项检查

无。全部改动在 pfb 工作区内（git 管理），无对外/花钱/删工作区外/改框架源码。s5_state_machine.py 冻结期（pilot 在跑）本 goal 不触碰。
