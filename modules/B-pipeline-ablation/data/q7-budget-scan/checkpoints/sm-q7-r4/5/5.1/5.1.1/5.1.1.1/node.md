# N229: NVMe SSD 运维人力成本的工作点 A（高自动化/低人工）：采用全栈自动化存储平台（如 Ceph/MinIO + Ansible），FTE 需求降至 0.2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

NVMe SSD 运维人力成本的工作点 A（高自动化/低人工）：采用全栈自动化存储平台（如 Ceph/MinIO + Ansible），FTE 需求降至 0.2，C_ops = 0.2 × ¥200,000 = ¥40,000/年；此工作点隐含软件许可或开发成本 ¥30,000/年，总运维相关支出 ¥70,000/年。

## Corrected Claim

NVMe SSD 运维人力成本的工作点 A（高自动化/低人工）：采用全栈自动化存储平台（如 Ceph/MinIO + Ansible），FTE 需求降至 0.2，C_ops = 0.2 × ¥200,000 = ¥40,000/年；此工作点隐含软件许可或开发成本 ¥30,000/年，总运维相关支出 ¥70,000/年。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.2*200k=40k, 40k+30k=70k），且符合全栈自动化降低人力成本的工程常识。

## Search Query

ceph minio automated storage operations cost fte
