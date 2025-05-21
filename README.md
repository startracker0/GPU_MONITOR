# GPU_MONITOR
A lightweight script for `GPU monitoring`. Automatically emails the user when VRAM usage drops below a specified threshold and then exits the script.  

一个轻量级 `GPU 监控`脚本，当显存使用情况低于预设阈值时将会自动发送邮件至指定邮箱，并退出脚本。

This script is mainly used to check whether the `training is completed` and whether `the GPUs are idle`.

本脚本主要用于查看`训练是否完成/显卡是否闲置`。


## 1. GPU 监控设置(GPU Monitoring Settings)
- 本脚本支持通过 `gpu_id` 监控指定GPU显，`threshold`是预设的显存阈值，默认为10MiB，`check_interval`为检测时间间隔，默认为300s。
- This script supports monitoring the VRAM of a specified GPU through the gpu_id. The `threshold` is the preset video memory threshold, with a default value of 10 MiB. `check_interval` is the detection time interval, with a default value of 300 seconds.
  
https://github.com/startracker0/GPU_MONITOR/blob/768c15b4ba13627d60066e395b45449944bbc283/monitor.py#L128-L129

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

## 4. 运行(Run)
``
 nohup python monitor.py >monitor.log 2>&1&
 ``
