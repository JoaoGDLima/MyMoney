$( document ).ready(function() {

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var searchBtnLanc = $('#search-btn-lanc');
    var searchFormLanc = $('#search-form-lanc');
    
    $(deleteBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar este registro?');

        if(result) {
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    
    $(searchBtnLanc).on('click', function() {
        searchFormLanc.submit();
    });

});