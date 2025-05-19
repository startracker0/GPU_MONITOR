# GPU_MONITOR
A lightweight script for `GPU monitoring`. Automatically emails the user when VRAM usage drops below a specified threshold and then exits the script.  

一个轻量级 `GPU 监控`脚本，当显存使用情况低于预设阈值时将会自动发送邮件至指定邮箱，并退出脚本。

This script is mainly used to check whether the `training is completed` and whether `the GPUs are idle`.

本脚本主要用于查看`训练是否完成/显卡是否闲置`。


## 1. GPU 监控设置(GPU Monitoring Settings)
- 本脚本支持通过 `gpu_id` 监控指定GPU显存
- This script supports monitoring a specified GPU via `GPU ID`
  
https://github.com/startracker0/GPU_MONITOR/blob/7b2ce5dc82628e60fe8c771739732847fe5a75dd/monitor.py#L129-L132

---

## 2. 邮箱服务器配置(Email Server Configuration)

- 默认使用QQ邮箱，更换邮箱需修改 `smtp_server` 和 `smtp_port`
- Default QQ Mail. For other providers, update `smtp_server` & `smtp_port`

https://github.com/startracker0/GPU_MONITOR/blob/5c82370c6a80983f0fc4472eae3e13820bfee080/monitor.py#L8-L12


---

## 3. 安全密码获取(Secure Password Acquisition)
- 必须使用**邮箱安全密码**（非登录密码）
- Use **application-specific password** (NOT login password)

[Reference Blog](https://blog.csdn.net/qq_42076902/article/details/131900459)

