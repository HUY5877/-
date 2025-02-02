window.onload = function () {
    const {createEditor, createToolbar} = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        },
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })
    $("#pub").click(function (event) {
        event.preventDefault();
        let title = $('input[name="title"]').val();
        let kind = $('select[name="kind"]').val();
        let content = editor.getHtml();
        let csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax('/pub' , {
            method: 'POST',
            data: {
                title,kind,content,csrfmiddlewaretoken
            },
            // 只存在success情况
            success: function (result) {
                // alert(result['code']+result['message']);
                if (result['code'] == '200' ) {
                    id = result['data']['blog_id'];
                    alert('博客发送成功,点击确定进入详情页面');
                    window.location = ('/blog/' + id)
                }else{

                     alert(result['code']+result['message']);

                }
            }

        })


    });
}