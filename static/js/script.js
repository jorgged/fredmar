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
          $("#modal-book").modal("hide");
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


    /* Binding */

    // preguntar
    $(".js-preguntar").click(loadForm);
    $("#preguntaModal").on("submit", ".js-preguntar-create-form", saveForm);
});





    // Create book
    $(".js-create-book").click(loadForm);
    $("#modal-book").on("submit", ".js-book-create-form", saveForm);

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
    $("#modal-book").on("submit", ".js-book-update-form", saveForm);

  // Delete book
  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-book-delete-form", saveForm);