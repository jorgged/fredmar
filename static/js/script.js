

$(".js-show-category").on("click","option",function () {
    console.log("worked!");
})

$(function () {
            var CategoryBtn = function(){
            var btn = $(this);
            $.ajax({
                url: btn.attr("data_url"),
                data: btn.attr("data_category"),
                type: 'get',
                dataType: 'json',
                success: function (data) {
                    $("#product-card").html(data.products_card);
                }
            });
            return false;
        };
            $(".js-show-category").on("click",CategoryBtn);
    });