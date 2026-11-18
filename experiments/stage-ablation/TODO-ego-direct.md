# ego-direct 一次修好（2026-11-18）

背景：D 问"返回和 claim 不一样，AI 能不能自己换 query / 去权威网站查"。
已实现 `_generate_new_query`（换 query 重试）+ `_ego_direct_fetch`（LLM 选权威站直接访问）。
wiki 全文通道完美（84041 字符，r5 里 7 节点 evidence 含 wiki 特征，verify 正确质询"来源是否直接支持该数值"）。
techpowerup 浏览器通道有 2 个 bug，本次一次修好。

## 诊断（2026-11-18 实测）
- 访问 techpowerup 具体 GPU 页：bodyLen=13443，tableCount=3，title 正确 → 规格表在 table 里
- 但代码通道 A 访问的是 `https://{dom}` **根路径**（首页），首页没 GPU 规格表
- 提取用 innerText 取最长容器：body 最长但前 3000 字全是导航+论坛帖，规格 table 在后面被截断丢掉
- LLM 编 URL 有重定向风险（rtx-5090.c3944 → 实际 4070 Mobile）

## Todo
1. [修] 浏览器提取策略：table 优先（规格数据在 table，innerText 被导航污染）
2. [修] LLM 给 specific_urls（确定的具体页），浏览器优先访问，否则根路径兜底
3. [验证] techpowerup 能提取到 GPU 规格（CUDA cores / memory / TDP）
4. [确认] wiki 主力通道稳定（已工作，不重跑）
5. [等] verify-only 跑完（9/118 后台）看最终 cov/depth

## 固有限制（诚实标注，不硬修）
- LLM 编 URL 重定向风险：verify 层"不相关"判定兜底（已验证 N289 正确降级）
- 8787 后端 502 过载：非我管辖（MEMORY: 别动推理引擎），watchdog 自动恢复
- 站内搜索导航到具体页：DOM 选择器站点特定、易脆，性价比低，不做
