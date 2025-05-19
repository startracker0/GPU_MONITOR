import smtplib
from email.mime.text import MIMEText
import subprocess
import time

def send_email(subject, content):
    """发送邮件的函数"""
    sender = 'you_email@qq.com'
    receiver = ['you_email@qq.com']
    password = 'yourpassword'
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(receiver)
    
    try:
        # 不使用with语句，手动管理连接
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender, password)
        
        try:
            server.sendmail(sender, receiver, msg.as_string())
            print("✅ 成功发送邮件")
        except Exception as e:
            print(f"❌ 邮件发送失败: {e}")
        
        # 正常关闭连接
        try:
            server.quit()
        except:
            # 忽略关闭连接时的错误
            pass
            
    except smtplib.SMTPException as e:
        print(f"❌ SMTP连接失败: {e}")

def get_gpu_memory_usage():
    """获取GPU显存使用情况"""
    try:
        # 使用nvidia-smi命令获取GPU信息
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=index,memory.used,memory.total,utilization.gpu', '--format=csv,noheader,nounits'])
        output = output.decode('utf-8').strip()
        
        gpu_info = []
        for line in output.split('\n'):
            values = line.split(', ')
            if len(values) >= 3:
                gpu_idx = int(values[0])
                memory_used = float(values[1])
                memory_total = float(values[2])
                gpu_util = float(values[3]) if len(values) > 3 else 0
                
                usage_percent = (memory_used / memory_total) * 100
                gpu_info.append({
                    'index': gpu_idx,
                    'memory_used': memory_used,
                    'memory_total': memory_total,
                    'usage_percent': usage_percent,
                    'gpu_util': gpu_util
                })
        
        return gpu_info
    
    except Exception as e:
        print(f"Error getting GPU info: {e}")
        return []

def monitor_gpu(threshold=0.0002, check_interval=300):
    """监控GPU显存占用率低于阈值的情况，每个GPU只通知一次"""
    print(f"GPU监控已启动，阈值: {threshold}%，检查间隔: {check_interval}秒")
    
    # 记录已经报警的GPU，避免重复发送邮件
    alerted_gpus = set()
    
    # 启动时发送初始状态报告
    gpu_info = get_gpu_memory_usage()
    initial_report = "GPU监控已启动 - 当前状态:\n\n"
    
    for gpu in gpu_info:
        initial_report += f"GPU {gpu['index']}: {gpu['usage_percent']:.1f}% ({gpu['memory_used']:.0f}MB/{gpu['memory_total']:.0f}MB) 使用率: {gpu['gpu_util']:.1f}%\n"
    
    # 发送初始报告邮件
    send_email("GPU监控已启动 - 初始状态报告", initial_report)
    
    while True:
        gpu_info = get_gpu_memory_usage()
        alert_required = False
        alert_message = "GPU显存占用率低于阈值通知:\n\n"
        
        for gpu in gpu_info:
            gpu_id = gpu['index']
            
            # 检测显存占用率低于阈值且未报警过的GPU
            if gpu['usage_percent'] < threshold and gpu_id not in alerted_gpus:
                alert_required = True
                alerted_gpus.add(gpu_id)  # 添加到已报警列表
                alert_message += f"GPU {gpu_id}: {gpu['usage_percent']:.1f}% ({gpu['memory_used']:.0f}MB/{gpu['memory_total']:.0f}MB) 使用率: {gpu['gpu_util']:.1f}%\n"
        
        # 只有当有新的GPU显存占用率低于阈值时才发送邮件
        if alert_required:
            send_email(f"GPU显存占用率低于{threshold}%通知", alert_message)
            print('结束GPU检测')
            return
        
        time.sleep(check_interval)

if __name__ == "__main__":
    # 启动GPU监控，0.0002阈值，每5分钟检查一次
    monitor_gpu(threshold=0.0002, check_interval=300)
