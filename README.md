# GPU_MONITOR
A lightweight script for `GPUs monitoring`. Automatically emails the user when VRAM usage drops below a specified threshold and then exit the script.  

一个轻量级 `GPU 监控`脚本，当显存使用情况低于预设阈值时将会自动发送邮件至指定邮箱，并退出脚本。

This script is mainly used to check whether the `training is completed` and whether `the GPUs are idle`.

本脚本主要用于查看`训练是否完成/显卡是否闲置`。

The `password` field requires an **application-specific password** instead of your regular email password.

请使用**邮箱安全密码**（非登录密码）填写 `password` 字段。

   - [You can refer to the blog to obtain a secure password(获取安全密码可参考博客)](https://blog.csdn.net/qq_42076902/article/details/131900459)
     
## tips
This script supports monitoring the VRAM of a specified GPU through the `GPU ID`. You can make modifications here.

本脚本支持通过gpu_id监控指定GPU显存，您可以在此处进行修改。

https://github.com/startracker0/GPU_MONITOR/blob/7b2ce5dc82628e60fe8c771739732847fe5a75dd/monitor.py#L129

The default email used by this script is QQ Mail. Please change the following parameters by yourself. If you need to change it to another email, please query the `smtp_server` and `smtp_port` of the corresponding email by yourself.

本脚本默认使用的邮箱为QQ邮箱。请自行更换以下参数；如需更换为其他邮箱请自行查询对应邮箱的`smtp_server`与`smtp_port`

https://github.com/startracker0/GPU_MONITOR/blob/5c82370c6a80983f0fc4472eae3e13820bfee080/monitor.py#L8-L12
