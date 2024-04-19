$(function(){
$.ajax({
    url:"http://127.0.0.1:5500/students/json/stu_score.json", 
    data:"",
    type:"get",
    dataType:"json",
    success:function(data){
        //alert("데이터 가져오기 성공");
        console.log(data);
        s_count = data.length;
        let htmlData = "";
        for(let i=0;i<10;i++){
            htmlData += "<tr id='"+data[i].no+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'></td>";
            htmlData += "<td>"+data[i].no+"</td>";
            htmlData += "<td>"+data[i].name+"</td>";
            htmlData += "<td>"+data[i].kor+"</td>";
            htmlData += "<td>"+data[i].eng+"</td>";
            htmlData += "<td>"+data[i].math+"</td>";
            htmlData += "<td>"+data[i].total+"</td>";
            htmlData += "<td>"+data[i].avg+"</td>";
            htmlData += "<td>"+data[i].rank+"</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";
        }//for
        // html소스를 tbody 추가
        $("#body").html(htmlData);
    },
    error:function(){ alert("에러"); }
  });//ajax
});


$(function(){
    $.ajax({
        url:"",
        data:"",
        type:"",
        datatype:"",
        success:function(data){

        },
        error:function(){

        }


    });
});