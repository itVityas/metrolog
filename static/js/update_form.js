const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
const form = document.getElementById("modal_form");
const modal_delete = new bootstrap.Modal(document.getElementById("modal_window_delete"));
const form_delete = document.getElementById("modal_form_del");

function fill_modal_window(e) {
    console.log(form.action);

    const row = e.parentElement.parentElement;
    const cells = row.children;

    const id = cells[0].textContent;
    const type = cells[1].textContent;
    const group = cells[2].textContent;
    const name = cells[3].textContent;
    
    form.elements['id'].value = id;
    form.elements['type'].value = type;
    form.elements['group'].value = group;
    form.elements['name'].value = name;

    form.action = "" + id + "/update/";
    modal.show();

    /*fetch(form.action, {
        method: 'get',
    })
    .then(response => response.text())
    .then(data => {
        container.innerHTML = data;
        const modal = new bootstrap.Modal(document.getElementById("modal_window"));
        modal.show();
    })
    .catch((error) => {
        console.error('Error:', error);
    });*/
};

function flush_modal_window(e) {
    form.elements['id'].value = null;
    form.elements['type'].value = null;
    form.elements['group'].value = null;
    form.elements['name'].value = null;

    form.action = "add/";
    modal.show();
}

function show_delete_modal(e){
    const row = e.parentElement.parentElement;
    const cells = row.children;

    const id = cells[0].textContent;

    form_delete.action = "" + id + "/delete/"
    modal_delete.show();
}