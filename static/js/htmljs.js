document.write("<script language='javascript' src='/static/js/json3.js'></script>");
document.write("<script language='javascript' src='/static/js/json2.js'></script>");
document.write("<script language='javascript' src='/static/js/fly.min.js'></script>");
/*************************/
  function addTr(tab, row, trHtml){
     //获取table最后一行 $("#tab tr:last")
     //获取table第一行 $("#tab tr").eq(0)
     //获取table倒数第二行 $("#tab tr").eq(-2)
     var $tr=$("#"+tab+" tr").eq(row);
     if($tr.size()==0){
        alert("指定的table id或行数不存在！");
        return;
     }
     $tr.after(trHtml);
  }

  function delTr(ckb){
     //获取选中的复选框，然后循环遍历删除
     var ckbs=$("input[name="+ckb+"]:checked");
     if(ckbs.size()==0){
        alert("要删除指定行，需选中要删除的行！");
        return;
     }
           ckbs.each(function(){
              $(this).parent().parent().remove();
           });
  }

  /**
   * 全选
   *
   * allCkb 全选复选框的id
   * items 复选框的name
   */
   function allCheck(allCkb, items){
   $("#"+allCkb).click(function(){
      $('[name='+items+']:checkbox').attr("checked", this.checked );
   });
  }

  ////////添加一行、删除一行测试方法///////
  function selectall (){
   //全选
   allCheck("allCkb", "ckb");
  };

  function addTr2(tab, row){
      var num = id();
      var txt = "num" + num;
      var trHtml="<tr align='center' class='cesa'><td width='10%'><input type='checkbox' name='ckb'/></td><td width='30%'><input id =" + num + " style=\"width:  100%;\"></input></td><td width='30%'><input id= " + txt+" style=\"width:  100%;\"></input></td></tr>";
     addTr(tab, row, trHtml);
  }

  function delTr2(){
     delTr('ckb');
  }

  function id(){
      var  id = document.getElementById("tab").getElementsByTagName("tr");
      return id.length
  }

/*************************/

function assignment(Json) {
    // json复值
    var i = 1
    for(var p in Json){//遍历json对象的每个key/value对,p为key
        // 这个是key
        document.getElementById(i).value = p;
        var txt = "num"+i;
        // 这个是value
        document.getElementById(txt).value = Json[p] ;
        document.getElementById(txt).name = p;
        i++;
        }
}

function httpget(){
    fly.post('/dispathapi' ,data)
    .then(function (response) {
    console.log(response);
  })
}


// 处理josn 字符串
function syntaxHighlight(json) {
    if (typeof json != 'string') {
        json = JSON.stringify(json, undefined, 2);
    }
    json = json.replace(/&/g, '&').replace(/</g, '<').replace(/>/g, '>');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function(match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
             cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}

var songResJson={
      "service": "ALL",
     "qt": 581,
       "content": {
        "answer": {
       "song": "如果缘只到遇见",
          "albu1m": "如果缘只到遇见",
          "album1": "如果缘只到遇见",
          "albu2m": "如果缘只到遇见",
          "albu5m": "如果缘只到遇见",
          "albu4m": "如果缘只到遇见",
          "artist": "吴奇隆 严艺丹",
          "pic_url": "http://p1.music.126.net/-u3WgIXsFNCW7d8Jy7pCEA==/5921969627395387.jpg"
        },
        "scene": "music"
     }
    };
// 触发josn 处理
function jsonn() {
    document.getElementById('result').innerHTML = syntaxHighlight(songResJson);
}

function alt(data){
    // reset();
    var mycars = new Array(data);
    var json = mycars[0]["data"][0];
    var jsonLength=0;
    for (var i in json) {
            jsonLength++;
        };
    // 增加行
    for (var i =0;i<(jsonLength);i++){
            addTr2('tab', -1);
     };
    assignment(json);
}
