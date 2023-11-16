/*
------------------------------------------------------
------------------------------------------------------
This is the script per page, any changes to the page
------------------------------------------------------
------------------------------------------------------

*/
$(document).ready(function() {
    "use strict";
    // DATA TABLES SETTINGS
    $("#farmers").DataTable({
        keys: !0,
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function () {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });

});