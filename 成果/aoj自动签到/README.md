# [安徽科技学院AOJ](https://acm.webturing.com/) 自动签到  

-------------------------------------------------------  
## 使用方法  
* 将本代码部署在阿里云的函数计算服务上即可实现aoj每日自动签到  
## 部署方法  
1. 注册阿里云帐号  
    * 进入 [阿里云](https://promotion.aliyun.com/ntms/yunparter/invite.html?userCode=vd8zzwy8) 官网注册账户，并完成实名注册
    * 开通 [函数计算](https://www.aliyun.com/product/fc) 服务，及其要求你开通的其他服务  
2. 配置服务  
    * 进入控制台应用中心 [新建服务](https://fc.console.aliyun.com/fc/service/cn-shanghai/create) 并按照图片中填写，点击 _创建_  
    
        ![creat](https://s3.ax1x.com/2020/12/03/DoDhDA.png)
      
    * 进入 [新建函数](https://fc.console.aliyun.com/fc/service/cn-shanghai/aoj_sign/function/create)  
    * 选择 _事件函数_ 后，点击 _下一步_  
    * 按照图片填写后，点击完成  
    ![finish](https://s3.ax1x.com/2020/12/03/DorYVI.png)  
3. 部署
    * 