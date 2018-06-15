$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#preguntaModal .modal-content .modal-body").html("");
        $("#preguntaModal").modal("show");
      },
      success: function (data) {
        $("#preguntaModal .modal-content .modal-body").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#preguntaModal").modal("hide");
        }
      }
    });
    return false;
  };

    /* Binding */

    // preguntar
    $(".js-preguntar").click(loadForm);
    $("#preguntaModal").on("submit", ".js-preguntar-form", saveForm);
});




$( ".carousel-item:first-child" ).addClass("active");
