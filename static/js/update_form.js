

function fill_modal_window(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    const row = e.parentElement.parentElement;
    const cells = row.children;

    for(const [index, cell] of [...cells].entries()){
        if (index === cells.length - 2) {
            break;
        }
        if (index === 0) {
            continue;
        }
        switch ([...form.elements][index].type){
            case "checkbox":
                [...form.elements][index].checked = (cell.textContent === "Да") ? true : false;
                break;
            case "number":
                [...form.elements][index].value = (cell.textContent.includes(',')) ? parseFloat(cell.textContent.replace(',','.')) : parseInt(cell.textContent);
                break;
            default:
                [...form.elements][index].value = cell.textContent;
        }

    }

    const id = cells[0].textContent;
    form.action = "" + id + "/update/";
    modal.show();
};

function flush_modal_window(e) {
    const modal = new bootstrap.Modal(document.getElementById("modal_window_add"));
    const form = document.getElementById("modal_form");

    form.reset();
    form.action = "add/";
    modal.show();
}

function show_delete_modal(e){
    const modal_delete = new bootstrap.Modal(document.getElementById("modal_window_delete"));
    const delete_button = document.getElementById("delete_button");

    const row = e.parentElement.parentElement;
    const cells = row.children;

    const id = cells[0].textContent;

    delete_button.data = id;
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
        response.text().then(text =>{
            console.log(text)
            document.open()
            document.write(text)
            document.close()
        })
    })
    .catch(error => console.error('Error fetching data:', error));
}


function show_table(e, id_show){
    const tables = document.getElementById("table_container").children;
    const buttons = document.getElementById("buttons_container").children;

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('btn-light');
        buttons[i].classList.add('btn-primary-outline');
    }
    e.classList.remove('btn-primary-outline');
    e.classList.add('btn-light');

    for (var i = 0; i < tables.length; i++) {
        if(tables[i].id === id_show){
            tables[i].classList.remove('d-none');
        }else{
            tables[i].classList.add('d-none');
        }
    }
}