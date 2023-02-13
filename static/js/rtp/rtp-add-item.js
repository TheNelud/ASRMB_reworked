
$(document).ready(function() {
    $('.add-item').click(function(ev) {
        console.log("хуй")
        ev.preventDefault();
        let count = $('#items-form-container').children().length;
        let tmplMarkup = $('#item-template').html();
        let compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('tbody#items-form-container').append(compiledTmpl);

        // update form count
        $('#id_item_items-TOTAL_FORMS').attr('value', count+1);

        // some animate to scroll to view our new form
        $('html, body').animate({
                scrollTop: $("#add-item-button").position().top-200
            }, 800);
    });
});