window.onload = function(){
    $('#pubcomment').click(function (event) {
        event.preventDefault();
        let content = $('input[name="content"]').val();
        let csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        let blog_id = $('input[name="blog_id"]').val();
        $.ajax('/pub_comment',{
            method: 'GET',
            data :{
                content,csrfmiddlewaretoken,blog_id
            },
            success: function (result) {
                if (result['code'] == '200' ) {
                    $.ajax('/pub_comment',{
                        method: 'POST',
                        data : {
                            content,csrfmiddlewaretoken,blog_id
                        },
                        success: function (result) {
                            alert('评论发送成功')
                            window.location.href = '/blog/' + blog_id
                            // $('input[name="content"]').val('');
                        }
                    })
                }else{
                    alert('评论不能为空!!!!!')
                }
            }
        })
    })
}