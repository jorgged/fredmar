

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

/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "80%";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
     document.getElementById("mySidenav").style.width = "0";
     document.body.style.backgroundColor = "white";
 }