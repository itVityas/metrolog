
function fill_modal_window(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    const row = e.parentElement.parentElement;
    const cells = row.children;
/*
    const id = cells[0].textContent;
    const type = cells[1].textContent;
    const group = cells[2].textContent;
    const name = cells[3].textContent;
    
    form.elements['id'].value = id;
    form.elements['type'].value = type;
    form.elements['group'].value = group;
    form.elements['name'].value = name;
*/
    for(const [index, cell] of [...cells].entries()){
        if (index === cells.length - 2) {
            break;
        }
        [...form.elements][index+1].value = cell.textContent;
    }

    const id = cells[0].textContent;
    form.action = "" + id + "/update/";
    modal.show();
};

function flush_modal_window(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    for (const [index, elem] of [...form.elements].entries()) {
        if (index === [...form.elements].length - 1) {
            break;
        }
        if (index === 0) {
            continue;
        }
        elem.value = null;
    }
    /*
    form.elements['id'].value = null;
    form.elements['type'].value = null;
    form.elements['group'].value = null;
    form.elements['name'].value = null;
*/
    form.action = "add/";
    modal.show();
}

function show_delete_modal(e){
    const modal_delete = new bootstrap.Modal(document.getElementById("modal_window_delete"));
    const form_delete = document.getElementById("modal_form_del");
    //const delete_button = document.getElementById("delete_button");

    const row = e.parentElement.parentElement;
    const cells = row.children;

    const id = cells[0].textContent;

    form_delete.action = "" + id + "/delete/";
    //delete_button.data = id;
    modal_delete.show();
}

function makedelete(e){
    const csrfToken = e.children[0].value;
    fetch("" + e.data + "/delete/", {
        method: "DELETE",
        headers: {
            'X-CSRFToken': csrfToken
        },
    }).then(response => {
        window.location.href = response.url;
    })
    .catch(error => console.error('Error fetching data:', error));
}