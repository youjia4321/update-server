function edit(id) {
    $.ajax({
        async: true,
        url: 'edit/file',
        type: 'post',
        dataType: 'json',
        data: { 'id': id },
        beforeSend: function () {
            loadMsg = layer.msg('loading...', {
                icon: 16,
                time: 0,
                shade: 0.5
            });
        },
        success: function (result) {
            layer.close(loadMsg);
            if (result['code'] === '200') {
                var filename = result['filename'];
                var document_id = result['document_id'];
                var tag = result['tag'];
                var updated = result['updated']
            }
            layer.open({
                title: '在线编辑',
                type: 1,
                area: ['50%', '60%'], //宽高
                content: '<div class="col-md-12" style="padding: 20px">' +
                    '<form class="form-horizontal" role="form">' +
                    '  <div class="form-group">' +
                    '    <label for="firstname" class="col-sm-2 ">文件</label>' +
                    '    <div class="col-sm-10">' +
                    '      <input type="text" class="form-control" id="filename" value="' + filename + '" >' +
                    '    </div>' +
                    '  </div>' +
                    '  <div class="form-group">' +
                    '    <label for="lastname" class="col-sm-2 ">编号</label>' +
                    '    <div class="col-sm-10">' +
                    '      <input type="text" class="form-control" id="document_id" value="' + document_id + '" >' +
                    '    </div>' +
                    '  </div>' +
                    '  <div class="form-group">' +
                    '     <label for="lastname" class="col-sm-2 ">类型</label>' +
                    '    <div class="col-sm-10">' +
                    '      <input type="text" class="form-control" id="tag" value="' + tag + '">' +
                    '    </div>' +
                    '  </div>' +
                    '  <div class="form-group">' +
                    '    <div class="col-sm-10">' +
                    '      <div class="checkbox">' +
                    '        <label>' +
                    '          <input type="checkbox" value="' + updated + '">可更新' +
                    '        </label>' +
                    '      </div>' +
                    '    </div>' +
                    '  </div>' +
                    '</form></div>'
            });
        }
    });

}

function _delete(id) {
    layer.open({
        title: '系统提示',
        icon: 15,
        content: '确认删除？',
        btn: ['确定', '取消'],
        // btnAlign: 'c', // 按钮居中
        btn1: function () {
            $.ajax({
                async: true,
                url: 'delete/file',
                type: 'post',
                dataType: 'json',
                data: { 'id': id },
                beforeSend: function () {
                    loadMsg = layer.msg('loading...', {
                        icon: 16,
                        time: 0,
                        shade: 0.5
                    });
                },
                success: function (result) {
                    layer.close(loadMsg);
                    if (result['code'] === '200') {
                        layer.msg('删除成功', {
                            icon: 16,
                            shade: 0.5
                        });
                        location.reload();
                    }
                }
            })
        },
        btn2: function () {  // 取消
        }
    });

}