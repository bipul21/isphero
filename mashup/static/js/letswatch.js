$(function(){
    $('.setAlert').click(function (e) {
        setAlert($(this).attr("movieId"));
    });
});



function setAlert(movieId){
    var url="/setAlert";
    $.ajax({
        type:"GET",
        url:url,
        dataType:"json",
        data:{"id":movieId},
        success:function(data){
        }
    });
}
function getLoadingBar(){
    return $("<div />").attr("class","progress progress-striped active loading").append($("<div />").attr({"class":"bar","style":"width: 100%;"}));
}
function getSearchResult(query){
    var vertical= $("#categoryDropDown option:selected").val();
    var verticalName=  $("#categoryDropDown option:selected").text();
     var url="/search/"+vertical+"/"+query;
    $.ajax({
        type:"GET",
        url:url,
        dataType:"json",
        cache:true,
        beforeSend:function(){
            if($('#navbar-results').html().trim() == ''){
                $('#navbar-results').html('');
                $('#navbar-results').append(getLoadingBar());
            }
            $('#navbar-results').show();

            },
         complete:function(){

        },
        success:function(data){
            formSearchResultArea(verticalName,data);
        }
    });
}

