$(document).ready(function(){
    $('.item').on('click', function(){
        id = $(this).attr("id");
        $("tbody").addClass('bodyshow').removeClass('bodyhide');
        $("tr").each(function(index){
            if ($(this).attr('name') == id)
            {
                $(this).addClass("trshow").removeClass("trhide");
            }
            else
            {
                $(this).addClass("trhide").removeClass("trshow");
            }
        })
    })
});