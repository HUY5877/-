window.onload = function () {
    // 设置按钮点击绑定事件
    function work() {

        $("#send").click(function (event) {
            // event.preventDefault();
            //将js对象转化为jquery对象
            let $this = $(this);
            let email = $('input[name = "email" ]').val();
            if (!email) {
                alert("请先输入邮箱!");
                return;
            }
            //取消按钮的点击事件
            $this.off('click');

            // 发送ajax请求

            $.ajax('/author/sendemail?email=' + email, {
                method: 'GET',
                success: function(result) {
                    console.log(result);
                    if (result['code'] === 200 ){
                        alert('邮箱发送成功');
                    }else{

                        alert(result['message']);
                    }
                },


            })

            //如何做倒计时
            let cnt = 60;
            // 相当于无限制每秒调用一次这个函数
            let timer = setInterval(function () {
                if (cnt <= 0) {
                    $this.text('获取验证码')
                    // 所以此后要删除该定时器
                    clearInterval(timer);
                    //恢复点击事件
                    work();

                } else {
                    $this.text(cnt + "s" );
                    cnt--;
                }
            }, 1000);
        })
    }
    work();
};