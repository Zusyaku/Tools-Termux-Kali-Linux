'use strict';

function create() {
    let link_element = document.getElementById('link');
    let link = link_element.value;

    if (!link.length) {
        return;
    } 

    $.ajax({
        type: 'POST',
        url: '/create',
        data: { 'link': link }
    }).done(function(data) {
        let link_id = data['resp'];

        if (link_id) {
            link_element.value = link_id;
        }

        link_element.focus();
        link_element.select();
    });
}