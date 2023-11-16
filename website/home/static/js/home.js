/*
------------------------------------------------------
------------------------------------------------------
This is the script per page, any changes to the page
------------------------------------------------------
------------------------------------------------------
admin.html JS
*/

$('#quick_view_modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var ID = button.data('products-id');
    var PRODUCT_NAME = button.data('products-name');
    var OLD_PRICE = button.data('products-old-price');
    var NEW_PRICE = button.data('products-new-price');
    var PHOTO = button.data('products-photo');

    // Update the modal content with the data
    $("#openQuickView-product-id").text(ID);
    $("#openQuickView-product-name").text(PRODUCT_NAME);
    $("#openQuickView-product-oldprice").text('₱' + OLD_PRICE);
    $("#openQuickView-product-newprice").text('₱' + NEW_PRICE);
    $("#openQuickView-product-image").attr("src", '/static/website/img/product/' + PHOTO);
});

$('#addtowishlist_modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var PRODUCT_NAME = button.data('products-name');
    var PHOTO = button.data('products-photo');

    // Update the modal content with the data
    $("#addtowishlist-product-name").text(PRODUCT_NAME);
    $("#addtowishlist-product-image").attr("src", '/static/website/img/product/'+PHOTO);
});

$('#upcomingbidding_modal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var ID = button.data('products-id');
    var PRODUCT_NAME = button.data('products-name');
    var OLD_PRICE = button.data('products-old-price');
    var NEW_PRICE = button.data('products-new-price');
    var PHOTO = button.data('products-photo');

    // Update the modal content with the data
    $("#upcoming-product-id").text(ID);
    $("#upcoming-product-name").text(PRODUCT_NAME);
    $("#upcoming-product-oldprice").text('₱' + OLD_PRICE);
    $("#upcoming-product-newprice").text('₱' + NEW_PRICE);
    $("#upcoming-product-image").attr("src", '/static/website/img/product/' + PHOTO);
});
