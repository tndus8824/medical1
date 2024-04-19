$(function(){
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];


    let htmlData="";
    for(let i=0; i<no.length;i++){
    htmlData+="<tr id='"+no[i]+"'>";
    htmlData+="<td><input type='checkbox' id='stu' class='stuChk' value='"+no[i]+"'></td>";
    htmlDate+= "<td>"+no[i]+"</td>";
    htmlDate+= "<td>"+name[i]+"</td>";
    htmlDate+="<td>"+kor[i]+"</td>";
    htmlDate+="<td>"+eng[i]+"</td>";
    htmlDate+="<td>"+math[i]+"</td>";
    htmlDate+="<td>"+total[i]+"</td>";
    htmlDate+="<td>"+avg[i]+"</td>";
    htmlDate+="<td>0</td>";
    htmlDate+="<td><button class='delBtn'>삭제</button></td>";
    htmlData+="</tr>";
    }
$("#body").html(htmlDate);


$("#conformBtn").click(function(){
    $("#body").append(htmlData);
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");

});
//전체선택, 취소

$("allChk").click(function(){
    if($(".stuChk").each(function(){
        $(this).prop("checked",true);
    })

if($(".stuChk").each(false))

d
    //정보를 가져올 것들
    //1)학생입력누르면->입력창이 떠야함
    //2)확인/취소

});